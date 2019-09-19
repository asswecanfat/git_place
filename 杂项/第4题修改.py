class Counter:
    def __init__(self):
        self.counter = 0
    def __getattr__(self,name):
        pass
    def __getattribute__(self,name):
        return super().__getattribute__(name)
    def __setattr__(self,name,value):
        self.counter += 1
        super().__init__()
        super().__setattr__(name,value)
    def __delattr__(self,name):
        counter -= 1
        super().__delattr__(name)
        
