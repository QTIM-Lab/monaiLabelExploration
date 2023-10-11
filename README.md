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

# download Radiology sample app to local directory
monailabel apps --name radiology --download --output .

# download Task 2 MSD dataset
monailabel datasets --download --name Task09_Spleen --output .

# start the Radiology app in MONAI label server
# and start annotating the downloaded images using deepedit model
monailabel start_server --app radiology --studies Task09_Spleen/imagesTr --conf models deepedit
```

![server_running](server_running.jpg)
