#!/usr/bin/env python

# Local install torch if not system wide

## Install packages
# pip3 install torch numpy

# Add PATH=$PATH:/home/<username>/.local/bin to .bashrc
import torch
import traceback
import random
with open('gpus.txt', 'w') as f:
    random_order = list(range(8))
    random.shuffle(random_order)
    print(random_order)
    for i in random_order:
        print(i)
        #write to file
        f.write(str(i)+'\n')
        try:
            a = torch.rand(1000, 1000, device=f'cuda:{i}')
            b = torch.rand(1000, 1000, device=f'cuda:{i}')
            c = a * b
            print(c)
            print('worked on cuda', i)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print(e)
            print('Failed cuda on', i)
            f.write(f'Failed cuda on {i}\n')
            f.write(str(e)+'\n')
            f.write(traceback.format_exc()+'\n')
