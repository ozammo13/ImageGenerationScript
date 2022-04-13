import bpy
import random
import os
import sys
body = ['PASTEHERE','FILLTHEGAPS','','ADDMOREIFNEEDED'] #replace with exact names (copy and paste)
gills = ['','','','','',''] #feel free to rename the variables
eyes = ['', '' , '','','','']
hat = ['', '' , '','','','']
mouth = ['', '' , '','','','']
background = ['', '' , '','','','']
special = ['', '' , '','','','']
counter = 1





while counter != 61: 
    coll = bpy.context.view_layer.layer_collection
    for x in bpy.context.view_layer.layer_collection.collection.children:
            x.hide_render = True
    bn = random.randint(0, 9) #lists start at 0, so if your list has 10 items in it, you will need to change the final number to 9 (10 - 1)
    gn = random.randint(0, 5)
    en = random.randint(0, 5)
    hn = random.randint(0, 15)
    mn = random.randint(0, 5)
    bg = random.randint(0, 2)
    scn = random.randint(0,5)
    bpy.data.collections[body[bn]].hide_render = False #if you rename the variables, dont forget to change these(the body[bn] bit)
    bpy.data.collections[gills[gn]].hide_render = False
    bpy.data.collections[eyes[en]].hide_render = False
    bpy.data.collections[hat[hn]].hide_render = False
    bpy.data.collections[mouth[mn]].hide_render = False
    bpy.data.collections[background[bg]].hide_render = False
    
    specialcounter = random.randint(1,8)
    if specialcounter == 4:
        bpy.data.collections[special[scn]].hide_render = False

        

    bpy.ops.render.render(write_still=True)
    counter = counter + 1

coll = bpy.context.view_layer.layer_collection 
for x in bpy.context.view_layer.layer_collection.collection.children:
            x.hide_render = False #unhides everything from render
