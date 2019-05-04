# pythonutils

Some miscellaneous Python Utilities

1) Bulk Google Static Maps Extraction

   Two files : cities.csv and gmapstatic.py
   cities.csv file has three columns
   First one is City name, next two are latitude and longitude
   There should't be any header column.
   gmapstatic.py : You should take Google Static maps API key 
   and assign it to the variable "api_key" in the script.
   You are prompted to select the csv file and the directory
   in which the output map images are to be stored.
   There is a sleep time of five seconds after the request is made
   to the google server, and after the write statement. you can    adjust this time as per your requirement.
2) csvutils.py : csv file viewing and editing utility.
   It also can convert the csv file to the xml file.
   First row should be the header row in the csv file.
3) imgbnw.py: It converts all png images to black and white png
   images in bulk mode. You have to replace the input and output
   folder names in the lines
   path = 'c:\\mapimages\\'
   newpath = 'c:\\mapimages\\gray\\'
