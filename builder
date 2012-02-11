#!/bin/bash

#
# Set up virtualenv and install python modules
#

#[ -d ~/virtualenv ] ||
#    virtualenv --python=python2.7 ~/virtualenv || exit 1
#. ~/virtualenv/bin/activate
#
#[ -f requirements.txt ] &&
#    pip install --download-cache=~/.pip-cache -r requirements.txt || exit 1

# If you want any environment variables to persist in the
# run-time environment, set them below
#cat >>~/profile <<EOF
#. ~/virtualenv/bin/activate
#EOF

rsync -av stunnel $HOME/

