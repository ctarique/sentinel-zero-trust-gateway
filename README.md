# Project Sentinel: Zero-Trust Edge Gateway Architecture

```mermaid
flowchart TD
    %% Global Apple-Engineering Styling
    classDef layer fill:#ffffff,stroke:#d2d2d7,stroke-width:1px,color:#1d1d1f,font-family:sans-serif;
    classDef secure fill:#ffffff,stroke:#0071e3,stroke-width:2px,color:#0071e3,rx:15,ry:15;
    classDef critical fill:#1d1d1f,stroke:#1d1d1f,color:#ffffff,rx:10,ry:10;
    classDef soft fill:#f5f5f7,stroke:#d2d2d7,color:#1d1d1f,rx:10,ry:10;
    classDef deployment fill:#ffffff,stroke:#34c759,stroke-width:2px,color:#34c759,stroke-dasharray: 5 5;

    subgraph Management ["I. THE TRUSTED PERIMETER (Identity & Deployment)"]
        direction LR
        Admin["💻 Authorized Workstation<br/>(MacBook / Windows)"]:::soft
        Auth["🔑 Ed25519 Signatures<br/>(MFA Access)"]:::secure
        Dev["📦 Air-Gap Courier<br/>(Sanitized Artifacts)"]:::deployment
    end

    subgraph Network ["II. THE NETWORK CHOKEPOINT (Infrastructure)"]
        direction TB
        VPN{{"🌐 SEMO Student VPN<br/>(SSO Gateway)"}}:::secure
        Bastion["🖥️ Windows RDP Host<br/>(Whitelisted Bastion)"]:::soft
        FW["🛡️ nftables Layer 2 HLAC<br/>(Default-Deny Policy)"]:::secure
    end

    subgraph Gateway ["III. THE SENTINEL CORE (Raspberry Pi 4)"]
        direction TB
        Daemon["🐍 sentinel_daemon.py<br/>(Bare-Metal systemd)"]:::soft
        
        subgraph Kernel ["K-SPACE OBSERVABILITY"]
            direction LR
            eBPF["🔍 eBPF Syscall Hooks<br/>(Phase 2)"]:::secure
            AI["🧠 AI Threat Inference<br/>(Phase 3)"]:::secure
        end

        subgraph Environment ["VISION & ACCESS"]
            direction LR
            AP["📡 Private Video AP<br/>(WPA2 Encrypted)"]:::soft
            CV["👁️ OpenCV Lane Analytics<br/>(Feedback Loop)"]:::soft
        end
    end

    subgraph Physical ["IV. THE CPS ENCLAVE (Hardwired Air-Gap)"]
        direction TB
        Hub["🔌 ESP32 Hub Bridge<br/>(D0WDQ6)"]:::critical
        
        subgraph Hardware ["WIRELESS EDGE"]
            direction LR
            TV["📺 Dynamic TV Track<br/>& Mission Control"]:::secure
            Edge["🚗 ESP32 Edge Car<br/>(WROVER-DEV)"]:::critical
        end
    end

    %% --- THE UNBREAKABLE PIPELINE ---
    Admin & Auth --- VPN
    VPN --- Bastion
    Dev -. "Reverse SCP Deployment" .-> Bastion
    Bastion -- "Whitelisted MAC/IP" --- FW
    FW --- Daemon
    Daemon -- "Serial Syscalls" --- eBPF
    eBPF -- "USB Serial (/dev/ttyUSB0)" --- Hub
    eBPF --- AI
    AI -- "Kill Switch Signal" --> Daemon
    Hub -. "Encrypted ESP-NOW" .-> Edge
    Edge -- "HTTP Video (wlan0)" --> AP
    AP -- "Telemetry JSON" --> Daemon
    TV -. "Optical Data" .-> Edge
    TV -- "Port 5000 / Web UI" --> AP

    class Management,Network,Gateway,Physical layer;

    Project Overview

Sentinel is a hardened, zero-trust edge gateway designed to secure Cyber-Physical Systems (CPS) within a remote IoT laboratory. Operating within a highly restrictive university enterprise network, this architecture establishes an isolated command-and-control boundary between a shared student sandbox and autonomous edge nodes.

This repository houses the Gateway Infrastructure, focusing on identity-based access controls, cryptographic lockouts, network micro-segmentation, and bare-metal service routing.

Hardware Topology: The Dual-Zone Boundary

To prevent unauthorized lateral movement and secure the flashing process, the physical architecture is strictly divided into two distinct zones connected via a single ethernet switch:

Zone 1: The Student Sandbox

Shared Enterprise Workstation (Windows): Students authenticate via enterprise AD to access this machine remotely.

Secondary ESP32 Hub: Connected directly to the workstation via USB. Students use the Arduino IDE to safely compile and flash secondary microcontrollers without ever touching the primary infrastructure.

Zone 2: The Sentinel Boundary

The Gateway (Raspberry Pi): The core routing and security layer. It hosts the Python Flask web portal (located in /gateway) that operates natively on bare-metal via systemd (see sentinel.service.template) to ensure uninterrupted host-level observability for Phase II eBPF integration. It features a "Digital Twin" JSON Lane Builder to visually map physical tracks and render real-time vehicle telemetry.

Primary ESP32 Controller (Hub): Connected to the Pi via secure USB serial on /dev/ttyUSB0.

Mission Control Smart TV: Acts as the physical visual boundary for the vehicles and connects exclusively to the isolated Gateway AP to display the Zero-Trust dashboard.

Autonomous Edge Nodes: The vehicles utilize a Split-Channel model: an encrypted ESP-NOW wireless bridge for low-latency control commands and a private, isolated Gateway-hosted Access Point (Sentinel_Vision) for high-bandwidth video ingestion.

Security & Access Control Constraints

Because the gateway operates in a shared enterprise environment, it employs a strict "Default-Deny" inbound policy and identity-based access controls.

Network Micro-segmentation (Tiered HLAC): Inbound traffic is regulated via nftables (see docs/firewall_setup.md). SSH access is strictly constrained to authorized administrators, while the Smart TV is whitelisted strictly for Port 5000 to access the web UI.

Zero-Trust Identity Enforcement: Transitioning away from IP-based micro-segmentation, the gateway employs an SSH Cryptographic Lockout. Password authentication is completely disabled. Access to the Raspberry Pi is exclusively restricted to Ed25519 key pairs stored securely on the administrative profiles of authorized management workstations.

Interaction Model: Students cannot directly flash or SSH into the Sentinel Boundary. All interaction with the autonomous cars occurs strictly through the Pi’s bare-metal Flask web portal.

Remote Access: Off-campus management is architected to utilize the existing university VPN and a designated Windows Bastion Host to ensure the gateway remains shielded from the public internet.

Tech Stack

Security & Infrastructure: Linux (nftables), Ed25519 Cryptography, systemd.

Backend Gateway: Python 3, Flask, PySerial, JSON Parsing, fcntl (Thread-safe concurrent logging).

Hardware & Wireless: Raspberry Pi 4, ESP32, ESP-NOW (CCMP Encrypted), hostapd / dnsmasq (Private AP).

Roadmap: Phase II

This secure gateway serves as the foundational infrastructure for Phase II threat detection capabilities. Upcoming developments include implementing eBPF (Extended Berkeley Packet Filter) kernel hooks and AI-driven anomaly detection directly on the Raspberry Pi to monitor and mitigate runtime threats targeting the edge nodes.

Author: Tarique Chowdhury

License: MIT