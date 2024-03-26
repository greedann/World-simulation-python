# Life simulation
## The subject of objected oriented programming(OOP)

The goal of the project is to write an object-oriented life simulation application in python. For visualization of the simulation the graphical library tkinter is used.

The application implements 2 main classes of organisms:
* Animals 
* Plants

These classes are expanded into subspecies, which have their own behavioral and characteristic features. The player can control the movement of the person. Also, the person has a special ability when activated which he can pass 2 squares for 1 move. When activated, it works for 5 rounds. And the next 5 rounds can't be activated.

There are 2 methods available to control the simulation:
* With buttons in the graphical interface
* With keys on the keyboard

The application also allows you to save and load the current state of the simulation. On startup, the simulation world is filled with creatures in random order

## Key Bindings

Hotkeys can be viewed in the application by pressing the button `Show hint` or in the table above
| Key | Action
| ----- | -----
| <kbd>Space</kbd> | Go to the next round
| <kbd>U</kbd> | Use special ability
| <kbd>S</kbd> | Save current state to file
| <kbd>L</kbd> | Load current state from file
| `Arrows` | Move around the field

## Installation

To run the application locally you need to bend the repository.
```bash
$ git clone https://github.com/greedann/World-simulation-python.git
$ cd World-simulation-python
```
Create virtual invironment and install requirements
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
And run aplication
```bash
$ python main.py
```
Now aplication is ready to use