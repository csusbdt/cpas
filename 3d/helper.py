import bpy
import subprocess

scene = bpy.context.scene

def setup():
	subprocess.run(["rm -f temp/*"], shell=True, check=True)

def render():
    scene.render.filepath = '//temp/'
#    data_context = { "blend_data": bpy.context.blend_data, "scene": scene }
#    bpy.ops.render.render(data_context, animation=True)
    bpy.ops.render.render(animation=True)
    cmd = """
        ffmpeg  -f image2           \
                -pattern_type glob  \
                -framerate 30       \
                -i 'temp/*.png'     \
                -s 720x480          \
                -y                  \
                -pix_fmt yuv420p    \
                anim.mp4
    """
    subprocess.run([cmd], shell=True, check=True)

