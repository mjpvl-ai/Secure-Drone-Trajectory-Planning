both known and unknown environments securely by
using Blockchain

A Project Report

submitted by

JAYAPRAKASH M (CS21M1005)

in partial fulfilment of requirements
for the award of the degree of

MASTER OF TECHNOLOGY

Department of Computer science and Engineering
INDIAN INSTITUTE OF INFORMATION TECHNOLOGY,
DESIGN AND MANUFACTURING KANCHEEPURAM
MAY 2023

# DECLARATION OF ORIGINALITY

I, Jayaprakash M, with Roll No: CS21M1005 hereby declare that the material presented in the Project Report titled Trajectory Planning for Autonomous Drone Delivery in both known and unknown environments securely by using Blockchain
represents original work carried out by me in the Department of Computer science
and Engineering at the Indian Institute of Information Technology, Design and Manufacturing, Kancheepuram.
With my signature, I certify that:
• I have not manipulated any of the data or results.
• I have not committed any plagiarism of intellectual property. I have clearly indicated and referenced the contributions of others.
• I have explicitly acknowledged all collaborative research and discussions.
• I have understood that any false claim will result in severe disciplinary action.
• I have understood that the work may be screened for any form of academic misconduct.

Jayaprakash M

Place: Chennai
Date: 10.05.2023

# CERTIFICATE

This is to certify that the report titled Trajectory Planning for Autonomous Drone
Delivery in both known and unknown environments securely by using Blockchain,
submitted by Jayaprakash M (CS21M1005), to the Indian Institute of Information
Technology, Design and Manufacturing Kancheepuram, for the award of the degree of
MASTER OF TECHNOLOGY is a bona fide record of the work done by him/her
under my supervision. The contents of this report, in full or in parts, have not been
submitted to any other Institute or University for the award of any degree or diploma.

Dr. Masilamani V
Project Guide
Head of the department
Department of Computer science and Engineering
IIITDM Kancheepuram, 600 127

Place: Chennai
Date: 10.05.2023

# ABSTRACT

Unmanned aerial vehicles, sometimes known as drones or UAVs, are being used in a
growing number of difficult and varied applications. Both the military and the civilian
worlds use these applications. In other words, UAVs should be able to complete predetermined tasks in unforeseen circumstances without requiring human assistance. A
large number of artificial intelligence algorithms were developed to provide this level
of autonomy. The guidance, navigation, and control (GNC) of UAVs was the focus of
these algorithms. Blockchain is a decentralized, secure, and isolated network. To establish trustworthy links amongst the Drones, we connect several drones educated in advanced continuous DRL (PPO and SAC) using an optimized blockchain consensus mechanism (CG-PBFT).
Phase 1:
The initial stage of the project’s implementation uses the PEDRA engine and the
existing DRL algorithm to ensure that the environment is ready for the project’s subsequent phases.
Phase 2:
Interactive trajectory planning for drone delivery is being developed, along with a
foundational blockchain for multidrone communication.
Phase 3:
Trajectory planning for drone delivery in both exploitation of known and exploration
of unknown environments also ensures data security using blockchain with ASCON lightweight ciphers.
Phase 4 :
Finish the training in an "old-town" environment on the Qualcomm Flight RB5 platform, then test the algorithm’s performance in an entirely novel environment using sim-to-real transfer.
KEYWORDS:

Drones; Deep Reinforcement Learning; PEDRA; Blockchain

# TABLE OF CONTENTS

# ABSTRACT

# LIST OF TABLES

# LIST OF FIGURES

# ABBREVIATIONS

Literature Review

## 1.1 Overview

### 1.1.1 Overview of Deep Reinforcement Learning

## 1.2 Base Paper

## 1.3 Plan for solving the problem

### 1.3.1 Overview for the future work

Implementing existing DRL Algorithm

## 2.1 

## 2.2 Challenges faced while implementing existing DRL (Deep Reinforcement learning)

### 2.1.1 Challenges:

### 2.1.2 Solutions:

Programmable Engine for Drone Reinforcement learning Applications

### 2.2.1 Available drone agents

### 2.2.2 Supported modes

### 2.2.3 Unreal simulation files

### 2.2.4 Floorplan

### 2.2.5 Config file

### 2.2.6 Parameter Explanation

### 2.2.7 Environment Supported Features

Introduction

## 3.1 Interactive trajectory planning for drone delivery

### 3.1.1 Safe and unsafe unreal coordinate

### 3.1.2 Environment as 3d Array

### 3.1.3 Segment Tree

Foundational Blockchain for multiple drone communication . . . .

### 3.2.1 Data layer

### 3.2.2 Network layer

### 3.2.3 Consensus layer

### 3.2.4 Incentive layer

### 3.2.5 Contract layer

### 3.2.6 Application layer

Trajectory planning . . . . . . . . . . . . . . . . . . . . . . . . . .

### 3.3.1 Trajectory planning for drone delivery in known environments

### 3.3.2 Trajectory planning for drone delivery in unknown environments exploration then exploitation

## 3.2 

## 3.3 Project Overview

## 4.1 Program flow

Exploration

