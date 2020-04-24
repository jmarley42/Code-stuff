#######################################################
#
#  MoM_Helper_Methods
#
#  Helper methods for Master of Magic save editor
#
#  Author:  John Marley
#
#######################################################

from Resources.MoM_Save_Game_Stuff import *

def Calc_Addr(typ, num, offset):
    """ calculate data array index """

    if typ == "wiz":
        return Wiz_Start+Wiz_Block*num+Wiz_Offs[offset]
    elif typ == "cit":
        return City_Start+City_Block*num+City_Offs[offset]

#######################################################

def Tiles(i):
    """ method to remove animations from map-tile index """
    
    # animation locations for Arcanus
    anims_Arc = [18,34,38,42,46,50,54,58,62,66,70,74,78,82,86,90,94,98,102,106,114,209,213,217,221, 
                 225,229,233,237,241,245,249,253,257,261,265,269,279,283,287,299,591,727]

    # animation locations for Myrror
    anims_Myr = [922,926,930,934,938,942,946,950,954,958,962,966,970,974,978,982,1082,1086,1090,1094, 
                 1098,1102,1106,1110,1114,1118,1122,1126,1130,1134,1138,1142,1152,1156,1160,1172]
    
    n = i

    # n < 888 means an Arcanus tile 
    # for either plane, add 3 for each animation
    if n < 888:
        for a in anims_Arc:
            if n > a:
                n += 3
    else:
        for a in anims_Myr:
            if n > a:
                n += 3
    return n

#######################################################

def Mask(img_1, img_2):
    """ Method to superimpose image 2 on image 1 """
    
    img_1.paste(img_2,mask=img_2)

#######################################################

def Merge_Strings(*args):
    """ combine a series of strings into one """

    tmp_string = ""
    for a in args:
        tmp_string = tmp_string + a

    return tmp_string

#######################################################
