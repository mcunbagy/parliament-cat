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
        komsupuanlar = set()
        

        #komsu renklerin puanlarini bul
        for tup in renkler:
          if (y+50 < 750):
            if tuple(img[y+50,x]) in tup: puan1 = tup[1]
            else:puan1=0
          else:puan1=0
          if (x+50 < 750):
            if tuple(img[y, x+50]) in tup: puan2 = tup[1]
            else:puan2=0
          else:puan2=0
          if (y - 50 > 0 ):          
            if tuple(img[y-50, x]) in tup: puan3 = tup[1]
            else:puan3=0
          else:puan3=0
          if (x-50 >0 ):
            if tuple(img[y, x-50]) in tup: puan4 = tup[1]
            else:puan4=0
          else:puan4=0
          if (y+50 < 750) and (x+50 < 750):
            if tuple(img[y+50, x+50]) in tup: puan5 = tup[1]
            else:puan5=0
          else:puan5=0
          if (y-50 >0) and (x-50 >0):
            if tuple(img[y-50, x-50]) in tup: puan6 = tup[1]
            else:puan6=0
          else:puan6=0
          if (y+50 < 750) and (x-50 >0):
            if tuple(img[y+50, x-50]) in tup: puan7 = tup[1]
            else:puan7=0
          else:puan7=0
          if (y-50 >0) and (x+50 < 750):
            if tuple(img[y-50, x+50]) in tup: puan8 = tup[1]
            else:puan8=0
          else:puan8=0
          if (y+100<750):
            if tuple(img[y+100,x]) in tup: puan9 = tup[1]
            else:puan9=0
          else:puan9=0
          if (x+100 < 750):
            if tuple(img[y,x+100]) in tup: puan10 = tup[1]
            else:puan10=0
          else:puan10=0
          if (y-100 > 0):
            if tuple(img[y-100,x]) in tup: puan11 = tup[1]
            else:puan11=0
          else:puan11=0
          if (x-100 > 0):
            if tuple(img[y, x-100]) in tup: puan12 = tup[1]
            else:puan12=0
          else:puan12=0
        
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

