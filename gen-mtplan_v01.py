##master plan generator
##jarvis fosdick 10-28-05

import math, Image, ImageDraw, random, cmath, os

wi = 320
hi = 108
xsc = 1
ysc = 1
s_name = 'to_plan_004.tif'


scr = Image.new('RGB',(wi,hi),(0,0,0))
base = Image.open('h:/c_bak/la446/project/landuse/__site-area.tif')
ebldgs = Image.open('h:/c_bak/la446/project/landuse/__site-e-bldg.tif')
eroads = Image.open('h:/c_bak/la446/project/landuse/__site-e-roads.tif')
rden = Image.open('h:/c_bak/la446/project/landuse/__site-roads-enhance1.tif')
use = Image.open('h:/c_bak/la446/project/landuse/__site-use-pro.tif')
c001 = Image.open('h:/c_bak/la446/project/landuse/__site-pro-center001.tif')
c002 = Image.open('h:/c_bak/la446/project/landuse/__site-pro-center002.tif')
sedge = Image.open('h:/c_bak/la446/project/landuse/__site-edge.tif')
bb = (0,0,99,32)
def area_cnt(im, pat):
    cnt = 0
    for i in im.getdata():
        if i == pat:
            cnt = cnt+1
    return cnt
        
def image2matrix(im):
    bb = im.getbbox()
    nl=set()
    for x in range(bb[0],bb[2]):
        for y in range(bb[1],bb[3]):
            nl.add([(x,y) + base.getpixel((x,y))])
    return nl
def fill_order(bb):
    #bb = im.getbbox()
    p1 = getmpt(bb)
    pat_list = [p1]
    loop_cnt = 1
    cnt = 0
    pcnt = 0
    while cnt < (bb[2]*bb[3])/4:
        if bb[2] > (p1[0]+(cnt+int((math.cos(pcnt*math.pi))))) and bb[3] > (p1[1]+(cnt+(int(math.sin(pcnt*math.pi))))):
            pat_list.append([(p1[0]+(cnt*int((math.cos(pcnt*math.pi))))),(p1[1]+(cnt*int((math.sin(pcnt*math.pi)))))])
        loop_cnt=loop_cnt+1
        pcnt = pcnt + 0.5
        if loop_cnt==4:
            loop_cnt=0
            cnt = cnt+1
    return pat_list
        
def scale(pt):
    sc_ss = set()
    for a in range((pt[0]*xsc),((pt[0]+1)*(xsc))):
        for b in range((pt[1]*ysc),((pt[1]+1)*(ysc))):
            sc_ss.add((a,b))
    return sc_ss
    
def prange(tl, br):
    pr = []
    for x in range(tl[0], br[0]):
        for y in range(tl[1], br[1]):
            pr.append([x,y])
    return pr
                           
def fill_color(ss, color, scr):
    for i in ss:
        scr.putpixel(i, color)
def fill_pattern(im, ss, pattern):
    #s = list(ss)
    #s.sort
    #ss = set(s)
    imp = Image.open(getrpic(pattern))
    idata = imp.getdata()
    #p_fill = fill_order((pt[0],pt[1],(im.getbbox()[2]+pt[0]),(im.getbbox()[3]+pt[1])))
    cnt = 0
    for i in ss:
        im.putpixel(i,idata[cnt])
        if cnt == len(idata):
            cnt = 0
        else:
            cnt = cnt+1
    
    return im
    
##    for i in ss:
##        for e in prange(i,((i[0]*xsc),(i[1]*ysc))):
##            scr.putpixel((i[0]+e[0],i[1]+e[1]), imp.getpixel(e))
    

def cknbr(base, color, x, y):
    nl=set()
    bb = base.getbbox()
    #px = fl.getpixel((x,y))
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if bb[0] < a < bb[2] and bb[1] < b < bb[3]:
                if color == base.getpixel((a,b)):
                    nl.add((a,b))
    return nl
def no_nbr(base, color, x, y):
    nl=set()
    bb = base.getbbox()
    #px = fl.getpixel((x,y))
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if bb[0] < a < bb[2] and bb[1] < b < bb[3]:
                if color != base.getpixel((a,b)):
                    nl.add((a,b))
    return nl

def look4contig(base, x, y) :     
    flag = 1
    cnt2 = 0
    color = base.getpixel((x,y))
    ss = set([])     
    while True :
        intss = ss
        ss = ss|(cknbr(base, color, x, y))   
        if len(ss) > 1:
            for a in ss:
                ss = ss|cknbr(base, color, a[0],a[1])
        if intss >= ss:
            return ss
    return ss

    
                
        
    cnt1 = cnt1 + 1
