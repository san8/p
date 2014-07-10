"""
def project_created(sender, instance, created, **kwargs):
    if instance.status == 'Started processing.':
        return 
    else:
        project = NewProject.objects.get(id=instance.id)
        url_list = []
        if project.fastq_file1:
            if project.fastq_file2:
                url_list = [project.fastq_file1, project.fastq_file2]
            else:
                url_list = [project.fastq_file1]
        elif project.vcf_file1:
            url_list = [project.vcf_file1,]
        if url_list: 
            result = get_ftp_files.apply_async(args=[project.id, url_list,])
            if result.ready():
                print 'pasdf'
                instance.status = 'Started processing.'
                instance.save() 

""" 

