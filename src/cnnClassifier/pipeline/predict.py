import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model_path = os.path.abspath("artifacts/training/model.keras")

        # Check if model exists before loading
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")

        # Load the model once
        self.model = load_model(self.model_path)

    def preprocess_image(self):
        """Load and preprocess the image for model prediction"""
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = img / 255.0  # Normalize pixel values
        img = np.expand_dims(img, axis=0)
        return img

    def predict(self):
        """Predict the class of the given image"""
        img = self.preprocess_image()
        predictions = self.model.predict(img)
        result = np.argmax(predictions, axis=1)

        # Class labels (ensure they match your training data)
        classes = ["Coccidiosis", "Healthy"]  # Modify if needed
        predicted_label = classes[result[0]]
        confidence = float(np.max(predictions))  # Get confidence score

        return [{"image": predicted_label, "confidence": confidence}]
