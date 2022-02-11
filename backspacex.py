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
        renkler = self.renks.values()

        #komsu renklerin puanlarini bul
        for tup in renkler:
          if (y+50 < 750):
            if tuple(img[y+50,x]) in tup: komsupuanlar.add(tup[1])
          if (x+50 < 750):
            if tuple(img[y, x+50]) in tup: komsupuanlar.add(tup[1])
          if (y - 50 > 0 ):          
            if tuple(img[y-50, x]) in tup: komsupuanlar.add(tup[1])
          if (x-50 >0 ):
            if tuple(img[y, x-50]) in tup: komsupuanlar.add(tup[1])
          if (y+50 < 750) and (x+50 < 750):
            if tuple(img[y+50, x+50]) in tup: komsupuanlar.add(tup[1])
          if (y-50 >0) and (x-50 >0):
            if tuple(img[y-50, x-50]) in tup: komsupuanlar.add(tup[1])
          if (y+50 < 750) and (x-50 >0):
            if tuple(img[y+50, x-50]) in tup: komsupuanlar.add(tup[1])
          if (y-50 >0) and (x+50 < 750):
            if tuple(img[y-50, x+50]) in tup: komsupuanlar.add(tup[1])
          if (y+100<750):
            if tuple(img[y+100,x]) in tup: komsupuanlar.add(tup[1])
          if (x+100 < 750):
            if tuple(img[y,x+100]) in tup: komsupuanlar.add(tup[1])
          if (y-100 > 0):
            if tuple(img[y-100,x]) in tup: komsupuanlar.add(tup[1])
          if (x-100 > 0):
            if tuple(img[y, x-100]) in tup: komsupuanlar.add(tup[1])
        
        #hedef noktasini bul ve oraya git  
        hedef = max(komsupuanlar)
        if hedef == puan1: 
            return  [ [y, x+1] , [y+50, x+1] , [y+50, x+2] ]
        
        if hedef == puan2:
            return  [ [y , x+50 ] , [y+1 , x+50 ] , [y+1 ,x+51] ]
        
        if hedef == puan3: 
            return  [ [y, x+1 ] , [y-50 , x+1 ] , [y-50 , x+2 ] ]
        
        if hedef == puan4:
            return  [ [y , x-50 ] , [y+1 , x-50 ] , [y+1 , x-51 ] ]
        
        if hedef == puan5: 
            return  [ [y , x+50 ] , [y+50 , x+50 ] , [y+50 , x+51]  ]
        
        if hedef == puan6:
            return  [ [y , x-50 ] , [y-50 , x-50 ] , [ y-50 , x-51 ] ]
        
        if hedef == puan7: 
            return  [ [y , x-50 ], [ y-50 , x-50 ] , [ y-50 ,x-51 ]  ]
        
        if hedef == puan8:
            return  [ [y , x+50 ] , [y-50 , x+50 ] , [ y-50 , x+51 ]  ]
        
        if hedef == puan9:
            return  [ [y , x+1 ] , [ y+100 , x+1 ]  , [ y+100 ,x+2 ] ]
        
        if hedef == puan10:
            return  [ [y , x+100 ] , [ y+1 , x+100 ], [ y+1 , x+101 ] ]
        
        if hedef == puan11:
            return  [ [y , x+1 ] , [ y-100 ,x+1 ],   [ y-100 , x+2 ] ]
        
        if hedef == puan12:
            return  [ [y, x-100 ] , [y+1 , x-100 ] , [ y+1 , x-101 ] ]
        
        else : 
            return  [ [y, x+50 ] , [ y+50 , x+50 ],  [ y+50 , x+51 ] ]

