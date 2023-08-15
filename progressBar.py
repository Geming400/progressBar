# class arguments:
'''
current_value: The current value
max_value: The maximum value of the progress bar
bars_max: The number of bars that will be rendered (example with ten bars: ----------)
symbols: The symbols that are rendered for showing the current progress bar state (the first index is the full bar and the second is the empty bar)
text: The text that will be rendered above the progress bar
'''

# Creating a function that clear the screen (cls)
def clear_screen():
    print("\n" * 1000) # Doing this because of mac 

# Creating the class
class progress_bar():
    def __init__(self, current_value=0, max_value=100, bars_max=10, symbols:list = ["|", "-"], text="progressBar text"): # MIN_VALUE = 0 (not modifiable)
        #self.min = min_value
        self.max_step = max_value # The maximal number of step to display all of the progress bar
        self.current = current_value # The current step number of where the progress of your execution is 
        self.bars_max = bars_max # The maximum number of bars (characters) to display
        self.symbols = symbols
        self.text = text

        # Normally, will work without this checking, but we need extra check :D


    def render(self, doPrint=True):
        # |||------------           Default way to render the progress bar (3 bars full, 7 bars empty)
        # currentR, R = Round (Will be rounded, but only below + don't care >:) )
        self.currentR = self.current / self.max_step
        self.barsToRender = int(self.currentR * self.bars_max)
        self.renderResult = ""
        #print(self.currentR)
        if self.current > 100:
            print("You can't have the current value being more than 100")
        else:
            for x in range(0, self.barsToRender): # A loop to count how many bars are full
                self.renderResult = self.renderResult + self.symbols[0]

            for x in range(0, self.bars_max - self.barsToRender): # A loop to count how many bars are empty
                self.renderResult = self.renderResult + self.symbols[1]

            if doPrint == False: # Check if it will print the bar or simply return it.
                if self.text == "": # If there is no given text, then it will not return the text at all
                    return self.renderResult
                else:
                    return self.text + "\n" + self.renderResult
            else:
                if self.text == "": # If there is no given text, then it will not print the text at all
                    print(self.renderResult)
                else:
                    print(self.text + '\n' + self.renderResult)
                    #print(str(self.current) + '\n' + self.renderResult)


    # INT = THE NUMBER THAT WILL BE SET/ADD.
    def add(self, to_add=10, cls=True): # Let you add a value to the current value of the progress bar
        self.current += to_add
        if cls:clear_screen()


    def set_value(self, to_set, cls=True): # Let you set the value of the progress bar
        self.current = to_set
        if cls:clear_screen()
    

    def add_and_render(self, to_add=10, cls=True): # Let you add a number to the current value, and then render the progress bar
        if cls:clear_screen()

        self.add(to_add)
        self.render()