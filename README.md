# Bash Menu Builder

This package help you build menu for yours console scripts

## Installation
For install package to your project use this command:
```shell
pip3 install bash-menu-builder
```

## Use
Example of use menu:
```python
from bash_menu_builder import View, MenuItemDto

def banner() -> str:
    return 'I\'m Banner Text'

def script_one():
    # Call Services or do something

def script_two():
    # Call Services or do something

def script_three():
    # Call Services or do something

if __name__ == "__main__":
    View([
        MenuItemDto('Script Title 1', 'one', script_one),
        MenuItemDto('Script Title 2', 'two', script_two),
        MenuItemDto('Script Title 3', 'one-more', script_three),
    ], banner())
```

## Draw menu
The menu draw via class ``View`` which get params of array with DTOs and text of banner (optional)
The MenuItemDto have 3 params ``def __init__(self, title: str, option_name: str, handler: object):``
 - ``title: str`` - the title of menu item
 - ``option_name: str`` - the option name for call menu via console
 - ``handler: object`` - the handler of menu item. What exactly script do after select this menu item.

## How it works
<img src="./doc/example-1.png" alt="How it works" style="width:100%;" />

After select menu number and press Enter will run script in function. When script finish process menu will draw again.

Also you can call script without drawing menu. Just set option when call python script file, ex. ``python3 main.py --one-more``
In this case will run script for menu **'Script Title 3'**. When script finish process menu will not draw again and program will close.

<img src="./doc/example-2.png" alt="How it works" style="width:100%;" />