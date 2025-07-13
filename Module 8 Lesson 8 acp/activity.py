class Robot:
    # Constructor to initialize the robot's attributes
    def __init__(self, name,model,purpose):
        self.name = name
        self.model = model 
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am model: {self.model}.")
        print(f"My purpose is: {self.purpose}.")

# Create a robot object
my_robot = Robot("RoboMaryam", "TX-2025", "Helping students to learn Python.")

# Introduce the robot
my_robot.introduce()