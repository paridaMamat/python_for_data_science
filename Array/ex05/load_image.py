import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_load(path: str):
    """
    loads an image, prints its format, and its pixels
    content in RGB format
    """
    try:
        img = Image.open(path)

        if img.format.upper() != 'JPEG':
            raise ValueError("Image format Only JPG and JPEG are allowed")

        img = img.convert('RGB')

        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
        plt.imshow(img_array)
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.1: Original", wrap=True, horizontalalignment='center', fontsize=12)
        plt.axis("off")
        plt.show()
        return img_array

    except FileNotFoundError:
        print(f"Error: File {path} not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
