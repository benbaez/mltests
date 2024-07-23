# Stable Diffusion Stress script

## Purpose is to stress the GPUs so that any hardware problems will show

stable-diffusion-stress.py requires "requests" and "json" module.

### H100 testing requires the Juggernaut XL model:

https://civitai.com/models/133005?modelVersionId=471120

'''
./stable-diffusion-stress.py -p h100hyper.param
'''
