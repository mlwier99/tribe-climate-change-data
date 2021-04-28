#Packages
import requests 
import os, time, random, errno
from datetime import datetime
from datetime import date
from ast import literal_eval
import pdfkit
import urllib
import signal 
import googlesearch # Package documentation: https://python-googlesearch.readthedocs.io/en/latest/
#from googlesearch import search
import sys

print("googlesearch package located in" ,googlesearch.__file__)

####################################### Directory Changes
orgdir = os.getcwd() 
print("The original working directory is:", orgdir) 

if os.path.exists('/home/michelle/Dropbox/RA Work/Spring 2021, TP/Native Environment Data/')==True: 
  os.chdir('/home/michelle/Dropbox/RA Work/Spring 2021, TP/Native Environment Data/')
else: 
  os.chdir('./Dropbox/RA Work/Spring 2021, TP/Native Environment Data/')

if os.path.exists('Tribe Directories'): 
  print('Directory contining tribe sub-directories exists.')
else:
  os.mkdir('./Tribe Directories')
  print("Created directory that will contain the tribe sub-directories.")

###################################### Lists
# Tribes 
tribe_names = [
#"Tunica-Biloxi Indian Tribe of Louisiana",
#"Tuolumne Band of Me-Wuk Indians of the Tuolumne Rancheria of California",
#"United Auburn Indian Community of the Auburn Rancheria of California",
#"Upper Sioux Community",
#"Village of Alakanuk",
#"Village of Kalskag",
#"Village of Lower Kalskag",
"Village of Venetie",
#"White Mountain Apache Tribe of the Fort Apache Reservation",
#"Wilton Rancheria",
#"Yocha Dehe Wintun Nation, California",
#"Yomba Shoshone Tribe of the Yomba Reservation",
#"Puyallup Tribe of the Puyallup Reservation"
]

print("Number of tribes in list:", len(tribe_names))

#Search terms (in quotes/strict)
search_terms = ['"climate change"', '"enviornmental"', '"global warming"']
print("Search terms:", search_terms)


###################################### Creating Subdirectories
#Google Searches 
# writing tribe name as "category" into .docx 

for t in range(0,len(tribe_names)): #for each tribe
#creating tribe subdirectories
  tribe_subdir = './Tribe Directories/' + tribe_names[t]
  if os.path.exists(tribe_subdir)==False: 
    os.mkdir(tribe_subdir)
#Tribe-Specific: Docuemnts Folder for Each Tribe
  tribe_doc_subdir = './Tribe Directories/' + tribe_names[t] + "/PDFs"
  if os.path.exists(tribe_doc_subdir)==False: 
    os.mkdir(tribe_doc_subdir)
#Tribe-Specific: Link .docx for Each Tribe
  tribe_path = "./Tribe Directories/" + tribe_names[t] + "/" + tribe_names[t] + "_links.txt"
  if os.path.isfile(tribe_path)==False:  #if file doesn't exist
    with open(tribe_path, "w") as file: #creating link-dump docx 
      file.write(tribe_names[t]) #writing in the tribe name 
      file.write("\n\n") #extra space after tribe heading
      file.close #closing file 
  #Tribe-Specific: Docuemnts Folder for Each Tribe
  tribe_doc_subdir = './Tribe Directories/' + tribe_names[t] + "/PDFs"
  if os.path.exists(tribe_doc_subdir)==False: 
    os.mkdir(tribe_doc_subdir)

    
  #Actually determining and running search 
  link_docx = tribe_path
  t_num_index = t 
  t_index = f'{t_num_index}' #making tribe index a string
  total_tribes = f'{len(tribe_names)}'
  print('Finding links for ' + tribe_names[t]) #tell user which tribe and term search for 
  for s in range(len(search_terms)): #for the tribe's three search terms
    search_term = (tribe_names[t] + ' ' + search_terms[s]) #create term that's tribe + cc or gw or env
    googleresults = googlesearch.search(search_term, num_results=10) #and get first ten results from google for each cc/gw/env
    with open(link_docx, "a") as file: #open that link-dump docx for appending links 
      file.write("\n")
      file.write(search_terms[s]) #and copy each link into that file
      file.write("\n") #while making sure to have a new line between each
    #print("Number of results in list: " + f'{len(googleresults)}')
    while len(googleresults) > 10:
      del googleresults[-1]
      #print("Number of google link results: " + f'{len(googleresults)}')
    print("Number of results in list: " + f'{len(googleresults)}')
    for r in range(0,len(googleresults)): #for each link (ten per term, thirty per tribe)
      print('Tribe ' + t_index + " of "+ total_tribes + " (" + tribe_names[t] + ")")
      r_num_index = r  
      r_index = f'{r_num_index}' #making results index a string
      if search_terms[s]=='"climate change"':
        search_term_short = "cc"
      if search_terms[s]=='"enviornmental"':
        search_term_short = "env"
      if search_terms[s]=='"global warming"':
        search_term_short = "gw"
      #print("Progress: " + search_term_short + " " + r_index) 
      with open(link_docx, "a") as file: #open that link-dump docx for appending links 
        file.write(r_index)
        file.write(". ")
        file.write(googleresults[r]) #and copy each link into that file
        file.write("\n") #while making sure to have a new line between each
        time.sleep(1) #and now sleep for a few seconds to avoid 429. 
      
      
      link_as_pdf = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".pdf"
      pdf_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".pdf"
      docx_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".docx"
      excel_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".xlsx"
      xml_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".xml"
      txt_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".txt"
      png_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".png"
      jpg_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + ".jpg"
      youtube_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short +  r_index + "_youtube.pdf"
      
      if googleresults[r].endswith('pdf'):
        print(search_term_short + " " + r_index + " (pdf)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(pdf_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif f'{googleresults[r]}'.startswith('https://www.youtube.com/'):
        print(search_term_short + " " + r_index + " (youtube video)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(youtube_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('docx'):
        print(search_term_short + " " + r_index + " (docx)")
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(docx_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('xlsx'):
        print(search_term_short + " " + r_index + " (xlsx)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(excel_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('xml'):
        print(search_term_short + " " + r_index + " (xml)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(xml_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('jpg'):
        print(search_term_short + " " + r_index + " (jpg)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(jpg_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('jpeg'):
        print(search_term_short + " " + r_index + " (jpg)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(jpg_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('png'):
        print(search_term_short + " " + r_index + " (png)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(png_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif googleresults[r].endswith('txt'):
        print(search_term_short + " " + r_index + " (txt)") 
        try: 
          url = googleresults[r] 
          r = requests.get(url, stream=True)
          with open(txt_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      else:
        print(search_term_short + " " + r_index + " (unknown/html)") 
        try:
          pdfkit.from_url(googleresults[r], link_as_pdf)
        except:
          pass 
            

