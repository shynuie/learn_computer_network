# 6.V. Ethernet

"dominant" wired LAN technology:
* first widely used LAN technology
* simpler, cheap
* kept up with speed rate: 10 Mbps - 400 Gbps
* single chip, multiple speeds (e.g., Broadcom BCM5761)

## Ethernet

* `bus`: popular through mid 90s
    * all nodes in same collision domain (can collide with each other)

* `switched`: prevails today
    * active link-layer 2 switch in center
    * each "spoke" runs a (separate) Ethernet protocol (nodes do not collide with each other)

## Ethernet frame structure

<img src=imgs/Ethernet_frame_structure.png>

| 8 bytes | 6 bytes | 6 bytes | 2 bytes | 46~1500 bytes | 4 bytes |

* The address in frame header is MAC address
* type refers to the protocol type of upper/network layer
    * 0800: IPv4
    * ARP

* `preamble:`
    * used to synchronize receiver, sender clock rates
    * 7 bytes of 10101010 followed by one byte of 10101011

* `addresses:` 6-byte source, destination `MAC address`
    * if adapter receives frame with matching destination address, or with broadcast address (e.g., ARP packet), it passes data in frame to network layer protocol
    * otherwise adapter discards frame

* `type`: indicates higher layer protocol
    * mostly IP but others possible, e.g., Novell IPX, Apple Talk
    * used to demultiplex up at receiver

* `CRC`: cyclic redundancy check at receiver
    * error detected: frame is dropped

## Ethernet: unreliable, connectionless

* NIC = Network Interface Card

* connectionless: no handshaking between sending and receiving NICs

* unreliable: receiving NIC doesn't send ACKs or NAKs to sending NIC
    * data in dropped frames recovered only if initial sender uses higher layer rdt (e.g., TCP), otherwise dropped data lost

## 802.3 Ethernet standards: link & physical layers

* `many` different Ethernet standards
    * common MAC protocol and frame format
    * different speeds: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, >= 40 Gbps
    * different physical layer media: fiber, cable
<img src=imgs/Ethernet_standards.png>

* 1000BASE-T : 1Mbps/ twisted pair
* SR/LR: short/long distance fiber