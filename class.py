class Car (object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerating")
        "accelerator functionality here"

    def change_gear(self,gear_type):
        print("gear changed")
        "gear related functionality here"

        
     
