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
    
    
    



   