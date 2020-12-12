
# -*- coding: UTF-8 -*-
#Created by xclowns

import os,sys,time

 # JANGAN DISALAHGUNAKAN #

def main():
    time.sleep(1)
    os.system ('clear')
    print ''
    os.system ('figlet Tools')
    print'================================='
    print' Author : xclowns'
    print' Team   : aing solo gan:)'
    print'================================='
    print'++++++++++++ M E N U ++++++++++++'
    print'[1] Dark Fb v1.7 '
    print'[2] Dark Fb v1.8 '
    print'[3] Dark Fb Premium '
    print'[4] Dark Fb New'
    print'[5] Dark Fb Diamond '
    print'[0] Exit '
    gans = raw_input ('==> ')
    if gans in ['1']:
        time.sleep(1)
        os.system ('git clone https://github.com/Mr-XsZ/Dark-Fb')
        print ('$ lanjut ketikan cd Dark-Fb')
        print ('$ lalu python2 dark.py')
        exit()
    if gans in ['2']:
        time.sleep(1)
        os.system ('git clone https://github.com/wira2611/Pro2611')
        print ('$ lanjut ketikan cd Pro2611')
        print ('$ lalu python2 Pro.py')
        exit()
    if gans in ['3']:
        time.sleep(1)
        os.system ('git clone https://github.com/TheMagizz/DarkPremium')
        print ('$lanjut ketikan cd DarkPremium')
        print ('$ lalu python2 DarkFB.py')
        exit()
    if gans in ['4']:
        time.sleep(1)
        os.system ('git clone https://github.com/KingMrZ17/DarkFbNew')
        print ('$ lanjut ketikan cd DarkFbNew')
        print ('$ lalu python2 darkfb.py')
        print (' + Username INDONESIA')
        print (' + Password MAJU')
        exit()
    if gans in ['5']:
        time.sleep(1)
        os.system('git clone https://github.com/wira2611/diamon')
        print ('$ lanjut ketikan cd diamon')
        print ('$ lalu  python2 diamond-1.py')
        exit()
    if gans in ['0']:
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        print ' Pilih Yang Bener cok . . .'
        time.sleep(1)
        main()

main()

        
