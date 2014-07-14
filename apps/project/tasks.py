from celery import Celery
from os import mkdir 
from os.path import join 
from ftplib import FTP
from urlparse import urlparse 

from pearl.settings import BASE_DIR


app = Celery('project_tasks', backend='amqp', broker='amqp://')

@app.task()
def project_created(project_id):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 'Raw Files Uploaded':
        url_list = []
        if project.fastq_file1:
            if project.fastq_file2:
                url_list = [project.fastq_file1, project.fastq_file2]
            else:
                url_list = [project.fastq_file1]
        elif project.vcf_file1:
            url_list = [project.vcf_file1,]
        if url_list: 
            get_ftp_files.apply_async(args=[project.id, url_list,]).get() 
            update_status.apply_async(args=[project.id,])
        return 'Projected created successfully'
    else:
        return 


@app.task()
def get_ftp_files(project_id, url_list=''):
    try:
        local_dir = join(BASE_DIR, 'files/NewProject/', str(project_id)) 
        mkdir(local_dir)
        for url in url_list:
            parsed_url = urlparse(url)
            ftp = FTP(parsed_url.netloc)
            ftp.login()
            file_name = parsed_url.path.split('/')[-1:][0]
            path = parsed_url.path[:-len(file_name)]
            ftp.cwd(path)
            local_file = join(local_dir, file_name)
            ftp.retrbinary('RETR ' + file_name, open(local_file, 'wb').write)
            ftp.quit()
        return 'Successfully fetched the files.'
    except:
        return 'Unable to fetch files.'
        

@app.task()
def update_status(project_id):
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    project.status = 'Started Processing'
    project.save() 
    return 'Status updated successfully'


