import sys
import os
import csv
import os
import pandas as pd
import csv
from .loader import Loader
from master.models import *

def clear():
    Lesson.objects.all().delete()
    StandardCodesAndVerbiage.objects.all().delete()
    SMPText.objects.all().delete()


def ConvertToCsv():
    cwd = os.getcwd()


    dir_path = #INSERTPATHTOFOLDERHERE
    files_to_do_first = ['SMP Text.xlsx','Standards Codes and Verbiage.xlsx']

    for file in files_to_do_first:
        if('.xlsx' in file and '$' not in file):
            xls = pd.ExcelFile(dir_path + '/' + file)
            for sheet in xls.sheet_names:
                df = pd.read_excel(dir_path + '/' + file, sheet_name=sheet,index=False,dtype=str,skiprows=1)
                new_file_name = file.replace('.xlsx',"").replace(' ','')
                csv_file = df.to_csv(index=False)
                split = csv_file.splitlines()
                loaded = Loader(new_file_name,split)
                loaded.loadSheet()


    for file in os.listdir(dir_path):
        if('.xlsx' in file and '$' not in file and file != 'SMP Text.xlsx' and file != 'Standards Codes and Verbiage.xlsx'):
            xls = pd.ExcelFile(dir_path + '/' + file)


            for sheet in xls.sheet_names:
                df = pd.read_excel(dir_path + '/' + file, sheet_name=sheet,index=False,dtype=str,skiprows=1)
                new_file_name = file.replace('.xlsx',"").replace(' ','')
                csv_file = df.to_csv(index=False)
                split = csv_file.splitlines()
                loaded = Loader(new_file_name,split)
                loaded.loadSheet()
