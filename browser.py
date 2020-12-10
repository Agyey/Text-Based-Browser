import re
import sys
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

def valid_url(url):
    url = re.search("^(https?://(www\.)?)?\w+\.\w{2,3}$", url)
    return url

def match_url(url):
    base_url = re.search("(?<=www.)?\w+\.\w{2,3}$", url)
    web_pages = {
        'nytimes.com': nytimes_com,
        'bloomberg.com': bloomberg_com
    }
    return web_pages.get(base_url.group(), None)


# Get saved tabs and create on
saved_tabs_dir = sys.argv[-1]
file_names = []
if not os.path.isdir(saved_tabs_dir):
    os.makedirs(saved_tabs_dir)
# write your code here
while True:
    command = input()
    validurl = valid_url(command)
    if validurl:
        validurl = validurl.group()
        webpage = match_url(validurl)
        print(webpage)
        if webpage:
            file_name = validurl.split('.')[0]
            with open(os.path.join(saved_tabs_dir, file_name), 'w') as f:
                f.write(webpage)
        else:
            print('Error Page Not Found')
    elif command == 'exit':
        break
    elif command in file_names:
        with open(os.path.join(saved_tabs_dir, command)) as f:
            print(f.read())
    else:
        print('Error Invalid Command')
