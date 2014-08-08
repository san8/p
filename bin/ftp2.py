import urllib2, shutil

#url = "ftp://pearl:pearl@localhost/fastq_files/sample1.fastq.gz"
url = "ftp://pearl:pearl@localhost/fastq_files/sample1.fastq.gz"
ftp_file = urllib2.urlopen(url)
file_name = url.split('/')[-1]
print file_name 
with open(file_name, "wb") as file_header:
    shutil.copyfileobj(ftp_file, file_header)
