## Course Website

Course description and instructions are in the [wiki](https://github.com/csusbdt/cpas/wiki).

## Working in a Python3 Virtual Environment

If you are working on a lab machine or any other machine for which 
you do not have administrator privileges, then you will need to
work in a Python3 virtual environment in order to install modules.
The instructions given here show how to set this up in OS X and Linux.
I'm not sure of the procedure needed under Windows.

To create and work in a Python3 virtual environment,
see [28.3. venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).
Here are my notes.

~~~
python3 -m venv env
~~~

This creates a folder named _env_ in the current directory and copies
into it the binaries and configuration files for a Python virtual environment.

To work in the environment, activate the environment as follows.

~~~
source env/bin/activate
~~~

After activation, pip will install new modules into _env_.

Also, installation such as the following will result in 
installation into the virtual environment.

~~~
git clone git@github.com:csusbdt/Python-Markdown.git
cd Python-Markdown
python setup.py install
~~~

Note that the command `python` will run Python3 after activation.

