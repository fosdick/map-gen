## generate land use matrix
##jarvis fosdick, october 25, 2005

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

def getmpt(box):
    x = int(box[0]/box[2])
    y = int(box[1]/box[3])
    return list(x,y)
    
def getrpic(type):
    pics = os.listdir('h:/c_bak/la446/project/landuse/'+type)
    lng = random.randrange(0,len(pics))
    return 'h:/c_bak/la446/project/landuse/'+type+'/'+pics[lng]

def cknbr(xy, file):
    for x in range(xy[0]-1, xy[0]+1):
        for y in range(xy[1]+1, xy[1]-1):
            if list((x,y)) == xy:
                nl.append([x,y])
    return nl
    
    

while cnt1 < 10000 :
#for x in range(bb[2]):
    #for y in range (bb[3]):
        
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

##    if ckpx == (255,0,1):
##        imp = Image.open(getrpic('person'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)

##    if ckpx == (0,255,1):
##        imp = Image.open(getrpic('bike'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)

    if ckpx == (0,0,255):
        imp = Image.open(getrpic('streets'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x*xsc, bbp[1]+y*ysc, bbp[2]+x*xsc, bbp[3]+y*ysc))
        scr.paste(imp, bbpt)
        #scr.save('h:/c_bak/la446/project/landuse/'+s_name)

##    if ckpx == (0,255,255):
##        imp = Image.open(getrpic('gateways'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##
##    if ckpx == (255,255,1):
##        imp = Image.open(getrpic('fens'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)          
##
##    if ckpx == (255,0,255):
##        imp = Image.open(getrpic('overpass'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)

##    if ckpx == (255,125,0):
##        imp = Image.open(getrpic('garden'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (255,125,125):
##        imp = Image.open(getrpic('pocket'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (255,153,0):
##        imp = Image.open(getrpic('plaza'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (0,88,37):
##        imp = Image.open(getrpic('main'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (121,0,0):
##        imp = Image.open(getrpic('roofg'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (0,174,239):
##        imp = Image.open(getrpic('court'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x*10, bbp[1]+y*10, bbp[2]+x*10, bbp[3]+y*10))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (0,169,157):
##        imp = Image.open(getrpic('res'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (74,0,72):
##        imp = Image.open(getrpic('mix'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)
##
##    if ckpx == (198,156,109):
##        imp = Image.open(getrpic('center'))
##        imp.copy()
##        bbp = imp.getbbox()
##        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
##        scr.paste(imp, bbpt)
##        scr.save('h:/c_bak/la446/project/landuse/'+s_name)

    cnt1 = cnt1 + 1
    
scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    
    
    