'''
This script is used to aggregate messages from the Discord data package into a single CSV file.

Place this script inside of a directory that contains the extracted "package" folder from Discord and run it.

Created by Ron Bodnar
https://github.com/ronbodnar

Licensed under the MIT License: http://opensource.org/licenses/MIT
'''
import os
import csv 

from glob import glob
from csv import writer

DISCORD_PACKAGE_PATH = "{}{}package{}".format(os.getcwd(), os.sep, os.sep)

numConversations = numAttachments = 0

messages = []
files = [file for path, subdir, files in os.walk(DISCORD_PACKAGE_PATH) for file in glob(os.path.join(path, "*.csv"))]

for file in files:
    with open(file, encoding="utf-8") as file:
        reader = csv.reader(file)
        slashIndexes = [pos for pos, char in enumerate(file.name) if char == "\\"]
        correspondentId = file.name[slashIndexes[6]+1:slashIndexes[7]]
        numConversations += 1
        for row in reader:
            if row[0] == 'ID' and row[1] == 'Timestamp':
                continue
            
            if row[3]:
                numLinks = row[3].split('& ')
                numAttachments += len(numLinks)
                
            messages.append([correspondentId, row[0], row[1], row[2], row[3]])
             
for message in messages:
    with open('messages.csv', 'a', newline='', encoding="utf-8") as file:
        fwriter = writer(file)
        fwriter.writerow(message)
        file.close()
        
print("Total number of unique conversations: {}".format(numConversations))
print("Total number of messages found: {}".format(len(messages)))
print("Total number of messages containing an attachment: {}".format(numAttachments))