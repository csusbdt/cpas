import bpy
import helper
from random import randint
import math

helper.setup()

scene = bpy.data.scenes['Scene']
bpy.ops.object.delete() 

camera = bpy.data.objects['Camera']
camera.location = 4 * camera.location

bpy.ops.object.lamp_add(
    type='SUN', 
    radius=1, 
    location=(-3, 4, 5)
)

mat = bpy.data.materials.new('mat')

class Object:
    def __init__(self):
        max = 10
        x = randint(-max, max)
        y = randint(-max, max)
        z = randint(-max, max)
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        self.object = bpy.context.object

duration = 30
scene.frame_end = scene.render.fps * duration

remainingFrames = 0

def resetRemainingFrames():
    global remainingFrames
    remainingFrames = math.floor(scene.render.fps * .55)

resetRemainingFrames()

def frame_change_handler(scene):
    global remainingFrames
    remainingFrames = remainingFrames - 1
    if remainingFrames <= 0:
        resetRemainingFrames()
        obj = Object()

bpy.app.handlers.frame_change_pre.append(frame_change_handler)

helper.render()

