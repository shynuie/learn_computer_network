# 7.V. Bluetooth

## Personal area networks: Bluetooth

* less than 10 m diameter
* ad hoc: no infrastructure
* 2.4-2.5 GHz ISM radio band, up to 3 Mbps
* master controller / clients devices:
    * master polls clients, grants requests for client transmissions

<img src=imgs/bluetooth.png>

* for further power consumption control -> Bluetooth LE
* TDM, 625 msec sec. slot
* FDM, sender uses 79 frequency channels in known, pseudo(偽)-random order slot-to-slot (spread spectrum)
    * other devices/equipment not in piconet only interfere in some slots
* `parked mode`: clients can "go to sleep" (park) and later wake up. (preserve battery)
* `bootstrapping`: nodes self-assemble (plug and play) into piconet