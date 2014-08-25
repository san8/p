celery -A apps.project.tasks worker -l info -c 1 -n project_queue &
celery -A apps.project.tasks worker -l info -c 1 -n ftp_fastq -Q ftp_fastq &
celery -A apps.project.tasks worker -l info -c 1 -n ftp_vcf -Q ftp_vcf &

