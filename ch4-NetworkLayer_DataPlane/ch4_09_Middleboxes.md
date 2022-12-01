# 4.IX. Middleboxes

## Middlebox (RFC 3234)

" any intermediary box performing functions apart from normal, standard functions of an IP router on the data path between a source host and destination host"

* Middleboxes everywhere
    middleboxes provides vary service/function on network, such as:
    * `NAT`: home, cellular, institutional
    * `Firewalls, IDS`: corporate, institutional, service provider, ISPs
    * `Application-specific`: service providers, institutional, CDN
    * `Load balancers`: corporate, service provider, data center, mobile nets
    * `Caches`: service provider, mobile, CDNs

* initially: proprietary(closed) hardware solutions
* move towards "white box" hardware implementing open API
    * programmable local actions via match+action(OpenFlow)
    * move towards innovation/differentiable in software
* `SDN`:(logically) centralized control and configuration management often in private/public cloud
* `network functions virtualization (NFV)`: programable services over white box networking, computation, storage
