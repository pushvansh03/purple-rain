rain_color = (138, 43, 226)
bg_color = (230, 230, 250)
width = 640
height = 360

def change_color() :
    global rain_color, bg_color
    rain_color, bg_color = bg_color, rain_color

def get_raincolor() :
    global rain_color
    return rain_color

def get_bgcolor() :
    global bg_color
    return bg_color
