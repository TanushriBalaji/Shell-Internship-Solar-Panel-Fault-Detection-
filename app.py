x`from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from PIL import Image
import gradio as gr

# Load the model
model = load_model("solar_fault_detection_model.h5")

# Define class names
class_names = ["Bird-drop", "Clean", "Dusty", "Electrical-damage", "Physical-Damage", "Snow-Covered"]

# Preprocessing function
def preprocess_image(image):
    image = image.resize((224, 224))  # resize same as your training
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Prediction function
def predict(img):
    processed = preprocess_image(img)
    prediction = model.predict(processed)
    index = np.argmax(prediction)
    confidence = float(np.max(prediction))
    return {class_names[index]: confidence}

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=1),
    title="Solar Panel Fault Detection",
    description="Upload a solar panel image to detect its condition.",
)

interface.launch()
