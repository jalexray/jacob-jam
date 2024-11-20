import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
	SERVER_MODE = os.environ.get('SERVER_MODE') or 'development'
	
	# Filepath
	FILEPATH = basedir