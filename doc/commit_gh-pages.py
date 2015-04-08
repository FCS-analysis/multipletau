#!/usr/bin/env python
from __future__ import print_function
import os
from os.path import abspath,dirname
import sys
import subprocess as sp


os.chdir(dirname(dirname(abspath(__file__))))


def checkout_master():
    # go back to master
    sp.check_output(["git", 'checkout', 'master'])

    print("Applying saved stash.")
    # get last stash
    sp.check_output(["git", 'stash', 'apply'])


def checkout_ghpages():
    # commit changes of master
    print("Automatically stashing current changes.")
    sp.check_output(["git", 'stash'])

    # checkout the gh-pages branch
    sp.check_output(["git", 'checkout', 'gh-pages'])

checkout_ghpages()


# copy built files
if os.system("cp -r ./build/sphinx/html/* ./") != 0:
    checkout_master()
    sys.exit()

for item in os.listdir("./build/sphinx/html/"):
    # Make sure we have added all files from html
    if not item.startswith("."):
        os.system("git add ./{}".format(item))

# commit changes
if len(sp.check_output(["git", "diff", "HEAD"]).strip()) > 0:
    sp.check_output(["git", 'commit', '-a', '-m', '"automated doc upload"'])

# push
try:
    sp.check_output(["git", 'push'])
except:
    print("Could not push to gh-pages.")

checkout_master()
