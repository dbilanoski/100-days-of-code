### Challenge: 
  # There is a .zip file called 'unzip_me_for_instructions.zip' on the github repo of the course, unzip it, open the .txt file with Python, read the instructions and see if you can figure out what you need to do!


# Download a file (since I do not have whole repo cloned)
  # For that, I need requests or urllib library

from urllib import request
import os
import re

# Define url with file for download
url = "https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/raw/master/12-Advanced%20Python%20Modules/08-Advanced-Python-Module-Exercise/unzip_me_for_instructions.zip"

# Define local filename for saving the downloaded file
local = os.getcwd()+"\\instructions.zip"

request.urlretrieve(url, local)

# Unzip it

import zipfile

instructions = zipfile.ZipFile(local,"r")
instructions.extractall(os.getcwd()+"\\extracted")

# Got the instructions
'''
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
Good luck!
'''

# Prepare regex pattern
phone_pattern = r"\d{3}-\d{3}-\d{4}"

# Get the files with OS methods
lookup_folder = os.walk(os.getcwd()+"\\extracted")

for folder, subfolders, files in lookup_folder:

  for file in files:
    # We need to open file, then dump content into variable
    # Then check with regex pattern if there is a match

    # To get absoulute path to file we use os.path.join(folder, file)
    with open(os.path.join(folder,file)) as current_file:
      contents = current_file.read()
      match = re.search(phone_pattern,contents)

      if match:
       print(match.group())
       print(os.path.join(folder,file))
       break

# Result 719-266-2837 in E:\Projekti\Python_learning\11_Useful_Python_Modules\challenge_files\extracted\extracted_content\Four\EMTGPSXQEJX.txt