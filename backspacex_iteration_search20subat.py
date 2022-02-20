import numpy as np
import time
class backspacex:
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
        self.clrs = clrDictionary

                                                                                                                                                                                                           
    def run(self, img, info):
      # get current location 
      loc, game_point = info[self.name]
      y,x = loc # get current y,x coordinates
      #self.renkler['white']=((255,255,255),0,0)
      renkler = tuple(self.clrs.values())   #diger versiyonda burasi tuple degil set

      #komsu renklerin puanlarini bul
      #5 secenek var
      kisa_islemler1 = [0,26,-26,51,-51]
      kisa_islemler2 = [0,51,-51,76,-76]
      uzun_islemler = [0,76,-76, 101,-101]
      #ekstrem_islemler1 = [-100,100,-125,125]
      
      
      hedef_puan = 0
      hedef_puan2= 0
      hedef_puan3 =0 
      hedef_coord = [ [y,x] , [y,x] , [y,x] ]
      
      for sayi1 in kisa_islemler1:
          if y+sayi1<50 or y+sayi1>700 : continue
          for sayi2 in kisa_islemler1:
              if x+sayi2<50 or x+sayi2>700 : continue
              if sayi1==0 and sayi2==0 : continue
              if tuple(img[y+sayi1, x+sayi2]) == (255,255,255):continue
              if tuple(img[y+sayi1, x+sayi2]) == (1,1,1):continue
              for i in range(len(renkler)):
                  if tuple(img[y+sayi1, x+sayi2]) == renkler[i][0]:
                      puan=renkler[i][1]
                      if puan>hedef_puan and puan<=game_point:
                          hedef_puan=puan
                          hedef_coord[0]=[y+sayi1, x+sayi2]

                      break
      hedef_coord[1]=hedef_coord[0]
      ny , nx = hedef_coord[0]
          

      for sayi1 in kisa_islemler2:
          if ny+sayi1<50 or ny+sayi1>700 : continue
          for sayi2 in kisa_islemler2:
              if nx+sayi2<0 or nx+sayi2>=750 : continue
              if sayi1==0 and sayi2==0 : continue

              if tuple(img[ny+sayi1, nx+sayi2]) == (255,255,255):continue
              if tuple(img[ny+sayi1, nx+sayi2]) == (1,1,1):continue
              for i in range(len(renkler)):
                  if tuple(img[ny+sayi1, nx+sayi2]) == renkler[i][0]:
                      puan2=renkler[i][1]
                      if puan2>hedef_puan2 and puan2<=game_point-hedef_puan:
                          hedef_puan2 = puan2
                          hedef_coord[1]=[ny+sayi1, nx+sayi2]
                          #if hedef_coord[0]==[y,x] : 
                          #    hedef_coord[0]=[ny+sayi1,nx+sayi2]
                          #    hedef_coord[1]=[ny+sayi1, nx+sayi2]
                          #    hedef_coord[2]=[ny+sayi1, nx+sayi2]
                          #else :
                          #    hedef_coord[1]=[ny+sayi1, nx+sayi2]
                          #    hedef_coord[2]=[ny+sayi1, nx+sayi2]
                      break
      if hedef_coord[0]==[y,x] : hedef_coord[0]=hedef_coord[1] 
      ny,nx=hedef_coord[0]
      ny2,nx2=hedef_coord[1]
      hedef_coord[2]=hedef_coord[1]

      
      for sayi1 in uzun_islemler:
          if ny2+sayi1<50 or ny2+sayi1>700 : continue
          for sayi2 in uzun_islemler:
              if nx2+sayi2<0 or nx2+sayi2>700 : continue
              if sayi1==0 and sayi2==0 : continue
              if tuple(img[ny2+sayi1, nx2+sayi2]) == (255,255,255):continue
              if tuple(img[ny2+sayi1, nx2+sayi2]) == (1,1,1):continue

      
              for i in range(len(renkler)):
                  if tuple(img[ny2+sayi1, nx2+sayi2]) == renkler[i][0]:
                      puan3=renkler[i][1]
                      if puan3>hedef_puan3 and puan3<=game_point-hedef_puan-hedef_puan2:
                          hedef_puan3 = puan3
                          hedef_coord[2]=[ny2+sayi1,nx2+sayi2]
                          #if hedef_coord[0]==[y,x]:
                          #    hedef_coord[0]=[ny2+sayi1,nx2+sayi2]
                          #    hedef_coord[1]=[ny2+sayi1,nx2+sayi2]
                          #    hedef_coord[2]=[ny2+sayi1,nx2+sayi2]
                          #elif hedef_coord[1]==[y,x]:
                          #    hedef_coord[1]=[ny2+sayi1,nx2+sayi2]
                          #    hedef_coord[2]=[ny2+sayi1,nx2+sayi2]
                          #else : 
                          #    hedef_coord[2]=[ny2+sayi1,nx2+sayi2]
                      break
      if hedef_coord[1]==[y,x] : hedef_coord[1]=hedef_coord[2]
      #if hedef_coord[0]==[y,x] : hedef_coord[0]=hedef_coord[2]
      
      ny,nx=hedef_coord[0]
      ny2,nx2=hedef_coord[1]
      ny3,nx3=hedef_coord[2]
     
      while ( hedef_coord == [ [y,x],[y,x],[y,x] ] ):
          k=1
          islemler = [-50 , 50 , 0]
          for sayi1 in islemler:
              if y+sayi1*k<50 or y+sayi1*k>700 : continue
              for sayi2 in islemler:
                  if x+sayi2*k<50 or x+sayi2*k>700 : continue
                  if sayi1==0 and sayi2==0 : continue
                  if tuple(img[y+sayi1*k, x+sayi2*k]) == (255,255,255):continue
                  if tuple(img[y+sayi1*k, x+sayi2*k]) == (1,1,1):continue
                  for i in range(len(renkler)):
                      if tuple(img[y+sayi1*k, x+sayi2*k]) == renkler[i][0]:
                          puan=renkler[i][1]
                          if puan>hedef_puan and puan<=game_point:
                              hedef_puan=puan
                              hedef_coord[0]=[y+sayi1*k, x+sayi2*k]    
                          break
          if hedef_coord[0]!=[y,x]:
            ny , nx = hedef_coord[0]          
            ny2,nx2 = hedef_coord[0]
            ny3,nx3 = hedef_coord[0]
            break
          
          k+=1
          
        #return[ [y,nx] [ny,nx] [ny,nx2] , [ny2,nx2] ]
      return[ [y, nx] , [ny,nx] , [ny,nx2] , [ny2,nx2] , [ny2,nx3] , [ny3,nx3] ]
