from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class DCT:
    def __init__(self):
        self.input_dct2d = None
        self.output_dct2d = None
        
        self.input_idct2d = None
        self.output_idct2d = None

    def get_2d_dct(self, image, n_coef = 0):
        self.input_dct2d = image

        output = np.zeros(image.shape)

        R = output.shape[0]
        C = output.shape[1]

        for k in range(R):
            ck = np.sqrt(0.5) if k == 0 else 1
            for l in range(C):
                cl = np.sqrt(0.5) if l == 0 else 1
                for m in range(R):
                    for n in range(C):
                        output[k][l] += image[m][n] * np.cos(((2*m + 1) * k*np.pi)/(2*R)) * np.cos(((2*n + 1) * l*np.pi)/(2*C))
                output[k][l] *= ck * cl

        output *= 2.0/np.sqrt(R*C)

        if n_coef > 0:
            output.sort()
            for i in range(n_coef, n):
                output[i] = 0

        self.output_dct2d = output

        return output
        
    def get_2d_dct_sep(self, image, n_coef = 0):
        self.input_dct2d = image
        
        output = np.zeros(image.shape)
        
        for row in range(image.shape[0]):
            output[row, :] = self.get_1d_dct(image[row, :], n_coef)
        
        for column in range(image.shape[1]):
            output[:, column] = self.get_1d_dct(output[:, column], n_coef)

        self.output_dct2d = output      
        
        return output
    
    def get_1d_dct(self, image, n_coef = 0):
        output = np.zeros(image.shape)
        n = len(image)

        for k in range(n):
            ck = np.sqrt(0.5) if k == 0 else 1
            for i in range(n):
                output[k] += image[i] * np.cos(2 * np.pi * k / (2.0 * n) * i + (k * np.pi) / (2.0 * n))
            output[k] *= ck

        output *= np.sqrt(2.0/n)

        if type(n_coef) == float or type(n_coef) == np.float32:
            n_coef = int(n_coef * len(output))


        if n_coef > 0:
            output.sort()
            for i in range(n_coef, n):
                output[i] = 0

        return output

    def get_inv_2d_dct(self, dct = None):
        if type(dct) == type(None):
            dct = self.output_dct2d
            
        self.input_idct2d = dct

        output = np.zeros(dct.shape)

        R = output.shape[0]
        C = output.shape[1]

        for m in range(R):
            for n in range(C):
                for k in range(R):
                    ck = np.sqrt(0.5) if k == 0 else 1
                    for l in range(C):
                        cl = np.sqrt(0.5) if l == 0 else 1
                        output[m][n] += ck * cl * dct[k][l] * np.cos(((2*m + 1) * k*np.pi)/(2*R)) * np.cos(((2*n + 1) * l*np.pi)/(2*C))

        output *= (2 / np.sqrt(R*C))

        self.output_idct2d = np.round(output)

        self.output_idct2d[self.output_idct2d < 0] = 0
        self.output_idct2d[self.output_idct2d > 255] = 255
        

        return output
    
    def get_inv_2d_dct_sep(self, dct = None):
        
        if type(dct) == type(None):
            dct = self.output_dct2d
            
        self.input_idct2d = dct
        
        output = np.zeros(dct.shape)

        for row in range(dct.shape[0]):
            output[row, :] = self.get_inv_1d_dct(dct[row, :])
            
        for column in range(dct.shape[1]):
            output[:, column] = self.get_inv_1d_dct(output[:, column])
                
        self.output_idct2d = np.round(output)

        self.output_idct2d[self.output_idct2d < 0] = 0
        self.output_idct2d[self.output_idct2d > 255] = 255
        
        return output
        
    def get_inv_1d_dct(self, dct):
        output = np.zeros(dct.shape)
        n = len(dct)

        for i in range(n):
            for k in range(n):
                ck = np.sqrt(0.5) if k == 0 else 1
                output[i] += ck * dct[k] * np.cos(2 * np.pi * k / (2.0 * n) * i + (k * np.pi) / (2.0 * n))
            output[i] *= np.sqrt(2.0 / n)

        return output
    
    def show_process(self):
        return self.input_dct2d, self.output_dct2d, self.output_idct2d