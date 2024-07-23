#!/usr/bin/env python

import argparse
import time
from random import randint
import requests
import threading
import json
# https://github.com/anderskm/gputil
import GPUtil

def send_req(url,headers,data):
    # Need equivalent to -o /dev/null
    r = requests.post(url, data, headers)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--param', nargs='?', const='default.param', default='default.param', help='Parameter file to use', required=False)
parser.add_argument('-v', '--verbose', help='verbose', action='store_true')
parser.add_argument('-d', '--debug', help='debug', action='store_true')
args = parser.parse_args()

# Port for the API, easy diffusion is 9000
url_port = '9000'

# Declaring Word Lists
word1=["a", "an", "the","some", "many",]
word2=["red", "green", "blue", "silver", "yellow", "bronze", "magenta", "pink", "purple",]
word3=["man", "woman", "girl", "boy", "cat", "dog","fish", "snake", "pig", "cow", "bird", "car", "bike", "truck", "train", "aeroplane",]
word4=["running", "sitting", "standing", "walking", "jumping", "skipping", "lying", "laying", "driving", "sliding", "rolling", "hopping", "crawling", "flying",]
word5=["on", "in", "around", "inside", "outside", "under", "over", "beside",]
word6=["chrome", "steel", "platinum", "bronze", "diamond", "ruby", "emerald", "carbon fiber", "plastic", "glass", "aluminium", "stone", "rock", "tile", "wood", "brick", "cork", "stained glass", "mosaic", "silver", "paper", "cardboard", "gold", "crystal", "carpet",]
word7=["house", "Village", "town", "city", "island", "country", "Continent", "planet", "tree", "wall", "bush", "river", "sea", "ocean",]

# sd-v1-5, sd_xl_base_1.0
# stable_diffusion_model = 'sd_xl_base_1.0'

# reading parameters from a file
with open(args.param) as f:
    # data = f.read()
    # print(data)
    prompt_json_data = json.load(f)

print(prompt_json_data)

# prompt_json_data |= { "use_stable_diffusion_model": stable_diffusion_model }

number = 0
while number < 10000000000:
    prompt_random=(word1[randint(0,len(word1)-1)]+" "+word2[randint(0,len(word2)-1)]+" "+word3[randint(0,len(word3)-1)]+" "+word4[randint(0,len(word4)-1)]+" "+word5[randint(0,len(word5)-1)]+" "+word6[randint(0,len(word6)-1)]+" "+word7[randint(0,len(word7)-1)])

    print(prompt_random)

    prompt_json_data |= { "prompt": prompt_random }

    json_data = json.dumps(prompt_json_data, indent=2)

    print(json_data)

    url = 'http://localhost:' + url_port + '/render'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    threading.Thread(target=send_req(url,headers,json_data)).start()

    number = number + 1

    deviceIDs = []

    while not deviceIDs:
        deviceIDs = GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])
        GPUtil.showUtilization()
        time.sleep (1)
