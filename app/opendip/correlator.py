from PIL import Image
import numpy as np
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Correlator:
    
    def __init__(self):
        self.image = None
        self.filter = None

    def __padding(self, horizontal_padding, vertical_padding):
        padded_image = np.zeros((self.image.shape[0] + 2 * vertical_padding, self.image.shape[1] + 2 * horizontal_padding, 3))
        padded_image[vertical_padding : -vertical_padding, horizontal_padding : -horizontal_padding, :] = self.image 

        return padded_image
        
        
    def apply_correlation(self, image_path, filter_matrix, zero_padding = True):
        self.image = np.asarray(Image.open(image_path).convert('RGB'))
        self.filter = filter_matrix
        
        horizontal_padding = self.filter.shape[0]//2
        vertical_padding = self.filter.shape[1]//2
        output = np.zeros((self.image.shape[0], self.image.shape[1], 3))
        

        print(f"{horizontal_padding} and {vertical_padding}")
        if zero_padding:
            self.image  = self.__padding(horizontal_padding, vertical_padding)
            
        for i in range(self.image.shape[0] - self.filter.shape[0]):
            for j in range(self.image.shape[1] - self.filter.shape[1]):
                for k in range(3):
#                     print(i , j , k)
#                     print(i + self.filter.shape[0], j + self.filter.shape[1])
                    output[i,j,k] = np.sum(np.multiply(self.filter, self.image[i: i + self.filter.shape[0], j: j + self.filter.shape[1], k]))
            
        return self.image, output
    
    def apply_norm_correlation(self, image_path, filter_matrix, zero_padding = True):
        self.image = np.asarray(Image.open(image_path).convert('RGB'))
        self.filter = filter_matrix

        if zero_padding:
            padded_image = self.__padding()
                    
        return self.image, padded_image

c = Correlator()

filter_matrix = np.ones((9, 9), np.float32)/81

image, padded_image = c.apply_correlation("../assets/Imagens_teste/2817540617.jpg", filter_matrix, zero_padding=True)

print(image.shape)
print(padded_image.shape)
image = Image.fromarray(image.astype('uint8'))
image.show()
plt.imshow(padded_image.astype(int))
plt.show()