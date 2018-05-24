# Getting Started with Python's Pytest

### Create Virtual Environment

See book https://github.com/mattharrison/Tiny-Python-3.6-Notebook
See "Environments" near bottom of python.rst file for how to create a virtual environment.

He has an advanced Pytest course.

He uses Python IDLE editor:

    python -m idlelib.idle

To run pytest, I had to go to the top-level directory and run:

    PYTHONPATH=. pytest

To avoid having to specify PYTHONPATH each time you run the command, create a setup.py file:

    from distutils.core import setup

    setup(name='Block',
          py_modules = ['block']
          )

Then run to install the block module in your Python path:

    pip install -e .
