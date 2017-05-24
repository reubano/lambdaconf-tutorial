[![Binder](http://mybinder.org/badge.svg)](http://beta.mybinder.org:/repo/reubano/lambdaconf-tutorial)

# lambdaconf-tutorial

Materials for the LambdaConf tutorial, "A Functional Programming approach to data  processing in Python".

## Preparation

This is an interactive (hands-on) tutorial. As such, you can choose to follow along [locally](#local) on your laptop, or [remotely](#remote) in a [binder notebook](http://beta.mybinder.org:/repo/reubano/lambdaconf-tutorial).

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

pip3 --version
# pip 9.0.1 from ...
```

*(Optional)* Setup and activate a [virtual environment](http://docs.python-guide.org/en/latest/dev/        virtualenvs/#virtualenvironments-ref)

```bash
pip3 install virtualenv
virtualenv lambdaconf-tutorial
source lambdaconf-tutorial/bin/activate
```

*(Optional)* install [jyupter](http://docs.python-guide.org/en/latest/dev/        virtualenvs/#virtualenvironments-ref)

Install the packages to be used during the workshop


```bash
# if you are working in a virtualenv 
pip install riko==0.51.0    

# if you are *not* in a virtualenv 
pip3 install --user riko==0.51.0

```

Start the interactive Python 

Play around with the code

- [Presentation](raw???presentation)
- [Exercises](raw???exercises)
- [Solutions](raw???solutions)

### Remote

Play around with the code

- [Presentation](http://beta.mybinder.org:/repo/reubano/lambdaconf-tutorial)
- [Exercises](http://beta.mybinder.org:/repo/reubano/lambdaconf-tutorial)
- [Solutions](http://beta.mybinder.org:/repo/reubano/lambdaconf-tutorial)
