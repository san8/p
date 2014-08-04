#shell script to run tests and report coverage

coverage run manage.py test -v 2 --settings=pearl.settings.local 
coverage html
google-chrome htmlcov/index.html

