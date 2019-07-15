## find lines
##jarvis fosdick, october 25, 2005

import math, Image, ImageDraw, random, cmath, os
wi = 100
hi = 100
xsc = 50
ysc = 18
s_name = 'line_002.tif'
cnt1 = 0

scr = Image.new('RGB',(wi,hi),(0,0,0))
base = Image.open('h:/c_bak/la446/project/landuse/line1.tif')
bb = base.getbbox()

def getmpt(box):
    x = int(box[0]/box[2])
    y = int(box[1]/box[3])
    return list(x,y)
    
def getrpic(type):
    pics = os.listdir('h:/c_bak/la446/project/landuse/'+type)
    lng = random.randrange(0,len(pics))
    return 'h:/c_bak/la446/project/landuse/'+type+'/'+pics[lng]

def cknbr(xy, fl):
    nl=[]
    for x in range(xy[0]-1, xy[0]+2):
        for y in range(xy[1]-1, xy[1]+2):
            if fl.getpixel(xy) == fl.getpixel((x,y)):
                nl.append([x,y])
    return nl

while cnt1 < 1 :

        
    #x = random.randrange(0,bb[-2])
    #y = random.randrange(0,bb[-1])
    x = 12
    y = 40
    ckpx = base.getpixel((x,y))

    #if ckpx[0] < 33 and ckpx[1] < 33 and ckpx[2] < 33:
    if ckpx[0]==ckpx[1]==ckpx[2]:
        #imp = Image.open(getrpic('wall'))
        #imp.copy()
        #bbp = imp.getbbox()
        #bbpt = list((bbp[0]+x*xsc, bbp[1]+y*ysc, bbp[2]+x*xsc, bbp[3]+y*ysc))
        flag = 1
        nblist = cknbr((x,y), base)
        orxy = [x,y]
        cnt2 = 0
    while flag == 1:
            for p in nblist:
                scr.putpixel(p,(0,255,0))
                flag = 0
                
                if cnt2 > 2000:
                    nblist=()
                    
                if len(nblist) > 1:
                    cknbr01 = cknbr((p[0],p[1]), base)
                    for np in cknbr01:
                        scr.putpixel(np,(0,255,0))
                        if len(cknbr01) > 1:
                            nblist = cknbr01
                            flag = 1
                        else: flag = 0
                else: flag = 0
            if cnt2 > 2000:
                nblist=()
            cnt2 = cnt2+1
    
                
        
    cnt1 = cnt1 + 1
   
scr.save('h:/c_bak/la446/project/landuse/'+s_name)        