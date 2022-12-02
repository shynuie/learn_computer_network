# 5.VI. OpenFlow

## OpenFlow protocol

* operates between controller, switch

* TCP used to exchange messages
    * optional encryption

* three classes of OpenFlow messages:
    * controller-to-switch
    * asynchronous異步 (switch to controller)
    * symmetric (misc.)

* distinct from OpenFlow API
    * API used to specify generalized forwarding actions

## Controller-to-switch messages

* `features:` controller queries switch features, switch replies
* `configure:` controller queries/sets switch configuration parameters
* `modify-state:` add, delete, modify flow entries in the OpenFlow tables
* `packet-out:` controller can send this packet out of specific switch port

## Switch-to-controller messages
* `packet-in:` transfer packet (and its control) to controller. See packet-out message from controller

* `flow-removed:` flow table entry deleted at switch

* `port status:` inform controller of a change on a port.