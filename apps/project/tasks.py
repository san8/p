from celery import Celery
from os import mkdir 
from os.path import join 
from ftplib import FTP
from urlparse import urlparse 

from pearl.settings import BASE_DIR


app = Celery('project_tasks', backend='amqp', broker='amqp://',
             include=['apps.processing.tasks'])

@app.task()
def project_created(project_id):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 0:
        get_ftp_files.apply_async(args=[project_id,])
        return 'Successfully created project.'
    else:
        return 'Status is NOT ZERO'


@app.task()
def get_ftp_files(project_id, ):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    url_list = [project.fastq_file1, project.fastq_file2, project.vcf_file1]
    url_list = filter(None, url_list)
    try: 
        local_dir = join(BASE_DIR, 'files/NewProject/', str(project_id)) 
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
        from apps.processing.tasks import do_processing 
        do_processing.apply_async(args=[project_id,])
        return 'Successfully fetched the files.'
    except:
        project.status = -1
        project.save() 
        return 'Unable to fetch files.'
        
