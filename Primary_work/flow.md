# Detailed Plan
- Introduction
1. A UAV fleet designed to operate autonomously to detect targets.
2. Capable of flying over grassy land and navigating through different terrains (land, water, air).
3. Utilizes swarm technology for communication and coordination.

- Methodology
1. Each drone will be equipped with a flight controller, LiDAR sensor, and color sensor.
2. The drones will communicate using ESP8266 modules (simulated for virtual testing).
3. The drones will be programmed to avoid collisions and identify targets based on specified criteria.

-System Design
1. Drones will have a robust design to handle different terrains.
2. The system will initiate an open field test flight using a remote control.

![WhatsApp Image 2024-06-18 at 7 00 39 PM](https://github.com/mkhekare/BOTBRAINS_BATTLE_UAV_drone_system/assets/52950861/b7c5bd61-72ac-4fa1-b28c-66ce5b3d5f9f)

```
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
        # Simulate object detection with LiDAR
        object_height = random.choice([10, 15, 20])
        if object_height == 15:
            return True
        return False
    
    def check_color(self):
        # Simulate color detection
        color = random.choice(['red', 'green', 'blue'])
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
```
