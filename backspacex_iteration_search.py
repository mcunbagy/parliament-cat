import numpy as np
import time
class oyuncuclass:
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
        self.renkler = clrDictionary

                                                                                                                                                                                                           
    def run(self, img, info):
      imS = img.shape[0] # assume square image and get size
      # get current location 
      loc, game_point = info[self.name]
      y,x = loc # get current y,x coordinates
      # a very simple randomizer
      maxL = self.maxStep # total travel
      self.renkler['white']=((255,255,255),0,0)
      renkler = tuple(self.renkler.values())           #diger versiyonda burasi tuple degil set
        
      #komsu renklerin puanlarini bul
      #5 secenek var
      islemler = [-50,0,50,100,-100]
      hedef_puan = 0
      hedef_coord = [y+50, x]
      for sayi1 in islemler:
        for sayi2 in islemler:
          #if tuple(img[y+sayi1,x+sayi2]) == tuple(renkler[0][0]):
          if y+sayi1<0 or y+sayi1>750 : continue
          if x+sayi2<0 or x+sayi2>750 : continue

          if tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[0][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[0][1])
            puan=renkler[0][1]
            if puan>hedef_puan:
              #print('0')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[1][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[1][1])
            puan=renkler[1][1]
            if puan>hedef_puan:
              #print('1')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[2][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[2][1])
            puan=renkler[2][1]
            if puan>hedef_puan:
              #print('2')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[3][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[3][1])
            puan=renkler[3][1]
            if puan>hedef_puan:
              #print('3')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[4][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[4][1])
            puan=renkler[4][1]
            if puan>hedef_puan:
              #print('4')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[5][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[5][1])
            puan=renkler[5][1]
            if puan>hedef_puan:
              #print('5')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[6][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[6][1])
            puan=renkler[6][1]
            if puan>hedef_puan:
              #print('6')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[7][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[7][1])
            puan=renkler[7][1]
            if puan>hedef_puan:
              #print('7')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          elif tuple(img[y+sayi1, x+sayi2]) == tuple(renkler[8][0]):
            #print(tuple(img[y+sayi1,x+sayi2]))
            #print(renkler[8][1])
            puan=renkler[8][1]
            if puan>hedef_puan:
              #print('8')
              hedef_puan=puan
              hedef_coord=[y+sayi1,x+sayi2]
          
          else :
            continue
            
      ny,nx= hedef_coord
      return[ [y,nx] , [ny,nx], [ny,nx+1] ]
