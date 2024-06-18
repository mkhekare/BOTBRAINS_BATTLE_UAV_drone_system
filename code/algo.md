## Algorithm/Flow
#Initialization
1. Drones are initialized and connected to the simulated ESP8266 network.
2. Each drone is assigned a unique ID and starting position.

- Search Operation
1. Drones move randomly within a predefined area.
2. They use LiDAR sensors to detect objects and measure their height.
3. If an object of height 15 cm is detected, the color sensor checks the object's color.
4. If the object is green, the drone communicates the discovery to the other drones.

- Communication and Coordination
1. When a drone finds the target, it sends a message to the other drones using the simulated ESP8266 network.
2. Upon receiving the message, the other drones stop their search.
