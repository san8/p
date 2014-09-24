celery multi start project_queue -A apps.processing.tasks -l info --without-gossip -Q celery --autoreload

celery multi start ftp_fastq -A apps.processing.tasks -l info --without-gossip -c 1  -Q ftp_fastq --autoreload

celery multi start proc_fastq -A apps.processing.tasks -l info --without-gossip -c 1  -Q proc_fastq --autoreload

celery multi start ftp_vcf -A apps.processing.tasks -l info --without-gossip -c 8 -Q ftp_vcf --autoreload

celery multi start proc_vcf -A apps.processing.tasks -l info --without-gossip -c 8  -Q proc_vcf --autoreload

