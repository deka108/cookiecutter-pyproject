import os
import re
import sys
from subprocess import check_call, CalledProcessError
try:
    from shutil import which
except ImportError:
    from distutils.spawn import find_executable as which

MODULE_REGEX = r'^[_a-z][_a-z0-9-]+$'

project_name = '{{ cookiecutter.pkg_name }}'

if not re.match(MODULE_REGEX, project_name):
    print('ERROR: {} is not a valid Dash App project name!\n'
          'Project Name should be lowercase, cannot begin with digits, '
          'contains no special character and may contain hyphens or underscores'.format(project_name))
    sys.exit(1)

# Check if make is available, if not exit the program
if not which("make") :
    sys.exit("No `make` installed. Please install `make` on your workspace.")
