# Research Journal: Sentinel Gateway Project

## [ENTRY 01] Foundational Milestones & Architecture (March 2026)
**Project Phase:** Phase 1: Infrastructure & Hardening

### Daily Objective
Establish the physical and logical "Zero-Trust" baseline for the Sentinel Gateway.

### Experimental Log
- **Sentinel Identity:** Hardened Raspberry Pi by disabling password-based SSH and enforcing **Ed25519 cryptographic keys**.
- **Surface Reduction:** Physically disabled WiFi/BT on ESP32-CAM.
- **Firewall:** Initialized `nftables` with a "Drop All" default policy.
- **Air-Gap Protocol:** Formulated the "Air-Gap Courier" workflow for secure code deployment via physical media.

---

## [ENTRY 02] Hardware Resilience & Concurrency (April 8, 2026)
**Project Phase:** Phase 1.5: Stability & Logic Hardening

### Daily Objective
Resolve environment-specific deployment errors and ensure thread-safe hardware communication.

### Technical Challenges & Resolutions
| Issue | Root Cause | Resolution |
| :--- | :--- | :--- |
| **Docker Failure** | `iptables` dependency in air-gap | Set `"iptables": false` in `daemon.json` |
| **Kernel Error -32** | USB 2.0 Power Sag (500mA) | Migrated to **USB 3.0 Blue Port (900mA)** |
| **Buffer Scrambling**| Race conditions on serial port | Implemented `threading.Lock()` (Mutex) |

### Results & Artifacts
- **Validation:** 100% data integrity achieved across 10 simultaneous threads.
- **Proof:** ESP32-CAM returned `LED_ON_OK` responses with no stalls.

---

## [ENTRY 03] Multi-Endpoint Identity & Repository Sanitization (April 13, 2026)
**Project Phase:** Phase 1: Infrastructure & Hardening

### Daily Objective
Establish unique cryptographic identities for management endpoints and implement a sanitization workflow for secure version control.

### Experimental Log
- **Identity Hardening:** Generated and deployed unique **Ed25519** key pairs for both the M1 MacBook Pro and the Windows workstation. 
- **SSH Lockdown:** Successfully disabled password-based authentication. Identified and neutralized a configuration override in `/etc/ssh/sshd_config.d/50-cloud-init.conf` that was permitting password fallbacks.
- **Client Automation:** Configured `~/.ssh/config` on both machines to map custom identity files and utilized the macOS Keychain (`UseKeychain yes`) for frictionless, passphrase-protected entry.
- **Repository Sanitization:** Implemented a `.env` / `.env.example` architecture to decouple sensitive lab infrastructure data (SEMO IP ranges and administrative credentials) from the GitHub-hosted codebase.

### Technical Challenges & Resolutions
| Issue | Root Cause | Resolution |
| :--- | :--- | :--- |
| **SSH Timeout (Mac)** | Routing conflict in dual-homed setup | Manually assigned static IP **150.201.166.20** to Ethernet adapter; left gateway blank to isolate traffic. |
| **Auth Persistence** | `cloud-init` drop-in configuration | Modified `50-cloud-init.conf` to explicitly set `PasswordAuthentication no`. |
| **Git Push Rejection** | Remote/Local branch divergence | Performed a `git pull` to integrate remote changes (README/License) before finalizing the push. |