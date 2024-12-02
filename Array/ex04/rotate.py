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
        shape_full = zoomed_img.shape
        shape_2d = zoomed_img.shape[:2]
        print(f"The shape of the image is: {shape_full} or {shape_2d}")
        print(zoomed_img)

        return zoomed_img

    except Exception as e:
        print(f"Error: {e}")


def manual_transpose(zoomed_img):
    """
    transposes a 2D array manually
    """
    transposed = []  # Initialize the transposed array

    # Outer loop for columns (new rows in the transposed image)
    for i in range(len(zoomed_img[0])):
        new_row = []  # Initialize a new row for the transposed image
        # Inner loop for rows (new columns in the transposed image)
        for j in range(len(zoomed_img)):
            new_row.append(zoomed_img[j][i])  # Add each pixel to the new row
        transposed.append(new_row)  # Add the new row to the transposed array
    return np.array(transposed)


def display_image(transposed):
    """
    Display the new shape and data of the transposed image.
    """
    print(f"New shape after Transpose: {transposed.shape[:2]}")

    transposed = np.array(transposed).squeeze()
    print(transposed)
    plt.imshow(transposed, cmap='gray')
    plt.axis("on")  # Display axis
    plt.show()


def main():
    """
    load the image "animal.jpeg", print some information
    about it and display it after "zooming"
    """
    try:
        img_array = ft_load("animal.jpeg")
        if img_array is not None:
            zoomed_img = zoom_img(img_array)
            transposed = manual_transpose(zoomed_img)
            display_image(transposed)

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
