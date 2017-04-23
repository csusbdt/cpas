rm -f anim.mp4
rm -f temp/*.png 

export PYTHONPATH=.:$PYTHONPATH

/Applications/blender.app/Contents/MacOS/blender -b --python-exit-code 1 -P anim4.py

if [ $? -eq "0" ]; then 
    open anim.mp4
else
    exit 1; fi
fi

