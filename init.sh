#!/bin/bash

virtualenv .demo
ln -s .demo/bin/activate .
source .demo/bin/activate

# Link system-wide pandas/numpy/matplotlib (you have ones, I'm sure)
# Should work in Linux Mint / Ubuntu / maybe Debian
ln -sf /usr/lib/python2.7/dist-packages/{glib,gobject,cairo,gtk-2.0,pygtk.py,pygtk.pth,dateutil,pyparsing.py} $VIRTUAL_ENV/lib/python2.7/site-packages
ln -sf /usr/lib/python2.7/dist-packages/numpy $VIRTUAL_ENV/lib/python2.7/site-packages
ln -sf /usr/local/lib/python2.7/dist-packages/pandas $VIRTUAL_ENV/lib/python2.7/site-packages
ln -sf /usr/lib/pymodules/python2.7/{pylab.py,matplotlib} $VIRTUAL_ENV/lib/python2.7/site-packages

pip install pytz
pip install ipython
pip install zerodb-server
