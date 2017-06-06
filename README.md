[![Binder](http://mybinder.org/badge.svg)](http://beta.mybinder.org/v2/gh/reubano/lambdaconf-tutorial/master)

# lambdaconf-tutorial

Materials for the LambdaConf tutorial, "A Functional Programming approach to data  processing in Python".
Presentation slides can be found at https://speakerdeck.com/reubano/a-functional-programming-approach-to-data-processing-in-python

## Preparation

This is an interactive (hands-on) tutorial. As such, you can choose to follow along [locally](#local) on your laptop, or [remotely](#remote) in a [binder notebook](http://beta.mybinder.org/v2/gh/reubano/lambdaconf-tutorial/master).

### Local

Clone this repo

```bash
git clone https://github.com/reubano/lambdaconf-tutorial.git
cd lambdaconf-tutorial
```

Make sure you have a recent version of [Python 3 and pip 3](http://docs.python-guide.org/en/latest/starting/installation/)

```bash
# follow directions for your platform from the above link above

python3 --version
# Python 3.6.1

pip3 install --upgrade pip
pip3 --version
# pip 9.0.1 from ...
```

(Optional) Setup and activate a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)

```bash
pip3 install virtualenv
virtualenv lambdaconf-tutorial
source lambdaconf-tutorial/bin/activate
```

(Optional) install [iPython](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#the-four-most-helpful-commands), an enhanced Python shell

```bash
# if you are working in a virtualenv
pip install ipython

# if you are *not* in a virtualenv
pip3 install --user ipython
```

Install the packages to be used during the workshop

```bash
# if you are working in a virtualenv
pip install riko==0.51.0

# if you are *not* in a virtualenv
pip3 install --user riko==0.51.0
```

Start the interactive Python

```bash
# if you installed iPython
ipython

# if you did *not* install iPython
python3
```

You should now be in an interactive shell that looks something like this:

```
Python 3.6.1 (default, May 24 2017, 01:02:17)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

In this interactive shell, you can enter any valid Python and immediately see the result.

```
>>> 1 + 3
4
>>> x = 1 + 3
>>> x
4
```

To play around with the code, view the following files in your text editor of your choice.

- [Presentation](https://github.com/reubano/lambdaconf-tutorial/blob/master/presentation.py): use to follow along as I talk, and reference during the exercises
- [Exercises](https://github.com/reubano/lambdaconf-tutorial/blob/master/exercises.py): test your own code by typing `python3 exercises.py` in the terminal (*NOT* a python shell)
- [Solutions](https://github.com/reubano/lambdaconf-tutorial/blob/master/solutions.py): see how the solution should look by typing `python3 solutions.py` in the terminal (*NOT* a python shell)

### Remote

To play around with the code, [visit mybinder](http://beta.mybinder.org/v2/gh/reubano/lambdaconf-tutorial/master) and select the appropriate notebook.

- Presentation (`presentation.ipynb`): use to follow along as I talk, and reference during the exercises
- Exercises (`exercises.ipynb`): test your own code by typing directly into your browser
- Solutions (`solution.ipynb`): interact with the solution and view the intermediate results

## A few tips

- if you are new to Python, browse through the [Python tutorial](https://docs.python.org/3.6/tutorial/index.html)
- if you are new to meza, checkout the [meza readme](https://github.com/reubano/meza/blob/master/README.rst#hello-world)
