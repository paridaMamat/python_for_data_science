from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def display_image(image_array):
    """
    Display grayscale images
    """
    array_3d = np.random.rand(10, 10, 3) 
    plt.imshow(image_array)
    plt.axis('off')  # Hide axis
    plt.show()


def main():
    img_array = ft_load("landscape.jpg")
    display_image(img_array)
    # red_channel = img_array[:, :, 0]
    # green_channel = img_array[:, :, 1]
    # blue_channel = img_array[:, :, 2]

    # display_image(red_channel)
    # display_image(green_channel)
    # display_image(blue_channel)


if __name__ == "__main__":
    main()