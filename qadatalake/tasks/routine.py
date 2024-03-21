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

class Routine:
    def __init__(self):
        endpoint = getenv("ENDPOINT")
        db = getenv("DB")
        access_key = getenv("ACCESS_KEY")
        secret_key = getenv("SECRET_KEY")
        self.ac = Arctic(f's3s://{endpoint}:{db}?access={access_key}&secret={secret_key}')

    def list_all_symbols(self):
        print("[QA DATALAKE] : START SYMBOL LISTING")
        print(f"CURRENTLY HAVE {len(self.ac.list_libraries())} DBS FOR LIST")
        print("STARTING LISTING LOOP")
        for symbol in self.ac.list_libraries():
            load = self.ac.get_library(symbol)
            load.list_symbols()
            print(f"[QA DEBUG] | SYMBOL : {symbol} LISTED")
            print(f"[QA DEBUG] | {symbol} HAS {len(load.list_symbols())} SYMBOLS")
            print("====================================")        