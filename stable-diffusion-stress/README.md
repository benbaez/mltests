# Stable Diffusion Stress script

## Purpose is to stress the GPUs so that any hardware problems will show

Nvidia stress tests and others like NVIDIA/Bopper and NVIDIA/deepops did not replicate issues we would see during traning.

stable-diffusion-stress.py requires "requests" and "json" module.

### H100 testing requires the Juggernaut XL model:

https://civitai.com/models/133005?modelVersionId=471120

'''
./stable-diffusion-stress.py -p h100hyper.param
'''

### Instructions for installation

#### Clone Easy Diffusion repo that support A100 GPUs.

git clone https://github.com/benbaez/easydiffusion.git

#### Download extra models

Download sd_xl_base_1.0.safetensors from sd_xl_base_1.0.safetensors · stabilityai/stable-diffusion-xl-base-1.0 at main and place under ./easydiffusion/models/stable-diffusion/

#### Copy down to a separate directory the script to stress GPUs.

Requests module is required. https://github.com/benbaez/mltests/blob/main/stable-diffusion-stress/stable-diffusion-stress.py

https://github.com/benbaez/mltests/blob/main/stable-diffusion-stress/h100hyper.param

#### Clone GPUtil library used with stress script

https://github.com/anderskm/gputil

Copy GPUtil within gputil repo to same directory as stable-diffusion-stress.py

#### Configure Easy Diffusion

```
cd easydiffusion
cp scripts/start.sh ./start.sh
cp scripts/config.yaml.sample ./config.yaml
# Edit ./config.yaml
# Change to: open_browser_on_start: false
./start.sh
```

### Execute testing

Execute stable-diffusion-stress.py. CTRL-C to exit, but it will keep looping until stopped. 

Look at Easy Diffusion STDOUT for any cuda errors. I usually run 'watch -n 1 nvidia-smi' on another terminal to watch load.
