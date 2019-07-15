scr1=Image.open('h:/c_bak/la446/project/landuse/'+s_name)
#scr1 =get_im.getdata()
cnt1 = 0
xsc = 1
ysc = 1
bb = (172,40,188,48)
while cnt1 < 20 :
    ss = set()
    x = random.randrange(bb[0],bb[-2])
    y = random.randrange(bb[1],bb[-1])
    #ckpx = scr1.getpixel((x,y))  
    ckpx = (x,y)
    if c_fuzz(scr1.getpixel(ckpx),(255,125,0),5):
        ss = find_near(scr1,ckpx,(237,27,36),5,10)
        for i in ss:
             fill_color(scale(i),(255,255,0),scr1)   

    #print "\n...Main Road to Proposed Center 001"
    if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):
        ss = find_near(scr1,ckpx,(237,27,36),5,10)
        for i in ss:
            fill_color(scale(i),(255,255,0),scr1)
            
##    #print "\n...Walking to Proposed Center 001"
    if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):

        ss=(find_near(scr1,ckpx,(109,207,246),5,10))
        for i in ss:
            fill_pattern(scr1, scale(i), 'cover')
        ss=(find_near(scr1,ckpx,(0,166,80),5,10))
        for i in ss:
             fill_pattern(scr1, scale(i), 'cover')
##    #print "\n...Walking to Residential"
    if c_fuzz(scr1.getpixel(ckpx),(0,144,54),10) or c_fuzz(scr1.getpixel(ckpx),(222,237,203),10):
        
        ss=(find_near(scr1,ckpx,(0,144,54),5,10))
        for i in ss:
             fill_color(scale(i),(0,166,80),scr1)
        ss=(find_near(scr1,ckpx,(222,237,203),5,10))
        for i in ss:
             fill_color(scale(i),(0,166,80),scr1)
##    #print "\n...Alley and Residential"
    if c_fuzz(scr1.getpixel(ckpx),(255,255,0),5):
        ss=find_near(scr1,ckpx,(255,255,0),10,10)
        if len(ss) > 60:
            for i in ss:
             fill_pattern(scr1, scale(i), 'plaza')
##    #print "\n...Large Walking Areas to Plaza"
    if c_fuzz(scr1.getpixel(ckpx),(0,166,80),10) or c_fuzz(scr1.getpixel(ckpx),(109,207,246),10):
        
        ss = (find_near(scr1,ckpx,(168,99,168),5,10))
        for i in ss:
             fill_color(scale(i),(255,255,0),scr1)
        ss = (find_near(scr1,ckpx,(145,61,105),5,10))
        for i in ss:
             fill_color(scale(i),(255,255,0),scr1)
##    #print "\n...Residential Next to Idustirial"
    if c_fuzz(scr1.getpixel(ckpx),(255,125,0),10):
        ss = (find_near(scr1,ckpx,(109,207,246),5,10))
        for i in ss:
             fill_pattern(scr1, scale(i), 'commer')
        ss = (find_near(scr1,ckpx,(0,166,80),5,10))
        for i in ss:
             fill_pattern(scr1, scale(i), 'commer')
##    #print "\n...Retail and Commerce by Main Roads"

    cnt1 = cnt1+1

scr1.save('h:/c_bak/la446/project/landuse/'+'to_'+s_name)