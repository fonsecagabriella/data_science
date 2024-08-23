credentials, PROJECT_ID = authenticate()

REGION = "us-central1"

import vertexai

vertexai.init( project=PROJECT_ID,
location= REGION,
credentials = credentials)

from vertexai.generative_models import GenerativeModel

model = GenerativeModel("gemini-1.0-pro-002")

from utils import gemini

gemini("What is a multimodel model?", model=model)

prompt_1 = """"
In short, what is deeplearning.ai
""""

# the stream here gives the answer to be used as soon as it is being generated,
# you don't have to wait for it
response_1 = model.generate_content(prompt1, stream=True)

for response in response_1:
    print(response) #here you get a json response

# to get an text response:
for response in response_1:
    print(response.text)

# to be able to use other formats, must import
from vertexai.generative_models import (
    GenerativeModel,
    Image, 
    Part
)

multimodel_model = GenerativeModel("gemini-1.0-pro-vision-001")

# load from local file
image = Image.load_from_file("image.ong")

prompt_3 = "whats in this image?"

# here you combine the image and the prompt
contents_image = [image, prompt]

from utils import print_multimodal_prompt
print("--- Prompt ----")
print_multimodal_prompt(contents_image)

gemini_vision(contents_image, model=multimodel_model)

