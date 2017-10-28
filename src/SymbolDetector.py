import cv2
import numpy as np
import meta
import os
import models.Rectangle as Rectangle
import src.pre_process as part1
import src.symbol_segmentation as part2
import src.symbol_recognition as part3
import src.charToMidi as part4

def getTrainDict():
    '''
    Creates a features list from given symbol images in train directory in form of a hashmap
    :return: a hashmap(dictionary) of labelled symbols(key) and their features(value) from train directory
    '''
    trainDir = os.listdir(meta.getRootDir() + '/images/labelled_symbol/')
    trainDict = {}
    for symbolFile in trainDir:
        image = cv2.imread(meta.getRootDir() + '/images/labelled_symbol/' + symbolFile, cv2.IMREAD_GRAYSCALE)
        scaledImage = part3.scaleSymbol(image)
        meta.saveImage(scaledImage,symbolFile)
        symbolName = symbolFile.split('.')
        trainDict[symbolName[0]] = scaledImage
    return trainDict


def getTestSymbols(color_image):
    '''
    Segments the image into lines
    For each of these lines, finds individual symbol and gets a list of such symbols in
      a list of Rectangle objects.
    :param color_image: input image
    :return: list of Rectangle objects, each object shows outline of a symbol
    '''

    input_lines,stanzalinecount = part1.getLines(color_image)
    rectList = []
    for tuple in input_lines:
        rectList.append(Rectangle.Rectangle(tuple[0], tuple[1]))
    return part2.segmentImage(color_image, rectList)


def main_first(color_image):
    '''
    Takes an image, and segments it into a list of symbol images,
     and detects which music symbol best matches this symbol image.
    :param color_image: input image
    :return: list of identified symbols
    '''
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    trainDict = getTrainDict()
    testSymbols = getTestSymbols(color_image)
    testResults = []
    count = 0
    for symbol in testSymbols:
        gray_symbol = gray_image[symbol.colst:symbol.colen, symbol.rowst:symbol.rowen]
        scaledsymbol = part3.scaleSymbol(gray_symbol)
        count = count + 1
        ans = trainDict.keys()[1]
        anscount = len(np.where(scaledsymbol == trainDict[ans]))
        for trainedSymbol in trainDict.keys():
            matchcount = np.sum(scaledsymbol == trainDict[trainedSymbol])
            if matchcount > anscount:
                ans, anscount = trainedSymbol, matchcount
        testResults.append(ans)
        #meta.saveImage(scaledsymbol, ans+str(count)+"kafi.jpeg")
    return testResults

if __name__ == "__main__":
    color_image = cv2.imread(meta.getRootDir() + '/images/kafi.jpeg', cv2.IMREAD_COLOR)
    testResults = main_first(color_image)
    for i in range(len(testResults)):
         if testResults[i] == 'hy' and i>0:
             testResults[i] = testResults[i-1]
    print testResults
    part4.keyMapping(testResults,'kafi')
