# For step by step mode------------------------------------------------------------------------

class FunctionPressEnterToContinue:
    """
    This class implements the unnecessary step by step implementation of the code.
    Though unnecessary, this class allows me to show a bit of OOP programming to solve
    a problem in a context where objects are not really necessary.
    """
    def __init__(self):
        self.answered = False
        self.question = 'n'
        self.y_n_to_true_false = {
            'y': True,
            'n': False
        }

    def should_proceed(self):
        """
        Stops the program at the end of each step, so whomever is verifying the code may analyze it step by step.
        You may use the Debugger instead.
        :return: Stops the programme until the user press enter.
        """
        if not self.answered:
            self.question = input('Do you want to activate step by step mode?(y, n) ')
            while self.question != 'y' and self.question != 'n':
                print("Wrong input! You may type only 'y' or 'n'.")
                self.question = input('Do you want to activate step by step mode?(y, n) ')
            self.answered = True

        step_by_step = self.y_n_to_true_false[self.question]

        if step_by_step:
            input('Press enter to continue... ')
