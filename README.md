# **Sentinel: Secure IoT Remote Gateway**

### **Project Overview**
Sentinel is a hardened, containerized gateway designed for the remote management of autonomous IoT edge nodes. Developed as the foundational infrastructure for a two-phase research thesis, this system facilitates secure communication between a management workstation and ESP32-based rovers within a laboratory environment.

The project focuses on implementing a Zero-Trust network model, ensuring that the control plane is isolated from the broader network while maintaining high-performance serial throughput for real-time hardware commands.

---

### **System Architecture**
The platform utilizes a three-tier architecture to maintain hardware isolation:

1. **Management Tier:** A workstation interface utilizing a web-based dashboard to issue commands.
2. **Gateway Tier (Sentinel):** A Raspberry Pi 4 running a Dockerized Flask application. This layer handles authentication, logging, and protocol translation.
3. **Edge Tier:** ESP32-WROVER-DEV microcontrollers connected via USB/Serial. These nodes execute physical movement and sensor data collection.

---

### **Key Implementation Details**

**Serial Handshake & Stability**
A significant challenge in the development phase was the ESP32’s hardware auto-reset feature. Standard serial initialization toggles the DTR (Data Terminal Ready) and RTS (Request to Send) lines, which causes the microcontroller to reboot. Sentinel implements a specific handshake logic in the Python backend to suppress these signals, ensuring that the connection remains persistent and the rover's state is preserved during remote sessions.

**Zero-Trust Networking**
To secure the gateway in a shared university network environment, Sentinel employs a "Default-Deny" inbound policy using `nftables`. The firewall is configured to ignore all traffic except for explicitly defined management subnets. This ensures that the gateway and its connected rovers remain invisible to unauthorized devices on the local network.

**Concurrent Data Integrity**
The system tracks every command, response, and network latency in a centralized telemetry log. To prevent data corruption during high-frequency operations, Sentinel utilizes the `fcntl` library to implement advisory record locking, ensuring thread-safe writes to the persistent CSV logs.

---

### **Tech Stack**
* **Backend:** Python 3, Flask, Docker
* **Security:** nftables, fcntl
* **Hardware Interface:** PySerial
* **Edge Hardware:** Raspberry Pi 4, ESP32-WROVER-DEV

---

### **Installation and Deployment**

**Prerequisites**
* Docker and Docker Compose installed on the host machine.
* Target hardware connected to `/dev/ttyUSB0`.

**Deployment Steps**

### **Installation and Deployment**

1. **Clone the Repository**
```bash
git clone [https://github.com/ctarique/iot-lab-remote-gateway.git](https://github.com/ctarique/iot-lab-remote-gateway.git)
cd iot-lab-remote-gateway
```
2. **Launch the Gateway**
```bash
docker-compose up -d --build
```
3. **Access the Interface**
```bash
The dashboard is available at: http://<gateway-ip>:5000
```
### **Repository Structure**
*   **/firmware**: C++ source code for the ESP32 edge nodes.
*   **/templates**: Frontend dashboard and UI assets.
*   **/docs**: Security specifications and network diagrams.
*   **app.py**: Primary gateway logic and serial management.

---

### **Academic Context**
This repository covers **Thesis I: Secure Infrastructure**. The established framework will serve as the communication backbone for **Thesis II**, which focuses on the deployment of autonomous navigation and computer vision algorithms on the edge nodes.

**Author:** Tarique Chowdhury  
**License:** MIT
