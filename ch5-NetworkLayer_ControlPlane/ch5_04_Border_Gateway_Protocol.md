# 5.IV. Border Gateway Protocol (BGP)

## Internet inter-AS routing: BGP

* `BGP (Border Gateway Protocol):` the de facto inter-domain routing protocol
    * "glue that holds Internet together"

* allows subnet to advertise its existence, and the destinations it can reach, to rest of Internet

* BGP provides each AS a means  to:
    * eBGP: obtain subnet reachability information from neighboring ASes
    * iBGP: propagate reachability information to all AS-internal routers.
    * determine "good" routes to other networks based on reachability information and `policy`
    <img src=imgs/BGP_1.png>

* `BGP session`: two BGP routers ("peers") exchange BGP messages over semi-permanent TCP connection:
    * advertising paths to different destination network prefixes (BGP is a "path vector" protocol)
    <img src=imgs/BGP_2.png>

* BGP advertised route: prefix + attributes
    * prefix: destination being advertised
    * tow important attributes:
        * AS-PATH: list of ASes through which prefix advertisement has passed
        * NEXT-HOP: Indicates specific internal-AS router to next-hop AS

* `Policy based routing:`
    * gateway receiving route advertisement uses import policy to accept/decline path (e.g., never route through AS Y).
    * AS policy also determines whether to advertise path to other neighboring ASes
    <img src=imgs/BGP_3.png>
    <img src=imgs/BGP_4.png>

* BGP messages
    * `OPEN`: opens TCP connection to remote BGP peer and authenticates sending BGP peer
    * `UPDATE`: advertise new path (or withdraw old)
    * `KEEPALIVE`: keeps connection alive in absence of UPDATES; also ACKs OPEN request
    * `NOTIFICATION`: reports errors in previous msg; also used to close connection

## Why different Intra-, Inter-AS routing?

* `policy:`
    * inter-AS: admin wants control over how its traffic routed, who routes through its network
    * intra-AS: single admin, so policy less of an issue

* `scale:`
    * hierarchical routing saves table size, reduced update traffic

* `performance:`
    * intra-AS: can focus on performance
    * inter-AS: policy dominates over performance

## BGP route selection

* router may learn about more than one route to destination AS, selects route based on:
    1. local preference value attribute: policy decision
    2. shortest AS-PATH
    3. closet NEXT-HOP router: hot potato routing
    4. additional criteria