# IoT Lab Network Architecture

## Overview

The IoT lab consists of a Raspberry Pi gateway connected to an ESP32 device via serial communication. The gateway exposes a web interface that allows remote control of the ESP32. The firewall is currently set to only allow ssh from lab switch subnet.

## Components

Workstation
Used for firmware flashing, debugging, and SSH access to the Raspberry Pi.

Raspberry Pi Gateway
Runs a Flask web application and acts as the central control node.

ESP32 Microcontroller
Receives commands from the Raspberry Pi via serial and controls hardware components.

Workstation
Used for remote SSH access and documentation.

## Network Layout

University Network
        |
     Ethernet Switch
      |          |
Workstation   Raspberry Pi
                   |
               USB Serial
                   |
                  ESP32

## Security Controls

The Raspberry Pi gateway enforces network security using nftables.

Default firewall policy: DROP

Allowed connections:

SSH from trusted subnet
Flask web interface on port 5000
ICMP for diagnostics

All other inbound traffic is blocked.