# BOTBRAINS_BATTLE_UAV_drone_system
# Autonomous UAV Fleet for Target Detection

## Introduction
In this project, we develop an autonomous UAV fleet capable of searching for a specific target among various objects in an open field. The drones communicate using swarm technology and avoid collisions using sensors. This project demonstrates a simulated environment to test the UAVs' functionalities without physical hardware.

## Features
- Autonomous flight and landing
- Object detection using LiDAR sensors
- Target identification using color sensors
- Communication between drones using ESP8266 Wi-Fi module simulation
- Collision avoidance

## Methodology

### Understanding Swarm Drones
Swarm drones operate using collective behavior based on algorithms inspired by nature (like bee swarms or bird flocks). They coordinate and perform tasks collaboratively.

### Communication using ESP8266
The ESP8266 Wi-Fi module is simulated to establish a mesh network for drone-to-drone communication. Drones share information about their status and findings.

### Design Changes in Drones
- **Waterproofing**: Ensuring that all electronic components are sealed and protected from water.
- **Floating Mechanism**: Adding buoyant materials or structures to allow the drone to land on water surfaces.
- **Reinforced Landing Gear**: Using stronger materials for the landing gear to handle rough terrains.

### Autonomous Search Algorithm
Each drone operates autonomously using the following sensors:
- **LiDAR**: For object detection.
- **Color Sensor**: For target identification.
- **ESP8266**: For communication.

### References:
- "Design and Development of Autonomous Drone for Search and Rescue Operations" by S. K. Singh et al. (2020)
- "Autonomous Drone for Environmental Monitoring Using Lidar and Camera" by J. M. Lee et al. (2019)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9841964/
- https://www.mdpi.com/1424-8220/21/8/2642

![UAV_drone_system_flowchart](https://github.com/mkhekare/BOTBRAINS_BATTLE_UAV_drone_system/assets/52950861/8732cf44-b769-412f-b46f-afc853c4eee0)

