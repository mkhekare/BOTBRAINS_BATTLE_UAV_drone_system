## Autonomous Search Algorithm

import random
import time

class Drone:
    def __init__(self, id):
        self.id = id
        self.position = (0, 0)
        self.target_found = False
    
    def move(self):
        self.position = (random.randint(0, 100), random.randint(0, 100))
        print(f"Drone {self.id} moved to {self.position}")
    
    def detect_object(self):
        object_height = random.choice([10, 15, 20])
        print(f"Drone {self.id} detected object with height {object_height} cm")
        if object_height == 15:
            return True
        return False
    
    def check_color(self):
        color = random.choice(['red', 'green', 'blue'])
        print(f"Drone {self.id} detected color {color}")
        if color == 'green':
            return True
        return False
    
    def communicate(self, other_drones):
        for drone in other_drones:
            drone.receive_signal(self.id)
    
    def receive_signal(self, sender_id):
        print(f"Drone {self.id} received signal from Drone {sender_id}")
        self.target_found = True
    
    def search(self, other_drones):
        while not self.target_found:
            self.move()
            if self.detect_object():
                if self.check_color():
                    self.target_found = True
                    self.communicate(other_drones)
                    print(f"Drone {self.id} found the target!")
                    break
            time.sleep(1)

def main():
    drone1 = Drone(1)
    drone2 = Drone(2)
    drone3 = Drone(3)
    
    drones = [drone1, drone2, drone3]
    
    for drone in drones:
        drone.search(drones)

if __name__ == "__main__":
    main()
