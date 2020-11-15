from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Correlator:
    
    def __init__(self):
        self.image = None
        self.filter = None

    def __padding(self, horizontal_padding, vertical_padding):
        padded_image = np.zeros((self.image.shape[0] + 2 * vertical_padding, self.image.shape[1] + 2 * horizontal_padding, 3))

        if vertical_padding == 0:
            padded_image[:, horizontal_padding : -horizontal_padding, :] = self.image 
        elif horizontal_padding == 0:
            padded_image[vertical_padding : -vertical_padding, :, :] = self.image 
        else:
            padded_image[vertical_padding : -vertical_padding, horizontal_padding : -horizontal_padding, :] = self.image 
    
        return padded_image
        
    def apply_correlation(self, image_path, filter_matrix, zero_padding = False):
        # self.image = np.array(Image.open(image_path).convert('RGB'))
        self.image = image_path.copy();
        self.image = np.array(self.image);
        self.filter = filter_matrix
  
        num_rows =np.shape(self.image)[0]
        num_cols = np.shape(self.image)[1]
  
        vertical_padding = self.filter.shape[0]//2
        horizontal_padding = self.filter.shape[1]//2
        
        if not horizontal_padding and not vertical_padding:
            print("Could not execute padding due to filter shape. Try a Bi dimensional kernel.")
            zero_padding = False
        
        if zero_padding:
            preprocessed_img = self.__padding(horizontal_padding, vertical_padding)
            output = np.zeros((num_rows, num_cols, 3))
        else:
            preprocessed_img = self.image
            output = np.zeros((num_rows - 2 * vertical_padding, num_cols - 2 * horizontal_padding, 3))
    
        for i in range(preprocessed_img.shape[0] - self.filter.shape[0]):
            for j in range(preprocessed_img.shape[1] - self.filter.shape[1]):
                for k in range(3):
                    output[i,j,k] = np.sum(np.multiply(self.filter, preprocessed_img[i: i + self.filter.shape[0], j: j + self.filter.shape[1], k]))
        
        output[output < 0] = 0
        output[output > 255] = 255
        
        return  output
    
    def apply_norm_correlation(self, image_path, filter_matrix, zero_padding = True):
        # self.image = np.array(Image.open(image_path).convert('RGB'))
        self.image = image_path.copy()
        self.filter = filter_matrix

        epsilon = 1e-7
        
        vertical_padding = self.filter.shape[0]//2
        horizontal_padding = self.filter.shape[1]//2
        
        if not horizontal_padding and not vertical_padding:
            print("Could not execute padding due to filter shape. Try a Bi dimensional kernel.")
            zero_padding = False
        
        if zero_padding:
            preprocessed_img = self.__padding(horizontal_padding, vertical_padding)
            output = np.zeros((self.image.shape[0], self.image.shape[1], 3))
        else:
            preprocessed_img = self.image
            output = np.zeros((self.image.shape[0] - 2 * vertical_padding, self.image.shape[1] - 2 * horizontal_padding, 3))
    

        filter_diff = self.filter - np.mean(self.filter)
        print(filter_diff.shape)
        normalized_filter = filter_diff/np.sum(np.abs(filter_diff + epsilon))
        
        if np.argmax(normalized_filter) == 0:
            print("Warning : Filter has mean zero. Normalization will result in a black image.")

        for i in range(preprocessed_img.shape[0] - self.filter.shape[0]):
            for j in range(preprocessed_img.shape[1] - self.filter.shape[1]):
                for k in range(3):
                    window = preprocessed_img[i: i + self.filter.shape[0], j: j + self.filter.shape[1], k]
                    window_diff = window - np.mean(window)
                    output[i,j,k] += np.sum(np.multiply((window_diff)/np.sum(np.abs(window_diff + epsilon)), normalized_filter))
                
        output = (output - np.min(output))/(np.max(output) - np.min(output))
        
        return self.image, preprocessed_img, output

    def apply_sobel_filter(self, image_path, zero_padding=False, mode="vertical"):
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
        
        return self.apply_correlation(image_path, sobel_filter, zero_padding=zero_padding)
    
    def apply_box_filter(self, image_path, box_shape=(3,3), zero_padding=True):
        divisor = box_shape[0] * box_shape[1]
        return self.apply_correlation(image_path, np.ones((box_shape[0],box_shape[1]))/divisor, zero_padding)
    
    def apply_median_filter(self, image_path, filter_shape=(3,3), zero_padding=True):
        self.image = np.array(Image.open(image_path).convert('RGB'))

        vertical_padding = filter_shape[0]//2
        horizontal_padding = filter_shape[1]//2

        if not horizontal_padding and not vertical_padding:
            print("Could not execute padding due to filter shape. Try a Bi dimensional kernel.")
            zero_padding = False

        if zero_padding:
            preprocessed_img = self.__padding(horizontal_padding, vertical_padding)
            output = np.zeros((self.image.shape[0], self.image.shape[1], 3))
        else:
            preprocessed_img = self.image
            output = np.zeros((self.image.shape[0] - 2 * vertical_padding, self.image.shape[1] - 2 * horizontal_padding, 3))

        for i in range(preprocessed_img.shape[0] - filter_shape[0]):
            for j in range(preprocessed_img.shape[1] - filter_shape[1]):
                for k in range(3):
                    output[i,j,k] = np.median(preprocessed_img[i: i + filter_shape[0], j: j + filter_shape[1], k])
        
        return self.image, preprocessed_img, output