import subprocess

#subprocess.run(["rm -f temp/*"], shell=True, check=True)

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

