# EDEN Project: 2nd Meeting Action Plan

> Complete action plan document for the second meeting

## 📋 Meeting Overview

**Date**: [To be scheduled]  
**Duration**: 1-2 hours  
**Objective**: Present tech stack, assign immediate tasks, and get team started

---

## 🎯 Meeting Objectives

By the end of this meeting, each team member should:
- [ ] Understand the complete tech stack and architecture
- [ ] Know their specific first tasks and deadlines
- [ ] Have access to all necessary resources
- [ ] Understand how their work fits into the bigger picture
- [ ] Know how to communicate and get help

---

## 📋 Meeting Agenda

### 1. Project Overview (15 minutes)
- **Presenter**: Vedant
- **Content**: 
  - Review the "split-brain" architecture
  - Explain tech stack and how components work together
  - Show system flow diagram

### 2. Tech Stack Deep Dive (30 minutes)
- **Presenter**: Vedant
- **Content**: Go through each component from the action plan:
  - Host PC (NVIDIA GPU) + Isaac Sim
  - Jetson Nano 2GB as robot brain
  - ROS 2 communication framework
  - ROS MCP Server as translator
  - Local LLMs (Ollama/phi-3)
  - CAD Software (Fusion 360)

### 3. Team Assignments & Immediate Tasks (45 minutes)
- **Presenter**: Vedant
- **Content**: Present specific tasks for each team member

#### Mechanical & Design Team
- **Dillon (Lead) & William**: GPTTARS analysis and mechanical design
- **Sebastian Dayer**: AI/Mechanical bridge role

#### Electrical & Embedded Systems Team  
- **Juan (Lead) & Krish**: Jetson Nano setup and basic control

#### Software, AI & Simulation Team
- **Andrew (Lead)**: Isaac Sim setup and ROS 2 integration
- **Paavan (Lead)**: ROS MCP Server integration
- **Sebastian Chu**: Senior AI/Software leadership
- **Haren**: Ollama LLM setup and testing

### 4. Resource Distribution (15 minutes)
- **Presenter**: Vedant
- **Content**: Share all the specific links and resources
- **Action**: Send resource links to all team members

### 5. Q&A and Next Steps (15 minutes)
- **Facilitator**: Vedant
- **Content**: 
  - Answer questions about assignments
  - Confirm understanding of tech stack
  - Set up communication channels
  - Schedule first check-ins

---

## 🤖 Team Assignments & Immediate Tasks

### Mechanical & Design Team

#### Dillon (Lead) & William
**Focus**: Create the physical robot chassis, inspired by modular humanoid robots (GPTTARS project)

##### Primary Task
- **Goal**: Lead the mechanical design by analyzing GPTTARS project structure
- **Focus Areas**:
  - Modularity and movement mechanisms
  - Stability and articulation with minimal parts
  - Design principles as base for our robot

