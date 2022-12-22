# 6.I. Link layer

## Link layer: Introduction

Terminology:
* nodes: hosts and routers
* links: channels connecting adjacent(鄰近) nodes
    * wired
    * wireless
    * LANs
* packet in layer-2: `frame`


## Link layer: services

* `framing, link access`:
    * encapsulate datagram into frame, adding header, trailer
    * channel access if shared medium (medium access control/MAC)
    * "MAC" address in frame header identify source, destination(different from IP address!)

* `reliable delivery` between adjacent nodes
    * seldom used on low bit-error links
    * wireless links: high error rates
    * Question Why both link-level and end-end reliability
        * link-level only: hard to process if pkg is lost on medium router
        * end-end only: slow to react

* `flow control(optional)`

* `error detection`

* `error correction`
    * once receiver identifies bit error(s), correct it without retransmission
    * not worth to implement for links with low error rate/low cost for retransmission

* `half-duplex(雙工) and full-duplex`
    * with half-duplex, nodes at both ends of link can transmit, but not at same time. (e.g. WiFi)

## Where is the link layer implemented?

* in each-and-every host
* link layer implemented in `network interface card (NIC)` or on a chip
    * Ethernet, WiFi card or chip
    * implements link, physical layer

* attaches into host's system buses