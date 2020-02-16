#!usr/bin/python

import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
import datetime

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "Enter subscription key"
assert subscription_key



# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westcentralus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "Enter vision base url"
analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.

print("Enter Image URL in your Computer")
image_path = raw_input()

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Objects'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

dic = response.json()

#count = 0

iteration = len(dic['objects'])

# Replace <search_obj> with your search object.
search_obj = 'bird'


image.save('/home/lalith/Documents/bird project/input images/{}'.format(count),'JPEG')

print('input image saved...')

for i in range(iteration):
    
   bird1 = dic['objects'][i]['object']

   bird2 = dic['objects'][i]['parent']['object']
  
   
   if bird1 == search_obj or bird2 == search_obj:

     Top = (dic['objects'][i]['rectangle']['y'])

     Left = (dic['objects'][i]['rectangle']['x'])

     Width = (dic['objects'][i]['rectangle']['w'])

     Height = (dic['objects'][i]['rectangle']['h'])

     image = Image.open(image_path)

     area = (Left, Top, Left + Width, Top + Height)
   
     bird = image.crop(area)   
       
     bird.show()

     count = datetime.datetime.now()

     bird.save('/home/lalith/Documents/bird project/croped images/{}'.format(count), 'JPEG')
     print("croped picture saved...")
    
   else:
     print('this is not a bird...')

