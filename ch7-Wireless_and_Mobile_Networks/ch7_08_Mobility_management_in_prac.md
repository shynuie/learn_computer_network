# 7.VIII. Mobility management (practice)

<img src=imgs/major_mobility_tasks.png>

## Configuring LTE control-plane elements
<img src=imgs/control_plane_configuring.png>

* Mobile communicates with local MME via BS control-plane channel
* MME uses mobile's IMSI info to contact mobile's home HSS
    * retrieve authentication, encryption, network service information
    * home HHS knows mobile now resident in visited network
* BS, mobile select parameters for BS-mobile data-plane radio channel

## Establish tunnels

<img src=imgs/establish_tunnel.png>

* S-GW to BS tunnel: when mobile changes base stations, simply change endpoint IP address of tunnel
* S-GW to home P-GW tunnel: implementation of indirect routing
* tunneling via GTP (GPRS tunneling protocol): mobiles's datagram to streaming server encapsulated using GTP inside UDP, inside datagram

## Handover between BSs in sme cellular network

<img src=imgs/handover.png>

1. current (source) BS selects target BS, sends Handover Request message to target BS
2. target BS pre-allocates ratio time slots, responds with HR ACK with info for mobile
3. source BS informs mobile of new BS
    * mobile can now send via new BS - handover looks complete to mobile
4. source BS stops sending datagrams to mobile, instead forwards to new BS (who forwards to mobile over radio channel)

<img src=imgs/handover2.png>

5. target BS informs MME that it is new BS for mobile
    * MME instructs S-GW to change tunnel endpoint to be new target BS
6. target BS ACKs back to source BS: handover complete, source BS can release resources
7. mobile's datagrams now flow through new tunnel from target BS to S-GW

## Mobile IP

<img src=imgs/mobile_ip.png>

## Wireless, mobility: impact on higher layer protocols

<img src=imgs/impact_on_higher_layer.png>