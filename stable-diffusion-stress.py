#!/usr/bin/env python

import time
from random import randint
import requests
import json
import torch
# https://github.com/anderskm/gputil
import GPUtil

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

number = 0
while number < 10000000000:
    prompt_random=(word1[randint(0,len(word1)-1)]+" "+word2[randint(0,len(word2)-1)]+" "+word3[randint(0,len(word3)-1)]+" "+word4[randint(0,len(word4)-1)]+" "+word5[randint(0,len(word5)-1)]+" "+word6[randint(0,len(word6)-1)]+" "+word7[randint(0,len(word7)-1)])

    print(prompt_random)

    prompt_json_data = {
        "prompt": prompt_random,
        "seed": 3628755307,
        "used_random_seed": "false",
        "negative_prompt": "",
        "num_outputs": 1,
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "width": 1024,
        "height": 1024,
        "vram_usage_level": "balanced",
        "sampler_name": "euler_a",
        "use_stable_diffusion_model": "sd-v1-5",
        "clip_skip": "false",
        "use_vae_model": "",
        "stream_progress_updates": "true",
        "stream_image_progress": "false",
        "show_only_filtered_image": "true",
        "block_nsfw": "false",
        "output_format": "jpeg",
        "output_quality": 90,
        "output_lossless": "false",
        "metadata_output_format": "none",
        "active_tags": [],
        "inactive_tags": [],
        "use_face_correction": "GFPGANv1.4",
        "use_upscale": "RealESRGAN_x4plus",
        "upscale_amount": "4",
        "enable_vae_tiling": "true"
    }

    json_data = json.dumps(prompt_json_data, indent=2)

    print(json_data)

    url = 'http://localhost:' + url_port + '/render'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    # Need equivalent to -o /dev/null
    r = requests.post(url, data=json_data, headers=headers)

    number = number + 1

    deviceIDs = []

    while not deviceIDs:
        time.sleep (10)

        deviceIDs = GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])

GPUtil.showUtilization()
