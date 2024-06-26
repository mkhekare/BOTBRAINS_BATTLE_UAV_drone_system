# ***Main Components***
- Drone Class: Represents an individual drone.
- Swarm Communication: Simulated using a network class to handle communication between drones.
- Flight Controller: Simulates the flight control and movement of the drones.
- Remote Control: Initiates the open field test flight.

# Explanation

- ESP8266 Class: Simulates the communication network for the drones.

1. connect(drone): Adds a drone to the network.
2. send_message(sender, message): Sends a message to all drones in the network except the sender.

- Drone Class: Represents an individual drone.

1. __init__(self, id, network): Initializes the drone with an ID and connects it to the network.
2. receive_message(self, message): Handles receiving messages.
3. communicate(self): Sends a message to other drones indicating the target is found.
4. move(self): Simulates the drone moving to a random position.
5. detect_object(self): Simulates object detection using LiDAR.
6. check_color(self): Simulates color detection.
7. search(self, other_drones): Simulates the search operation and communicates if the target is found.

- Flight Controller Class: Manages the drones and initiates the test flight.

initiate_test_flight(self): Starts the search operation for all drones concurrently using threads.

- Main Function: Sets up the network, drones, and flight controller, and initiates the open field test flight.
