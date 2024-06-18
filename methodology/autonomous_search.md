## Autonomous Drone Operation and Coordination
# Each amphibious drone in the fleet is equipped with the following capabilities:
1.	Flight Autonomy:
-	Pre-programmed flight paths based on GPS coordinates.
-	Autonomous takeoff and landing capabilities.
2.	Multi-Terrain Navigation:
- Autonomous navigation on land using wheels or tracks.
- Buoyant design and propulsion for water navigation.
3.	Target Identification:
-	Use LiDAR to detect objects with a height of 15cm.
-	Measure the object's dimensions and use a color sensor to detect the color green.
4.	Swarm Communication:
-	Upon identifying the target, the drone sends the location data to other drones using swarm communication protocols.
-	The other drones halt their search once the target is found and communicated.
5.	Collision Avoidance:
-	Use LiDAR data to avoid obstacles and prevent collisions with other drones.
-	Implement collision avoidance algorithms to navigate safely in the search area.
