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
