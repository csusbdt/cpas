import bpy
import subprocess

cube = bpy.data.objects['Cube']
cube.location.x = -3

scene = bpy.data.scenes['Scene']

# Make the animation 3 seconds in duration.
scene.frame_end = scene.render.fps * 3

scene.render.filepath = '//temp/'

data_context = {"blend_data": bpy.context.blend_data, "scene": scene}

def my_handler(scene):
    # Move cube one unit in the positive X direction per second.
    cube.location.x = cube.location.x + 1 / scene.render.fps

bpy.app.handlers.frame_change_pre.append(my_handler)

bpy.ops.render.render(data_context, animation=True)

subprocess.run(["""
ffmpeg  -f image2           \
        -pattern_type glob  \
        -framerate 30       \
        -i 'temp/*.png'     \
        -s 720x480          \
        -y                  \
        -pix_fmt yuv420p    \
        anim3.mp4
"""], shell=True, check=True)

