# progress Bar
`progressBar` is an open-source python module to help you making progress bar easily! *(not in python `PIP`)*

## **LICENSE**
This **repo** is under the [Mozilla Public License 2.0](https://choosealicense.com/licenses/mpl-2.0/#) license, you can do mostly anything with it.

## Some definitions
`cls`: **CL**ear **S**creen

## How to use it:
### class arguments
When first opening the file, you can see this:
```py
# class arguments:
'''
current_value: The current value
max_value: The maximum value of the progress bar
bars_max: The number of bars that will be rendered (example with ten bars: ----------)
symbols: The symbols that are rendered for showing the current progress bar state (the first index is the full bar and the second is the empty bar)
text: The text that will be rendered above the progress bar
'''
```
This is the help about the progress bar arguments.

### starting off
**First** you need to import and create an object.
```py
import progressBar  # importing the module

bar = progress_bar()  # creating the "bar" object
```
Doing this will create an object named `bar`, but this is not enough.\
But imagine I want to:
- display 15 characters to render the **progress bar**
- have a **progress bar** looking like this: `|||||:::::::::::::`

The code for this would be:
```py
import progressBar  # importing the module

Pbar = progress_bar(bars_max=17, symbols=["|", ":"])  # creating the "bar" object
```
> *If you don't understand what `bars_max` and `symbols` mean, check [this](https://github.com/Geming400/progressBar/blob/main/README.md#how-to-use-it).*

### render
**Rendering** is as simple as executing a function!\
Once you have your object, *(in this case, `bar`)* you just execute that piece of code:
```py
import progressBar  # importing the module

Pbar = progress_bar(bars_max=17, symbols=["|", ":"])  # creating the "bar" object
Pbar.render(doPrint=True) # render the bar. You can set the "doPrint" argument to False to prevent the printing. (by default True)
```

### adding a value to the object
A **progress bar** needs to move! Imagine the life of it without moving... `emotional story, I know :(`\
There is 3 function to do it:
```py
add(to_add=10, cls=True)
```

```py
set_value(to_set=50, cls=True)
```

```py
add_and_render(to_add=10, cls=True)
```

Here is an example:
```py
from time import sleep  # importing the modules
import progressBar

Pbar = progress_bar(bars_max=17, symbols=["|", ":"])  # creating the "bar" object
Pbar.render(doPrint=True) # render the bar. You can set the "doPrint" argument to False to prevent the printing. (by default True)

sleep(1) # wating 1 second, but replace this with your script

Pbar.add_and_render(to_add=10, cls=True) # add 10 (out of max_value (default: 100)) the the progress bar and then render it
```

### Advanced use
You can set use some variables to track the current progression of the `progress bar`
Here is the list:
- self.max_step = max_value ***(`max_value` is the function argument)***
- self.current = current_value
- self.bars_max = bars_max
- self.symbols = symbols
- self.text = text
  
*(Replace `self` by your python **object**!)*

## What is currently supported
*Current version: **1.0.0***

| Version | Feature                                                    | Supported                         |
| ------- | ---------------------------------------------------------- |---------------------------------- |
| 1.0.0   | to change the max value                                    | :white_check_mark:                |
| 1.0.0   | to set a new value                                         | :white_check_mark:                |
| 1.0.0   | to add a value                                             | :white_check_mark:                |
| 1.0.0   | to render the progress bar                                 | :white_check_mark:                |
| 1.0.0   | to change the look of the progress bar                     | :white_check_mark:                |
| 1.0.0   | to add an upper text when rendering                        | :white_check_mark:                |
| *?.?.?* | to change the min value                                    | :x: *(will likely never do this)* |
| *?.?.?* | to change the number of character displayed when rendering | :x:                               |
| *?.?.?* | to add a prefix when rendering                             | :x:                               |
| *?.?.?* | to add a suffix when rendering                             | :x:                 |
