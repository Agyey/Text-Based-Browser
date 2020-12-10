import re
import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore
init()

def valid_url(url):
    url = re.search("^(https?://(www\.)?)?[\w-]+(\.[\w-]+)+", url)
    return url

def match_url(url):
    if 'https' not in url:
        url = "https://" + url
    response = requests.get(url)
    if response:
        webpage = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
        return webpage.get_text()
    return None

def add_to_history(file_name):
    global history
    if file_name:
        history.append(file_name)

# Get saved tabs and create on
saved_tabs_dir = sys.argv[-1]
# Browsing History
history = []
file_names = []
file_name = ''
if not os.path.isdir(saved_tabs_dir):
    os.makedirs(saved_tabs_dir)
else:
    for name in os.listdir(saved_tabs_dir):
        file_names.append(name)
# write your code here
while True:
    command = input()
    validurl = valid_url(command)
    if validurl:
        validurl = validurl[0]
        webpage = match_url(validurl)
        if webpage:
            add_to_history(file_name)
            file_name = validurl.split('.')[-2]
            file_names.append(file_name)
            with open(os.path.join(saved_tabs_dir, file_name), 'w', encoding='utf-8') as f:
                f.write(webpage)
        else:
            print('Error Page Not Found')
            continue
    elif command == 'exit':
        break
    elif command in file_names:
        add_to_history(file_name)
        file_name = command
    elif command == 'back':
        file_name = history.pop()
    else:
        print('Error Invalid Command')
        continue
    # Display Web Page
    with open(os.path.join(saved_tabs_dir, file_name), encoding='utf-8') as f:
        print(Fore.BLUE + f.read())
