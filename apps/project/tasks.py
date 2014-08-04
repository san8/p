from celery import Celery
from os import mkdir 
from os.path import join 
from ftplib import FTP
from urlparse import urlparse 

from pearl.settings.base import BASE_DIR, NEW_PROJECT_DIR


app = Celery('project_tasks', backend='amqp', broker='amqp://',
             include=['apps.processing.tasks'])

@app.task()
def project_created(project_id):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 0:
        get_ftp_files.apply_async(args=[project_id,])
        print "Started FTP. Status = 0"
        return 0
    elif project.status == 1:
        from apps.processing.tasks import do_qc 
        do_qc.apply_async(args=[project_id,])
        print "Started QC. Status = 1"
    elif project.status == 3:
        if project.start_processing:
            from apps.processing.tasks import do_processing 
            do_processing.apply_async(args=[project_id,])
            print "Started Processing. Status = 3"
        else:
            project.status = -2
            project.save() 
            print "Terminated at QC."
    else:
        print project.status 
    return 1


@app.task()
def get_ftp_files(project_id,):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    url_list = project.url_list() 
    try: 
        local_dir = join(BASE_DIR, NEW_PROJECT_DIR, str(project_id)) 
        mkdir(local_dir)
        for url in url_list:
            parsed_url = urlparse(url)
            ftp = FTP(parsed_url.netloc)
            ftp.login('pearl', 'pearl')
            file_name = parsed_url.path.split('/')[-1:][0]
            path = parsed_url.path[:-len(file_name)]
            ftp.cwd(path)
            local_file = join(local_dir, file_name)
            ftp.retrbinary('RETR ' + file_name, open(local_file, 'wb').write)
            ftp.quit()
        project.status = 1
        project.save() 
        print 'Successfully fetched the files.'
        return 0
    except:
        project.status = -1
        project.save() 
        print 'Unable to fetch files.'
        return -1
        
