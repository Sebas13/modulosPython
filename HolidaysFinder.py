import argparse
import os
import webbrowser
import openpyxl

cwd = os.getcwd()

parser = argparse.ArgumentParser(description='Tool to compare holidays options')
parser.add_argument("--destination1", "-d1", help='First point of the destination you want to go')



