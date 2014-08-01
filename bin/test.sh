#shell script to run tests and report coverage

coverage run manage.py test apps/project -v 2 
coverage html
google-chrome htmlcov/index.html

