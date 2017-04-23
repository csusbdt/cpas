import bpy
import helper

helper.setup()

# Create scene.
cube = bpy.data.objects['Cube']

# Make the animation 3 seconds.
scene = bpy.context.scene
scene.render.fps = 30
scene.frame_start = 1
scene.frame_end = 90

# Create first key frame.
cube.location = [-3, 0, 0]
cube.keyframe_insert(data_path="location", frame=1)
cube.location = [3, 0, 0]
cube.keyframe_insert(data_path="location", frame=90)

#bpy.ops.anim.keyframe_insert_menu(type='Rotation')

helper.render()

