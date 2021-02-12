#Packages
import requests 
import os, time, random, errno
from datetime import datetime
from datetime import date
from ast import literal_eval
import pdfkit
import urllib
import googlesearch # Package documentation: https://python-googlesearch.readthedocs.io/en/latest/
#from googlesearch import search

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
"Rampart Village",
"Habematolel Pomo of Upper Lake",
"Monacan Indian Nation",
"Native Village of Nikolski",
"Kaibab Band of Paiute Indians of the Kaibab Indian Reservation",
"Ninilchik Village",
"Galena Village",
"King Salmon Tribe",
"Colorado River Indian Tribes of the Colorado River Indian Reservation California",
"Manokotak Village",
"Saint George Island",
"Native Village of Eagle",
"Citizen Potawatomi Nation",
"Native Village of Chignik Lagoon",
"Chignik Bay Tribal Council",
"Native Village of Teller",
"Navajo Nation Utah",
"Standing Rock Sioux Tribe North Dakota",
"Oscarville Traditional Village",
"Eastern Shoshone Tribe of the Wind River Reservation, Wyoming",
"Kewa Pueblo, New Mexico",
"Inupiat Community of the Arctic Slope",
"Village of Atmautluak",
"Akiachak Native Community",
"Ivanof Bay Tribe",
"Native Village of Napaskiak",
"Delaware Tribe of Indians",
"Ute Mountain Ute Tribe New Mexico",
"Penobscot Nation",
"Lime Village",
"Standing Rock Sioux Tribe South Dakota",
"Blackfeet Tribe of the Blackfeet Indian Reservation of Montana",
"Kaguyak Village",
"Petersburg Indian Association",
"Alabama-Quassarte Tribal Town",
"Sycuan Band of the Kumeyaay Nation",
"Village of Crooked Creek",
"Alabama-Coushatta Tribe of Texas",
"Pascua Yaqui Tribe of Arizona",
"Hoonah Indian Association",
"Native Village of Selawik",
"Winnemucca Indian Colony of Nevada",
"Shageluk Native Village",
"Village of Salamatoff",
"Pueblo of Taos",
"Pawnee Nation of Oklahoma",
"Little Traverse Bay Bands of Odawa Indians",
"Native Village of Napakiak",
"Native Village of Nunam Iqua",
"Lummi Tribe of the Lummi Reservation",
"Native Village of Nunapitchuk",
"Arctic Village",
"Saint Regis Mohawk Tribe",
"Southern Ute Indian Tribe of the Southern Ute Reservation",
"Pechanga Band of Luisemo Mission Indians of the Pechanga Reservation",
"Agua Caliente Band of Cahuilla Indians of the Agua Caliente Indian Reservation",
"Nooksack Indian Tribe of Washington",
"Navajo Nation Arizona",
"Rappahannock Tribe, Inc.",
"Northern Cheyenne Tribe of the Northern Cheyenne Indian Reservation",
"Native Village of Pitka's Point",
"Native Village of Cantwell",
"Cher-Ae Heights Indian Community of the Trinidad Rancheria",
"Native Village of Perryville",
"Three Affiliated Tribes of the Fort Berthold Reservation",
"Native Village of Kwigillingok",
"Native Village of Noatak",
"Native Village of Akutan",
"Native Village of Napaimute",
"Native Village of Tyonek",
"Nome Eskimo Community",
"Village of Iliamna",
"Organized Village of Kasaan",
"Native Village of Wales",
"Native Village of Kobuk",
"Jicarilla Apache Nation",
"Ugashik Village",
"Organized Village of Saxman",
"Native Village of Nightmute",
"Native Village of Ekuk",
"Sitka Tribe of Alaska",
"Native Village of Tununak",
"Pyramid Lake Paiute Tribe of the Pyramid Lake Reservation",
"Organized Village of Kake",
"Navajo Nation New Mexico",
"Evansville Village (aka Bettles Field)",
"Skull Valley Band of Goshute Indians of Utah",
"Confederated Tribes of the Goshute Reservation Utah",
"Tonkawa Tribe of Indians of Oklahoma",
"Village of Chefornak",
"La Jolla Band of Luiseno Indians, California",
"Native Village of Point Lay",
"Native Village of Tazlina",
"Native Village of Point Hope",
"Pribilof Islands Aleut Communities of St. Paul & St. George Islands",
"Pueblo of Jemez",
"Hopi Tribe of Arizona",
"Sac & Fox Nation of Missouri Nebraska",
"Sac & Fox Nation of Missouri Kansas",
"Pala Band of Mission Indians",
"Pamunkey Indian Tribe",
"Sac & Fox Tribe of the Mississippi in Iowa",
"Chitimacha Tribe of Louisiana",
"Yerington Paiute Tribe of the Yerington Colony & Campbell Ranch",
"Native Village of Shishmaref"
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
    print("Created folder for:", tribe_names[t])
  else: 
    print("Already-existing folder for:", tribe_names[t])
