#########
#
# QA Datalake
# - - - - - 
# Master CLI
# Manage the Dataleke from a easy CLI
# 3/24 QUANTARMY.COM
##########

from os import system 
from time import sleep
from dotenv import load_dotenv, set_key
from os import getenv
from arcticdb import Arctic

dotenv_path = '.env'
load_dotenv(dotenv_path)

class Metadata:
    def __init__(self):
        endpoint = getenv("ENDPOINT")
        db = getenv("DB")
        access_key = getenv("ACCESS_KEY")
        secret_key = getenv("SECRET_KEY")
        self.ac = Arctic(f's3s://{endpoint}:{db}?access={access_key}&secret={secret_key}')

    def stocks_metadata(self):
        pass