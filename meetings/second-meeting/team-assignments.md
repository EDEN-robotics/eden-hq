# EDEN Project: Team Assignments for 2nd Meeting

> Direct assignments from the action plan document

## 🤖 Mechanical & Design Team

### Dillon (Lead) & William
**Focus**: Create the physical robot chassis, inspired by modular humanoid robots (GPTTARS project)

#### Primary Task
- **Goal**: Lead the mechanical design by analyzing GPTTARS project structure
- **Focus Areas**:
  - Modularity and movement mechanisms
  - Stability and articulation with minimal parts
  - Design principles as base for our robot

#### Action Item
- **Research and present**: Short summary of mechanical principles and design elements from GPTTARS project
- **Focus on**: What aspects (modularity, joint design, movement style) we can adapt or improve upon
- **Resource**: [How to Build Your Own Replica of TARS from Interstellar](https://www.hackster.io/charlesdiaz/how-to-build-your-own-replica-of-tars-from-interstellar-224833#cad)

---

## ⚡ Electrical & Embedded Systems Team

### Juan (Lead) & Krish
**Focus**: Power up the Jetson Nano and connect essential electronics

#### Primary Task
- **Goal**: Get Jetson Nano 2GB running and control something simple
- **Responsibility**: Robot's entire electrical system

#### Action Item
- **Step 1**: Follow official "Getting Started" guide for Jetson Nano 2GB
- **Step 2**: Successfully boot the OS and run "Hello AI World" example
- **Step 3**: Write simple Python script to blink LED using GPIO pins
- **Resource**: [Jetson Nano 2GB Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)

---

## 💻 Software, AI & Simulation Team

### Andrew (Lead, ROS/ML) & Paavan (Lead, ROS/Software Arch)
**Focus**: Establish ROS 2 and simulation infrastructure

#### Andrew's Action Item
- **Priority**: Isaac Sim setup
- **Goal**: Install NVIDIA Isaac Sim and run basic "Hello World" example
- **Step 1**: Install Isaac Sim on host machine
- **Step 2**: Import simple robot model (TurtleBot)
- **Step 3**: Control it using ROS 2 messages
- **Resource**: [Isaac Sim Installation](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_workstation.html)

#### Paavan's Action Item
- **Priority**: ROS MCP Server integration
- **Goal**: Clone ros-mcp-server repository and understand API
- **Step 1**: Clone `ros-mcp-server` repository
- **Step 2**: Get it running and understand its API
- **Step 3**: Test by sending simple JSON command to see ROS 2 topic translation
- **Resource**: [ROS MCP Server GitHub](https://github.com/robotmcp/ros-mcp-server)

### Sebastian Dayer (AI/Mechanical Bridge) & Haren (AI/Software)

#### Sebastian Dayer's Tasks
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

#### Haren's Task
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
