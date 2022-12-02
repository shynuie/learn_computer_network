# 5.VII. ICMP

## ICMP: Internet control message protocol

* used by hosts and routers to communicate network-level information
    * error reporting: unreachable host, network, port, protocol
    * echo request/reply (used by ping)

* network-layer "above" IP:
    * ICMP messages carried in IP datagrams

* ICMP message: type, code plus first 8 bytes of IP datagram causing error

<img src=imgs/ICMP.png>


## Traceroute and ICMP

* source sends sets of UDP segments to destination
    * ${1_{st}}$ set has TTL = 1, ${2_{nd}}$ set has TTL = 2, ..., etc.
    * all the packets destination port are set to a unique/weird port value which guarantee us to receive dest port unreachable msg when the packet has arrived the destination
    * when the TTL is submitted to zero by particular router, that router will send a ICMP message back. By this method, we can evaluate how many routers are on the route to destination.
    * ICMP message possibly includes name of router & IP address
    * when ICMP msg arrives at source: record RTTs