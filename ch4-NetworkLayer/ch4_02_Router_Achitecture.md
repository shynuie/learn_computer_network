# 4.II Router Architecture

## high-level view of generic router architecture

<img src="imgs/routing_architecture.png">

### Input port functions
<img src="imgs/input_port_functions.png">

* switch fabric: examine each packet and determine its next destination/route

### Longest prefix matching

* When looking for forwarding table entry for given destination address, use `longest` address prefix that matches destination address.

<img src="imgs/longest_prefix_example.png">

* `Ans`: 0 and 1

* transport segment from sending to receiving host
* longest prefix matching: often performed using ternary(三元) content addressable memories (TCAMs)
    * content addressable: present address to TCAM. retrieve address in one clock cycle, regardless of table size
    * Cisco Catalyst: ~1M routing table entries in TCAM

---
## Switching fabrics

* transfer packet from input link to appropriate output link
* `switching rate`: rate at which packets can be transfer from inputs to outputs
    * often measured as multiple of input/output line rate
    * N inputs: switching rate N times line rate desirable

    <img src="imgs/switching_rate.png">

* three major types of switching fabrics
    <img src="imgs/switching_fabric_3types.png">

### Switching via memory
* traditional computers with switching under direct control of CPU
* packet copied to system's memory
* speed limited by memory bandwidth (2 bus crossings per datagram)
<img src="imgs/switching_via_memory.png">

### Switching via bus
* datagram from input port memory to output port memory via a shared bus
* `bus contention`: switching speed limited by bus bandwidth
* 32 Gbps bus, Cisco 5600: sufficient speed for access routers
<img src="imgs/switching_via_bus.png">

### Switching via interconnection network
* Crossbar, Clos networks, other interconnection nets initially developed to connect processors in multiprocessor
* `multistage switch`: ${n\times n}$ switch from multiple stages of smaller switches
* `exploiting parallelism`
    * fragment datagram into fixed length cells on entry
    * switch cells through the fabric, reassemble datagram at exit
<img src="imgs/switching_via_interconnection_network.png">

---
## Buffer Management

### Input port queuing

* If switch fabric slower than input ports combined -> queueing may occur at input queues
    * speedup, scale-up via parallelism

### `Head-of-the-Line (HOL) blocking:` queued datagram at front of queue prevents others in queue from moving forward

<img src="imgs/HOL_blocking.png">

### Output port queuing

<img src="imgs/output_port_queuing.png">

Two major issues:

* `Buffering` required when datagrams arrive from fabric faster than link transmission rate. `Drop policy:` which datagrams to drop if no free buffers? -> Datagrams can be lost due to congestion, lack of buffers

* `Scheduling discipline` choose among queued datagrams for transmission -> Priority scheduling - who gets best performance, network neutrality

---
<img src="imgs/output_port_queuing2.png">

* buffering when arrival rate via switch exceeds output line speed
* queuing (delay) and loss due to output port buffer overflow!

### Buffer Management

<img src="imgs/buffer_management.png">

`buffer management:`
* `drop:` which packet to add, drop when buffers are full
    * `tail drop`: drop arriving packet
    * `priority`: drop/remove on priority basis
* `marking:` which packets to mark to signal congestion (ECN, RED(Random Early Detection))

### Packet Scheduling
`packet scheduling:` deciding which packet to send next on link
* first come, first served
* priority
* round robin
* weighted fair queueing

### Scheduling policies: FCFS
`FCFS:` packets transmitted in order of arrival to output port
* a.k.a., First-In-First-Out (FIFO)

### Scheduling policies: priority
`Priority scheduling:`
* arriving traffic classified, queued by class
    * any header fields can be used for classification
    <img src="imgs/priority_scheduling.png">

* send packet from highest priority queue that has buffered packets
    * FCFS within priority class

### Scheduling policies: RR
`Round Robin(RR) scheduling:`
* arriving traffic classified, queued by class
    * any header fields can be used for classification
    <img src="imgs/RR_scheduling.png">

### Scheduling policies: weighted fair queuing
`Weighted Fair Queuing (WFQ):` generalized Round Robin

<img src="imgs/WFQ_scheduling.png">

* each class i, has weight, ${w_i}$, and gets weighted amount of service in each cycle: ${w_i\over{\sum _jw_j}}$
* minimum bandwidth guarantee (per-traffic-class)