from PIL import Image
import numpy as np
import streamlit as st

class Converter:
    
    def __init__(self):
        self.image = None
        self.image_transformed = None
        
    def RGB_2_YIQ(self, image_path = None, image_obj = None):
        """
        Y: 0.999 * R + 0.587 * G + 0.114 * B
        I: 0.596 * R -  0.274 * G - 0.322 * B
        Q: 0.211 * R - 0.523 * G + 0.312 * B
        """
        
        if image_path != None:
            # Open Image and transform into a numpy array
            image = Image.open(image_path)
            self.image = Image.open(image_path)
        elif image_obj != None:

            image = image_obj.copy()

        arr_img = np.asarray(image)
        
        # Makes a copy of the original image numpy array
        img_copy = arr_img.copy().astype(float)
        
        
        # Matrix YIQ
        matrix_yiq = np.array([[0.299, 0.587, 0.114],
                      [0.596, -0.274, -0.322],
                      [0.211, -0.523, 0.312]])
        
        # Dot operation
        """
        img_copy[:,:,0] = arr_img[:,:,0] * matrix_yiq[0][0] + arr_img[:,:,1] * matrix_yiq[0][1] + arr_img[:,:,2] * matrix_yiq[0][2]
        img_copy[:,:,1] = arr_img[:,:,1] * matrix_yiq[1][0] + arr_img[:,:,1] * matrix_yiq[1][1] + arr_img[:,:,2] * matrix_yiq[1][2]
        img_copy[:,:,2] = arr_img[:,:,2] * matrix_yiq[2][0] + arr_img[:,:,1] * matrix_yiq[2][1] + arr_img[:,:,2] * matrix_yiq[2][2]
        """
        img_copy = np.dot(arr_img, matrix_yiq.T.copy())
        
        # Transform numpy array to Image
        img_transformed = Image.fromarray(img_copy.astype('uint8'))
        self.image_transformed = Image.fromarray(img_copy.astype('uint8'))
        
        # Save Image
        #img_transformed.save('yiq.png')
        
        
        # Return Image, Image_Array
        return img_transformed, img_copy
    
    def YIQ_2_RGB(self, arr_img):
        """
        R: 1.0 * Y + 0.956 * I + 0.621 * Q
        G: 1.0 * Y – 0.272 * I – 0.647 * Q
        B: 1.0 * Y – 1.106 * I + 1.703 * Q
        """ 
     
        # Matrix RGB
        matrix_rgb = np.array([
                               [1.0, 0.956, 0.621],
                               [1.0, -0.272, -0.647],
                               [1.0, -1.106, 1.703]
                             ])
        # Dot Operation
        """
        img_copy[:,:,0] = arr_img[:,:,0] * matrix_rgb[0][0] + arr_img[:,:,1] * matrix_rgb[0][1] + arr_img[:,:,2] * matrix_rgb[0][2]
        img_copy[:,:,1] = arr_img[:,:,1] * matrix_rgb[1][0] + arr_img[:,:,1] * matrix_rgb[1][1] + arr_img[:,:,2] * matrix_rgb[1][2]
        img_copy[:,:,2] = arr_img[:,:,2] * matrix_rgb[2][0] + arr_img[:,:,1] * matrix_rgb[2][1] + arr_img[:,:,2] * matrix_rgb[2][2]
        """
        img_copy = np.dot(arr_img, matrix_rgb.T.copy())
        
        
        # setting RGB limits
        np.where(img_copy < 0, img_copy, 0)
        np.where(img_copy > 255, img_copy, 255)
        
        
        # Transform numpy array to Image
        img_transformed = Image.fromarray(img_copy.astype('uint8'))
        self.image_transformed = Image.fromarray(img_copy.astype('uint8'))
        
        # Save Image
        #img_transformed.save('rgb.png')
        
        # Return Image, Image_Array
        return img_transformed, img_copy
    
    def RGB_2_YIQ_2_RGB(self, image_path = None, image_obj = None):
        
        # Open Image and transform into a numpy array
        if image_path != None:
            # Open Image and transform into a numpy array
            image = Image.open(image_path)
            self.image = Image.open(image_path)
        elif image_obj != None:
            image = image_obj.copy()

        arr_img = np.asarray(image)
        
        # Makes a copy of the original image numpy array
        img_copy = arr_img.copy().astype(float)
        
        
        # Matrix YIQ
        matrix_yiq = np.array([[0.299, 0.587, 0.114],
                      [0.596, -0.274, -0.322],
                      [0.211, -0.523, 0.312]])
        
        # Dot operation
        """
        img_copy[:,:,0] = arr_img[:,:,0] * matrix_yiq[0][0] + arr_img[:,:,1] * matrix_yiq[0][1] + arr_img[:,:,2] * matrix_yiq[0][2]
        img_copy[:,:,1] = arr_img[:,:,1] * matrix_yiq[1][0] + arr_img[:,:,1] * matrix_yiq[1][1] + arr_img[:,:,2] * matrix_yiq[1][2]
        img_copy[:,:,2] = arr_img[:,:,2] * matrix_yiq[2][0] + arr_img[:,:,1] * matrix_yiq[2][1] + arr_img[:,:,2] * matrix_yiq[2][2]
        """
        img_copy = np.dot(arr_img, matrix_yiq.T.copy())
        
        # Transform numpy array to Image
        img_transformed = Image.fromarray(img_copy.astype('uint8'))
        self.image_transformed = Image.fromarray(img_copy.astype('uint8'))
        
        # Save Image
        #img_transformed.save('yiq.png')
        
        # Matrix RGB
        matrix_rgb = np.array([[1.0, 0.956, 0.621],
                               [1.0, -0.272, -0.647],
                               [1.0, -1.106, 1.703]])
        
        """
        img_copy2[:,:,0] = img_copy[:,:,0] * matrix_rgb[0][0] + img_copy[:,:,1] * matrix_rgb[0][1] + img_copy[:,:,2] * matrix_rgb[0][2]
        img_copy2[:,:,1] = img_copy[:,:,1] * matrix_rgb[1][0] + img_copy[:,:,1] * matrix_rgb[1][1] + img_copy[:,:,2] * matrix_rgb[1][2]
        img_copy2[:,:,2] = img_copy[:,:,2] * matrix_rgb[2][0] + img_copy[:,:,1] * matrix_rgb[2][1] + img_copy[:,:,2] * matrix_rgb[2][2]
        """
        img_copy2 = np.dot(img_copy, matrix_rgb.T.copy())
        
        # setting RGB limits
        np.where(img_copy2 < 0, img_copy2, 0)
        np.where(img_copy2 > 255, img_copy2, 255)
        
        # Transform numpy array to Image
        img_transformed = Image.fromarray(img_copy2.astype('uint8'))
        #Save Image
        #img_transformed.save('rgb.png')
        
        return img_transformed
        
        
        
        
        
    
    def visualize_image(self, image, capt = 'Image'):
        
        st.image(image, caption=capt, use_column_width=True)
    
    def visualize_all_process(self, original_img, yiq_image, yiq2rgb_img, capt = 'Transformation'):

        st.image([original_img, yiq_image, yiq2rgb_img], caption=capt, width=219)