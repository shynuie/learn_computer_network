# 6.VIII. Multi-Protocol label switching (MPLS)

`Goal`
high-speed IP forwarding among network of MPLS-capable routers, using fixed length label (instead of shortest prefix matching)
* faster lookup using fixed length identifier
* borrowing ideas from Virtual Circuit (VC) approach
* but IP datagram still keeps IP address
    <img src=imgs/MPLS.png>

## MPLS capable routers

* a.k.a label-switched router
* forward packets to outgoing interface based only on label value (don't inspect IP address)
    * MPLS forwarding table distinct from IP forwarding tables
* `flexibility`: MPLS forwarding decisions can differ from those of IP
    * use dest and source addr to route flows to same dest differently (traffic engineering)
    * re-route flows quickly if link fails: pre-computed backup paths

    <img src=imgs/MPLS_forwarding.png>

## MPLS signaling

* modify OSPF, IS-IS link-state flooding protocols to carry info used by MPLS routing:
    * e.g., link bandwidth, amount of "reserved" link bandwidth
* entry MPLS router use RSVP-TE signaling protocol to set up MPLS forwarding at downstream routers
    <img src=imgs/RSVP-TE.png>