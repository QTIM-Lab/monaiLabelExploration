import os, requests


url = "http://<your_server_address>:<port>/segmentation"  # Replace with your server address and endpoint
files = {'image': open('your_image_file_path', 'rb')}

response = requests.post(url, files=files)