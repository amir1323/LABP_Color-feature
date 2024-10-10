import cv2
import numpy as np
import math

def bilinear_interpolation(img,y,x):
    if (y - int(y) == 0) and (x - int(x) == 0):
        return img[int(y),int(x)]
    elif (y - int(y) == 0):
        x1 = int((x))
        x2 = int(x + 1)
        return (((x2 - x )/(x2-x1)*(img[int(y),int(x1)]))+((x-x1)/(x2-x1)*(img[int(y),int(x2)])))
    elif (x - int(x)==0):
        y1 = int((y))
        y2 = int(y + 1)
        return ((((y2-y)/(y2-y1))*(img[int(y1),int(x)]))+(((y-y1)/(y2-y1))*(img[int(y2),int(x)])))
    else :
        x1 = int((x))
        y1 = int((y))
        x2 = int(x+1)
        y2 = int(y+1)
        q11 = img[y1][x1]
        q12 = img[y2][x1]
        q21 = img[y1][x2]
        q22 = img[y2][x2]
        return ((1/((x2-x1)*(y2-y1))    *   (((x2-x)*((q11*(y2-y))+(q12*(y-y1))))+((x-x1)*((q21*(y2-y))+(q22*(y-y1)))))))




def circ_classical_lbp(img,y,x,r,p):
    binary_color = 0
    center = img[y , x]
    angles = np.linspace(0, 2 * np.pi, p + 1)[:-1]
    for angle in angles:
        y_point1 = (y - ((r-1) * np.sin(angle)))
        x_point1 = (x + ((r-1) * np.cos(angle)))
        y_point2 = (y - (r  * np.sin(angle)))
        x_point2 = (x + (r * np.cos(angle)))
        newval1 = bilinear_interpolation(img,y_point1,x_point1)
        newval2 = bilinear_interpolation(img, y_point2, x_point2)
        p_value = np.uint8(round( ( newval1 + newval2) / 2,0))
        binary_color <<= 1
        binary_color |= (p_value >= center)
    return binary_color


#############################################################################
path = "location"
total_hist = np.zeros((1000,256))
for i in range(0,1000):
    img_path = path+str(i)+".jpg"
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    newimg =np.zeros((height,width),dtype=np.uint8)
    r = 2
    p = 8
    pad_width = ((r, r), (r, r))
    exteded_img  = np.pad(img, pad_width, mode='edge')
    for y in range(r,height+r) :
        for x in range(r,width+r):
            newimg[y-r , x-r]=circ_classical_lbp(exteded_img,y,x,r,p)

    hist , bing_edges = np.histogram(newimg.flatten(),256)
    total_hist[i] = hist
    print(i)
np.save("Location",total_hist)