import subprocess
import os
import requests
import json
import os
import re

def ffsend(filename):
    # If space in filename remove it
    regex = r"[^a-zA-Z0-9\.]+"
    new_filename = re.sub(regex,'',filename)
    print('new_name: ' + new_filename)

    os.rename(filename, new_filename) 
    cmd = 'ffsend upload "{}"'.format(new_filename)
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True ).communicate()[0]
    str_output = str(output)
    link = str_output.split('  ')
    ff_link = link[1]
    try:
        os.remove(new_filename)
    except Exception as ex:
        print(ex)
    return(shorten_url(ff_link))

def shorten_url(urlToShorten):
        headers = {
            'public-api-token': 'shortest api token',
            }
        data = {
            'urlToShorten': urlToShorten
            }

        response = requests.put('https://api.shorte.st/v1/data/url', headers=headers, data=data)

        data = json.loads(response.text)
        return(data['shortenedUrl'])


filename = input('Enter File Name')
ffsend(filename)
