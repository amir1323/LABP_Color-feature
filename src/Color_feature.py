import cv2
import numpy as np

def make_hist(img,bins):#this is the fanction that create bin color
    #img is the image
    #bins -> is the number of bins if bins equal to 4 it will be 4*4*4
    histogram = np.zeros((bins,bins,bins),dtype='int32')#create bin * bin * bin histogram
    div = 256 // bins
    h,w,C = img.shape#extract each channel
    BGR = np.zeros(C,dtype='int32')
    for y in range(h) :
        for x in range(w) :
            for c in range(C) :
                BGR[c] = img[y,x,c]//div

            histogram[BGR[0],BGR[1],BGR[2]] += 1

    return histogram

bins = 8
path = "Location"#location of dataset directory
total_hist = np.zeros((10000,bins**3))#sets a matrix of features
for i in range(1,10001):#loop for opening image
    img_path = path+str(i)+".jpg"#create images name
    img = cv2.imread(img_path)#opening image
    total_hist[i-1] = make_hist(img,bins).flatten()#call faction
    print(-i)
np.save("Location",total_hist)