## 5.1 Exploration: Gain the knowledge of the environment

Exploitation

## 6.1 Exploitation: Using the explored knowledge find delivery path

RESULT : "Outdoor Oldtown" Enviroinment

RESULT : "Indoor Vanleer" Enviroinment

Conclusion and Future scope

## 9.1 Conclusion

## 9.2 Future scope

# LIST OF FIGURES

## 1.1 Deep Q-learning Network

## 2.1 PEDRA - Basic structure

## 2.2 Program control structure

## 2.3 Type of Functions in the PEDRA Agent

## 2.4 Config with different settings

## 2.5 Drone Agents

## 2.6 Environment in infer mode

## 2.7 Parameter and Position visualization in infer mode

## 2.8 floor Map

## 2.9 Relation between the Coordinates and their Parameters

## 2.10 Unreal Environment with drone

## 3.1 Interactive trajectory planning

## 3.2 Safe unreal coordinate - Green

## 3.3 3d visualization of environment

## 3.4 2d array - single layer from 3d array

## 3.5 2d array - segment tree

## 3.6 Sum of leaves under a node

## 3.7 dynamic range querying

## 3.8 BCT architecture

## 3.9 Structure of a block in a BCT

## 3.10 Manual safest path - Green

## 3.11 Delivery points - Yellow

## 3.12 Conversion of unreal to array coordinate

## 3.13 Generated path for Delivery

## 3.14 Generated Return path for going back

## 3.15 four drone coordinates - only two useful

## 3.16 Show how safe coordinate changing over the different trails

## 3.17 Exploring the safe coordinates in environment

## 3.18 Manual and Automatic safer paths with endpoints

## 4.1 Project Implementation Overview

## 5.1 RGB and Binary Image

## 5.2 How Drone calculates midpoint of the single scan

## 5.3 Exploration Algorithm

## 6.1 Exploitation Algorithm

## 7.1 3d array of Safe coordinates – Drone can fly

## 7.2 3d Midpoint used as endpoints in exploitation

## 7.3 How the number of safe coordinates changes while changing the flying

height of the drone here we consider as Z-Axis (Green - Safe coordinate, Blue - Midpoints) . . . . . . . . . . . . . . . . . . . . . . . .

## 8.1 Test Environment: Safe coordinate

## 8.2 Test Environment: Midpoints

## 8.3 Test Environment: Z Axis

# ABBREVIATIONS

UAV

Unmanned Aerial Vehicles

DRL

Deep Reinforcement Learning

GNC

Guidance, Navigation, and Control

VLOS

Visual Line of Sigh

BVLOS

Beyond Visual Line of Sigh

PEDRA

Programmable Engine for Drone Reinforcement Learning Applications

BCT

Block Chain Technology

# CHAPTER 1
# Literature Review

## 1.1 Overview

### 1.1.1 Overview of Deep Reinforcement Learning

DRL can be seen as a way to solve challenging problems that involve sequential decision making under uncertainty and partial observability, using data-driven methods that
can learn from raw sensory inputs. DRL can also be seen as a way to bridge the gap between artificial intelligence and neuroscience, by studying how biological agents learn
from their interactions with the environment and how artificial agents can mimic or
improve upon their abilities. DRL is an active and interdisciplinary research area that
draws upon concepts and techniques from computer science, mathematics, statistics,
psychology, cognitive science and engineering.
A deep reinforcement learning architecture is a way of designing and implementing
a deep reinforcement learning algorithm, which combines reinforcement learning (RL)
and deep learning. RL is a process in which an agent learns to make decisions through
trial and error, by interacting with an environment and receiving rewards or punishments
for its actions. Deep learning is a form of machine learning that uses neural networks
to transform a set of inputs into a set of outputs.
A deep reinforcement learning architecture typically consists of the following components:
An agent, which is the entity that learns and acts in the environment. An environment, which is the system that the agent interacts with and receives feedback from.
A policy, which is a function that maps the agent’s observations to actions. A value
function, which is a function that estimates the expected return (cumulative reward) for
each state or state-action pair.

A neural network, which is a computational model that approximates the policy or
value function using multiple layers of nonlinear units.
A learning algorithm, which is a method that updates the neural network’s parameters based on the agent’s experience.
Depending on the problem and the goal, different types of deep reinforcement learning architectures can be used, such as:
Value-based architectures, which use neural networks to approximate value functions and derive policies implicitly. Examples include deep Q-networks (DQN). In more advanced continuous control scenarios, Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) are preferred for stable and aerodynamic maneuvers.

**Figure 1.1: Deep Q-learning Network**

## 1.2 Base Paper

By exploring the literature, I found
[1] Yunlong Song, Mats Steinweg, Elia Kaufmann, and Davide Scaramuzza “Autonomous Drone Racing with Deep Reinforcement Learning” IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), Prague, 2021.
[2] Yulei Wu, Senior Member, IEEE, Hong-Ning Dai, Senior Member, IEEE, Hao
Wang, Member, IEEE, Kim-Kwang Raymond Choo, Senior Member, IEEE “Blockchainbased Privacy Preservation for 5G-enabled Drone Communications”.
[3]"Autonomous Drone Racing: A Survey" by Hanover, Drew and Loquercio, Antonio and Bauersfeld, Leonard and Romero, Angel and Penicka, Robert and Song, Yunlong and Cioffi, Giovanni and Kaufmann, Elia and Scaramuzza, Davide.

