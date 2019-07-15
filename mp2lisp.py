##convert image to AutoLisp Script
##to generate master plan, Nov 01, 2005
##jarvis fosdick

import math, Image, ImageDraw, random, cmath, os
##internal functions
def color2use(color):
        while True:
            if color == (252,198,137) or color == (255,247,153):
                return 'cover'
            elif color == (198,156,109) or color == (255,125,125):
                return 'plaza'
            elif color == (196,181,255) or color == (109,207,246):
                return 'Commmer'
            elif color == (255,125,0):
                return 'mroads'
            elif color == (168,99,168) or color == (145,61,105):
                return 'Idust'
            elif color == (109,207,246):
                return 'Retail'
            elif color == (0, 166,80):
                return 'Res'
            elif color == (0,114,54) or color == (222,237,203):
                return 'alley'
            elif color == (237,27,35):
                return 'Center'
            elif color == (0,0,255):
                return 'edge'
            elif color == (255,255,0):
                return 'ped'
            elif 0==0:
                return 'False'
            
##open .lsp file
mp_name = 'mp001.lsp'
f = file('h:/c_bak/la446/project/landuse/'+mp_name, 'w')

##get image and make into ss
im = Image.open('h:/c_bak/la446/project/landuse/to_plan_004.tif')
bb = im.getbbox()
#bb = (0,0,20,20)
ss = set()
for x in range(bb[0],bb[2]):
        for y in range(bb[1],bb[3]):
                ss.add((x,y))
##get pixel and find contig return contig_ss

while len(ss) > 0:
        px = ss.pop()
        
        
        if color2use(im.getpixel(px)) != 'False':
                px_ss = look4contig(im,px[0],px[1])
##create layer for contig pixels named Use_No

                la = color2use(im.getpixel(px))
                f.writelines('\n(command "layer" "m" "'+la+'" "" )')
                for  i in px_ss:
##insert each block
                        blk = la
                        f.writelines('\n(command "insert" "'+blk+'" \'('+str(i[0])+' '+str(-1*i[1])+') 1 1 0 )')
        ss = ss - px_ss
##subtract contig_ss from ss

##repeat until ss = 0
f.close()