####################################### Packages
import os
import csv, fnmatch

#excel file are annoying me atm, writing to csv instead

####################################### Directory Changes
if os.path.exists('/home/michelle/Dropbox/RA Work/Spring 2021, TP/Native Environment Data/'): 
  os.chdir('/home/michelle/Dropbox/RA Work/Spring 2021, TP/Native Environment Data/')
else: 
  os.chdir('./Dropbox/RA Work/Spring 2021, TP/Native Environment Data/')
  
print("Current directory is ", os.getcwd()) 

####################################### Writing to .csv

# Checking (potentially creating) Documents folder.
if os.path.exists('Documents'): 
  print('Documents folder exists.')
else:
  os.mkdir('./Documents')
  print("Created folder that will contain documents.")


# Creating and placing header on CSV file
file = "./Documents/List of Saved Links for Each Tribe.csv"

with open(file, 'w', newline='') as csvfile:
    count = csv.writer(csvfile, delimiter='\t')
    count.writerow(['Tribe'] + ['Total Files'] + ['Climate Change Files'] +
      ['Enviornment Files'] + ['Global Warming Files'] + ['Directory'])

# Path to directories, list of tribe directories. 
input_path = "./Tribe Directories/"
tribe_dirs = [d for d in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, d))]

# Loop through all tribe directories/PDF folder, counting number of files (total and each type)
for t in range(len(tribe_dirs)):
  print(tribe_dirs[t])
  pdf_path = './Tribe Directories/' + tribe_dirs[t] + "/PDFs/"
  
  total_folders = 0
  cc_folders = 0
  env_folders = 0 
  gw_folders = 0

  total_folders = len(os.listdir(pdf_path))
  cc_folders = len(fnmatch.filter(os.listdir(pdf_path),'cc*'))
  env_folders = len(fnmatch.filter(os.listdir(pdf_path),'env*'))
  gw_folders = len(fnmatch.filter(os.listdir(pdf_path),'gw*'))
  
  with open(file, 'a', newline='') as csvfile:
    writer=csv.writer(csvfile)
    count = csv.writer(csvfile, delimiter='\t')
    count.writerow([tribe_dirs[t]] + [total_folders] + [cc_folders] + 
      [env_folders] + [gw_folders] + [pdf_path])
  
