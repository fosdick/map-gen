## generate sections
##jarvis fosdick, october 25, 2005

import math, Image, ImageDraw, random, cmath, os
wi = 9000
hi = 1704
s_name = 'sec_from_plan_003.tif'
cnt1 = 0

scr = Image.new('RGB',(wi,hi),(0,0,0))
base = Image.open('h:/c_bak/la446/project/sections/base2.tif')
bb = base.getbbox()

def getmpt(box):
    x = int(box[0]/box[2])
    y = int(box[1]/box[3])
    return list(x,y)
    

def getrpic(type):
    pics = os.listdir('h:/c_bak/la446/project/sections/'+type)
    lng = random.randrange(0,len(pics))
    return 'h:/c_bak/la446/project/sections/'+type+'/'+pics[lng]
    
    

while cnt1 < 2500:
    x = random.randrange(0,bb[-2])
    y = random.randrange(0,bb[-1])
    ckpx = base.getpixel((x,y))

    if ckpx == (255,0,0):
        imp = Image.open(getrpic('bike'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,255,0):
        imp = Image.open(getrpic('corridor'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,0,255):
        imp = Image.open(getrpic('market'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,255,255):
        imp = Image.open(getrpic('gateways'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)


    if ckpx == (255,255,0):
        imp = Image.open(getrpic('ugPark'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)          

    if ckpx == (255,0,255):
        imp = Image.open(getrpic('overpass'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (255,125,0):
        imp = Image.open(getrpic('garden'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (255,125,125):
        imp = Image.open(getrpic('pocket'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (255,153,0):
        imp = Image.open(getrpic('plaza'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,88,37):
        imp = Image.open(getrpic('main'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (121,0,0):
        imp = Image.open(getrpic('roofg'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,174,239):
        imp = Image.open(getrpic('court'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (0,169,157):
        imp = Image.open(getrpic('res'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (74,0,72):
        imp = Image.open(getrpic('mix'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)

    if ckpx == (198,156,109):
        imp = Image.open(getrpic('center'))
        imp.copy()
        bbp = imp.getbbox()
        bbpt = list((bbp[0]+x, bbp[1]+y, bbp[2]+x, bbp[3]+y))
        scr.paste(imp, bbpt)
        scr.save('h:/c_bak/la446/project/sections/'+s_name)
    cnt1 = cnt1 + 1        
        
        
        