# Project Sentinel: Zero-Trust Edge Gateway Architecture

### **Project Overview**
Sentinel is a hardened, zero-trust edge gateway designed to secure Cyber-Physical Systems (CPS) within a remote IoT laboratory. Operating within a highly restrictive university enterprise network, this architecture establishes an isolated command-and-control boundary between a shared student sandbox and autonomous edge nodes. 

This repository houses **Phase I: Secure Infrastructure**, focusing on identity-based access controls, cryptographic lockouts, and network micro-segmentation.

---

### **Hardware Topology: The Dual-Zone Boundary**
To prevent unauthorized lateral movement and secure the flashing process, the physical architecture is strictly divided into two distinct zones connected via a single ethernet switch:

#### **Zone 1: The Student Sandbox**
* **Shared Enterprise Workstation (Windows):** Students authenticate via enterprise AD to access this machine remotely.
* **Secondary ESP32 Hub:** Connected directly to the workstation via USB. Students use the Arduino IDE to safely compile and flash secondary microcontrollers without ever touching the primary infrastructure.

#### **Zone 2: The Sentinel Boundary**
* **The Gateway (Raspberry Pi):** The core routing and security layer. It hosts the Flask web portal that students use to interact with the physical hardware.
* **Primary ESP32 Controller:** Connected to the Pi via secure USB serial. 
* **Autonomous Edge Nodes:** The primary ESP32 utilizes an ESP-NOW (MAC-to-MAC) wireless bridge to communicate with autonomous 3D-printed cars navigating a physical smart-TV obstacle course.

---

### **Security & Access Control Constraints**
Because the gateway operates in a shared enterprise environment, it employs a strict "Default-Deny" inbound policy and identity-based access controls.

* **Network Micro-segmentation:** Inbound traffic is regulated via `nftables`. SSH access is strictly constrained, and only explicitly defined management subnets can hit the Flask web UI.
* **Zero-Trust Identity Enforcement (Current Implementation):** Transitioning away from IP-based micro-segmentation, the gateway employs an **SSH Cryptographic Lockout**. Password authentication is completely disabled. Access to the Raspberry Pi is exclusively restricted to an Ed25519 key pair stored securely on the administrative profile of the Zone 1 workstation.
* **Interaction Model:** Students cannot directly flash or SSH into the Sentinel Boundary. All interaction with the autonomous cars occurs strictly through the Pi’s containerized Flask web portal.

---

### **Tech Stack**
* **Security & Infrastructure:** Linux (`nftables`), Ed25519 Cryptography, Docker
* **Backend Gateway:** Python 3, Flask, PySerial, `fcntl` (Thread-safe concurrent logging)
* **Hardware & Wireless:** Raspberry Pi, ESP32, ESP-NOW protocol

---

### **Roadmap: Phase II**
This secure gateway serves as the foundational infrastructure for Phase II threat detection capabilities. Upcoming developments include implementing **eBPF (Extended Berkeley Packet Filter) kernel hooks** and **AI-driven anomaly detection** directly on the Raspberry Pi to monitor and mitigate runtime threats targeting the edge nodes.

**Author:** Tarique Chowdhury  
**License:** MIT