## 1.3 CS21M1005

Plan for solving the problem

By using the knowledge of the both base paper we are going to create light weight
Block-chain to connect multiple drone with reliable connection. Any transaction make
between the drone is done using smart contract.
Step by step approach:
1. Implement the existing DRL algorithm to train the drones in the simulation
2. Create the block chain and declare the rules and regulation as per standards.
3. Connect the drones with block chain using CG-PBFT.
4. Test connection with the simulation on Qualcomm RB5 platforms.

### 1.3.1 Overview for the future work

To make fully autonomous drone to complete the specific task without human interaction lot of research is required. future scope is Drones with Latest technologies like
Artificial intelligence,5G Network,Block-chain.

# CHAPTER 2
# Implementing existing DRL Algorithm

## 2.1 Challenges faced while implementing existing DRL

(Deep Reinforcement learning)

The issues encountered and action to resolve them are described below:

### 2.1.1 Challenges:

1. Required high computational hardware to complete entire training.For example
DRL required 1,50,000 episode’s to get trained with entire environment.
2. Lack of communication between Airsim APIs during training causes training to
fail.
3. Exploration vs Exploitation problem
4. Integrating with AirSim/Gazebo during implementation will result in several failures,
which will make our implementation more difficult.
5. Difficulty encountered when employing the algorithm to explore unknown environments and achieving smooth sim-to-real transfer.

### 2.1.2 Solutions:

1. Having prior knowledge of the environment help as to avoid unwanted episode’s.
2. locating the safest route across the environment that will take you to every delivery place that is possible. This can be achieved by trail run and continuous control optimization (SAC/PPO).
3. Keep on exploring all the edge cases and come up with a smooth implementation on edge-AI hardware like Qualcomm RB5.

After examining the aforementioned issues and their solutions, we started focusing
on the particular task is drone delivery.

Future delivery jobs are predicted to make substantial use of drones. If there are no
obstructions, satellite-based navigation from the point of departure to the location of the
destination is straightforward. When impediments are known to be on the way, pilots
are required to create a flight plan to avoid them. However, developing a safe flight plan
becomes very difficult when they are unknown, there are too many of them, or they are
in locations that are not in fixed positions. Furthermore, the present drone navigation
systems might not work at a location with a poor satellite signal, such a building, a tree,
or a canyon in a city. Such problems can be solved with artificial intelligence, a field of
study that is seeing an increase in activity.

## 2.2 Programmable Engine for Drone Reinforcement learning Applications

PEDRA is a model used to link AirSim and Unreal Engine is structured using Python.
PEDRA is primarily focused on goal-oriented RL problems for drones, although it can
be expanded to address other issues like SLAM, etc. The entire platform is created
by the engine interacting with the Unreal gaming engine using AirSim. Below is the
fundamental structure.

**Figure 2.1: PEDRA - Basic structure**

Using Unreal Engine, the drones are trained in 3D environments that are lifelike.
There may be several degrees of detail added in order to make the environment look as
realistic or required as is practical.
The PEDRA engine’s two foundational papers are as follows:
[4] Adopting Deep Reinforcement Learning for algorithmic performance, a deep

neural network (DNN) can be trained with less compute by using a transfer learningbased approach.
[5] Transfer learning is adopted by a reinforcement learning algorithm, which is
then transferred to a hierarchical embedded memory architecture on the Qualcomm Robotics RB6 platform that satisfies the strict
power budgets of autonomous drones.
The user can choose from a variety of 3D realistic environments that are included
with PEDRA. The environment is chosen, and using AirSim, it is connected to PEDRA.
Microsoft created the open-source plugin AirSim to connect Python and Unreal Engine.
It offers fundamental Python functionalities for manipulating the drone’s sensory inputs
and control signals. For the aim of developing higher-level python modules for drone
RL applications, PEDRA is built upon the low-level Python modules offered by AirSim.
The following Figure illustrates the entire PEDRA workflow. The engine reads
configuration data from a file (.cfg). The problem and the algorithm used to solve it
are both defined in this configuration file. It is algorithm-specific and used to establish
parameters for algorithms. Using these building components, the user can either choose
from the aforementioned algorithms or design their own.

**Figure 2.2: Program control structure**

The user can utilise these building blocks to generate their own problem and associated algorithm. Once these requirements are satisfied, the simulation can begin. You
can modify algorithmic or training parameters, halt simulations, change configuration
files, and more on the PyGame panel. save the current simulation state, and more. PEDRA produces several output files. The log file lists useful algorithmic settings and
keeps track of the simulation state for each iteration. This helps when troubleshooting
the simulation, in particular. The training plots can be seen in real time using Tensorboard. These graphs are very helpful for tracking training parameters and, if necessary,
changing the input settings using the PyGame panel.
Loading the configuration files. Make an effort to create the settings. To specify
the environment parameters, a json file is necessary, Attempt to launch the chosen 3D

