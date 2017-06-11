import cv2
import numpy as np
import models.Rectangle as Rectangle
import meta

'''
Identify individual characters from given lines
Input - Image and cordinates of lines
Output - binary image and cordinates of characters
'''
def segmentImage(image,rectList):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    binary_image = cv2.threshold(gray_image,200,255,cv2.THRESH_BINARY)[1]
    rows, cols = binary_image.shape
    eroded_image = cv2.erode(binary_image,np.ones((3, 3), np.uint8), iterations=1)
    output = []
    count=0
#    meta.displayImage(eroded_image,"erode")
    for rect in rectList:
        start_point = rect.top_left
        end_point = rect.bottom_right
        (x1,y1) = start_point
        (x2,y2) = end_point
        vertical_histogram = np.zeros(y2+1)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if(eroded_image[i][j] == 0):
                    count += 1
                    vertical_histogram[j] = vertical_histogram[j]+1
#        calculates vertical_histogram
        i=y1
        while(i<=y2):
            while(i<=y2 and vertical_histogram[i]==0):
                i=i+1
            start = i
            while(i<=y2 and vertical_histogram[i]>0):
                i=i+1
            end=i
            if(end-start >= 7):
#                Identified a symbol
                output.append(Rectangle.Rectangle((start,x1),(end,x2)))
                cv2.rectangle(binary_image,(start,x1),(end,x2),0,1)
    meta.displayImage(binary_image,'binary')
    return output


if __name__ == "__main__":
    color_image = cv2.imread(meta.getRootDir() + '/images/vasant_cont.jpeg',cv2.IMREAD_COLOR)
    input_lines = [((0,0),(439,30)),((0,90),(439,120)),((0,213),(439,243))]
    rectList = []
    for tuple in input_lines:
        rectList.append(Rectangle.Rectangle(tuple[0],tuple[1]))
    o,binary_image = segmentImage(color_image,rectList)
    cv2.imshow('binary_image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
