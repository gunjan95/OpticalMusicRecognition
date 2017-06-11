# Input: Original Image
# Step 1: Identify Region of Interest(ROI)
# Step 2: Remove Noise


import cv2
import  meta
import models.Bandish as Ban
import models.Rectangle as Rect
import numpy as np

#
# ------------ Step 1 (Identification of ROI)------------------------------------------------------------



def getLines(color_image):
    '''
    It takes color image as input and detect lines
    :param color_image:
    :return: segmented lines
    '''
    lines = []
    gray = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
    image = np.copy(color_image)
    # meta.displayImage(image,'Lines')                                                        # grayscale
    thresh = meta.binary_inverse_threshold(gray,150)                                        # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,2))                               # kernel definition
    dilated = cv2.dilate(thresh,kernel,iterations = 10)                                     # dilate
    # meta.displayImage(dilated,'dilated')
    _,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)      # get contours


    #-------Step 2 Identification of lines --------------------------------------------------------------------

    binary_thresh = meta.binary_threshold(gray,150)
    #cv2.imshow('thresh',binary_thresh)
    # for each contour found, draw a rectangle around it on original image
    countourcount = 0;
    stanzalinecount = 0;
    for contour in contours:
        countourcount += 1;
        [x, y, w, h] = cv2.boundingRect(contour)                                    # get rectangle bounding contour
        if h < 40 or w < 40:                                                        # discard areas that are too small
            continue

        start_point = (x,y)
        end_point = (x+w,y+h)
        (x1, y1) = start_point
        (x2, y2) = end_point
        horizontal_histogram = np.zeros(y2+1)
        for i in range(y1, y2):
            for j in range(x1, x2):
                if (binary_thresh[i][j] == 0):
                    horizontal_histogram[i] = horizontal_histogram[i] + 1
        i = y1
        count = 0
        # print np.min(horizontal_histogram[y1+1:y2])
        # print np.max(horizontal_histogram)
        # print np.average(horizontal_histogram[y1+1:y2])
        while (i < y2):
            while (i < y2 and horizontal_histogram[i] <= 10):
                i = i + 1
            start = i
            while (i < y2 and horizontal_histogram[i] > 10):
                i = i + 1
            end = i
            if (end - start >= 15):
                #output.append(((start, y1), (end, y2)))
                count += 1
                if (count%2 == 1):
                    lines.append(((x1,start), (x2,end)))
                    if(countourcount == 0):
                        stanzalinecount += 1
                    cv2.rectangle(image, (x1,start), (x2,end), 0,2)

    meta.displayImage(image,'final')                                                # display image with contour
    return  lines,stanzalinecount







