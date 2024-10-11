# bilinear_interpolation.py
import numpy as np

def bilinear_interpolation(img, y, x):
    """
    Perform bilinear interpolation to estimate pixel values at non-integer coordinates.
    
    Parameters:
        img (numpy array): Input image array.
        y (float): Y-coordinate.
        x (float): X-coordinate.
        
    Returns:
        float: Interpolated pixel value.
    """
    if (y - int(y) == 0) and (x - int(x) == 0):
        return img[int(y), int(x)]
    elif (y - int(y) == 0):
        x1 = int(x)
        x2 = int(x + 1)
        return ((x2 - x) / (x2 - x1) * img[int(y), int(x1)] + (x - x1) / (x2 - x1) * img[int(y), int(x2)])
    elif (x - int(x) == 0):
        y1 = int(y)
        y2 = int(y + 1)
        return ((y2 - y) / (y2 - y1) * img[int(y1), int(x)] + (y - y1) / (y2 - y1) * img[int(y2), int(x)])
    else:
        x1 = int(x)
        y1 = int(y)
        x2 = int(x + 1)
        y2 = int(y + 1)
        q11 = img[y1][x1]
        q12 = img[y2][x1]
        q21 = img[y1][x2]
        q22 = img[y2][x2]
        return (1 / ((x2 - x1) * (y2 - y1)) * 
                ((x2 - x) * ((q11 * (y2 - y)) + (q12 * (y - y1))) + 
                (x - x1) * ((q21 * (y2 - y)) + (q22 * (y - y1)))))
