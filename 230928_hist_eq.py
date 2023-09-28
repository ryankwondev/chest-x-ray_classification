import os
from PIL import Image
import numpy as np
import cv2


def process_images(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                filepath = os.path.join(dirpath, filename)

                image = Image.open(filepath).convert("L")
                image = image.resize((256, 256))

                image_np = np.array(image)
                image_np = cv2.equalizeHist(image_np)
                image = Image.fromarray(image_np)

                image.save(filepath)
                print(f"Processed {filepath}")


root_directory = './dataset'
process_images(root_directory)
