from PIL import Image
import numpy as np

from PIL import ImageFilter

class Filter:
    def __init__(self):
        self.image = None
    
    def apply_negative_filter(self,image_path,R=True,G=True,B=True):
      # self.image = np.array(Image.open(image_path).convert('RGB'))
      self.image = Image.open(image_path)

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

      

      # Display the negative image

      self.image.show()

