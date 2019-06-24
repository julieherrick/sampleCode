from PIL import Image

def load_img(filename):
  im = Image.open(filename)
  return im

def show_img(im):
  im.show()

def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)
  
def obamicon(im):
   # Load the pixel data from im.
    
   # Create a list to hold the new image pixel data.
  
   # Define color constants to use for recoloring.
    
   # Process the pixels in the image.
      # Pixel intensity = R value + G value + B value
    
    # Save the filtered pixels as a new image