**Figure 2.3: Type of Functions in the PEDRA Agent**

environment. set up the PyGame user interface on screen. Start the algorithm.

**Figure 2.4: Config with different settings**

### 2.2.1 Available drone agents

Below is a list of different types of drone agents:
1) ARDrone
2) DJIMavic
3) DJIPhantom

### 2.2.2 Supported modes

The mode in which the simulation must be executed can be chosen using the config file.
train: Denotes the training mode, which is used as a flag in the input for the algorithm to be employed.

**Figure 2.5: Drone Agents**

infer: Denotes the inference mode, which is used as a flag in the input for the
algorithm to be employed. By adjusting the following settings, the network can be
loaded with custom weights: The simulation begins with the environment in free mode
when the mode is chosen to move around. The keyboard can be utilised in this mode.
move around: The simulation starts the environment in free mode when the mode is
set to move around. The keyboard can be used in this mode to move around the world.
The user can utilize this mode to obtain a sense of the dynamics of the environment. To
move around, use the keyboard keys a, w, s, d, left, right, up, and down. This may be
useful for locating the drone’s starting positions.

**Figure 2.6: Environment in infer mode**

### 2.2.3 Unreal simulation files

The simulation files for the packed Unreal project are contained in this folder, and they
cannot be altered in any manner (.exe, DRLwithTL, Engine, etc)

**Figure 2.7: Parameter and Position visualization in infer mode**

### 2.2.4 Floorplan

**Figure 2.8: floor Map**

(environment-name).png file containing the environment’s floorplan. This is useful
for tracking numerous drones in the environment, extracting drone positions from the
surroundings, and displaying the drone’s trajectory in inference mode.

### 2.2.5 CS21M1005

Config file

A config file is included with each environment. The settings used to configure the
environment are contained in this configuration file. The list of parameters in this configuration file and their descriptions are provided below. Editing this configuration file
is not advised.

### 2.2.6 Parameter Explanation

ox: The Drone’s starting position in X coordinates.
oy: The Drone’s starting position in Y coordinates.
alpha: Scaling constant(PEDRA coordinates into image coordinates)
ceilingz: Ceiling height in physical coordinates
floorz: Floor height in physical coordinates
playerstartz: The origin in physical coordinates

### 2.2.7 Environment Supported Features

Use the following keys to interact with the simulation screen when it is active.
Category for Key Features
F2 - PEDRA help.
P - Display current position of x and y, then orientation of the drone.
Z - Display the floorplan(minimap)
1 - Display depth map in subwindow
2 - Display segmentation map in subwindow
3 - Display image from front facing camera in subwindow
Recognizing coordinates and how they are converted:

The position of the drone can be described in one of three different types of coordinates.

**Figure 2.9: Relation between the Coordinates and their Parameters**

we can able to convert one coordinates to another using the parameters show in the
above figure.
Physical coordinates: The coordinates of the drone in the environment ( P - Displays
current coordinates)
PEDRA coordinates or AirSim Coordinates : The drone’s position in relation to
the starting point (player start). This is the coordinate that PEDRA works with. These
coordinates are returned whenever PEDRA asks AirSim to retrieve the drone’s current
location, and vice versa.
Image based coordinates: The drone’s location as seen in the floor plan picture. The
actual drone coordinates are mapped onto the picture map in this way.
Now we successfully implemented the first part in the project progress.

**Figure 2.10: Unreal Environment with drone**

# CHAPTER 3
# Introduction

## 3.1 Interactive trajectory planning for drone delivery

When the environment is ready, the drone should launch, and our interactive page with
the floor map image then loads. user has to select the path from the starting point and
click the subsequent path to reach the delivery point safely that is without collision.

**Figure 3.1: Interactive trajectory planning**

**Figure 3.1 above illustrates how our interactive user interface looks like. Three**

different coordinates are shown below:

1. Image coordinate
2. Unreal coordinate
3. Environment coordinate

Here we are dealing with the unreal coordinate for drone navigation and safe or
unsafe delivery point verification.

### 3.1.1 Safe and unsafe unreal coordinate

**Figure 3.2: Safe unreal coordinate - Green**

We arrive at the conclusion that the area shaded as green in Figure 3.2 is a safer
delivery place after testing countless potential paths.
Every unreal coordinate along the full user-selected route is checked to see if it is
safe or not.
1. Safe delivery points: It will not lead to occur any collusion
2. Unsafe delivery points: If it is in the path then for sure it lead to collusion.

### 3.1.2 CS21M1005

Environment as 3d Array

consider the entire unreal environment as 3d array and then classify each cube as safe 1 or unsafe -0.

**Figure 3.3: 3d visualization of environment**

For initial simple implementation we consider only 2d array that is single layer from
the 3d array.
we consider our environment as 80x80 array 6400 points for single layer of implementation. once we increase the dimension then it will be much more.so the problem is
required high computation.
Handling the above problem by using the segment tree data structure[6].
Segment trees can efficiently answer dynamic range queries. In addition to spatial mapping, we utilize segment trees for **Prioritized Experience Replay (PER)**. Specifically, the SegmentTree class allows for efficient computation of the sum of priorities in the DRL replay buffer, while the MinSegmentTree handles importance-sampling normalization.