def getmpt(box):
    x = int((box[2]+box[0])/2.0)
    y = int((box[3]+box[1])/2.0)
    return x,y
    
def getrpic(type):
    pics = os.listdir('h:/c_bak/la446/project/landuse/'+type)
    lng = random.randrange(0,len(pics))
    return 'h:/c_bak/la446/project/landuse/'+type+'/'+pics[lng]
def putrpx(im, ss, color, pc):
    pr_cnt = int(len(ss)*pc)
    while pr_cnt > 1:
        i = random.randrange(0,len(ss))
        im.putpixel(ss[i],color)
        pr_cnt = pr_cnt-1
    return im
def  not_white(im):
    bb = im.getbbox()
    ss = set()
    for a in range(0,bb[2]):
        for b in range(0, bb[3]):
            if im.getpixel((a,b)) != (255,255,255):
                ss.add((a,b))
    return ss
            
def c_fuzz(ck_color,color,fuzz):
    ss = set()
    ck=set()
    ck.add(ck_color)
    for a in range((color[0]-fuzz),(color[0]+fuzz)):
        for b in range((color[1]-fuzz),(color[1]+fuzz)):
            for c in range((color[2]-fuzz),(color[2]+fuzz)):
                ss.add((a,b,c))
                
    if ck.issubset(ss):
        return True
    else:
        return False
def find_near(img,ck_pt,color,rng,fz):
    ss = set()
    px_ss = set()
    bb = img.getbbox()
    for a in range((ck_pt[0]-rng),(ck_pt[0]+rng)):
        for b in range((ck_pt[1]-rng),(ck_pt[1]+rng)):
            ss.add((a,b))
    for i in ss:
        if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
            if c_fuzz(img.getpixel(i),color,fz):
                px_ss.add(i)

    return px_ss
def main():
    print "\n...Generating, please wait:"
    cnt1 = 0
    for i in not_white(sedge):
        fill_color(scale(i),(0,0,255),scr)
    
    print "\n...Site Border Edges"
    for i in not_white(eroads):
        fill_color(scale(i),(255,255,0),scr)
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...pedestrian spaces"
    for i in not_white(ebldgs):
        im = fill_pattern(scr,scale(i),'mixed')
        im.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...mixed use areas"
 
    while cnt1 < 500 :
           
        x = random.randrange(bb[0],bb[-2])
        y = random.randrange(bb[1],bb[-1])
        ckpx = use.getpixel((x,y))
        if ckpx == (168,99,168):
            ss = look4contig(use, x, y)
            for i in ss:
                fill_pattern(scr, scale(i), 'idust')
        if c_fuzz(ckpx,(0,114,54),(12)):
            ss = look4contig(use, x, y)
            for i in ss:
                fill_pattern(scr, scale(i), 'alley')
        
        cnt1 = cnt1+1
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...industrial spaces"
    print "\n...alley edges"
    for i in not_white(c001):
        fill_color(scale(i),(237,27,35),scr)
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...proposed centers 001"
    for i in not_white(c002):
        fill_color(scale(i),(237,27,35),scr)
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...proposed centers 002"
    cnt1 = 0
    for i in not_white(rden):
        fill_color(scale(i),rden.getpixel(i),scr)
    print "\n...main roads"
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\ndefining the Edges..."
    scr.save('h:/c_bak/la446/project/landuse/'+s_name)
    print "\n...Interpretating Edge Relationshiops"

scr1=Image.open('h:/c_bak/la446/project/landuse/to_04_to_plan_004.tif')
def edge():
    wi = 1000
    hi = 350
    scr2 = Image.new('RGB',(wi,hi),(0,0,0))
