import bpy

# Get a reference to the cube.
cube = bpy.data.objects['Cube']

# Move the cube 3 units in the positve X direction.
cube.location.x = -2

# Render an image from the scene camera.

# Set the output file pathname.
bpy.data.scenes['Scene'].render.filepath = './cube.png'

# Output the image.
bpy.ops.render.render(write_still=True)

