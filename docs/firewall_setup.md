# Raspberry Pi Gateway Firewall Configuration

## Objective

Implement a host-based firewall on the Raspberry Pi gateway to restrict inbound network access and enforce a default-deny security policy for the IoT lab environment.

The firewall ensures that only trusted devices on the lab network can access management and application services.

---

## Network Environment

Raspberry Pi IP address  
150.201.166.11

Workstation IP address  
150.201.167.242

Subnet mask  
255.255.254.0

Network range  
150.201.166.0 – 150.201.167.255

Gateway  
150.201.167.254

The subnet /23 allows communication between devices in the range above.

---

## Firewall Strategy

The firewall uses nftables with a default deny inbound policy.

Only explicitly permitted traffic is allowed.

Allowed traffic:

Loopback traffic (lo) for local system communication

Established and related connections using connection tracking

ICMP echo requests from the trusted lab subnet for diagnostics

SSH access on port 22 from the trusted subnet

Flask gateway web interface on port 5000 from the trusted subnet

All other inbound traffic is dropped.

---

## Final nftables Configuration

Location  
/etc/nftables.conf

table inet filter {

    # Trusted lab network allowed to access the gateway
    set trusted_subnet {
        type ipv4_addr
        flags interval;
        elements = { 150.201.166.0/23 }
    }

    chain input {
        type filter hook input priority 0;
        policy drop;

        ct state invalid drop;
        iif "lo" accept;
        ct state established,related accept;

        ip saddr @trusted_subnet icmp type echo-request accept;
        ip saddr @trusted_subnet tcp dport { 22, 5000 } accept;
    }
}
---

## Validation Steps

The firewall configuration was validated using the following commands:

sudo nft -c -f /etc/nftables.conf

sudo systemctl restart nftables

sudo nft list ruleset

sudo ss -tuln

SSH connectivity from the workstation was confirmed after the firewall was applied.

Access to the Flask gateway interface on port 5000 was also verified.

---

## Security Rationale

The gateway enforces a default deny inbound policy, which follows the principle of least privilege.

Only specific trusted network ranges are allowed to access management and application services.

Stateful packet filtering ensures that legitimate traffic associated with existing connections is permitted while blocking unsolicited inbound connections.

This approach reduces the attack surface of the gateway and prevents unauthorized access to IoT devices connected through the Raspberry Pi.

##Notes
ESP32 communication is local over USB (not affected by firewall rules)