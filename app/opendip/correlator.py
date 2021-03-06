from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Correlator:
    
    def __init__(self):
        self.image = None
        self.filter = None

    def padding(self, horizontal_padding, vertical_padding):
        padded_image = np.zeros((self.image.shape[0] + 2 * vertical_padding, self.image.shape[1] + 2 * horizontal_padding, 3))
        
        if vertical_padding == 0:
            padded_image[:, horizontal_padding : -horizontal_padding, :] = self.image 
        elif horizontal_padding == 0:
            padded_image[vertical_padding : -vertical_padding, :, :] = self.image 
        else:
            padded_image[vertical_padding : -vertical_padding, horizontal_padding : -horizontal_padding, :] = self.image 
    
        return padded_image
        
    def apply_correlation(self, image_path, filter_matrix, zero_padding = True):
        self.image = np.array(Image.open(image_path).convert('RGB'))
        self.filter = filter_matrix
        
        vertical_padding = self.filter.shape[0]//2
        horizontal_padding = self.filter.shape[1]//2
        
        if not horizontal_padding and not vertical_padding:
            print("Could not execute padding due to filter shape. Try a Bi dimensional kernel.")
            zero_padding = False
        
        if zero_padding:
            preprocessed_img = self.padding(horizontal_padding, vertical_padding)
            output = np.zeros((self.image.shape[0], self.image.shape[1], 3))
        else:
            preprocessed_img = self.image
            output = np.zeros((self.image.shape[0] - 2 * vertical_padding, self.image.shape[1] - 2 * horizontal_padding, 3))
    
        for i in range(preprocessed_img.shape[0] - self.filter.shape[0]):
            for j in range(preprocessed_img.shape[1] - self.filter.shape[1]):
                for k in range(3):
                    output[i,j,k] = np.sum(np.multiply(self.filter, preprocessed_img[i: i + self.filter.shape[0], j: j + self.filter.shape[1], k]))
        
        output[output < 0] = 0
        output[output > 255] = 255
        
        return self.image, preprocessed_img, output
    
    def apply_norm_correlation(self, image_path, filter_matrix):
        self.image = np.array(Image.open(image_path).convert('RGB'))
        self.filter = filter_matrix

        epsilon = 1e-7
        
        vertical_remnant = self.filter.shape[0]//2
        horizontal_remnant = self.filter.shape[1]//2
        
        preprocessed_img = self.image
        output = np.zeros((self.image.shape[0] - 2 * vertical_remnant, self.image.shape[1] - 2 * horizontal_remnant))
    

        filter_diff = []
        normalized_filter = []
        for i in range(3):
            filter_diff.append(self.filter[:,:,i] - np.mean(self.filter[:,:,i]))
            normalized_filter.append(filter_diff[i]/np.sum(np.abs(filter_diff[i] + epsilon)))
        
        if np.argmax(normalized_filter) == 0:
            print("Warning : Filter has mean zero. Normalization will result in a black image.")

        for i in range(preprocessed_img.shape[0] - self.filter.shape[0]):
            for j in range(preprocessed_img.shape[1] - self.filter.shape[1]):
                for k in range(3):
                    window = preprocessed_img[i: i + self.filter.shape[0], j: j + self.filter.shape[1], k]
                    window_diff = window - np.mean(window)
                    output[i,j] += np.sum(np.multiply((window_diff)/np.sum(np.abs(window_diff + epsilon)), normalized_filter[k]))

        output /= 3                
        output = (output - np.min(output))/(np.max(output) - np.min(output))
        
        return self.image, output