# 6.VI. Ethernet switch


## Ethernet switch
* Switch is a `link-layer` device: takes an active role
    * store, forward Ethernet frames
    * examine incoming frame's MAC address, selectively forward frame to one-or-more outgoing links when frame is to be forwarded on segment

* `transparent`: hosts unaware of presence of switches
* `plug-and-play, self-learning`
    * switches do not need to be configured

---

## Switch forwarding table
<img src=imgs/Switch.png>

---
`Question`

How does switch know A' reachable via interface 4, B' via interface 5?

`A`: by switch table, each entry:
* MAC address of host, interface to reach host, time stamp
* looks like a routing table
---

---
`Question`

How are entries created, maintained in switch table?

---

* switch `learns` which hosts can be reached through which interfaces
    
    <img src=imgs/switch_forward.png>

    * when frame received, switch "learns" location of sender = incoming LAN segment
    * records sender/location pair in switch table

    * when frame received at switch:
        1. record incoming link, MAC address of sending host
        2. index switch table using MAC destination address
        3. * if entry found for destination:
                * if destination on segment from which frame arrived -> drop frame  # seldom happen in today
                * else -> forward frame on interface indicated by entry
            * else: flood  # forward on all interfaces except arriving interface
            <img src=imgs/flood.png>

---

## Interconnecting switches

self-learning switches can be connected together:

<img src=imgs/interconnected_switches.png>

---
`Question`

How does ${S_1}$ know to forward frame destinated to G via ${S_4}$ and ${S_3}$

`A`: exactly the same as in single-switch case.

---
## Switches versus Routers

`both are stored-and-forward:`
* routers: network-layer devices
* switches: link-layer devices

`both have forwarding tables:`
* routers: compute tables using routing algorithms, IP addresses
* switches: learn forwarding table using flooding, learning, MAC addresses