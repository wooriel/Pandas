## -*- coding: utf-8 -*-
import pandas as pd
import sys

##Copy and paste this code to python version 3 and above
##Save it
##Download School.csv on the same file
##Right Click
##Select Command Promt (명령 프롬프트)
##Type python "[filename].py" "School.csv"
def main(lst):
    column = ["ID", "Name", "School"]
    for i in range(len(lst)):
        csv_file = pd.read_csv(lst[i], header=0, index_col=False, usecols = column)
        print(csv_file)

if __name__ == "__main__":
    #reading filenames from cmd
    if len(sys.argv) > 1:
        lst = []
        for i in range(1, len(sys.argv)):
            lst.append(sys.argv[i])
        main(lst)
    else:
        print("Error: Please Enter Input csv filenames")