#    scr1=Image.open('h:/c_bak/la446/project/landuse/to_01_to_plan_004.tif')
    cnt1 = 0
    cnt_100_ = 0

    bb = (0,0,999,349)
    for i in prange((scr1.getbbox()[0],scr1.getbbox()[1]),(scr1.getbbox()[2],scr1.getbbox()[3])):
        fill_color(scale(i),scr1.getpixel((i[0],i[1])),scr2)

    while cnt1 < 2000 :
        ss = set()
        x = random.randrange(bb[0],bb[-2])
        y = random.randrange(bb[1],bb[-1])
        #ckpx = scr1.getpixel((x,y))  
        ckpx = (x,y)
        if c_fuzz(scr1.getpixel(ckpx),(255,125,0),5):
            ss = find_near(scr1,ckpx,(237,27,36),5,10)
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(255,255,0),scr2)   

        #print "\n...Main Road to Proposed Center 001: add walking"
        if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):
            ss = find_near(scr1,ckpx,(237,27,36),5,10)
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(255,255,0),scr2)
                
    ##    #print "\n...Walking near Proposed Center 001 to walking"
        if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):

            ss=(find_near(scr1,ckpx,(109,207,246),2,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_pattern(scr2, scale(i), 'cover')
            ss=(find_near(scr1,ckpx,(0,166,80),7,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_pattern(scr2, scale(i), 'res')
    ##    #print "\n...Walking near Mixed to Cover and Residential"
        if c_fuzz(scr1.getpixel(ckpx),(0,144,54),10) or c_fuzz(scr1.getpixel(ckpx),(222,237,203),10):
            
            ss=(find_near(scr1,ckpx,(0,144,54),5,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(0,166,80),scr2)
            ss=(find_near(scr1,ckpx,(222,237,203),5,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(0,166,80),scr2)
    ##    #print "\n...Combine Alley and Residential"
        if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):
            ss=find_near(scr1,ckpx,(255,255,0),10,10)
            if len(ss) > 110:
                for i in ss:
                    if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                         fill_pattern(scr2, scale(i), 'plaza')
    ##    #print "\n...Large Walking Areas to Plaza"
        if c_fuzz(scr1.getpixel(ckpx),(0,166,80),10) or c_fuzz(scr1.getpixel(ckpx),(109,207,246),10):
            
            ss = (find_near(scr1,ckpx,(168,99,168),5,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(255,255,0),scr2)
            ss = (find_near(scr1,ckpx,(145,61,105),5,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_color(scale(i),(255,255,0),scr2)
    ##    #print "\n...Residential Next to Idustirial add yellow"
        if c_fuzz(scr1.getpixel(ckpx),(255,125,0),10):
            ss = (find_near(scr1,ckpx,(109,207,246),6,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_pattern(scr2, scale(i), 'commer')
            ss = (find_near(scr1,ckpx,(0,166,80),5,10))
            for i in ss:
                if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                    fill_pattern(scr2, scale(i), 'commer')
    ##    #print "\n...Retail and Commerce by Main Roads"
        if c_fuzz(scr1.getpixel(ckpx),(0,166,80),10):
            
            ss = (find_near(scr1,ckpx,(0,166,80),8,10))
            if len(ss) > 200:
                for i in ss:
                    if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                        fill_pattern(scr2, scale(i), 'mixed')

    ##    #print "\n...To consentrated RES : Mix!"
        if c_fuzz(scr1.getpixel(ckpx),(109,207,246),10):
            
            ss = (find_near(scr1,ckpx,(109,207,246),8,10))
            if len(ss) > 200:
                for i in ss:
                    if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]:
                        fill_pattern(scr2, scale(i), 'mixed')

    ##    #print "\n...To consentrated Bussiness : Mix!"
        if c_fuzz(scr1.getpixel(ckpx),(0,166,80),10):
            
            ss = (find_near(scr1,ckpx,(0,166,80),3,10))
            if len(ss) < 20:
                for a in ss:
                    for i in prange(((a[0]-2),(a[1]-2)),((a[0]+2),(a[1]+2))):
                        if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3]and scr1.getpixel((i[0],i[1])) != (255,125,0):
                            fill_pattern(scr2, scale(i), 'res')

    ##    #print "\n...To isolated RES : More RES!"
        if c_fuzz(scr1.getpixel(ckpx),(255,255,0),10):
            
            ss = (find_near(scr1,ckpx,(255,255,0),6,10))
            if len(ss) < 112:
                for a in ss:
                    for i in prange(((a[0]-4),(a[1]-4)),((a[0]+4),(a[1]+4))):
                        if bb[0] < i[0] < bb[2] and  bb[1] < i[1] < bb[3] and scr1.getpixel((i[0],i[1])) != (255,125,0):
                            fill_color(scale(i),(255,255,0),scr2)

    ##    #print "\n...To Short a Walk : More walking!"
                    

        cnt1 = cnt1+1

            

    scr2.save('h:/c_bak/la446/project/landuse/'+'to_05_'+s_name)
