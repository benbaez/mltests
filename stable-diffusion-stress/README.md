# Stable Diffusion Stress script

## Purpose is to stress the GPUs so that any hardware problems will show

Nvidia stress tests and others like NVIDIA/Bopper and NVIDIA/deepops did not replicate issues we would see during training.

### Model usage

Modes are stored in easydiffusion/models/stable-diffusion folder.

#### Download extra models

Download sd_xl_base_1.0.safetensors from [sd_xl_base_1.0.safetensors · stabilityai/stable-diffusion-xl-base-1.0 at main](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors) and place under ./easydiffusion/models/stable-diffusion/

#### H100 testing requires the Juggernaut XL model:

https://civitai.com/models/133005?modelVersionId=471120

```
./stable-diffusion-stress.py -p h100hyper.param
```

### Instructions for installation stable-diffusion-stress.py

#### Clone my Easy Diffusion repo that support Nvidia A100 GPUs.

git clone https://github.com/benbaez/easydiffusion.git

#### Copy down to a separate directory the script to stress GPUs.

Suggest mltests for directory name.

https://github.com/benbaez/mltests/blob/main/stable-diffusion-stress/stable-diffusion-stress.py

NOTE: stable-diffusion-stress.py requires "requests" and "json" module, which should be installed by default.

##### Default parameter file

https://github.com/benbaez/mltests/blob/main/stable-diffusion-stress/default.param

##### A100 example parameter file

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
screen ./start.sh
```

### Execute testing

Execute without -p to load default.param

```
screen stable-diffusion-stress.py
```

For H100 or GH200

```
screen stable-diffusion-stress.py -p h100hyper.param
```

Script will keep looping until stopped. CTRL-C to exit. 

Look at Easy Diffusion STDOUT for any cuda errors. I usually execute 

```
watch -n 1 nvidia-smi
```

on another terminal to watch load.
