import numpy as np
import time
class oyuncuclass:
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
        self.renks = clrDictionary

                                                                                                                                                                                                           
    def run(self, img, info):
        imS = img.shape[0] # assume square image and get size
        # get current location 
        loc, game_point = info[self.name]
        y,x = loc # get current y,x coordinates
        # a very simple randomizer
        maxL = self.maxStep # total travel
        self.renks['white']=((255,255,255),0,0)
        renkler = tuple(self.renks.values())           #diger versiyonda burasi tuple degil set
        
        #komsu renklerin puanlarini bul
        #5 secenek var
        islemler = [-50,0,50,100,-100]
        hedef_puan = 0
        
        for sayi1 in islemler:
          for sayi2 in islemler:
            if tuple(img[y+sayi1,x+sayi2]) == renkler[0][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[1][0]:
              puan=renkler[0][1]
              hedef_puan=max(hedef_puan, puan)
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[2][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[3][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[4][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[5][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[6][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[7][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[8][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[9][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[10][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[11][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[12][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[13][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[14][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[15][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            elif tuple(img[y+sayi1,x+sayi2]) == renkler[16][0]:
              puan=renkler[0][1]
              if puan>hedef_puan:
                hedef_puan=puan
                hedef_coord=[y+sayi1, x+sayi2]
            else :
              continue
            
            ny,nx=hedef_coord
            return[ [y,nx] , [ny,nx], [ny,nx+1] ]
       
