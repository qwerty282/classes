class Button:
    def __init__(self):
        self.click = 0
 
    def click(self):
        self.click += 1
 
    def reset(self):
        self.click = 0
 
    def click_count(self):
        print(self.click)
