# 7.VII. Mobility management (principles)

* What is mobility?

<img src=imgs/mobility_spectrum.png>

## Mobility approaches

`let network (routers) handle it:`
* routers advertise well-known name, address (e.g., permanent 32-bit IP address), or number(e.g., cell#) of visiting mobile node via usual routing table exchange
* internet routing could do this already `with no` changes! Routing tables indicate where each mobile located via longest prefix match!
* not scalable to billions of mobiles!

`let end-system handle it:` functionality at the "edge"
* `indirect routing`: communication from correspondent to mobile goes through home network, then forwarded to remote mobile
* `direct routing`: correspondent gets foreign address of mobile, send directly to mobile

## How to find target that move frequently?

The importance of having a "home":
* a definitive source of information about you
* a place where people can find out where you are

## Home network, visited network 4G/5G

<img src=imgs/home_network_vs_visited_network.png>

## Registration: home needs to know where you are!

<img src=imgs/registration.png>

end result:
* visited mobility manager knows about the mobile
* home HSS knows location of mobile

## Mobility with indirect routing
<img src=imgs/indirect_routing.png>

* triangle routing:
    * inefficient when correspondent and mobile are in same network

* mobile moves among visited networks: transparent to correspondent!
    * registers in new visited network
    * new visited network registers with home HSS
    * datagrams continue to be forwarded from home network to mobile in new network
    * `on-going(e.g., TCP) connection between correspondent and mobile can be maintained!`


## Mobility with direct routing

<img src=imgs/direct_routing.png>

* overcomes triangle routing inefficiencies
* `non-transparent to correspondent`: correspondent must get care-of-address from home agent