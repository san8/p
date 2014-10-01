celery multi start project_queue -A apps.processing.tasks -l info --without-gossip -Q celery 

celery multi start ftp_fastq -A apps.processing.tasks -l info --without-gossip -c 1  -Q ftp_fastq

celery multi start proc_fastq -A apps.processing.tasks -l info --without-gossip -c 1  -Q proc_fastq 

celery multi start ftp_vcf -A apps.processing.tasks -l info --without-gossip -c 8 -Q ftp_vcf 

celery multi start proc_vcf -A apps.processing.tasks -l info --without-gossip -c 8  -Q proc_vcf 

