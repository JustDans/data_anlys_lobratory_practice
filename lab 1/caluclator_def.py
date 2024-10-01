from functions_calc import *

def calculator():
    while(True):
        choose_mode()
        inp = input("введите '1' если хотите повторить цикл")
        if (inp!='1'):
            print("цикл завершён")
            break