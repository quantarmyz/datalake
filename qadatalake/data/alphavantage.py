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
import requests
from dotenv import load_dotenv, set_key
from os import getenv
from arcticdb import Arctic
import pandas as pd 
from datetime import datetime

dotenv_path = '.env'
load_dotenv(dotenv_path)

class AlphaVantage:
    def __init__(self):
        endpoint = getenv("ENDPOINT")
        db = getenv("DB")
        access_key = getenv("ACCESS_KEY")
        secret_key = getenv("SECRET_KEY")
        self.ac = Arctic(f's3s://{endpoint}:{db}?access={access_key}&secret={secret_key}')
        self.apikey = 'D1KJ0VXUQTA6O172'
        self.macro_db = 'alphavantage'
        self.unemployment_ticker = 'UNEMPLOYMENT.MACRO.US'
        self.inflation_ticker = 'INFLATION.MACRO.US'

    def us_unemployment(self):
        url = f'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={self.apikey}&datatype=csv'
        paro = pd.read_csv(url)
        paro['timestamp'] = pd.to_datetime(paro['timestamp'])
        paro = paro.set_index(paro['timestamp'].sort_index(ascending=False))
        paro = paro.drop(columns=['timestamp'])
        print(paro)
        if self.ac.has_library(self.macro_db):
            last_update = datetime.strptime(getenv(self.macro_db), "%Y-%m-%d")
            today = datetime.now()
            if (today - last_update).days >= 15:
                self.ac.get_library(self.macro_db).append(self.unemployment_ticker, paro)
                set_key('.env', self.macro_db, today.strftime("%Y-%m-%d"))
                print('[QA DEBUG] | UNEMPLOYMENT DATA STORED')
            else:
                print('[QA DEBUG] | UNEMPLOYMENT DATA ALREADY UPDATED ')
        else:
            self.ac.create_library(self.macro_db)
            pointer = self.ac.get_library(self.macro_db)
            pointer.write(self.unemployment_ticker, paro)
            set_key('.env', self.macro_db, datetime.now().strftime("%Y-%m-%d"))
            print('[QA DEBUG] | UNEMPLOYMENT DATA STORED')

    def us_inflation(self):
        url = f'https://www.alphavantage.co/query?function=INFLATION&apikey={self.apikey}&datatype=csv'
        inflation = pd.read_csv(url)
        inflation['timestamp'] = pd.to_datetime(inflation['timestamp'])
        inflation = inflation.set_index(inflation['timestamp'].sort_index(ascending=False))
        inflation = inflation.drop(columns=['timestamp'])
        print(inflation)
        if self.ac.has_library(self.macro_db):
            last_update = datetime.strptime(getenv(self.macro_db), "%Y-%m-%d")
            today = datetime.now()
            if (today - last_update).days >= 15:
                self.ac.get_library(self.macro_db).append(self.inflation_ticker, inflation)
                set_key(dotenv_path, self.macro_db, today.strftime("%Y-%m-%d"))
                print('[QA DEBUG] | UNEMPLOYMENT DATA STORED')
            else:
                print('[QA DEBUG] | UNEMPLOYMENT DATA ALREADY UPDATED ')
        else:
            self.ac.create_library(self.macro_db)
            pointer = self.ac.get_library(self.macro_db)
            pointer.write(self.inflation_ticker, inflation)
            set_key('.env', self.macro_db, datetime.now().strftime("%Y-%m-%d"))
            print('[QA DEBUG] | UNEMPLOYMENT DATA STORED')