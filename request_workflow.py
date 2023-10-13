import os, monailabel, requests
from dotenv import load_dotenv

load_dotenv()

SERVER=os.environ.get('server')
PORT=os.environ.get('port')
base_url = f"http://{SERVER}:{PORT}/"


#### Client Init (GET)
url = base_url + f"info/"
client_init_response = requests.get(url)
client_init_response.content

#### Next Image Selection (GET)
strategy="random"
url = base_url + f"activelearning/{strategy}"
next_image_response = requests.post(url)
next_image_response.content
# b'{"id":"BRATS_047","weight":1697163052,"path":"/home/bbearce/Documents/monaiLabelExploration/datasets/Task01_BrainTumour/imagesTr/BRATS_047.nii.gz","ts":1697084681,"name":"BRATS_047.nii.gz"}'

#### Inference (POST)
model="mednist"
headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}
files = {
    'params': (None, '{}', 'application/json'),
    'file': ('000000.jpeg', open('/home/bbearce/Documents/monaiLabelExploration/tutorials/MedNIST/AbdomenCT/000000.jpeg', 'rb'), 'image/jpeg'),
    'label': (None, '', 'text/plain'),
}
url = base_url + f"infer/{model}?output=json"
inference_response = requests.post(url, headers=headers, files=files)
inference_response.content
# b'{"prediction":[{"idx":0,"label":"AbdomenCT","score":1.8630764484405518},{"idx":1,"label":"BreastMRI","score":-0.6298333406448364},{"idx":2,"label":"CXR","score":-0.5690193176269531},{"idx":3,"label":"ChestCT","score":-0.15074892342090607},{"idx":4,"label":"Hand","score":-0.39861854910850525},{"idx":5,"label":"HeadCT","score":-0.5673792958259583}],"label_names":["AbdomenCT","BreastMRI","CXR","ChestCT","Hand","HeadCT"],"latencies":{"pre":0.0,"infer":0.04,"invert":0.0,"post":0.0,"write":0.0,"total":0.05,"transform":{"pre":{"LoadImaged":0.0006,"EnsureChannelFirstd":0.0002,"ScaleIntensityd":0.0004}}}}'

#### Submit Final Label (GET)
url = base_url + f"datastore/"
submit_final_label_response = requests.get()

#### Train Model (GET)
url = base_url + f"train/"
train_model_response = requests.get()