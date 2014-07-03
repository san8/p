from urlparse import urlparse 
from ftplib import FTP

from celery import Celery

app = Celery('ftp_tasks', backend='amqp', broker='amqp://')

@app.task()
def get_ftp_files(project_id='', url_list=''):
    try:
        for url in url_list:
            parsed_url = urlparse(url)
            ftp = FTP(parsed_url.netloc)
            ftp.login()
            file_name = parsed_url.path.split('/')[-1:][0]
            path = parsed_url.path[:-len(file_name)]
            ftp.cwd(path)
            local_file_name = str(project_id) + file_name
            ftp.retrbinary('RETR ' + file_name, open(local_file_name, 'wb').write)
            ftp.quit()
    except:
        print "Unable to fetch files"
        

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
