import os
import sys

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))

# Where our files are located.
sys.path.append(CURRENT_DIR )

# Location of the virtualenv.
sys.path.append(PROJECT_DIR + '/aqenv/lib/python3.7/site-packages/')

from app import app as application