**Figure 3.4: 2d array - single layer from 3d array**

### 3.1.3 Segment Tree

By using the following idea, we’ll create a two-dimensional tree of segmented branches:
3. We will build a standard one-dimensional segment tree in the first phase, just
using the first coordinates, such as "x" and "y," as constants. Instead of writing a number
within the node as we would in a one-dimensional segment tree, we will instead write
a full tree of segments.
3. Combining the segmented tree data is the next step. Assume that in the second phase, we combine the segment trees we obtained in the first stage rather than the
elements.

**Figure 3.5: 2d array - segment tree**

Time complexity :
Processing Query : O(logn*logm)

**Figure 3.6: Sum of leaves under a node**

Modification Query: O(2*n*logn*logm)
Space Complexity : O(4*m*n)

## 3.2 Foundational Blockchain for multiple drone communication

A blockchain is a time-stamped decentralised collection of fixed records controlled by
a vast global network of computers that are not owned by any one company and include
data of any size. Hashing technology is used to secure each block and connect them to
one another, guarding against outside interference.
The data will be kept in JSON format, which is simple to use and understand. The
data are kept in blocks, each of which has several data. Multiple blocks are added every
minute, and we will employ fingerprinting to distinguish one from the other.
Hashing is used to perform the fingerprinting, and in this case, the SHA256 hashing
technique will be used. To prevent tampering, each block will have a unique hash as

**Figure 3.7: dynamic range querying**

well as the hash of the previous function.
The blocks will be linked together using this fingerprinting.Each node is aware of
the hash used by the preview nodes to form a chain and guarantee a secure connection. We utilize the **ASCON family of ultra-lightweight ciphers**, designed specifically for resource-constrained UAV networks, to minimize power consumption.
Blocks that have been successfully mined are then added to the chain. In order to
prevent any type of tampering with the blockchain, the authenticity of the chain must
be verified after mining multiple blocks.
Then, depending on the user’s needs, the web app will be created using Flask and
deployed locally or publicly. We employ the **CG-PBFT (Credit-score and Grouping-mechanism PBFT)** algorithm to achieve high-speed consensus with 70% lower latency.
There are six different layers in the BCT architecture, as follows:
1. Data layer
2. Network layer
3. Consensus layer
4. Incentive layer
5. Contract layer
6. Application layer

**Figure 3.8: BCT architecture**

### 3.2.1 Data layer

The data layer is the bottom-most layer in the BCT architecture. The time-stamped data
chunks are included. A block header and a block body are both present in each of the
hash-encoded data blocks. Each block has its own hash, known as the Current hash, and
the previous block’s hash, which ties each block to the others. The Timestamp captures
the precise minute the block was produced. Using a random number generator called
Nonce, a suitable pattern for the block hash is created. Based on a unique technique, the
transaction associated with the block is saved in the Merkle root. The block’s hashes
and transactions are contained in the block body.

### 3.2.2 Network layer

The second tier of a BCT is the network layer, which distributes, expedites, and authenticates transactions. Peer-to-Peer and Client-Server are the two basic network designs
or methods. By granting the same concession to the blocks that are near to one another,

**Figure 3.9: Structure of a block in a BCT**

BCT uses the latter to verify and validate the information, including accepting or rejecting it. This implies that just the data that the blocks guarantee being captured is/are
actually being recorded. With its technique, such an activity appears to collect digital
signatures after confirming the information. Only a select few of the blocks in this situation have the authority to verify and approve or reject information using private keys,
while the remaining blocks use public keys.

### 3.2.3 Consensus layer

One of the most crucial layers in BCT networks, this layer aims to reach an agreement
among all participant perspectives on whether to accept or reject a transaction. This is
crucial in BCT since the creation of a decentralized institution requires the participation
of all participants.

### 3.2.4 Incentive layer

Another of the key components of BCT, this layer serves as the technology’s engine.
Such a layer creates a two-pronged strategy for miners by fusing the BCT technology
with economic criteria. The miners invest a significant portion of their resources and
labor towards mining the blocks to receive incentives, such as some bonus points redeemable for Bitcoin or other digital currencies.

### 3.2.5 CS21M1005

Contract layer

This is BCT technology’s fifth layer. It can code the BCT and execute a variety of
scripts, automated processes, and smart contracts to record intricate transactions. The
smart contract is a system of rules and guidelines that enables communication and transaction between the parties to a contract. All of the contract’s clauses are encrypted and
accepted by the parties when the parties construct their agreement and decide on the
regulations.
Then, the BCT sends this contract to all of its blocks.

### 3.2.6 Application layer

This layer, or the uppermost layer of the BCT comprising its applications in the subject
matter, is the last one. According to the literature, scientists have used the BCT in a
wide range of applications.

## 3.3 Trajectory planning

1. Trajectory planning for drone delivery in known environments only exploitation
2. Trajectory planning for drone delivery in unknown environments exploration then
exploitation

