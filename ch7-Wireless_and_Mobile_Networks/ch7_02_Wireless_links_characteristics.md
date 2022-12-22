# 7.II. Wireless links characteristics

`differences from wired link`

* `decreased signal strength`: radio signal attenuates(衰減) as it propagates through matter (path loss)

* `interference(干擾) from other sources`： wireless network frequencies (e.g., 2.4 GHz) shared by many devices (e.g., WiFi, cellular, motors): interference

* `multi-path propagation`: radio signal reflects off object ground, arriving at destination at slightly different times

* SNR: signal-to-noise ratio
    * larger SNR -> easier to extract signal from noise
    * given physical layer:
        increase power -> increase SNR - > decrease BER(bit error rate)
    *  given SNR:choose physical layer that meets BER requirement, giving highest throughput
        * SNR may change with mobility: dynamically adapt physical layer (modulation tech, rate)

        <img src=imgs/ber.png>

        * QAM 256, QAM 16: the numbers follow with QAM means that how many bits one signal can represent

* Multiple wireless senders, receivers create additional problems (beyond multiple access)
    <img src=imgs/hidden_terminal.png>
    * `Hidden terminal problem`
        * B, A hear each other
        * B, C hear each other
        * A, C can not hear each other means A, C unaware of their interference at B
        <img src=imgs/hidden_terminal2.png>
