from PIL import Image
import numpy as np
import streamlit as st
from PIL import ImageFilter

class Filter:
    def __init__(self):
        self.image = None
        self.output = None


    def apply_negative_filter(self, image_path, R=True,G=True,B=True):
        image = np.array(Image.open(image_path).convert('RGB'))


        if R:
            image[:,:,0] = 255 - image[:,:,0]

        if G:
            image[:,:,1] = 255 - image[:,:,1]

        if B:
            image[:,:,2] = 255 - image[:,:,2]

        transf_image = Image.fromarray(image.astype('uint8'))
        return transf_image

    def visualize_image(self, image, capt = 'Image'):
        
      st.image(image, caption=capt, use_column_width=True)

