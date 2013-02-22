# Installation
##################################################################


git clone git@github.com:wddcode/wdd911.git
cd wdd911/django/01-introduction/
virtualenv env
source env/bin/activate

# requirements
pip install -r requirements/requirements.txt

# initialize
./manage.py syncdb --all
./manage.py migrate --fake

# run!
./manage.py runserver

-> http://localhost:8000/