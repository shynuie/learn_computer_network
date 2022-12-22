# 6.IX. Datacenter networks

## Datacenter networks

* 10's to 100's of thousands of hosts, often closely coupled, in close proximity:
    * e-business (e.g. Amazon)
    * content-servers (e.g. YouTube, Akamai, Apple, Microsoft)
    * search engines, data mining (e.g., Google)

`challenges`
* multiple applications, each serving massive numbers of clients
* reliability
* managing/balancing load, avoiding processing, networking, data bottlenecks

## Elements

<img src=imgs/datacenter_elements.png>

<img src=imgs/facebook_F16.png>

## Multi-Path

* rich interconnection among switches, racks:
    * increased throughput between racks (multiple routing paths possible)
    * increased reliability via redundancy
<img src=imgs/datacenter_multipath.png>

## Application-layer routing

`load balancer`: application-layer routing:
* receives external client requests
* directs workload within data center
* returns results to external client (hiding data center internals from client)

## Datacenter networks: protocol innovations

* link layer:
    * RoCE: remote DMA (RDMA) over Converged Ethernet
        * get data from destination host's RAM

* transport layer:
    * ECN (explicit congestion notification) used in transport-layer congestion control (DCTCP, DCQCN)
    * experimentation with hop-by-hop (backpressure) congestion control

* routing, management:
    * SDN widely used within/among organizations' datacenters
    * placed related services, data as close as possible (e.g., in same rack or nearby rack) to minimize tier02, tier-1 communication