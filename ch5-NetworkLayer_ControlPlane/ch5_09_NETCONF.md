# 5.IX. NETCONF

## Overview

* `goal`: actively manage/configure devices network-wide

* operates between managing server and managed network devices

    * actions: retrieve, set, modify, activate configurations
    * atomic-commit (set all or not set at all) actions over multiple devices
    * query operational data and statistics
    * subscribe to notifications from devices

* remote procedure call (RPC) paradigm
    * NETCONF protocol msg encoded in XML
    * exchanged over secure, reliable transport (e.g., TLS) protocol

<img src=imgs/NETCONF.png>

## Selected NETCONF Operations

<img src=imgs/NETCONF2.png>

## Sample NETCONF RPC message

<img src=imgs/NETCONF3.png>

* MTU = maximum transmission unit

## YANG

* data modeling language used to specify structure syntax, semantics of NETCONF network management data
    * built-in data types, like SMI

* XML document describing device, capabilities can be generated from YANG description

* can express constraints among data that must be satisfied by a valid NETCONF configuration
    * ensure NETCONF configurations satisfy correctness, consistency constraints

    <img src=imgs/NETCONF4.png>