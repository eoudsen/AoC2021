class Fish:

    def __init__(self, count=8):
        self.counter = count

    def reset(self):
        self.counter = 6

    def pass_day(self):
        if self.counter == 0:
            self.reset()
            return True
        self.counter -= 1
        return False