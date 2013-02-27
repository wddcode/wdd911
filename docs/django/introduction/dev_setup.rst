Preparing your computer for development
#######################################

.. seealso::

   :ref:`installing-pip`


OS X
****

Xcode
=====

To get all the development libraries and tools install `Apple's Xcode <https://itunes.apple.com/ch/app/xcode/id497799835?mt=12&uo=4>`_ 

You will also need the `Xcode Command Line Tools` (gcc compiler etc.):

 - open Xcode
 - > Preferences
 - > Downloads
 - > Command Line Tools 'install'


(Home)brew
==========

::

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
    
JPEG dev-library
================

::

    brew install libjpeg
    
    
    
To enable jpeg support on existing virtualenvs you'll have to re-install pil:


::

    pip uninstall pil
    pip install pil
    
    
Check the console output, it should look something like (important part is: `JPEG support available`):

::

    --------------------------------------------------------------------
    --- TKINTER support available
    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available
    *** FREETYPE2 support not available
    *** LITTLECMS support not available
    --------------------------------------------------------------------
    
    
Code Directory
================    
    
For easy code access and snippet copy-pasting, symlink your workspace folder to `~/code`

::

    ln -s /Users/replace-this-with-your-username/Documents/Code /Users/replace-this-with-your-username/code
    



Linux (debian based)
********************

Aptana
======

::

    sudo apt-get install openjdk-7-jre libwebkitgtk-1.0-0 


Download latest aptana studio and extract it to /opt/ ( or other appropriate path... )
    
Development libraries & other tools
===================================

::

    sudo apt-get install aptitude
    sudo aptitude install build-essential python-setuptools python-dev git-core libjpeg-dev
    sudo easy_install pip
    sudo pip install virtualenv
    
    
Code Directory
================    
    
For easy code access and snippet copy-pasting, symlink your workspace folder to `~/code`

::

    lln -s /home/user/Documents/Code /home/user/code
    


    
    
   