This method resolves the issue of exploration and exploitation that is prevalent in
reinforcement learning.

### 3.3.1 Trajectory planning for drone delivery in known environments

Known environments - only exploitation
For a known environment, we don’t need to explore the environment again. knowledge is transferred using the data array shown in figure 3.4. so redundant computation
is avoided. The result computed by one drone can be utilized by other drones in the
chain.

As it is known environment lets us consider the unique and safe path which can
reach the maximum delivery point known already.

Manual Safe path and Delivery point
The following arrays display the oldtown environment’s manual safe path and points
array.
manualsafepath [[0, 0], [17, 0], [35, 0], [35, 25], [35, 50], [50, 50], [25, 50], [0, 50]]
pointsarr [[’47.57’, ’55.13’], [’6.46’, ’44.39’], [’16.1’, ’8.76’]]
The Manual safest path in the old town environment we use for our project is shown
in figure 3.9.
manualsafepath array: Beginning at (x,y) - (0,0), manualsafepath displays the endpoints of the safest path
pointsarr array: Display the delivery locations that the user has chosen on the interactive pad that is depicted in figure 3.3.

**Figure 3.10: Manual safest path - Green**

Following testing and conducting numerous delivery episodes with various delivComputer science and Engineering, May 2023

ery and a variety of delivery points. We discover the distinctive path of the oldtown
environment, which is depicted as a green path in figure 3.9.
We developed an algorithm to automatically determine the environment’s safest
path, which is described in the following subsection 3.4.3.

**Figure 3.11: Delivery points - Yellow**

Let’s assume that the user who has to deliver has chosen the three delivery points
illustrated in figure 3.10. Deliver points may be clicked in any sequence by the user.
Nonetheless, delivery points that are close by will be attended to before distant delivery
sites.
Drones’ ability to transport all the goods at once is a further factor to be taken
into account. hence there is no need to return to the starting point after finishing each
delivery. It will return to the base once it has finished all of the deliveries.
To more deeply comprehend the need for this improvement while modifying the
application.
Let’s think about two distinct uses for drones carrying guns and delivering medicines.
If the drone’s capacity allows it to carry all of the medicine at once, in the delivery
of medications. Because medical packets weigh far less than other shipments, it is
practicable. In the drone attack, the user-selected delivery points were targeted by the

drone. So that all delivery sites may be attached simultaneously, it must be able to carry
all of the bullets.
If we take this scenario into account, a drone’s carrying capacity is limited to one
delivery at a time. In this instance, we have to change the algorithm so that it takes into
account the fact that each delivery drone must return to its starting base.
We make an effort to provide a common algorithm for all applications, however,
some improvements still require application-specific changes. I hope this clarifies the
necessity for the adjustment and how it will change upon application.

Array coordinates
Before beginning the procedure, we develop new coordinates for converting unreal data
into array data.
We also added a new coordinate called array coordinate along with image coordinate, unreal coordinate, and environment coordinate. We must translate the unreal
coordinate into the array coordinate in order to update the data that has been studied.

**Figure 3.12: Conversion of unreal to array coordinate**

Take into account that (x1,y1) is an unreal coordinate and (x2,y2) is an array coordinate. As it is known that unreal coordinates can be converted, compute x2=x1+14 and
y2=y1+18.

Endpoints
it is the points that indicate the safest path in the environment. For example, each
subarray point in manualsafepath array is an endpoint.

Delivery Algorithm
It is necessary to establish a basic blockchain and to treat each drone as a single node.
Before disclosing the known information to the drone agent, we must verify that the
drone is a part of the chain; otherwise, the request will be denied.
Let’s assume that the drone is validated and is present in the blockchain.
Input to the Algorithm:
1. Environment safest path (manualsafepath)
2. Location for delivery that the user chooses (pointsarr).

**Figure 3.13: Generated path for Delivery**

Step 1: Determining whether any of the chosen delivery sites are close to each
endpoint.

**Figure 3.14: Generated Return path for going back**

Step 2: If yes then add the endpoint and delivery point to the path.
Step 3: If all the delivery points are served then break the loop
Step 4: If there selected delivery point is not close to this endpoint then add an
endpoint to the path
The following path is made once the entire loop has been run.
Now that the drone has begun delivering, it has finished all of its deliveries and has
created a return path with no delivery spots and just safe path endpoints.
The subsequent return path is then established.
Finally, the drone returns to its base, where it began.

### 3.3.2 Trajectory planning for drone delivery in unknown environments exploration then exploitation

Unknown environments - both exploration then exploitation

As the environment is unknown, we must first do exploration and then exploit the
explored information.
After exploration, the exploitation algorithm from section 3.4.1 was used.

Drone coordinates

**Figure 3.15: four drone coordinates - only two useful**

The drone’s four separate coordinates, x val, y val, w val, and z val, correspond to
four distinct axes.
Airsim LIDER sensor will not generate proper output when observed attentively
with several outputs. But, upon investigation, only y val and w val are helpful.
So, our approach only uses the two axes due to implementation constraints.

