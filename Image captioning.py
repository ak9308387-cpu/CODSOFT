# Install required libraries
!pip install transformers pillow torch -q

# Import libraries
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from google.colab import files

# Load pre-trained BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Upload image
uploaded = files.upload()

# Read image
image_name = list(uploaded.keys())[0]
image = Image.open(image_name).convert("RGB")

# Generate caption
inputs = processor(image, return_tensors="pt")
output = model.generate(**inputs)

# Display result
caption = processor.decode(output[0], skip_special_tokens=True)

print("\n==============================")
print("Generated Caption:")
print(caption)
print("==============================")
