import os
from urlparse import urlparse 
from ftplib import FTP
from os.path import join 

BASE_DIR = '/home/k3/work/pearl/pearl'

def get_ftp_files(project_id='', url_list=''):
        local_dir = os.path.join(BASE_DIR, 'files/NewProject/', str(project_id)) 
        os.mkdir(local_dir)    
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


if __name__ =="__main__":
    get_ftp_files('asdfas', ['ftp://ftp.asdf.com/asdf/aasd', 'ftp://ftp.asdf.com/asdf'])
    #get_ftp_files('234', ['ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/ERA021/ERA021502/ERX010282/ERR029554.fastq.bz2', 'ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/ERA021/ERA021502/ERA021502.experiment.xml'])

