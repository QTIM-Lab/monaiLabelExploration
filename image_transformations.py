import os, requests
import nibabel as nib
import numpy as np
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

SERVER=os.environ.get('server')
PORT=os.environ.get('port')


# * For API Workflow when we are ready * #
# /model/{model} GET

# /iner/{model} POST
# url = f"http://{SERVER}:{PORT}/infer/deepedit"  # Replace with your server address and endpoint
# query_params = {
#     "image": "your_image_value",  # Replace with actual value or omit if not needed
#     "session_id": "your_session_id_value",  # Replace or omit if not needed
#     "output": "your_output_value",  # Replace or omit if not needed
#     "token": "your_token_value"  # Replace or omit if not needed
# }
# form_data = {
#     "params": "{}",
#     "file": ("your_file_name", open('Task09_Spleen/imagesTs/spleen_1.nii.gz', 'rb'))
# }
# response = requests.post(url, files=files)
# response.json()

# Curl Business
# curl -X 'POST' \
#   'http://0.0.0.0:8000/infer/deepedit?output=image' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'params={}' \
#   -F 'file=@/home/bbearce/Documents/monaiLabelExploration/Task09_Spleen/imagesTr/spleen_2.nii.gz;type=application/gzip' \
#   -F 'label=' -o /home/bbearce/Documents/monaiLabelExploration/tmpnh7155oc.nii.gz


# NIFTI Business (2D)

# Load the NIfTI image using nibabel
nifti_path = 'datasets/Task01_BrainTumour/imagesTs/BRATS_485.nii.gz'
nifti_img = nib.load(nifti_path)
data = nifti_img.get_fdata()
data.shape # (240, 240, 155, 4)

# Check if it's a single slice
# if data.shape[2] != 1:
#     raise ValueError("The NIfTI image should have only one slice for this conversion.")

# Get rid of the third dimension and normalize the values between 0 and 255
slice=60
data_2d = data[:, :, slice]
data_2d.shape
# Reshape it to a 3D volume with a depth of 1
data_3d = data_2d[:, :, np.newaxis]
data_3d.shape

normalized_data_2d = ((data_2d - data_2d.min()) / (data_2d.max() - data_2d.min()) * 255).astype(np.uint8)
normalized_data_3d = normalized_data_2d[:, :, np.newaxis]
normalized_data_3d.shape

# Create a new NIfTI image with the affine from the original image
new_nifti_img = nib.Nifti1Image(normalized_data_3d, affine=nifti_img.affine)

# Save the new NIfTI image
nib.save(new_nifti_img, f'datasets/Task01_BrainTumour/imagesTs/BRATS_485_slice-{slice}.nii.gz')

# Convert numpy array to a PIL image
img = Image.fromarray(normalized_data_2d)
img = img.convert("RGB")

# Save the image as JPG
if not os.path.exists('TEMP_DATA'):
    os.mkdir('TEMP_DATA')
image_path_2D = f'TEMP_DATA/BRATS_485_slice-{slice}.jpg'
img.save(image_path_2D)




# NIFTI Business (3D)

# Load the NIfTI image using nibabel
nifti_path = 'datasets/Task01_BrainTumour/imagesTs/BRATS_485.nii.gz'
nifti_img = nib.load(nifti_path)
data = nifti_img.get_fdata()
data.shape # (240, 240, 155, 4)

# *We Don't need to do anything as it is already 3D and can be consumed as is.* #