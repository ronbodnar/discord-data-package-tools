'''
This script is used to download attachment files from Discord data packages.

Place this script inside of a directory that contains the extracted "package" folder from Discord and run it.

Created by Ron Bodnar
https://github.com/ronbodnar

Licensed under the MIT License: http://opensource.org/licenses/MIT
'''
import os
import csv
import requests

from glob import glob
from csv import writer

# Constant variables for directories
OUTPUT_DIRECTORY = "attachments"
DISCORD_PACKAGE_PATH = "{}{}package{}".format(os.getcwd(), os.sep, os.sep)

index = 0
links = []
files = [file for path, subdir, files in os.walk(DISCORD_PACKAGE_PATH) for file in glob(os.path.join(path, "*.csv"))]

print(f"Scanning messages for attachments in {DISCORD_PACKAGE_PATH}...")

# Iterate over all csv files in Discord package data directory
for file in files:
    print("Scanning {} for attachments...".format(file), end="")
    with open(file, encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # Multiple attachments can be split by a '& ' delimiter, we want to capture those.
            if '& ' in row[3]:
                split = row[3].split("& ")
                for s in split:
                    links.append(s.replace('& ', '').split("?ex=")[0])
                    
            # Multiple attachments can be split by a ',' delimiter, we want to capture those.
            elif ',' in row[3]:
                split = row[3].split(",")
                for s in split:
                    links.append(s.split("?ex=")[0])
                    
            # Capture everything else except for "Attachments" headers.
            elif row[3] and 'Attachments' not in row[3]:
                links.append(row[3].split("?ex=")[0])
        print("DONE")
                
print("Number of attachment links found: {}".format(len(links)))
print("Populating attachment-links.csv file with {} links...".format(len(links)), end="")

# Iterate over the found links and populate the attachment-links.csv file.
for link in links:
    with open('attachment-links.csv', 'a', newline='', encoding="utf-8") as file:
        fwriter = writer(file)
        fwriter.writerow([link])
        file.close()
        
print("DONE")

print("Setting up directories for attachment downloads...", end="")
os.makedirs('attachments', exist_ok=True) # Create the attachments directory, ignore if exists.
print("DONE")
       
print("Beginning downloads...")
# Iterate over all links found in the messages CSV files.
for link in links:
    slashIndexes = [pos for pos, char in enumerate(link) if char == "/"] # Find a list of indexes for the "/" character within the link.
    
    file_name = link[slashIndexes[5]:] # Extracted file name from the link.
    file_path = '{}{}{}'.format(OUTPUT_DIRECTORY, os.sep, file_name)
    
    print("Downloading attachment {}/{} from {}...".format(index, len(links), link), end="")
    
    with open(file_path, 'wb') as handler:
        data = requests.get(link).content
        handler.write(data)
        index += 1
        print("DONE")