import bpy
import helper

helper.setup()

cube = bpy.data.objects['Cube']
cube.location.x = -3

scene = bpy.data.scenes['Scene']

# Make the animation 3 seconds in duration.
scene.frame_end = scene.render.fps * 3

def my_handler(scene):
    # Move cube one unit in the positive X direction per second.
    cube.location.x = cube.location.x + 1 / scene.render.fps

bpy.app.handlers.frame_change_pre.append(my_handler)

helper.render()

