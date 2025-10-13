# Ready Set Code — Shift + Design

## Installation Instructions
Download and install the following:
1. Download Python [here](https://www.python.org/downloads/). For Windows, make sure the "add to PATH" option is checked.
2. Download VS Code [here](https://code.visualstudio.com/Download)
3. Install the Python extension by Microsoft in VS Code

![recording 2](https://github.com/user-attachments/assets/90acbeb6-09a3-4a6b-ba4a-bef45dc1d93a)

### Verify your installation
Let's create a simple program that prints out "Hello World!" to verify if everything is properly installed.

![recording](https://github.com/user-attachments/assets/5498533c-d98e-4efd-80c9-234a688af4c0)

A few things to note:
1. We'll be coding in Python which means that all of our files need to end in **.py**.
2. `print` is an example of a *function*. You can easily tell because there are parentheses () immediately after its name.
3. Inside `print`'s parentheses, we gave it the data "Hello World!" There are many types of data, this data is called a *string*, string as in a string of letters or characters.
4. Functions are like machines, `print` is a function that takes input and outputs it to the screen, kind of like how a printer takes a digital document and prints it onto a page.

### Downloading the starter code
Great, now let's download the starter files we've provided for you in this repo.



[![video](https://github.com/user-attachments/assets/b901ff25-4a31-41e4-8657-dce9f4cab6e2)](https://github.com/user-attachments/assets/b63690b1-cb41-4dcd-973d-0831804726b0)


A few things to note:
1. The terminal is a text-based way to interact with the computer instead of the graphical way we are all used to.
2. `python3 -m venv .` creates a virtual Python environment. You can think of this like a workspace for us to download packages (more on that below). If `python3` isn't recognized by the computer, use `python` instead.
3. `source bin/activate` sets our current workspace to the one we just made. On Windows, the command might be different `.\Scripts\activate`.
4. `pip install pygame` installs the pygame package (more on that below).
5. `python starter.py` runs our starter.py program. You can alternatively click the play button at the top right!
6. To switch back to our normal workspace, just type `deactivate` into the terminal!

### Installing packages
A package in Python is a bundle of code someone else wrote. We use packages to avoid having to reinvent the wheel. Python comes with a lot of pre-installed packages, but for this class
we will need to install two packages ourselves called `pygame` and `pyserial`. They will help us make our game! In the video we already showed you how to install `pygame` using `pip install`,
go ahead and install `pyserial` in the same way (`pip install pyserial`).

**If any of the above steps fail, don't worry! You can either try problem solving it yourself with help from the Internet or wait until class day.**

