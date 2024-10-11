# lbp_function.py
import numpy as np
from bilinear_interpolation import bilinear_interpolation

def circ_classical_labp(img, y, x, r, p):
    """
    Compute the circular classical Local Avrage Binary Pattern (LABP).
    
    Parameters:
        img (numpy array): Input grayscale image.
        y (int): Y-coordinate of the pixel.
        x (int): X-coordinate of the pixel.
        r (int): Radius for LBP.
        p (int): Number of neighbors.
        
    Returns:
        int: LABP value for the central pixel.
    """
    binary_color = 0
    center = img[y, x]
    angles = np.linspace(0, 2 * np.pi, p + 1)[:-1]

    for angle in angles:
        y_point1 = (y - ((r - 1) * np.sin(angle)))
        x_point1 = (x + ((r - 1) * np.cos(angle)))
        y_point2 = (y - (r * np.sin(angle)))
        x_point2 = (x + (r * np.cos(angle)))
        
        newval1 = bilinear_interpolation(img, y_point1, x_point1)
        newval2 = bilinear_interpolation(img, y_point2, x_point2)
        p_value = np.uint8(round((newval1 + newval2) / 2, 0))
        
        binary_color <<= 1
        binary_color |= (p_value >= center)

    return binary_color
