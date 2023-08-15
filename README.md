# progress Bar
`progressBar` is an easy to use progress bar script in python!

## **LICENSE**
This **repo** use the [mit](https://choosealicense.com/licenses/mit/) license, you could do mostly anything with [it](https://github.com/Geming400/progressBar).

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

This is the help about the progress bar arguments.\
**next**, you need to import and create an object.
```py
import progressBar  # importing the module

bar = progress_bar()  # creating the "bar" object
```
Doing this will create an object named `bar`, but this is not enough.
I want to:
- display 15 characters to render the **progress bar**
- have a **progress bar** looking like this: `|||::::`

The code for it would be:
```py
import progressBar  # importing the module

bar = progress_bar(bars_max=17, symbols=["|", ":"])  # creating the "bar" object
```
If you don't understand what `bars_max` and `symbols` mean, check [this](class arguments).
