import bpy
import helper
from random import randint
import math

helper.setup()

scene = bpy.data.scenes['Scene']
bpy.ops.object.delete() 

mat = bpy.data.materials.new('mat')

class Object:
    def __init__():
        x = randint(-3, 3)
        y = randint(-3, 3)
        z = randint(-3, 3)
        location = self.location(x, y, z)
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        self.object = bpy.context.object

scene.frame_end = scene.render.fps * 1

remainingFrames = 0

def resetRemainingFrames():
    remainingFrames = math.floor(scene.render.fps * .25)

#resetRemaningFrames()

def frame_change_handler(scene):
    remainingFrames = remainingFrames - 1
    if remainingFrames <= 0:
        resetRemainingFrames()
        obj = Object()

bpy.app.handlers.frame_change_pre.append(frame_change_handler)

helper.render()