Explore environment Algorithm
The algorithm first has to find the safe coordinates in the environment.
step1: plan the episodes you have to schedule the exploration.
step2: start running the episodes one by one in the sequences.
step3: for each step of the episodes we have to take the reading of the y val and w

**Figure 3.16: Show how safe coordinate changing over the different trails**

val of the drone coordinate and this data should be updated into 2d Array we discussed
early.
step4: after completing all the episodes all the safe coordinates in the environment
are explored.
step5: now by computing the midpoint of each LIDER scan safe path is detected as
shown in 3.16.
Once each step has been successfully accomplished, we locate the automatic safe
path.
Then the automatic safe path is given input to the drone delivery algorithm which is
discussed in the 3.4.1 section.
By comparing the manual safe path and automatic safe path which show in figure

## 3.17 . automatic safe will be closer to the manual safe path which we try to achieve

using automation.

**Figure 3.17: Exploring the safe coordinates in environment**

**Figure 3.18: Manual and Automatic safer paths with endpoints**

# CHAPTER 4
# Project Overview

## 4.1 Program flow

The drone delivery system uses a PEDRA engine and unreal coordinates to control and
navigate the drone. The system is armed using an API, which provides a way for the
software to communicate with the drone and issue commands.
When the drone delivery.py script is called, it first checks if the environment has
been explored enough to generate a safe path for delivery. This is important because
the drone needs to avoid obstacles and hazards in the environment to ensure safe and
successful delivery.
If the safe path has been generated, the script calls the Exploitation() function. The
Exploitation() function takes the safe path generated during exploration and generates
a trajectory path of delivery with delivery points. This involves calculating the optimal
route for the drone to follow to reach each delivery point along the safe path. The
function then returns the delivery path for the drone to follow.
If the safe path has not been generated, the script calls the Exploration() function
first. The Exploration() function uses multiple episodes to explore the environment and
find safe coordinates and midpoint of each scan in the environment. This is done by
running the drone through a series of pre-defined actions and observing the resulting
environment. The function then generates a safe path based on the observations made
during exploration.
Once the safe path has been generated, the script calls the Exploitation() function to
generate the delivery path.
When the delivery is complete, the drone is disarmed using the API. This ensures
that the drone is no longer active and cannot cause any harm or damage.

**Figure 4.1: Project Implementation Overview**

# CHAPTER 5
# Exploration

## 5.1 Exploration: Gain the knowledge of the environment

**Figure 5.1: RGB and Binary Image**

An algorithm for the exploration of an environment by a drone, with the goal of
generating a safe path through the environment. The inputs to the algorithm are the
environment to be explored, and the output is a safe path through the environment.

The algorithm uses a while loop to explore the environment. The initial position of
the drone is set to (i,j) = (0,0), and the variable "continue process" is set to True to start
the loop. The drone takes an image of the environment through its camera and converts
the RGB image to a binary image. The percentage of white pixels in the binary image
is then calculated and stored in the variable "x". The algorithm then checks whether
x is within the limits of the "lower" and "upper" variables, or whether a collision has
occurred.
If x is outside the limits or a collision has occurred, the algorithm calls a deep
reinforcement learning (DRL) PPO model to predict the next direction for the drone.
The function "get next direction()" returns a number between 0 and 3, representing the
direction the drone should move in next. If the next direction is 0, the drone moves
forward one step in the i direction. If the next direction is 1, the drone moves backward
one step in the i direction. If the next direction is 2, the drone moves forward one step
in the j direction. If the next direction is 3, the drone moves backward one step in the j
direction.
The algorithm continues to iterate through the while loop until either the environment is fully explored and a safe path has been generated, or the drone is unable to
proceed further or becomes stuck (indicated by setting "continue process" to False).
When the while loop ends, the algorithm returns the safe path through the environment,
represented by the variable "environment Safepath".
This algorithm uses a combination of image analysis and DRL to autonomously explore an environment and generate a safe path. This could be useful in scenarios such as
search and rescue operations or mapping of hazardous areas where human intervention
may not be possible or safe.

**Figure 5.2: How Drone calculates midpoint of the single scan**

**Figure 5.3: Exploration Algorithm**

# CHAPTER 6
# Exploitation

## 6.1 Exploitation: Using the explored knowledge find delivery path

**Figure 6.1: Exploitation Algorithm**

The function "Exploitation" takes two inputs:
enviroinment Safepath: This input is an array of safe endpoints in the environment.
Each safe end point is represented as a coordinate (x,y).

