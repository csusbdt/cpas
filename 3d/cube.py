import bpy
cube = bpy.data.objects['Cube']
cube.location.x = 3

import code
namespace = globals().copy()
namespace.update(locals())

# let use enter Python commands; enter Ctrl-D to terminate.
code.interact(local=namespace)  

bpy.data.scenes['Scene'].render.filepath = 'cube.png'
bpy.ops.render.render(write_still=True)

