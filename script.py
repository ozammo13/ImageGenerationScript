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

        
       
    #writefiles
    
    save_path = r"FILEPATH" #change file paths
    file_name = str(counter)+'.json'
    completeName = os.path.join(save_path, file_name)
    
    file1 = open(completeName, "x")
    file1.write("{\n")
    file1.write("  \"name\": \"Axo #1\",\n")
    file1.write("  \"description\": \"Axolotl Investors\",\n")
    file1.write("  \"edition\": 1,\n")
    file1.write("  \"attributes\": [\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Background\",\n")
    file1.write("     \"value\": \""+background[bg]+"\"\n")
    file1.write("    },\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Body\",\n")
    file1.write("     \"value\": \""+body[bn]+"\"\n")
    file1.write("    },\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Gills\",\n")
    file1.write("     \"value\": \""+gills[gn]+"\"\n")
    file1.write("    },\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Eyes\",\n")
    file1.write("     \"value\": \""+eyes[en]+"\"\n")
    file1.write("    },\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Mouth\",\n")
    file1.write("     \"value\": \""+mouth[mn]+"\"\n")
    file1.write("    },\n")
    
    
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Hat\",\n")
    file1.write("     \"value\": \""+hat[hn]+"\"\n")
    file1.write("    },\n")
    
    file1.write("    {\n")
    file1.write("     \"trait_type\": \"Special\",\n")    
    file1.write("     \"value\": \""+special[scn]+"\"\n")
    file1.write("    }\n")
    file1.write("   ],\n")
    file1.write("   \"compiler\": \"HashLips Art Engine\"\n")
    file1.write("}\n")
    file1.close()

            

             
             
            
            
    
    
    
    filepath = '\\'+str(counter) #leave this, if you want it to have a name and a number, add it next to the //( eg. \\Axolotl #)
    bpy.context.scene.render.filepath = r"FILEPATH" + filepath #change file paths
    bpy.ops.render.render(write_still=True)
    counter = counter + 1

coll = bpy.context.view_layer.layer_collection 
for x in bpy.context.view_layer.layer_collection.collection.children:
            x.hide_render = False #unhides everything from render
