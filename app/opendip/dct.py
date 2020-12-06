from PIL import Image
import numpy as np

class DCT:
    
    def __init__(self):
        self.image = None

    def get_bidimensional_dct(self, image_path):
        self.image = np.array(Image.open(image_path).convert('RGB'))
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
                        self.resulting_image[k][l] += self.image[k][l][0] * (np.cos((2 * m  + 1) * k * np.pi)/ ( 2 * R )) * (np.cos((2 * n + 1) * l * np.pi) / 2 * C)
                
                self.resulting_image[k][l] *= ck * cl

        self.resulting_image *= 2 / np.sqrt(R*C)

        return self.resulting_image

    def get_onedimensional_dct(self, rotation="vertical"):
        pass

    def preserve_levels(self, n):
        pass

    def get_inverse_bidimensional_dct(self):

        #trunca no final
        pass

    def execute_pipeline(self, image_path, n, two_d=False):
        if two_d:
            self.get_bidimensional_dct(image_path)
        else:
            self.get_onedimensional_dct(rotation="vertical")
            self.get_onedimensional_dct(rotation="horizontal")

        self.preserve_levels(n)
        self.get_inverse_bidimensional_dct()

        pass