#Tribe-Specific: Docuemnts Folder for Each Tribe
  tribe_doc_subdir = './Tribe Directories/' + tribe_names[t] + "/PDFs"
  if os.path.exists(tribe_doc_subdir)==False: 
    os.mkdir(tribe_doc_subdir)
    print("Created documents folder for:", tribe_names[t])
  else: 
    print("Already-existing document folder for:", tribe_names[t])
#Tribe-Specific: Link .docx for Each Tribe
  tribe_path = "./Tribe Directories/" + tribe_names[t] + "/" + tribe_names[t] + "_links.txt"
  if os.path.isfile(tribe_path)==False:  #if file doesn't exist
    with open(tribe_path, "w") as file: #creating link-dump docx 
      file.write(tribe_names[t]) #writing in the tribe name 
      file.write("\n\n") #extra space after tribe heading
      file.close #closing file 
    print("Created .txt link file for:", tribe_names[t])
  else: 
    print("Already-existing .txt link file for:", tribe_names[t])
  #Tribe-Specific: Docuemnts Folder for Each Tribe
  tribe_doc_subdir = './Tribe Directories/' + tribe_names[t] + "/PDFs"
  if os.path.exists(tribe_doc_subdir)==False: 
    os.mkdir(tribe_doc_subdir)
    print("Created documents folder for:", tribe_names[t])
  else: 
    print("Already-existing document folder for:", tribe_names[t])
    
    
  #Actually determining and running search 
  link_docx = tribe_path
  for s in range(len(search_terms)): #for the tribe's three search terms
    search_term = (tribe_names[t] + ' ' + search_terms[s]) #create term that's tribe + cc or gw or env
    print('Finding links for ' + search_term) #tell user which tribe and term search for 
    search_results = googlesearch.search(search_term, num_results=9) #and get first ten results from google for each cc/gw/env
    s_num_index = s
    s_index = f'{s_num_index}'
    with open(link_docx, "a") as file: #open that link-dump docx for appending links 
      file.write("\n")
      file.write(search_terms[s]) #and copy each link into that file
      file.write("\n") #while making sure to have a new line between each
    for r in range(len(search_results)): #for each link (ten per term, thirty per tribe)
      r_num_index = r  
      t_num_index = t 
      r_index = f'{r_num_index}' #making results index a string
      t_index = f'{t_num_index}' #making tribe index a string
      total_tribes = f'{len(tribe_names)-1}'
      if search_terms[s]=='"climate change"':
        search_term_short = "cc"
      if search_terms[s]=='"enviornmental"':
        search_term_short = "env"
      if search_terms[s]=='"global warming"':
        search_term_short = "gw"
      print("Progress: link " + r_index + " for " + search_terms[s] + ", tribe " + t_index + " of "+ total_tribes + " total.")
      with open(link_docx, "a") as file: #open that link-dump docx for appending links 
        file.write(r_index)
        file.write(". ")
        file.write(search_results[r]) #and copy each link into that file
        file.write("\n") #while making sure to have a new line between each
        time.sleep(1) #and now sleep for a few seconds to avoid 429. 
      
      
      link_as_pdf = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".pdf"
      pdf_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".pdf"
      docx_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".docx"
      excel_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".xlsx"
      xml_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".xml"
      txt_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".txt"
      png_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".png"
      jpg_download = "./Tribe Directories/" + tribe_names[t] + "/PDFs/" + search_term_short + "_link" +  r_index + ".jpg"
      if search_results[r].endswith('pdf'):
        print("pdf")#download pdf 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(pdf_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('docx'):
        print("docx")#download docx 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(docx_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('xlsx'):
        print("excel")#download xlsx 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(excel_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('xml'):
        print("xml")#download xml 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(xml_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('jpg'):
        print("jpg")#download jpg 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(jpg_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('jpeg'):
        print("jpg")#download jpg 
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(jpg_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('png'):
        print("png")#download png
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(png_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      elif search_results[r].endswith('txt'):
        print("txt")#download txt
        try: 
          url = search_results[r] 
          r = requests.get(url, stream=True)
          with open(txt_download, 'wb') as f:
            f.write(r.content)
        except: 
          pass
      else:
        print("link")
        try:
          pdfkit.from_url(search_results[r], link_as_pdf)
        except:
          pass 
            
      