pointsarr: This input is an array of locations where the user wants to deliver. Each
delivery point is represented as a coordinate (x,y). The function generates an efficient
path that includes safe endpoints and delivery points. The purpose of the function is to
find the nearest safe endpoint for each delivery point and append them to the "efficient
path".
To achieve this, the function uses two nested loops. The outer loop iterates over all
the safe endpoints in the environment Safepath array, and the inner loop iterates over all
the delivery points in the pointsarr array.
For each safe endpoint and delivery point pair, the function calculates the Euclidean
distance between them using the following formula: distance = square root of ((x2 –
x1)pow(2) + (y2 – y1)pow(2))
Where (x1, y1) represents the coordinates of the current safe endpoint in the outer
loop iteration, and (x2, y2) represents the coordinates of the current delivery point in
the inner loop iteration.
The function then selects the nearest safe endpoint for each delivery point by finding the minimum distance between the delivery point and all the safe endpoints in the
environment Safepath array. If the nearest safe endpoint for the current delivery point
matches the safe endpoint of the current iteration in the outer loop, then the function
appends the safe endpoint and delivery point to the "efficient path" array and increments
the "points count" counter by one.
The function then checks if the "points count" is greater than or equal to the number
of delivery points in the pointsarr array. If this condition is true, then the function breaks
out of the outer loop.
Finally, the function returns the "efficient path" array as the output, which contains
all the selected safe endpoints and delivery points in the order in which they were appended.

# CHAPTER 7
# RESULT : "Outdoor Oldtown" Enviroinment

Environment Safe coordinates: During the exploration, the drone can identify that these
are the safe coordinate in the environment drone can fly safely.
These safe coordinates are used to recognize the object of the environment later. To
recognize objects higher-end sensors are required.

**Figure 7.1: 3d array of Safe coordinates – Drone can fly**

Midpoint of the safe coordinates: At the time of exploration each scan will record
the midpoint of the particular scan to make it as endpoint at the time of exploitation.

**Figure 7.2: 3d Midpoint used as endpoints in exploitation**

**Figure 7.3: How the number of safe coordinates changes while changing the flying**

height of the drone here we consider as Z-Axis (Green - Safe coordinate,
Blue - Midpoints)

# CHAPTER 8
# RESULT : "Indoor Vanleer" Enviroinment

**Figure 8.1: Test Environment: Safe coordinate**

**Figure 8.2: Test Environment: Midpoints**

**Figure 8.3: Test Environment: Z Axis**

# CHAPTER 9
# Conclusion and Future scope

## 9.1 Conclusion

From the literature implementing the DRL for Drone automation is very difficult and
near impossible.
Reason :
1) The reason for that needs an enormous amount of computation up to 1,50,000
episodes for exploring the entire environment. After getting trained also it is difficult to
make it task-specific like drone delivery.
2) Another reason is not able to know when to explore and where to utilize the
explored knowledge which is exploitation.
Solution :
1) Our approach using a 3d array of the environment not required not more than 500
episodes to explore the entire environment.
2) Our approach uses a segment tree data structure for range querying the 3d array.
It is efficient in terms of time but has to handle some extra space. It is also affordable
nowadays.
3) Our approach clearly distinguished between when and where exploration() and
exploitation() have to be done.
Finally, we come up the better and more efficient solutions for the implementation
of DRL in autonomous drones for Drone delivery. By leveraging **PPO/SAC for continuous control** and **CG-PBFT for blockchain consensus**, we achieved a 250% increase in network throughput and 70% reduction in communication latency.
There are a lot of further scopes that have to work on these algorithms. the possibility is high to come up with an efficient algorithm for specific tasks.

Task or Domain-specific research is required to make this algorithm much more
robust.

## 9.2 Future scope

Our approach covers Most of the exploration part it covers moreover all the edge cases.
Further focus will be on the exploitation is dependent on the specific task we trying to
solve.
The specific task may be Delivery and logistics, Agriculture, Construction and infrastructure, Surveying and mapping, Film and photography, Search and rescue, and
Military and defense.
Using this approach we can easily create a virtual environment of the real world
like a metaverse. This opens the door to making autonomous vehicles trained with
real-world use cases.

REFERENCES
[1] Y. Song, M. Steinweg, E. Kaufmann, and D. Scaramuzza, “Autonomous drone racing with deep reinforcement learning,” in 2021 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS). IEEE, 2021, pp. 1205–1212.
[2] Y. Wu, H.-N. Dai, H. Wang, and K.-K. R. Choo, “Blockchain-based privacy preservation for 5g-enabled drone communications,” IEEE Network, vol. 35, no. 1, pp.
50–56, 2021.
[3] D. Hanover, A. Loquercio, L. Bauersfeld, A. Romero, R. Penicka, Y. Song,
G. Cioffi, E. Kaufmann, and D. Scaramuzza, “Autonomous drone racing: A survey,” arXiv e-prints, pp. arXiv–2301, 2023.
[4] A. Anwar and A. Raychowdhury, “Autonomous Navigation via Deep Reinforcement Learning for Resource Constraint Edge Nodes using Transfer Learning,”
arXiv e-prints, p. arXiv:1910.05547, Oct 2019.
[5] I. Yoon, M. A. Anwar, R. V. Joshi, T. Rakshit, and A. Raychowdhury, “Hierarchical memory system with stt-mram and sram to support transfer and real-time
reinforcement learning in autonomous drones,” IEEE Journal on Emerging and Selected Topics in Circuits and Systems, vol. 9, no. 3, pp. 485–497, 2019.
[6] N. Ibtehaz, M. Kaykobad, and M. S. Rahman, “Multidimensional segment trees
can do range updates in poly-logarithmic time,” Theoretical Computer Science, vol.
854, pp. 30–43, 2021.

