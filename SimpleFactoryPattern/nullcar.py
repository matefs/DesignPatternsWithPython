class NullCar():
    def __init__(self,carname):
        self._carname = carname
    
    def start(self):
        print(f"unknown car {self._carname}")
    
    def stop(self):
        pass