import colorgram
colors=colorgram.extract('hafi.jpg',30)
rgb_colors=[]
for colour in colors:
    r=colour.rgb.r
    g=colour.rgb.g
    b=colour.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)