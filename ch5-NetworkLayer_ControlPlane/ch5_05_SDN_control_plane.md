# 5.V. SDN control plane

## Software defined networking (SDN)

* Internet networking layer: historically implemented via distributed, per-router control approach:
    * `monolithic` router contains switching hardware, runs proprietary implementation of Internet standard protocols(IP, RIP, IS-IS, OSPF, BGP) in proprietary router OS (e.g., Cisco IOS)
    * not flexible. different "middleboxes" for different network layer functions: firewalls, load balancers, NAT boxes,.. function is determined by provider

## SDN control plane

* Remote controller computes, installs forwarding tables in routers
    <img src="imgs/SDN.png">

## Why a logically centralized control plane?

* easier network management: avoid router misconfigurations, greater flexibility of traffic flows
* table-based forwarding (recall OpenFlow API) allows "programming" routers
    * centralized "programming" easier: compute tables centrally and distribute
    * distributed "programming" more difficult: compute table as result of distributed algorithm (protocol) implemented in each-and-every router
* open(non-proprietary) implementation of control plane
    * foster innovation: let 1000 flowers bloom