##### Action Item
- **Research and present**: Short summary of mechanical principles and design elements from GPTTARS project
- **Focus on**: What aspects (modularity, joint design, movement style) we can adapt or improve upon
- **Resource**: [How to Build Your Own Replica of TARS from Interstellar](https://www.hackster.io/charlesdiaz/how-to-build-your-own-replica-of-tars-from-interstellar-224833#cad)

#### Sebastian Dayer (AI/Mechanical Bridge)
**Unique Role**: Bridging software and hardware

##### AI Task
- **Focus**: On-device computer vision
- **Goal**: On Jetson Nano (once set up by electrical team), run basic object detection model using camera
- **Objective**: Detect common object (cup or person) and print result
- **Resource**: [Jetson AI Fundamentals](https://github.com/dusty-nv/jetson-ai-fundamentals)

##### Mechanical Task
- **Focus**: Work directly with Dillon and William
- **Goal**: Join mechanical team in GPTTARS project analysis
- **Objective**: Provide AI perspective on how AI can leverage specific mechanical designs

---

### ⚡ Electrical & Embedded Systems Team

#### Juan (Lead) & Krish
**Focus**: Power up the Jetson Nano and connect essential electronics

##### Primary Task
- **Goal**: Get Jetson Nano 2GB running and control something simple
- **Responsibility**: Robot's entire electrical system

##### Action Item
- **Step 1**: Follow official "Getting Started" guide for Jetson Nano 2GB
- **Step 2**: Successfully boot the OS and run "Hello AI World" example
- **Step 3**: Write simple Python script to blink LED using GPIO pins
- **Resource**: [Jetson Nano 2GB Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)

---

### 💻 Software, AI & Simulation Team

#### Andrew (Lead, ROS/ML) & Paavan (Lead, ROS/Software Arch)
**Focus**: Establish ROS 2 and simulation infrastructure

##### Andrew's Action Item
- **Priority**: Isaac Sim setup
- **Goal**: Install NVIDIA Isaac Sim and run basic "Hello World" example
- **Step 1**: Install Isaac Sim on host machine
- **Step 2**: Import simple robot model (TurtleBot)
- **Step 3**: Control it using ROS 2 messages
- **Resource**: [Isaac Sim Installation](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_workstation.html)

##### Paavan's Action Item
- **Priority**: ROS MCP Server integration
- **Goal**: Clone ros-mcp-server repository and understand API
- **Step 1**: Clone `ros-mcp-server` repository
- **Step 2**: Get it running and understand its API
- **Step 3**: Test by sending simple JSON command to see ROS 2 topic translation
- **Resource**: [ROS MCP Server GitHub](https://github.com/robotmcp/ros-mcp-server)

#### Haren (AI/Software)
- **Focus**: Learn AI and software stack fundamentals
- **Goal**: Assist Andrew and Paavan while learning the stack
- **Action Item**: Set up local LLM on machine using Ollama
- **Step 1**: Install Ollama
- **Step 2**: Run phi-3 model
- **Step 3**: Experiment with prompts to understand how it responds
- **Resource**: [Ollama](https://ollama.ai/)

---

## 📊 Project Lead & Research

### Vedant
**Role**: Oversee project integration, manage timeline, lead research on novel cognition layer

#### Action Items
- **Create**: Shared GitHub repository
- **Set up**: Discord channels
- **Schedule**: First sub-team check-ins
- **Begin**: Literature review on reinforcement learning frameworks compatible with Isaac Sim

---

## 🔧 Tech Stack Explanation

### 🧠 Split-Brain Architecture Overview

#### Host PC (NVIDIA GPU) + Isaac Sim
- **Role**: High-level AI, simulation, and complex processing
- **Components**: 
  - NVIDIA GPU for AI model inference
  - Isaac Sim for robot simulation and testing
  - ROS 2 for communication framework
- **Purpose**: Run sophisticated AI models and simulate robot behavior before deployment

#### Jetson Nano 2GB as Robot Brain
- **Role**: On-robot real-time operations and control
- **Components**:
  - On-device computer vision
  - Real-time sensor processing
  - Basic AI inference
- **Purpose**: Handle immediate robot control and sensor data processing

### 🔄 System Flow

#### 1. User Input → LLM Processing
- **Input**: Natural language commands from user
- **Processing**: Local LLM (Ollama/phi-3) processes command
- **Output**: Structured robot commands

#### 2. LLM → ROS MCP Server Translation
- **Input**: Structured commands from LLM
- **Processing**: ROS MCP Server translates to ROS 2 messages
- **Output**: ROS 2 topics and services

#### 3. ROS 2 → Isaac Sim Simulation
- **Input**: ROS 2 messages from MCP Server
- **Processing**: Isaac Sim simulates robot behavior
- **Output**: Simulated robot actions and sensor data

#### 4. Simulation → Real Robot Deployment
- **Input**: Validated commands from simulation
- **Processing**: Commands sent to Jetson Nano
- **Output**: Real robot movement and actions

### 🔧 Component Interactions

#### Communication Flow
```
User → LLM → ROS MCP Server → ROS 2 → Isaac Sim → Jetson Nano → Robot
```

#### Key Components
1. **Local LLM (Ollama/phi-3)**: Natural language processing
2. **ROS MCP Server**: Command translation and API
3. **ROS 2**: Communication framework
4. **Isaac Sim**: Robot simulation and testing
5. **Jetson Nano**: On-robot control and AI
6. **Fusion 360**: CAD design and mechanical modeling

#### Data Flow
- **Commands**: Flow from user to robot
- **Sensor Data**: Flow from robot to simulation
- **Feedback**: Continuous loop between simulation and real robot

### 🎯 Why This Architecture?

#### Benefits
- **Simulation First**: Test everything in Isaac Sim before real deployment
- **Local Processing**: No cloud dependency, works offline
- **Modular Design**: Each component can be developed independently
- **Real-time Control**: Jetson Nano handles immediate robot needs
- **AI Integration**: LLM provides natural language interface

#### Development Strategy
- **Parallel Development**: Teams can work on different components simultaneously
- **Integration Testing**: Isaac Sim provides safe testing environment
- **Incremental Progress**: Each component can be validated independently

---

## 📚 Resource Links

### 🤖 Mechanical & Design Team

#### GPTTARS Project Analysis
- **Primary Resource**: [How to Build Your Own Replica of TARS from Interstellar](https://www.hackster.io/charlesdiaz/how-to-build-your-own-replica-of-tars-from-interstellar-224833#cad)
- **Focus**: Modularity, movement mechanisms, stability, minimal parts

### ⚡ Electrical & Embedded Systems Team

#### Jetson Nano 2GB Setup
- **Primary Resource**: [Jetson Nano 2GB Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)
- **Focus**: OS boot, "Hello AI World" example, GPIO control

#### AI Fundamentals
- **Resource**: [Jetson AI Fundamentals](https://github.com/dusty-nv/jetson-ai-fundamentals)
- **Focus**: Computer vision, object detection, on-device AI

### 💻 Software, AI & Simulation Team

#### Isaac Sim Setup
- **Primary Resource**: [Isaac Sim Installation](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_workstation.html)
- **Focus**: Installation, basic robot control, ROS 2 integration

#### ROS MCP Server
- **Primary Resource**: [ROS MCP Server GitHub](https://github.com/robotmcp/ros-mcp-server)
- **Focus**: Clone repository, understand API, test JSON commands

#### Local LLM Setup
- **Primary Resource**: [Ollama](https://ollama.ai/)
- **Focus**: Install Ollama, run phi-3 model, test prompts

### 📚 Additional Resources

#### ROS 2 Documentation
- **Resource**: [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- **Focus**: Basic ROS 2 concepts, nodes, topics, services

#### NVIDIA Isaac Sim Documentation
- **Resource**: [Isaac Sim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/)
- **Focus**: Simulation setup, robot models, physics

#### Fusion 360 (CAD Software)
- **Resource**: [Fusion 360](https://www.autodesk.com/products/fusion-360)
- **Focus**: CAD design, 3D modeling, mechanical design

---

## 🎯 Quick Start Checklist

### For Mechanical Team
- [ ] Access GPTTARS project link
- [ ] Download CAD files and documentation
- [ ] Begin analysis of modular design principles

### For Electrical Team
- [ ] Access Jetson Nano getting started guide
- [ ] Download required software and drivers
- [ ] Begin hardware setup process

### For Software Team
- [ ] Access Isaac Sim installation guide
- [ ] Access ROS MCP Server repository
- [ ] Access Ollama installation page
- [ ] Begin software environment setup

---

## 🚀 Getting Started

### For Each Team
1. **Mechanical**: Focus on GPTTARS analysis and CAD design
2. **Electrical**: Get Jetson Nano running and controllable
3. **Software**: Set up Isaac Sim, ROS MCP Server, and Ollama
4. **Integration**: Connect all components through ROS 2

### Success Metrics
- [ ] Jetson Nano running "Hello AI World"
- [ ] Isaac Sim controlling simulated robot
- [ ] ROS MCP Server translating LLM commands
- [ ] Ollama phi-3 model responding to prompts
- [ ] GPTTARS analysis complete with design principles

---

*This architecture enables rapid development and testing while maintaining real-time robot control capabilities*
