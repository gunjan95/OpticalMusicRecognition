import cv2
import numpy as np
import meta
import os


def scaleSymbol(symbolImage):
    '''
    Truncates all the exterior white rows and columns, scales it to 16X16 size and returns it
    :param symbolImage: Image of a symbol
    :return: scaled image
    '''
    #meta.saveImage(symbolImage,"input.jpeg")
    symbolImage = meta.adapt_mean_threshold(symbolImage,blockSize=9,C=7)
    #meta.saveImage(symbolImage, "meanThres.jpeg")
    symbolImage = meta.binary_threshold(symbolImage,200)
    #symbolImage = meta.gauss_otsu_threshold(symbolImage,ksize=3)
    #meta.saveImage(symbolImage, "BinThres.jpeg")
    height, width = symbolImage.shape
    black_rows = np.where(np.any(symbolImage == 0, axis=1))[0]
    black_cols = np.where(np.any(symbolImage == 0, axis=0))[0]
    row_start,row_end = 0,height-1
    if len(black_rows) > 0:
        row_start, row_end = min(black_rows),max(black_rows)
    col_start,col_end = 0,width-1
    if len(black_cols) > 0:
        col_start, col_end = min(black_cols),max(black_cols)
    s = cv2.resize(symbolImage[row_start:row_end+1,col_start:col_end+1],(32,32))
    return meta.otsu_threshold(s)


if __name__ == "__main__":
    trainDir = os.listdir(meta.getRootDir() + '/images/labelled_symbol/')
    trainDict = {}
    for symbolFile in trainDir:
        print symbolFile
        image = cv2.imread(meta.getRootDir() + '/images/labelled_symbol/'+symbolFile, cv2.IMREAD_GRAYSCALE)
        scaledImage = scaleSymbol(image)
        meta.saveImage(scaledImage,"output.jpeg")
        trainDict[symbolFile[:-5]] = scaledImage
    print trainDict.keys()



    # meta.displayImage(scaledImage,"ScaledImage")