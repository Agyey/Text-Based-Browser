import re
import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
init()

def valid_url(url):
    url = re.search("^(https?://(www\.)?)?[\w-]+(\.[\w-]+)+", url)
    return url

def match_url(url):
    global file_names
    if 'https' not in url:
        url = "https://" + url
    response = requests.get(url)
    if response:
        webpage = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
        file_name = validurl.split('.')[-2]
        file_names.append(file_name)
        with open(os.path.join(saved_tabs_dir, file_name), 'w', encoding='utf-8') as f:
            for element in webpage.find_all(re.compile("p|a|ul|ol|li|^h[1-6]$")):
                if element.name == "a":
                    f.write(f"{Fore.BLUE + element.get_text()}\n")
                    f.write(f"{Style.RESET_ALL}\n")
                else:
                    f.write(f"{element.get_text()}\n")
        return file_name
    else:
        print('Error Page Not Found')
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
        add_to_history(file_name)
        file_name = match_url(validurl)
        if not file_name:
            continue
    elif command == 'exit':
        break
    elif command in file_names:
        add_to_history(file_name)
        file_name = command
    elif command == 'back':
        if history:
            file_name = history.pop()
        else:
            print('Error Invalid Command: No History to Show')
            continue
    else:
        print('Error Invalid Command')
        continue
    # Display Web Page
    with open(os.path.join(saved_tabs_dir, file_name), encoding='utf-8') as f:
        print(f.read())
