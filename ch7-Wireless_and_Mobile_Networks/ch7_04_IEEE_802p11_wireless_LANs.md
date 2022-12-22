# 7.IV. IEEE 802.11 wireless LANs

<img src=imgs/802p11.png>

* all use CSMA/CA for multiple access, and have base-station and ad-hoc network versions
    * CSMA (Carrier Sense Multiple Access):
        * check whether there's other hosts transmitting data. If yes, wait for a moment and check again
        * can reduce probability of collision occurring
    * CA (Collision Avoidance)

## 802.11 LAN architecture

<img src=imgs/802p11_LAN.png>

* wireless host communicates with base station
    * base station = access point (AP)
* Basic Service Set(BSS, a.k.a., "cell") in infrastructure mode contains:
    * wireless hosts
    * AP
    * ad hoc mode: hosts only

* In today, usually there will be a WiFi controller in switch which manages all WiFi device.


## 802.11 Channels, association

* spectrum divided into channels at different frequencies
    * AP admin chooses frequency for AP
    * interference possible: channel can be same as that chosen by neighboring AP!

* arriving host: must associate with an AP
    * scans channels, listening for beacon frames containing AP's name (SSID) and MAC address
    * select AP to associate with
    * then may perform authentication
    * then typically run DHCP to get IP address in AP's subnet
    <img src=imgs/associate_BBS.png>

## 802.11: passive/active scanning

`passive scanning:`
<img src=imgs/passive_scanning.png>

1. beacon frames sent from APs
2. association Request frame sent: H1 to selected AP
3. association Response frame sent from selected AP to H1

`active scanning`
<img src=imgs/active_scanning.png>

1. Probe Request frame broadcast from H1
2. Probe Response frames from APs
3. Association Request frame sent: H1 to selected AP
3. association Response frame sent from selected AP to H1


## 802.11: multiple access

* avoid collisions: ${2^+}$ nodes transmitting at same time
* 802.11: CSMA - sense before transmitting
    * don't collide with detected ongoing transmission by another node
* 802.11: no collision detection!
    * difficult to sense collisions: high transmitting signal, week received signal due to fading
    * can't sense all collisions in any case: hidden terminal, fading
    * goal: avoid collisions: CSMA/CollisionAvoidance

## 802.11:sender & receiver

<img src=imgs/sender_and_receiver.png>

* In WiFi, each packet should has one ACK packet as response

## Avoid collisions (more)

`idea`: sender "reserves" channel use for data frames using small reservation packets
* sender first transmits small request-to-send(RTS) packet to BSS using CSMA
    * RTSs may still collide with each other
* BS broadcasts clear-to-send CTS in response to RTS
* CTS heard by all nodes
    * sender transmits data frame
    * other stations defer transmissions
<img src=imgs/RTS.png>

## 802.11 frame: addressing

<img src=imgs/802p11frame.png>
<img src=imgs/802p11toEthernet.png>
<img src=imgs/802p11frame_more.png>

# 802.11: advanced capabilities

<img src=imgs/rate_adaptation.png>

`Rate adaptation`
* base station, mobile dynamically change transmission rate (physical layer modulation technique) as mobile moves, SNR varies
    * SNR decreases, BER increase as node moves away from base station
    * When BER becomes too high, switch to lower transmission rate but with lower BER

`power management`
* node-to-AP: "I am going to sleep until next beacon frame"
    * AP knows not to transmit frames to this node
    * node wakes up before next beacon frame
* beacon frame: contains list of mobiles with AP-to-mobile frames waiting to be sent
    * node will stay awake if AP-to-mobile frames to be sent; otherwise sleep again until next beacon frame