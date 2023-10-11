# MonaiLabelExploration
Get MonaiLabel server running and establish an input output workflow

## Initial Steps
[Docs](https://docs.monai.io/projects/label/en/latest/quickstart.html)

```bash
pyenv versions
pyenv virtualenv 3.10.4 monailabel-3.10.4

# Poetry
poetry config virtualenvs.create false
poetry config virtualenvs.in-project false
poetry add monailabel pandas

# install MONAI Label
pip install monailabel

# Download Sample Apps
monailabel apps # List sample apps
monailabel apps --download --name radiology --output apps

# Download MSD Datasets
monailabel datasets # List sample datasets
monailabel datasets --download --name Task09_Spleen --output datasets

# Run Deepedit Model.
# Options can be (deepedit|deepgrow|segmentation|segmentation_spleen|all) in case of radiology app.
# You can also pass comma separated models like --conf models deepedit,segmentation

# monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models all
monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit
```

![server_running](server_running.jpg)


## Curl Commands
Use http://<>:<>/#/ to explore the api and generate curl commands in the correct format.


### Workflow 
[ApplicationDeployment](https://docs.monai.io/projects/label/en/latest/appdeployment.html)

#### Client Init
```bash
curl -X 'GET' \
  'http://0.0.0.0:8000/info/' \
  -H 'accept: application/json'
```

#### Next Image Selection
```bash


```

#### Inference
```bash


```

#### Submit Final Label
```bash


```

#### Train Model
```bash


```
