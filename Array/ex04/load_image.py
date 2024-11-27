import numpy as np
from PIL import Image


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

        return img_array

    except FileNotFoundError:
        print(f"Error: File {path} not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
