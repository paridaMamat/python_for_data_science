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

        zoomed_img = img_array[starty:starty+new_height, startx:startx+new_width, 0:1]
        print(f"The shape of image is: {zoomed_img.shape}")
        print(zoomed_img)

        return zoomed_img
    
    except Exception as e:
        print(f"Error: {e}")


def manual_transpose(zoomed_img):
    """
    transposes a 2D array manually
    """
    transposed = [[zoomed_img[j][i] for j in range(len(zoomed_img))] for i in range(len(zoomed_img[0]))]
    return np.array(transposed)

def display_image(transposed):
    """
    Display the new shape and data of the transposed image.
    """
    print(f"New shape after Transpose: {transposed.shape[:2]}")
    
    # Format output for display similar to the expected 2D array format
    # for row in transposed[:10]:  # Print first 10 rows to limit output
    #     print(" ".join(map(str, row)))
    print(transposed)

     # Convert the transposed image back to a NumPy array and display it
    # transposed_array = np.array(transposed, dtype=np.uint8)
    plt.imshow(transposed, cmap='gray')
    plt.axis("on")  # Display axis
    plt.show()
    

def main():
    """
    load the image "animal.jpeg", print some information
    about it and display it after "zooming"
    """

    img_array = ft_load("animal.jpeg")
    if img_array is not None:
        zoomed_img = zoom_img(img_array)
        transposed = manual_transpose(zoomed_img)
        display_image(transposed)





if __name__ == "__main__":
    main()