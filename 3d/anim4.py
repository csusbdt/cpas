import bpy
import helper

helper.setup()

cube = bpy.data.objects['Cube']
scene = bpy.data.scenes['Scene']

cube.location.x = -3
scene.frame_end = scene.render.fps * 1

def frame_change_handler(scene):
    cube.location.x = cube.location.x + 2 / scene.render.fps

bpy.app.handlers.frame_change_pre.append(frame_change_handler)

helper.render()

