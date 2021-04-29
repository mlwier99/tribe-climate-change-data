# Tribal Climate Change Actions Data 

**Author:** Michelle Wier

**Original Date:** January 2021 to April 2021

**Last Updated Code:** April 2021

**Programs/Languages:** RStudio, Python, Mousepad, LibreOffice Calc/Microsoft Excel, LibreOffice Writer/Microsoft Office

## Project
### Description
Retrieves first page of Google results for all federally-recognized Native American tribes and downloads links regarding climate change actions.

## Files
### File Structure
  * suggested working directory for project: ``./home/[profile]/Native Environment Data/``
  * suggested path for scripts: ``./Scripts``
  * generated path and folders: ``./Documents``
  * generated path and folders: ``./Tribe Directories``
  * generated path and folders: ``./Tribe Directories/[each tribe looped through]`` 
  * generated path and folders: ``./Tribe Directories/[each tribe looped through]/PDFs``
  
### Files Uploaded
#### DirSearchPrint.py
* Combines each tribe from the Federal Registry (2021) with one of three search terms, then retreives the first ten results for each tribe-term. 
* If it doesn't already exist, will script creates ``./Tribe Directories folder.''
* During the loop, for each tribe that has been run, the code generates two additional folders: ``./Tribe Directories/[each tribe]`` and ``./Tribeies/[each tribe]/PDFs``. 
   + If these folders already exist, the script does *not* override over them. 
   + If the code is re-run, it's suggested that the tribe's folder is deleted or renamed manually.
* in each ``./Tribe Directories/[each tribe]``, a .txt file is created (``[tribe name]_links.txt``). This file will print a series of links, numbered, for the three different searc Directorh terms.
   + These .txt files are append-only, so if the code is re-run, make sure to delete or rename the .txt for the tribe that's being re-run (or the entire Tribe Directories folder). Otherwise, you'll have more than one section for each search-term.
* In the same loop as the list of links and the .txt file, the link will be saved. When the link is .pdf, .xlsx, .docx, etc, the same file extension will be on the saved copy of the link. If .html or unspecified, the link is printed/saved a .pdf. 
   + These are saved in ``./Tribe Directories/[each tribe]/PDFs``. The sub-folder name is due to the fact that a majority of the saved files are in .pdf format. 
   + Occassionally, this area of the process takes a long time. In many instances, it's necessary to crtl+c a tribe. If crtl+c is used once, then the loop moves on to the next tribe. This is suggested. Using crtl+c more than once on the same loop iteraction causes the entire code to stop running. If this happens, find the recent tribe sub-directory and delete it to prevent multiple entries for the same search-term in the .txt file. 
#### PDF List for Tribes.py
* creates a ``./Documents`` folder if it does not already exist (this folder will be in the same location as ``./Tribe Directories``. 
* creates ``./Documents/List of Saved Links for Each Tribe.csv``
* in ``./Documents/List of Saved Links for Each Tribe.csv``, follownig variables are recorded: 
   + each tribe that has a folder in ``./Tribe Directories``
   + the number of total files for each of those tribes 
   + the number of saved documents/downloaded links for each of the search terms (theoretically 30, but not every link is able to be saved) 
   + the name of the directory where the saved/downloaded links are contained
* this code WILL overwrite an existing ``./Documents/List of Saved Links for Each Tribe.csv``, so if you want to compare current to previous, I suggest manually renaming your existing file. 
#### TribeList.txt
* list of the tribes (590) that I cleaned (removed Unicode, etc) and copied to the script. The tribes should already be in the DirSearchPrint.py. 
#### Codebook.pdf
* Codebook for the coded data; data files (.xlsx) may be available upon request.

## Notes 
* I highly suggested this be run through the terminal (``./[script location]/DirSearchPrint.py`` and ``./[script location/PDF List for Tribes.py``). 
 <!-- Make sure to check the ./Tribe Directories/[each tribe] names occassionally. At one point, tribe names in the list were merged together, likely due to a missing comma between list items in the tribe name list. It should be fixed now, but it's something to keep an eye out for. -->
<!--  - Rather than deleting tribe sub-folders when I rerun a tribe, I rename folders--example, ./Tribe Directories  ./Tribe Direcotires_Feb when I rerun all the tribes in March, etc. I tend to zip the old folders to save space. -->
 
 
 
*Added to GH:* April 25 2021

*Updated on GH:* April 26, 2021

