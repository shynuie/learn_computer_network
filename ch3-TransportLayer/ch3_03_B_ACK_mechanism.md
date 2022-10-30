# 3.III.B. ACK Mechanism


## Go-Back-N
### Go-Back-N: sender

* sender: "window" of up to N, consecutive transmitted but unACKed pkts
    * k-bit seq # in pkt header

    <img src="imgs/go_back_n.png">

* `cumulative ACK:` ACK(n):ACKs all packets up to, including seq # n
    * on receiving ACK(n): move window forward to begin at n + 1
* timer for oldest in-flight packet
* timeout(n): retransmit packet n and all higher seq # packets in window


### Go-Back-N: receiver

* ACK-only: always send ACK for correctly-received packet so far, with highest `in-order` seq #
    * may generate duplicate ACKs
    * need only remember rcv_base
* on receipt of out-of-order packet:
    * can discard (don't buffer) or buffer: an implementation decision
    * re-ACK pkt with highest in-order seq #

    <img src="imgs/GO_BACK_N_receiver.png">

### Go-Back-N: Illustration

<img src="imgs/GOBACKN.png">
<img src="imgs/GOBACKN2.png">

---
## Selective ACK

* receiver individually acknowledges all correctly received packets
    * may generate duplicate ACKs
    * need only remember rcv_base

* sender times-out/retransmits individually for for unACKed packets
    * sender maintain timer for each unACKed pkt

* sender window
    * N consecutive seq #s
    * limit seq #s of sent, unACKed packets

<img src="imgs/selective_ACK.png">
<img src="imgs/selective_ACK_table.png">

### Selective ACK Illustration
<img src="imgs/selective_ACK_illu.png">