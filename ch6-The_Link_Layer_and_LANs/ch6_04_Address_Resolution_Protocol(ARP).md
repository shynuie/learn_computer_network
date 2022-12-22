# 6.IV. Address Resolution Protocol (ARP)

## MAC address

* 32-bit IP address:
    * network-layer address for interface
    * used for layer 3 (network layer) forwarding
    * e.g.,: 128.119.40.136

* MAC(or LAN or physical or Ethernet) address:
    * function: used "locally" to get frame from one interface to another physically-connected interface(same subnet, in IP-addressing sense)
    * 48-bit (6 * 2 * 4 bit) MAC address (for most LANs) burned in NIC ROM, also sometimes software settable
    * usually used in link-layer
    * e.g.: 1A-2F-BB-76-09-AD
    * usually the first three bytes represents manufacture, last three bytes represents the product serial ID.
    * MAC address allocation administered by IEEE
    * manufacturer buys portion of MAC address space

## Address resolution protocol (ARP)
---
`Question`
How to determine interface's MAC address, knowing its IP address?

---
* assumption: nodes in a same subnet (LAN);
* `ARP table`: each IP node (host, router) on LAN has table;
    * IP/MAC address mapping for some LAN nodes: <IP address; MAC address; TTL>
    * TTL (Time to live): time after which address mapping will be forgotten(typically 20 min)

* Example: A wants to send datagram to B
    * Assume B's MAC address not in A's ARP table
    * Steps:
        1. A broadcasts ARP query, containing B's IP addr
            * dest MAC address = `FF-FF-FF-FF-FF-FF` (broadcasting)
            * all nodes on LAN receive ARP query

            <img src=imgs/ARP_query1.png>
        2. B reply
            <img src=imgs/ARP_query2.png>
        3. A update ARP table
            <img src=imgs/ARP_query3.png>