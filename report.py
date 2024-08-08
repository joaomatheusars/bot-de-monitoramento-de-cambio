import os, sys
from docx2pdf import convert


def report(filename: str):
    if not os.path.isdir(f"{os.getcwd()}/report"): os.mkdir(f'{os.getcwd()}/report')
    
    report_name = filename.split('-')
    dir = f'{report_name[0]}-{report_name[1]}-{report_name[2]}'
    
    if not os.path.isdir(f'{os.getcwd()}/report/{dir}'): 
        os.mkdir(f'{os.getcwd()}/report/{dir}')
        sys.stderr = open("consoleoutput.log", "w")
        convert(f'{os.getcwd()}/word/{filename}.docx', f'{os.getcwd()}/report/{dir}')
    else:
        sys.stderr = open("consoleoutput.log", "w")
        convert(f'{os.getcwd()}/word/{filename}.docx', f'{os.getcwd()}/report/{dir}')
    