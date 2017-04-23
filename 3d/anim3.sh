rm -f anim4.mp4
rm -f temp/*.png 

/Applications/blender.app/Contents/MacOS/blender -b --python-exit-code 1 -P anim3.py

if NOT $?; then exit 1; fi

open anim3.mp4

