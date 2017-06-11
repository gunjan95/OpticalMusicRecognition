import cv2
import Rectangle as Rect
import numpy as np
import meta

from models.Verse import Verse

class Bandish:

    def __init__(self,image):
        self.image = image
        self.verses = []
        self.stanzaList = []

    def addStanza(self,rect):
        self.stanzaList.append(rect)

    def addVerse(self,verse):
        self.verses.append(verse)

    def displayVerses(self):
        for verse in self.verses:
            cv2.rectangle(self.image, verse.start, verse.end, (0, 0, 0), 1)
        meta.displayImage(self.image,'Verse')


    def displayStanza(self):
        for stanza in self.stanzaList:
            cv2.rectangle(self.image, stanza.top_left, stanza.bottom_right, (0, 0, 255), 1)
        meta.displayImage(self.image,'Stanza')
