import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array):
    """Inverts the color of the image received"""
    try:
        inverted = 255 - array
        plt.imshow(inverted)
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.2: Invert", wrap=True,
                    horizontalalignment='center', fontsize=12)
        plt.axis("off")
        plt.show()
        return inverted
    except Exception as e:
        print("Exception:", e)


def ft_red(array):
    """
    Keeps only the red channel of the image, setting others to zero.
    """
    try:
        red_filter = np.zeros_like(array)
        red_filter[:, :, 0] = array[:, :, 0]
        plt.imshow(red_filter)
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.3: Red", wrap=True,
                    horizontalalignment='center', fontsize=12)
        plt.axis("off")
        plt.show()
        return red_filter
    except Exception as e:
        print("Exception:", e)


def ft_green(array):
    """
    Keeps only the green channel of the image, setting others to zero.
    """
    try:
        green_filter = np.zeros_like(array)
        green_filter[:, :, 1] = array[:, :, 1]
        plt.imshow(green_filter)
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.4: Green", wrap=True,
                    horizontalalignment='center', fontsize=12)
        plt.axis("off")
        plt.show()
        return green_filter
    except Exception as e:
        print("Exception:", e)


def ft_blue(array):
    """
    Keeps only the blue channel of the image, setting others to zero.
    """
    try:
        blue_filter = np.zeros_like(array)
        blue_filter[:, :, 2] = array[:, :, 2]
        plt.imshow(blue_filter)
        plt.axis("off")
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.5: Blue", wrap=True,
                    horizontalalignment='center', fontsize=12)
        plt.show()
        return blue_filter
    except Exception as e:
        print("Exception:", e)


def ft_grey(array):
    """
    Converts the image to grayscale by averaging the RGB values,
    and replicates the grayscale values across all channels.

    Parameters:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The grayscale image array with the same shape as the input.
    """
    try:
        grey_array = np.mean(array, axis=2, keepdims=True).astype(np.uint8)
        grey_filter = np.repeat(grey_array, 3, axis=2)

        # Display the image
        plt.imshow(grey_filter)
        plt.axis("off")
        plt.subplots_adjust(bottom=0)
        plt.figtext(0.5, 0.05, "Figure VIII.6: Grey", wrap=True,
                    horizontalalignment='center', fontsize=12)
        plt.show()
    except Exception as e:
        print("Exception:", e)

    return grey_filter
