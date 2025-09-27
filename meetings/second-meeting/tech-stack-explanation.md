# EDEN Project: Tech Stack Explanation

> The "split-brain" architecture and system flow from the action plan document

## 🧠 Split-Brain Architecture Overview

### Host PC (NVIDIA GPU) + Isaac Sim
- **Role**: High-level AI, simulation, and complex processing
- **Components**: 
  - NVIDIA GPU for AI model inference
  - Isaac Sim for robot simulation and testing
  - ROS 2 for communication framework
- **Purpose**: Run sophisticated AI models and simulate robot behavior before deployment

### Jetson Nano 2GB as Robot Brain
- **Role**: On-robot real-time operations and control
- **Components**:
  - On-device computer vision
  - Real-time sensor processing
  - Basic AI inference
- **Purpose**: Handle immediate robot control and sensor data processing

---

## 🔄 System Flow

### 1. User Input → LLM Processing
- **Input**: Natural language commands from user
- **Processing**: Local LLM (Ollama/phi-3) processes command
- **Output**: Structured robot commands

### 2. LLM → ROS MCP Server Translation
- **Input**: Structured commands from LLM
- **Processing**: ROS MCP Server translates to ROS 2 messages
- **Output**: ROS 2 topics and services

### 3. ROS 2 → Isaac Sim Simulation
- **Input**: ROS 2 messages from MCP Server
- **Processing**: Isaac Sim simulates robot behavior
- **Output**: Simulated robot actions and sensor data

### 4. Simulation → Real Robot Deployment
- **Input**: Validated commands from simulation
- **Processing**: Commands sent to Jetson Nano
- **Output**: Real robot movement and actions

---

## 🔧 Component Interactions

### Communication Flow
```
User → LLM → ROS MCP Server → ROS 2 → Isaac Sim → Jetson Nano → Robot
```

### Key Components
1. **Local LLM (Ollama/phi-3)**: Natural language processing
2. **ROS MCP Server**: Command translation and API
3. **ROS 2**: Communication framework
4. **Isaac Sim**: Robot simulation and testing
5. **Jetson Nano**: On-robot control and AI
6. **Fusion 360**: CAD design and mechanical modeling

### Data Flow
- **Commands**: Flow from user to robot
- **Sensor Data**: Flow from robot to simulation
- **Feedback**: Continuous loop between simulation and real robot

---

## 🎯 Why This Architecture?

### Benefits
- **Simulation First**: Test everything in Isaac Sim before real deployment
- **Local Processing**: No cloud dependency, works offline
- **Modular Design**: Each component can be developed independently
- **Real-time Control**: Jetson Nano handles immediate robot needs
- **AI Integration**: LLM provides natural language interface

### Development Strategy
- **Parallel Development**: Teams can work on different components simultaneously
- **Integration Testing**: Isaac Sim provides safe testing environment
- **Incremental Progress**: Each component can be validated independently

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
