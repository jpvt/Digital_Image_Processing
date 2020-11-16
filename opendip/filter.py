from PIL import Image
import numpy as np
import streamlit as st
from PIL import ImageFilter
from .converter import Converter
from .correlator import Correlator

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

    def apply_negative_filter_in_y(self, image_path):
        #image = np.array(Image.open(image_path).convert('RGB'))

        converter = Converter()

        yiq_img, yiq_arr = converter.RGB_2_YIQ(image_path=image_path)

        yiq = yiq_arr.copy()

        yiq[:,:,0] = 255 - yiq[:,:,0]

        rgb_img, rgb_arr =  converter.YIQ_2_RGB(arr_img=yiq)

        rgb = rgb_img.copy()
        return rgb


    def visualize_image(self, image, capt = 'Image'):
        
      st.image(image, caption=capt, use_column_width=True)

    def apply_sobel_filter(self, image_path, zero_padding=True, mode="vertical"):

        c = Correlator()

        if mode == "vertical":
            sobel_filter = np.array([[-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])
        elif mode == "horizontal":
            sobel_filter = np.array([[-1,0,1],
                        [-2,0,2],
                        [-1,0,1]]).T
        else:
            print("Choose either vertical or Horizontal")
            return -1
        
        return c.apply_correlation(image_path, sobel_filter, zero_padding=zero_padding)
    
    def apply_box_filter(self, image_path, box_shape=(3,3), zero_padding=True):

        c = Correlator()

        divisor = box_shape[0] * box_shape[1]
        
        return c.apply_correlation(image_path, np.ones((box_shape[0],box_shape[1]))/divisor, zero_padding)
    
    def apply_median_filter(self, image_path, filter_shape=(3,3), zero_padding=True):

        c = Correlator()

        self.image = np.array(Image.open(image_path).convert('RGB'))

        c.image = self.image

        vertical_padding = filter_shape[0]//2
        horizontal_padding = filter_shape[1]//2

        if not horizontal_padding and not vertical_padding:
            print("Could not execute padding due to filter shape. Try a Bi dimensional kernel.")
            zero_padding = False

        if zero_padding:
            preprocessed_img = c.padding(horizontal_padding, vertical_padding)
            output = np.zeros((self.image.shape[0], self.image.shape[1], 3))
        else:
            preprocessed_img = self.image
            output = np.zeros((self.image.shape[0] - 2 * vertical_padding, self.image.shape[1] - 2 * horizontal_padding, 3))

        for i in range(preprocessed_img.shape[0] - filter_shape[0]):
            for j in range(preprocessed_img.shape[1] - filter_shape[1]):
                for k in range(3):
                    output[i,j,k] = np.median(preprocessed_img[i: i + filter_shape[0], j: j + filter_shape[1], k])
        
        return self.image, preprocessed_img, output