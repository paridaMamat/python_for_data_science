import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_img(img_array):
    """
    Get the shape information (height, width),
    and cut the image in 400 * 400.
    return new image pixel in array
    """
    try:
        height, width, channels = img_array.shape

        new_height, new_width = 400, 400
        startx = width // 2 - (new_width // 2) + 138
        starty = height // 2 - (new_height // 2) - 84

        zoomed_img =\
            img_array[starty:starty+new_height, startx:startx+new_width, 0:1]
        print("New shape after slicing:",
              zoomed_img.shape, "or", zoomed_img.shape[:2])
        print(zoomed_img)

        return zoomed_img

    except Exception as e:
        print(f"Error: {e}")


def display_image(zoomed_img):
    """
    Display grayscale images
    """
    plt.imshow(np.squeeze(zoomed_img), cmap='gray')
    plt.show()


def main():
    """
    load the image "animal.jpeg", print some information
    about it and display it after "zooming"
    """

    img_array = ft_load("animal.jpeg")
    print(img_array)
    if img_array is not None:
        zoomed_img = zoom_img(img_array)
        display_image(zoomed_img)


if __name__ == "__main__":
    main()
