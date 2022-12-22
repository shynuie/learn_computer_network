# 7.III. CDMA

## Code Division Multiple Access (CDMA)

* unique "code" assigned to each user; i.e., code set partitioning
    * all users share same frequency, but each user has own "chipping" sequence (i.e., code) to encode data
    * allow multiple users to "coexist(共存)" and transmit simultaneously with minimal interference (if codes are "orthogonal")

* `encoding`: inner product: (original data) ${\cdot}$ (chipping sequence)
* `decoding`: summed inner-product: (encoded data) ${\cdot}$ (chipping sequence)
    <img src=imgs/CDMA.png>
* CDMA: two-sender interference
    <img src=imgs/CDMA2.png>