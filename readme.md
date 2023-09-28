This is a AOS assignment for simulating a battlefield using gRPC in Python.

#### Team Members:
1. Sparsh Kumar 2022H1120293P
2. Shubham Shrivastav 2022H1120283P

#### Files:
1. battle_commander.py - Contains the logic for the battlefield commander.
2. battle_soldier.py - Contains the logic for each soldier in the battlefield.
3. battle.proto - Contains the rpc messages and services for communication between battle_commander.py and battle_soldier.py
4. requirements.txt - Contains all the required libraries
5. output_log.txt - Contains the output generated by battle_commander.txt
6. battle_commander_terminal.py - Same as battle_commander.py but prints out on terminal
7. battle_pb2.py & battle_pb2_grpc.py - grpc generated files.

#### Installation Instructions:
1. Clone/Copy the files to 2 machines on which you want to run client and server.
2. Ensure you have Python3.x installed on both of the machines.
3. Install the required dependencies on both the machines using: pip install -r requirements.txt

#### Running Instructions:
1. Change the IP addresses in battle_soldier.py and battle_commander.py to the current IP address of the server.
2. Start the gRPC server by executing: python battle_soldier.py on one machine.
3. Start the battlefield simulation by executing: python battle_commander.py on another machine. This will create output_log.txt file as output.

This simulation will continue for the time you've specified and you can view the output in the output_log.txt file. 
If you want to get output in terminal then execute : python battle_commander_terminal.py

#### Notes:

1. Ensure the gRPC server (from battle_soldier.py) is running before you execute the battle_commander.py to see the battlefield simulation.
2. Before starting another simulation, restart the existing gRPC server.

### Project Videos

#### Project Description

<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="Project Description.mp4" type="video/mp4">
  </video>
</figure>

#### Project Demonstraction

<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="Project Demonstration.mp4" type="video/mp4">
  </video>
</figure>
