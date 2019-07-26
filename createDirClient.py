import os
import argparse

# Script to create a new directory for a new client / project

cwd = os.getcwd()

parser = argparse.ArgumentParser(description = ' Create a directory with files')
parser.add_argument("--name", '-n', help = "Name of the folder")
parser.add_argument("--date", '-d', help = "Optional Date : Date of the Folder" )
args = parser.parse_args()

name = args.name

#Create /ClientName
os.makedirs(cwd + '\\' + name)

#Create /ClientName/Constantes Vitales
os.makedirs(cwd + '\\' + name + '\\' + 'Constantes Vitales')
os.makedirs(cwd + '\\' + name + '\\' + 'Historial Clinico')
os.makedirs(cwd + '\\' + name + '\\' + 'Notas de las sesiones')

