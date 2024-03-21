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
from tasks.routine import Routine 
from data.alphavantage import AlphaVantage

class QACLI:
    def __init__(self):
        self.version = "V.5.1.0-predator"

    def normal_routine(self):
        r = Routine()
        r.list_all_symbols()

    def unemployement_routine(self):
        r = AlphaVantage()
        r.us_unemployment()
        r.us_inflation()
    
    def kill(self):
        print("- - -")
        print("[QA DATALAKE] - BYE")
        exit()
        sleep(4)
        system('clear') 
    
    def display(self):
        while True:
            print("QA DATALAKE")
            print(self.version)
            print("1. LIST ALL SYMBOLS")
            print("2. UNEMPLOYMENT ROUTINE")
            print("3. KILL")

            opcion = input("RUN A COMMAND: ")

            if opcion == "1":
                self.normal_routine()
            elif opcion == "2":
                self.unemployement_routine()
            elif opcion == "3":
                self.kill()
            else:
                print("- - -")
                print("[QA DATALAKE] : (???) WRONG OPTION")

if __name__ == "__main__":
    menu = QACLI()
    menu.display()