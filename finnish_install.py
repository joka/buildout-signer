#!/usr/bin/env python

# Copyright (C) 2009, Mathieu PASQUET <mpa@makina-corpus.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'


import os
import sys
import re
import subprocess
import shutil

def main(bd, d):
    os.chdir(d)
    dmk = 'DJANGO_SETTINGS_MODULE'
    dm = os.path.abspath(
        os.path.join(bd, 'bin', 'django-admin.py')
    )
    if dmk in os.environ:
        os.environ[dmk]
    if not os.path.exists(os.path.join(d, 'signer_project', '__init__.py')):
        if os.path.exists('REPLACEME_REPLACEME'):
            shutil.rmtree('REPLACEME_REPLACEME')
        subprocess.Popen([dm, 'startproject', 'REPLACEME_REPLACEME']).wait()
        for f in os.listdir('REPLACEME_REPLACEME'):
            if not re.match('^(.*((\.pyc|\.pyo)))$', f):
                fp = os.path.join('REPLACEME_REPLACEME', f)
                content = re.sub('REPLACEME_REPLACEME',
                                 'signer_project.signer_project',
                                 open(fp).read(),
                                 re.M|re.S|re.U)
                if not os.path.exists('signer_project'):
                    os.makedirs('signer_project')
                open(os.path.join('signer_project', f), 'w').write(content)
    if os.path.exists('REPLACEME_REPLACEME'):
        shutil.rmtree('REPLACEME_REPLACEME')

if __name__ == '__main__':
    bd = os.path.abspath(os.path.dirname(__file__))
    dp = os.path.abspath(
        os.path.join(bd,
        'src', 'signer_project', 'src', 'signer_project'))
    main(bd, dp)

# vim:set et sts=4 ts=4 tw=80:
