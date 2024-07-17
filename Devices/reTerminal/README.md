# Getting Started with reTerminal

<p style={{textAlign: 'center'}}><img src="https://files.seeedstudio.com/wiki/ReTerminal/wiki_thumb.png" alt="pir" width="600" height="auto"/></p>

Introducing reTerminal, a new member of our reThings family. This future-ready Human-Machine Interface (HMI) device can easily and efficiently work with IoT and cloud systems to unlock endless scenarios at the edge.

reTerminal is powered by a Raspberry Pi Compute Module 4 (CM4) which is a Quad-Core Cortex-A72 CPU running at 1.5GHz and a 5-inch IPS capacitive multi-touch screen with a resolution of 1280 x 720. It has sufficient amount of RAM (4GB) to perform multitasking and also has sufficient amount of eMMC storage (32GB) to install an operating system, enabling fast boot up times and smooth overall experience. It has wireless connectivity with dual-band 2.4GHz/5GHz Wi-Fi and Bluetooth 5.0 BLE.

reTerminal consists of a high-speed expansion interface and rich I/O for more expandability. This device has security features such as a cryptographic co-processor with secure hardware-based key storage. It also has built-in modules such as an accelerometer, light sensor and an RTC (Real-Time Clock). reTerminal has a Gigabit Ethernet Port for faster network connections and also has dual USB 2.0 Type-A ports. The 40-pin header on the reTerminal opens it for a wide range of IoT applications.


reTerminal is shipped with Raspberry Pi OS out-of-the-box. So, all you have to do is connect it to power and start building your IoT, HMI and Edge AI applications right away!

| Released Date | Pre-Installed OS | Pre-Installed STM32 Firmware | Board Version | Additional Information |
|---|---|---|---|---|
| 06/15/2021 | 2021-06-02-Raspbian(modified)-32-bit | V1.0 | v1.3 | Initial |
| 08/03/2021 | 2021-06-02-Raspbian(modified)-32-bit | V1.1 | v1.4 |  |
| 09/03/2021 | 2021-06-02-Raspbian(modified)-32-bit | V1.6 | v1.6 | Change IO Expansion Chip from MCP23008-E to PCA9554, <br />Change Encryption Microchip from ATECC608A-SSHDA-B to ATECC608A-TNGTLSS-G [More Info](#../reTerminal-FAQ#q13-how-to-check-if-the-encryption-chip-is-atecc608a-sshda-b-or-atecc608a-tngtlss-g) |
| 11/02/2021 | 2021-09-14-Raspbian(modified)-32-bit | V1.8 | v1.6 |  |

## Features

- Integrated modular design with high stability and expandability
- Powered by Raspberry Pi Computer Module 4 with 4GB RAM & 32GB eMMC
- 5-Inch IPS capacitive multi-touch screen at 1280 x 720 and 293 PPI
- Wireless connectivity with dual-band 2.4GHz/5GHz Wi-Fi and Bluetooth 5.0 BLE
- High-speed expansion interface and rich I/O for more expandability
- Cryptographic co-processor with secure hardware-based key storage
- Built-in modules such as accelerometer, light sensor and RTC
- Gigabit Ethernet Port and Dual USB 2.0 Type-A ports
- 40-Pin header for IoT applications

## Specifications

<table style="table-layout: fixed; width: 743px;">
  <colgroup>
    <col style="width: 146px;" />
    <col style="width: 198px;" />
    <col style="width: 399px;" />
  </colgroup>
  <thead>
    <tr>
      <th colspan="2">Specification</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Platform</td>
      <td>Processor</td>
      <td>Broadcom BCM2711 quad-core Cortex-A72 (ARM v8)</td>
    </tr>
    <tr>
      <td>Frequency</td>
      <td>64-bit SoC @ 1.5GHz</td>
    </tr>
    <tr>
      <td rowspan="2">Memory</td>
      <td>Capacity</td>
      <td>4GB</td>
    </tr>
    <tr>
      <td>Technology</td>
      <td>LPDDR4 with on-die ECC</td>
    </tr>
    <tr>
      <td>eMMC</td>
      <td>Capacity</td>
      <td>32GB</td>
    </tr>
    <tr>
      <td rowspan="2">Wireless</td>
      <td>Wi-Fi</td>
      <td>2.4GHz and 5.0GHz IEEE 802.11b/g/n/ac</td>
    </tr>
    <tr>
      <td>Bluetooth</td>
      <td>Bluetooth 5.0, BLE</td>
    </tr>
    <tr>
      <td rowspan="2">Display</td>
      <td>LCD</td>
      <td>5-inch 720x1280 LCD</td>
    </tr>
    <tr>
      <td>Touch Panel</td>
      <td>Capacitive touch panel (support multi-touch)</td>
    </tr>
    <tr>
      <td rowspan="5">Video</td>
      <td>HDMI</td>
      <td>1 x Micro HDMI output (up to 4Kp60 supported)</td>
    </tr>
    <tr>
      <td>CSI</td>
      <td>1 x 2-lane MIPI CSI camera interface</td>
    </tr>
    <tr>
      <td rowspan="3">Multimedia</td>
      <td>H.265 (4Kp60 decode)</td>
    </tr>
    <tr>
      <td>H.264 (1080p60 decode,1080p30 encode)</td>
    </tr>
    <tr>
      <td>OpenGL ES 3.0 graphics</td>
    </tr>
    <tr>
      <td rowspan="10">Built-In Modules</td>
      <td rowspan="2">Real-Time Clock</td>
      <td>NXP Semiconductors PCF8563T</td>
    </tr>
    <tr>
      <td>Low backup current; typical 0.25μA at VDD = 3.0 V and Temperature = 25 ℃</td>
    </tr>
    <tr>
      <td rowspan="2">Accelerometer</td>
      <td>STMicroelectronics LIS3DHTR</td>
    </tr>
    <tr>
      <td>16-bit, ±2g/±4g/±8g/±16g dynamically selectable full scale</td>
    </tr>
    <tr>
      <td rowspan="2">Encryption</td>
      <td>Microchip ATECC608A</td>
    </tr>
    <tr>
      <td>Secure Hardware-Based Key Storage, Asymmetric Sign, Verify, Key Agreement</td>
    </tr>
    <tr>
      <td rowspan="2">Light Sensor</td>
      <td>Levelek LTR-303ALS-01</td>
    </tr>
    <tr>
      <td>Digital light sensor</td>
    </tr>
    <tr>
      <td>Internal IO Expansion</td>
      <td>Microchip MCP23008-E/ PCA9554</td>
    </tr>
    <tr>
      <td>Buzzer</td>
      <td>≥85dB @10cm 2700±300Hz</td>
    </tr>
    <tr>
      <td rowspan="12">External I/O</td>
      <td rowspan="8">GPIOs</td>
      <td>Up to 5 × UART</td>
    </tr>
    <tr>
      <td>Up to 5 × I2C</td>
    </tr>
    <tr>
      <td>Up to 5 × SPI</td>
    </tr>
    <tr>
      <td>1 × SDIO interface</td>
    </tr>
    <tr>
      <td>1 × DPI (Parallel RGB Display)</td>
    </tr>
    <tr>
      <td>1 × PCM</td>
    </tr>
    <tr>
      <td>1 × PWM channel</td>
    </tr>
    <tr>
      <td>Up to 3× GPCLK outputs</td>
    </tr>
    <tr>
      <td rowspan="4">Vertical expansion interface</td>
      <td>1 × PCIe 1-lane Host, Gen 2 (5Gbps)</td>
    </tr>
    <tr>
      <td>1 × USB 2.0 port (highspeed)</td>
    </tr>
    <tr>
      <td>26 x GPIOs</td>
    </tr>
    <tr>
      <td>POE</td>
    </tr>
    <tr>
      <td rowspan="2">Power</td>
      <td>Voltage</td>
      <td>5V DC</td>
    </tr>
    <tr>
      <td>Current</td>
      <td>3A(Minimum)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Operating Temperature</td>
      <td>0 - 70°C( For the LCD Screen: 0 - 60°C)</td>
    </tr>
    <tr>
      <td rowspan="2">Mechanical</td>
      <td>Dimensions</td>
      <td>140mm x 95mm x 21mm</td>
    </tr>
    <tr>
      <td>Weight</td>
      <td>285g</td>
    </tr>
  </tbody>
</table>

## Hardware Overview

<p style={{textAlign: 'center'}}><img src="https://files.seeedstudio.com/wiki/ReTerminal/HW_overview.png" alt="pir" width="1000" height="auto"/></p>

<p style={{textAlign: 'center'}}><img src="https://files.seeedstudio.com/wiki/ReTerminal/hw-overview-internal-v1.3.jpg" alt="pir" width="1000" height="auto"/></p>

## Block Diagram

<p style={{textAlign: 'center'}}><img src="https://files.seeedstudio.com/wiki/ReTerminal/reTerminal_block_diagram-v1.3.png" alt="pir" width="1000" height="auto"/></p>

## Pinout Diagram

 >[!NOTE]
 Please make sure to keep the reTerminal in the orientation as illustrated below. Here the LCD is facing right side and the back is facing left side.

<p style={{textAlign: 'center'}}><img src="https://files.seeedstudio.com/wiki/ReTerminal/pinout-v2.jpg" alt="pir" width="1000" height="auto"/></p>

 >[!NOTE]
Please carefully pay attention to the orientation of the reTerminal in the above diagram. The LCD and the onboard buttons are on the right side whereas the back of reTerminal is on the left side. Also the whole device is flipped upside down.



## FAQ

For Frequently Asked Questions, [click here](https://wiki.seeedstudio.com/reTerminal-FAQ) to visit the FAQs for reTerminal Usage wiki

## Resources

- **[PDF]** [reTerminal Schematics v1.6](https://files.seeedstudio.com/wiki/ReTerminal/reTerminal-v1.6_SCH.pdf)

- **[ZIP]** [reTerminal Schematics v1.6](https://files.seeedstudio.com/wiki/ReTerminal/reTerminal-v1.6_SCH.zip)

- **[PDF]** [reTerminal Schematics v1.3](https://files.seeedstudio.com/wiki/ReTerminal/reTerminal-v1.3_SCH.pdf)

- **[ZIP]** [reTerminal Schematics v1.3](https://files.seeedstudio.com/wiki/ReTerminal/reTerminal-v1.3_SCH.zip)

- **[STP]** [reTerminal 3D Model](https://files.seeedstudio.com/wiki/ReTerminal/resources/reTerminal-3d-model.stp)

- **[PDF]** [Raspberry Pi Compute Module 4 Datasheet](https://datasheets.raspberrypi.org/cm4/cm4-datasheet.pdf)

- **[Web Page]** [Raspberry Pi Official Documentation](https://www.raspberrypi.org/documentation/)
