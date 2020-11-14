from PIL import Image
import numpy as np
import streamlit as st
from PIL import ImageFilter

class Filter:
    def __init__(self):
        self.image = None
        self.output = None
    def apply_negative_filter(self,image_path,R=True,G=True,B=True):
     
      self.image = image_path.copy()
     
      for i in range(0, self.image.size[0]-1):

          for j in range(0, self.image.size[1]-1):
         
            # Get pixel value at (x,y) position of the image
            pixelColorVals = self.image.getpixel((i,j));
            if R:
              redPixel = 255- pixelColorVals[0]; 
            else:
              redPixel = pixelColorVals[0]
        
            if G:
              greenPixel = 255 - pixelColorVals[1];
            else:
              greenPixel = pixelColorVals[1];

            if B:
              bluePixel = 255 - pixelColorVals[2]; 
            else:
              bluePixel = pixelColorVals[2]
            # Modify the image with the inverted pixel values

            self.image.putpixel((i,j),(redPixel, greenPixel, bluePixel));
      return self.image
      

      # Display the negative image

      # self.image.show()
    def visualize_image(self, image, capt = 'Image'):
        
      st.image(image, caption=capt, use_column_width=True)

