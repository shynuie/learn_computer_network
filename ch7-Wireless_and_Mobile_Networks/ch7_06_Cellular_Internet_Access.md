# 7.VI. Cellular Internet Access

## 4G/5G cellular networks

* the solution for wide-area mobile Internet
* transmission rates up to 100's Mbps (4G)
* technical standards: 3rd Generation Partnership Project (3GPP)
    * www.3gpp.org
    * 4G: Long-Term Evolution (LTE) standard

## similarities to wired Internet
* edge/core distinction, but both below to same carrier
* global cellular network: a network of networks
* widespread use of protocols we've studied: HTTP, DNS, TCP, UDP, IP, NAT, separation of data/control planes, SDN, Ethernet, tunneling,
* interconnected to wired Internet

## differences from wired Internet
* different wireless link layer
* mobility as a 1st class service
* user "identity" (via SIM card)
* business model: users subscribe to a cellular provider
    * strong notion of "home network" versus roaming on visited nets
    * global access, with authentication infrastructure, and inter-carrier settlements

<img src=imgs/4G_LTE_arch.png>
<img src=imgs/LTE_basestation.png>
<img src=imgs/LTE_HSS.png>
<img src=imgs/LTE_S-GW_P-GW.png>
<img src=imgs/LTE_MME.png>

## LTE: data plane control plane separation

<img src=imgs/data_plane_control_plane.png>

## LTE: data plane protocol stack: first hop

`LTE link layer protocols`:
* packet Data Convergence: header compression, encryption
* Radio Link Control (RLC) Protocol: fragmentation/reassembly, reliable data transfer
* Medium Access: requesting, use of radio transmission slots

<img src=imgs/LTE_data_plane.png>

`LTE radio access network`:
* downstream channel: FDM, TDM within frequency channel(OFDM - orthogonal frequency division multiplexing)
    * orthogonal: minimal interference between channels
    * upstream: FDM, TDM similar to OFDM
* each active mobile device allocated two or more 0.5 ms time slots over 12 frequencies
    * scheduling algorithm not standardized - up to operator
    * 100's Mbps per device possible

## LTE data plane protocol stack: packet core
<img src=imgs/LTE_tunneling.png>

`tunneling:`
* mobile datagram encapsulated using GPRS Tunneling Protocol (GTP), sent inside UDP datagram to S-GW
* S-GW re-tunnels datagrams to P-GW
* supporting mobility: only tunneling endpoints change when mobile user moves

## LTE data plane: associating with a BS

<img src=imgs/LTE_dataplane.png>

## LTE sleep

<img src=imgs/LTE_sleep.png>

## Global cellular network: a network of IP networks

<img src=imgs/LTE_IPbased.png>

## 5G

<img src=imgs/5G.png>