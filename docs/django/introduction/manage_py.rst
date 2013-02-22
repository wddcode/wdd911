Django Basics
#############

.. seealso::

   :ref:`using-virtualenv`
        

        
First run of a project
**********************

This steps install the required modules, create the database tables, add a superuser etc.

Navigate to the project root
============================

::

    cd ~/code/whatever/your/path/looks/like/

Create and activate
===================
 
:: 

    virtualenv env
    source env/bin/activate


Install the requirements
========================

::

    pip install -r requirements/requirements.txt


Initialise the Database
=======================

::

    ./manage.py syncdb --all
    ./manage.py migrate --fake


Running the local development server
====================================

::

    ./manage.py runserver
    
optionaly specify address to bind and the port (default: `127.0.0.1:8000`) 

::

    ./manage.py runserver 0.0.0.0:8080
    

Working with migrations (south)
###############################


Prepare an app for south
************************

Only needed once per app, if not handled by south already.
(assuming your app is named `portfolio` ... :) )

::

    ./manage.py convert_to_south portfolio
    ./manage.py migrate portfolio

Create and apply migrations
***************************

.. warning::

   These commands have to be run after `every` change to a model!

::

    ./manage.py schemamigration portfolio --auto
    ./manage.py migrate portfolio



 
   