See the [wiki](https://github.com/csusbdt/cpas/wiki).

To create and work in Python3 virtual environment,
see [28.3. venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).
Here are my notes.

~~~
cd ~/cpas
python3 -m venv myenv
~~~

This created a folder named _myenv_ in the current directory,
which contains the binaries and configuration for a Python virtual environment.

To install modules into _myenv_, activite the envoronment and then use pip.

~~~
source myenv/bin/activate
pip install Django==1.7
~~~

