class Demo:
    def __getattr__(self,name):
	    print('FishC')
    def __getattribute__(self,name):
	    return super().__getattribute__(name)
    def __setattr__(self,name,value):
	    super().__setattr__(name,value)
