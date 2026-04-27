Browser (via SEMO VPN & Bastion Host)
   |
   | HTTP / Web Interface
   |
Bare-Metal Flask Gateway (Raspberry Pi)
   |                                  |
   | Serial (USB /dev/ttyUSB0)        | Private Wi-Fi AP (Sentinel_Vision)
   |                                  |
ESP32 Hub Bridge                      | HTTP Video Stream
   |                                  |
   +-------- (Encrypted ESP-NOW) -----+
                      |
          Autonomous ESP32 Vehicles
                      |
               Sensors + Camera