import numpy as np
import os
import cv2
from main_labp import process_images
from Color_feature import make_hist
from Presicion import chi_square_distance, euclidean_distance, canberra_distance, square_chord_distance

def run_labp_feature_extraction():
    """
    Run LBP feature extraction on the dataset images and save histograms.
    """
    print("Starting LBP feature extraction...")
    image_directory = "Dataset/"  # Path to the dataset directory
    number_of_images = 10000       # Adjust the number of images based on the dataset size
    radius = 2                    # Radius for LABP calculation
    num_neighbors = 8             # Number of neighbors for LABP

    process_images(image_directory, number_of_images, radius, num_neighbors)
    print("LBP feature extraction completed and saved to histograms.npy")

def run_color_hist_feature_extraction():
    """
    Run color histogram feature extraction on the dataset images and save histograms.
    """
    print("Starting color histogram feature extraction...")
    bins = 8 # this value can be set in 2 or 4 or 8 
    dataset_path = "Dataset/"#MAKE SURE DATASET IS ALREADY IN THE FOLDER
    total_hist = np.zeros((10000, bins**3))

    for i in range(1, 10001): # the Range of number in data set 
        # PLEASE NOTE THAT IF YOU ARE USING WANG(COREL-1K) DATASET CHANGE Range (0,1000)
        #IF YOU ARE USING COREL-10K DATASET CHANGE Range (1,10001)
        img_path = os.path.join(dataset_path, f"{i}.jpg")
        img = cv2.imread(img_path)
        if img is None:
            print(f"Image {img_path} not found, skipping.")
            continue
        total_hist[i-1] = make_hist(img, bins).flatten()
        print(f"Processed image {i}/10000")
    
    np.save("color_histograms.npy", total_hist)
    print("Color histogram extraction completed and saved to color_histograms.npy")

def run_combined_hist_precision_recall():
    """
    Combine LBP and color histograms and calculate precision/recall metrics.
    """
    print("Loading LBP and color histograms...")
    
    # Load the LBP and color histograms
    lbp_histograms = np.load("histograms.npy")
    color_histograms = np.load("color_histograms.npy")

    # Concatenate the histograms along the feature dimension
    combined_histograms = np.hstack((lbp_histograms, color_histograms))

    num_categories = 10 # this number can be change considering what dataset are uisng.
    elements_per_category = len(combined_histograms) // num_categories

    for N in range(10, 110, 10):
        for cotte in range(0, 1000, 1000):
            presg_tot = []
            for i in range(1000):
                T = combined_histograms[i]
                all_dis = np.zeros(len(combined_histograms), dtype='float32')
                
                for j in range(1000):
                    if i != j:
                        Q = combined_histograms[j]
                        # You can switch to other distances like euclidean_distance or canberra_distance
                        all_dis[j] = chi_square_distance(T, Q)
                    else:
                        all_dis[j] = np.inf
                
                mins_argo = np.argpartition(all_dis, N)[:N] // elements_per_category
                same_category = np.sum(mins_argo == i // elements_per_category)
                presg_tot.append(same_category / N)

            precision = np.mean(np.array(presg_tot)) * 100
            recall = (precision * N) / 100

            print(f'Combined histograms in {cotte} for N = {N}: Precision: {precision:.2f}%, Recall: {recall:.2f}%')

if __name__ == "__main__":
    # Run LBP feature extraction
    run_labp_feature_extraction()

    # Run color histogram feature extraction
    run_color_hist_feature_extraction()

    # Run precision/recall calculations on combined histograms
    run_combined_hist_precision_recall()
