import random
import time
from threading import Thread

class ESP8266:
    def __init__(self):
        self.network = []

    def connect(self, drone):
        self.network.append(drone)

    def send_message(self, sender, message):
        for drone in self.network:
            if drone.id != sender.id:
                drone.receive_message(message)

class Drone:
    def __init__(self, id, network):
        self.id = id
        self.position = (0, 0)
        self.target_found = False
        self.network = network
        network.connect(self)
    
    def receive_message(self, message):
        if message == "Target Found":
            self.target_found = True
            print(f"Drone {self.id} received message: {message}")
    
    def communicate(self):
        self.network.send_message(self, "Target Found")
        print(f"Drone {self.id} sent message: Target Found")
    
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
    
    def search(self, other_drones):
        while not self.target_found:
            self.move()
            if self.detect_object():
                if self.check_color():
                    self.target_found = True
                    self.communicate()
                    print(f"Drone {self.id} found the target!")
                    break
            time.sleep(1)

class FlightController:
    def __init__(self, drones):
        self.drones = drones
    
    def initiate_test_flight(self):
        threads = []
        for drone in self.drones:
            thread = Thread(target=drone.search, args=(self.drones,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()

def main():
    network = ESP8266()
    drone1 = Drone(1, network)
    drone2 = Drone(2, network)
    drone3 = Drone(3, network)
    
    drones = [drone1, drone2, drone3]
    flight_controller = FlightController(drones)
    
    # Simulate remote control to initiate test flight
    print("Initiating open field test flight...")
    flight_controller.initiate_test_flight()
    print("Test flight completed.")

if __name__ == "__main__":
    main()
