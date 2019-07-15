##master plan generator
##jarvis fosdick 10-28-05

import math, Image, ImageDraw, random, cmath, os

wi = 9000
hi = 1704
xsc = 50
ysc = 18
s_name = 'to_plan_007.tif'
cnt1 = 0

scr = Image.new('RGB',(wi,hi),(0,0,0))
base = Image.open('h:/c_bak/la446/project/landuse/figure1.tif')
bb = base.getbbox()
def image2matrix(im):
    for x in range(0,150):
        for y in range(0, 72):
            nl.add(((x,y),base.getpixel((x,y))))
    return nl
def prange(tl, br):
    pr = []
    for x in range(tl[0], br[0]):
        for y in range(tl[1], br[1]):
            pr.append([x,y])
    return pr
                           
def fill(rng, color, scr):
    for i in rng:
        scr.putpixel(color)    

def cknbr(fl, x, y):
    nl=set()
    bb = fl.getbbox()
    px = fl.getpixel((x,y))
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if bb[0] < a < bb[2] and bb[1] < b < bb[3]:
                if px == fl.getpixel((a,b)):
                    nl.add((a,b))
    return nl

def look4contig(base, x, y, do_times) :     
    flag = 1
    cnt2 = 0
    
    ss = set([])     
    while flag == 1 :  
        ss = ss|(cknbr(base, x, y))   
        if cnt2 > do_times:
            flag = 0
        if len(ss) > 1:
            for a in ss:
                #if not cknbr(base, a[0],a[1]).issubset(ss):
                ss = ss|cknbr(base, a[0],a[1])
        if cnt2 > do_times:
            flag = 0         
        cnt2 = cnt2+1
    return ss

    
                
        
    cnt1 = cnt1 + 1
def getmpt(box):
    x = int(box[0]/box[2])
    y = int(box[1]/box[3])
    return list(x,y)
    
def getrpic(type):
    pics = os.listdir('h:/c_bak/la446/project/landuse/'+type)
    lng = random.randrange(0,len(pics))
    return 'h:/c_bak/la446/project/landuse/'+type+'/'+pics[lng]

def main():
    while cnt1 < 10000 :
           
        x = random.randrange(0,bb[-2])
        y = random.randrange(0,bb[-1])
        ckpx = base.getpixel((x,y))

        if ckpx[0] < 15 and ckpx[1] < 15 and ckpx[2] < 15:
            imp = Image.open(getrpic('wall'))
            imp.copy()
            bbp = imp.getbbox()
            #bbp = list((bbp[0]*100,bbp[1]*100))
            bbpt = list((bbp[0]+x*xsc, bbp[1]+y*ysc, bbp[2]+x*xsc, bbp[3]+y*ysc))
            
            scr.paste(imp, bbpt)
            #scr.save('h:/c_bak/la446/project/landuse/'+s_name)

        if ckpx == (255,0,0):
            imp = Image.open(getrpic('person'))
            imp.copy()
            bbp = imp.getbbox()
            bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
            scr.paste(imp, bbpt)
            scr.save('h:/c_bak/la446/project/landuse/'+s_name)
        