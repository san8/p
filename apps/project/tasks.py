from celery import Celery
from os import mkdir 
from os.path import join 
from ftplib import FTP
from urlparse import urlparse 

from pearl.settings import BASE_DIR


app = Celery('ftp_tasks', backend='amqp', broker='amqp://')


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
        return "Fetched Files Successfully."
    except:
        return "Unable to Fetch Files."
        

@app.task(ignore_result=True)
def print_hello():
    print 'hi there... '


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results


