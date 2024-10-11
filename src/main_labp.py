# main.py
import cv2
import numpy as np
from labp_function import circ_classical_labp

def process_images(path, num_images, r, p):
    """
    Process a batch of images, compute LBP for each, and store histograms in a file.

    Parameters:
        path (str): Path to the directory containing images.
        num_images (int): Number of images to process.
        r (int): Radius for LBP computation.
        p (int): Number of neighbors (points) for LBP computation.
    """
    # Initialize an array to store histograms for all images
    total_hist = np.zeros((num_images, 256))

    # Iterate through each image
    for i in range(num_images):
        # Construct the path for the current image
        img_path = f"{path}{i}.jpg"
        # Read the image in grayscale
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            print(f"Image {img_path} not found, skipping.")
            continue

        # Get image dimensions
        height, width = img.shape
        # Initialize a new array to store the LBP image
        lbp_img = np.zeros((height, width), dtype=np.uint8)

        # Extend the image with padding to avoid boundary issues
        pad_width = ((r, r), (r, r))
        padded_img = np.pad(img, pad_width, mode='edge')

        # Calculate LBP for each pixel in the original (unpadded) image
        for y in range(r, height + r):
            for x in range(r, width + r):
                lbp_img[y - r, x - r] = circ_classical_lbp(padded_img, y, x, r, p)

        # Calculate histogram of the LBP image
        hist, _ = np.histogram(lbp_img.flatten(), bins=256, range=(0, 256))
        # Store the histogram in the total histogram array
        total_hist[i] = hist

        print(f"Processed image {i + 1}/{num_images}")

    # Save the total histograms to a file
    np.save("histograms.npy", total_hist)
    print(f"Histograms saved to 'histograms.npy'.")

# Example usage of the process_images function
if __name__ == "__main__":
    image_directory = "path/to/images/"
    number_of_images = 1000  # Number of images to process
    radius = 2  # LBP radius
    num_neighbors = 8  # Number of neighbors for LBP
    
    # Process the images and save histograms
    process_images(image_directory, number_of_images, radius, num_neighbors)
