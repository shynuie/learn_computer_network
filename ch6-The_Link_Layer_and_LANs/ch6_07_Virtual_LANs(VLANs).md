# 6.VII. Virtual LANs (VLANs)

---
`Question`:  
What happens as LAN size scale, users change point of attachment?

<img src=imgs/VLANs_eg.png>

`Single broadcast domain`
* scaling: all layer-2 broadcast traffic (ARP, DHCP, unknown MAC) must cross entire LAN
* efficiency, security, privacy issues

`administrative issues`
* CS user moves office to EE - physically attached to EE switch, but wants to remain logically attached to CS switch

---

## Virtual Local Area Network (VLAN)

switch(es) supporting VLAN capabilities can be configured to define multiple virtual LANs over single physical LAN infrastructure.

* `port-based VLAN`: switch ports grouped (by software) so that single physical switch...

    <img src=imgs/port-based_VLAN.png>

* `traffic isolation`: frames to/from ports 1-8 can only reach ports 1-8 in link layer
    * can also define VLAN based on MAC addresses of endpoint, rather than switch port
* `dynamic membership`: ports can be dynamically assigned among VLANs
* `forwarding between VLANs`: done via routing (just as with separate switches)
    * in practice vendors sell combined switches plus routers

---

## VLANs spanning multiple switches

* `trunk port`: carries frames between VLANs defined over multiple physical switches
    * frames forwarded within VLAN between switches can't be vanilla 802.1 frames (must carry VLAN ID info)
    * 802.1Q protocol adds/removed additional header fields for frames forwarded between trunk ports
        <img src=imgs/802p1Q.png>
    
    * insert a 2-byte Tag Protocol identifier before type
    * 2-byte Tag Control Information
        * 12 bit as VLAN ID
        * 3 bit priority