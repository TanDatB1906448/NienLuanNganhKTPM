import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("Key")
path = os.path.dirname(__file__)
UPLOAD_FOLDER = path + os.environ.get("uf")
DLMODEL = path + os.environ.get("modelPath")
# UPLOAD_FOLDER =os.getcwd() + os.environ.get("uf")