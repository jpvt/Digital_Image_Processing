from PIL import Image
import numpy as np

class DCT:
    
    def __init__(self):
        self.image = None

    def get_bidimensional_dct(self, image_path):
        self.image = np.array(Image.open(image_path).convert('L'))
        self.resulting_image = np.zeros(self.image.shape)

        R = self.resulting_image.shape[0]
        C = self.resulting_image.shape[1]

        for k in range(R):

            if k == 0:
                ck = np.sqrt(1/2)
            else:
                ck = 1
            
            for l in range(C):

                if l == 0:
                    cl = np.sqrt(1/2)
                else:
                    cl = 1
 
                for m in range(R):
                    for n in range(C):
                        self.resulting_image[k][l] += self.image[k][l] * (np.cos((2 * m  + 1) * k * np.pi)/ ( 2 * R )) * (np.cos((2 * n + 1) * l * np.pi) / 2 * C)
                
                self.resulting_image[k][l] *= ck * cl

        self.resulting_image *= 2 / np.sqrt(R*C)

        return self.resulting_image
    
    
    def get_bidimensional_dct_sep(self, image_path, n_coef = 0):

        self.image = np.array(Image.open(image_path).convert('L'))
        self.resulting_image = np.zeros(self.image.shape)

        R = self.resulting_image.shape[0]
        C = self.resulting_image.shape[1]

        for k in range(R):

            self.resulting_image[k, :] = self._get_onedimensional_dct(self.image[k, :], n_coef)
        
        for l in range(C):

            self.resulting_image[:, l] = self._get_onedimensional_dct(self.image[:, l], n_coef)

        return self.resulting_image
        
        
    def _get_onedimensional_dct(self, image, n_coef = 0):

        resulting_image = np.zeros(image.shape)

        N = len(self.image)

        for k in range(N):
            sum = 0

            for l in range(N):

                sum += image[l] * np.cos(2 * np.pi * k / (2.0 * N) * l + (k*np.pi)/(2.0*N))

            ck = np.sqrt(1/2) if k == 0 else 1
            resulting_image[k] = np.sqrt(2.0/N) * ck * sum

        if n_coef > 0:

            resulting_image.sort()

            for i in range(n_coef, N):

                resulting_image[i] = 0

        return resulting_image

    def preserve_levels(self, n):
        pass

    def get_inverse_bidimensional_dct(self):
        self.inverse_transformed_image = np.zeros(self.image.shape)

        R = self.resulting_image.shape[0]
        C = self.resulting_image.shape[1]

        for m in range(R):

            for n in range(C):
 
                for k in range(R):
                    
                    if k == 0:
                        ck = np.sqrt(1/2)
                    else:
                        ck = 1
                        
                    for l in range(C):

                        if l == 0:
                            cl = np.sqrt(1/2)
                        else:
                            cl = 1
                        
                        self.inverse_transformed_image[m][n] += ck * cl * self.resulting_image[k][l] * (np.cos((2 * m  + 1) * k * np.pi)/ ( 2 * R )) * (np.cos((2 * n + 1) * l * np.pi) / 2 * C)

        self.inverse_transformed_image *= 2 / np.sqrt(R*C)

        return self.inverse_transformed_image

    def execute_pipeline(self, image_path, n, two_d=False):
        if two_d:
            self.get_bidimensional_dct(image_path)
        else:
            self.get_onedimensional_dct(rotation="vertical")
            self.get_onedimensional_dct(rotation="horizontal")

        self.preserve_levels(n)
        self.get_inverse_bidimensional_dct()

        pass