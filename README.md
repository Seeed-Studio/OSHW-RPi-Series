# reComputer_R_Series


<p align="center"><img src="https://files.seeedstudio.com/wiki/reComputer-R1000/recomputer_r_images/01.png" alt="pir" width="400" height="auto"/></p>


The reComputer R1000 edge IoT controller is built on the high-performance Raspberry Pi CM4 platform, featuring a quad-core A72 processor with a maximum support of 8GB RAM and 32GB eMMC. Equipped with dual Ethernet interfaces that can be flexibly configured, it also includes 3 isolated RS485 channels supporting BACnet, Modbus RTU, Modbus TCP/IP ,and KNX protocols. With robust IoT network communication capabilities, the R1000 series supports multiple wireless communication options including 4G, LoRa®, Wi-Fi/BLE, allowing for flexible configurations to serve as corresponding wireless gateways. This controller is well-suited for remote device management, energy management, and various other scenarios in the field of smart buildings.

## Features

### Designed for Building Automation System
* Multiple isolated RS485 channels supports high and low speeds communication.
* Supports BACnet, Modbus RTU, Modbus TCP/IP and KNX protocol
* Up to 8GB RAM supports the processing of thousands of data points, ensuring efficient performance
* Clear dual-sided LED indicators help check operational status quickly
* High-quality metal case, compatible with DIN-rail and Wall installation 
* Supports Yocto and Buildroot for customized OS
### Powerful Performance
* Powered by Raspberry Pi CM4 
* Broadcom BCM2711 quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz 
* Up to 8GB RAM and 32GB eMMC
### Rich Wireless Capabilities
* On-chip Wi-Fi
* On-chip BLE
* Mini-PCIe1: LTE, USB LoRa®, USB Zigbee
* Mini-PCIe2: SPI LoRa®, USB LoRa®, USB Zigbee
### Rich Interfaces
* 3x RS485 (isolated）
* 1x 10M/100M/1000M Ethernet (Support PoE)
* 1x 10M/100M Ethernet
* 1x HDMI 2.0
* 2x Type-A USB2.0 
* 1x Type-C USB2.0 (USB console for OS update)
* 1x SIM card slot
### Safety and Reliability
* Hardware Watchdog(optional)
* UPS Supercapacitor(optional)
* Metal casing with PC side panels
* ESD: EN61000-4-2,level 3
* EFT: EN61000-4-4, level 2
* Surge: EN61000-4-5, level 2
* Production Lifetime: reComputer R1000 will remain in production until at least December 2030

<table>
  <tbody>
    <tr>
      <td style="width: 35.4622%;">Parameter</td>
      <td colspan="2" style="width: 63.1933%;">Description</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Hardware Spec</strong></td>
    </tr>
    <tr>
      <td style="width: 35.4622%;">Product Series</td>
      <td style="width: 31.5967%;">R10xx-10</td>
      <td style="width: 31.5966%;">R10xx-00</td>
    </tr>
    <tr>
      <td>CPU</td>
      <td colspan="2">Raspberry Pi CM4, Quad-core Cortex-A72@ 1.5GHz</td>
    </tr>
    <tr>
      <td>Operating System</td>
      <td colspan="2">Raspbian, Debian</td>
    </tr>
    <tr>
      <td>RAM</td>
      <td colspan="2">1GB/2GB/4GB/8GB</td>
    </tr>
    <tr>
      <td>eMMC</td>
      <td colspan="2">8GB/16GB/32GB</td>
    </tr>
    <tr>
      <td colspan="3"><strong>System Spec</strong></td>
    </tr>
    <tr>
      <td>Input</td>
      <td colspan="2">2-pin Terminal Block</td>
    </tr>
    <tr>
      <td>PoE(as powered device)</td>
      <td colspan="2">IEEE 802.3af Standard 12.95W PoE*</td>
    </tr>
    <tr>
      <td>Supply Voltage(AC/DC)</td>
      <td colspan="2">12~24V AC/9~36V DC</td>
    </tr>
    <tr>
      <td>Overvoltage Protection</td>
      <td colspan="2">40V</td>
    </tr>
    <tr>
      <td>Power Consumption</td>
      <td colspan="2">Idle:2.88W; Full Load:5.52W</td>
    </tr>
    <tr>
      <td>Power Switch</td>
      <td colspan="2">No</td>
    </tr>
    <tr>
      <td>Reboot Switch</td>
      <td colspan="2">Yes</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Interface</strong></td>
    </tr>
    <tr>
      <td rowspan="2">Ethernet</td>
      <td colspan="2">1 x 10/100/1000 Mbps(supports PoE*)</td>
    </tr>
    <tr>
      <td colspan="2">1 x 10/100 Mbps IEEE802.3/802.3u</td>
    </tr>
    <tr>
      <td rowspan="2">USB</td>
      <td colspan="2">2 x USB-A 2.0 Host</td>
    </tr>
    <tr>
      <td colspan="2">1 x USB-C 2.0 (For flashing OS)</td>
    </tr>
    <tr>
      <td>RS485</td>
      <td colspan="2">3 x 3-pin Terminal Block (isolated)</td>
    </tr>
    <tr>
      <td>HDMI</td>
      <td colspan="2">1 x HDMI 2.0</td>
    </tr>
    <tr>
      <td>SIM Card Slot</td>
      <td colspan="2">supports Standard SIM Card</td>
    </tr>
    <tr>
      <td>M.2 Slot</td>
      <td colspan="2">supports M.2 NVMe SSD</td>
    </tr>
    <tr>
      <td>LED</td>
      <td colspan="2">6 x LED indicators</td>
    </tr>
    <tr>
      <td>Buzzer</td>
      <td colspan="2">1</td>
    </tr>
    <tr>
      <td>Reset Button</td>
      <td colspan="2">1</td>
    </tr>
    <tr>
      <td>DSI(reserved)</td>
      <td colspan="2">supports LCD*(on board within the enclosure)</td>
    </tr>
    <tr>
      <td>Speaker(reserved)</td>
      <td colspan="2">supports Microphone*(on board within the enclosure)</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Wireless Communication</strong></td>
    </tr>
    <tr>
      <td>Wi-Fi 2.4/5.0 GHz</td>
      <td style="width: 31.5967%;">On-chip Wi-Fi*</td>
      <td style="width: 31.5966%;">No</td>
    </tr>
    <tr>
      <td>BLE 5.0</td>
      <td>On-chip BLE*</td>
      <td>No</td>
    </tr>
    <tr>
      <td>LoRa®</td>
      <td colspan="2">USB LoRa®/SPI LoRa®*</td>
    </tr>
    <tr>
      <td>4G Cellular</td>
      <td colspan="2">4G LTE*</td>
    </tr>
    <tr>
      <td>Zigbee</td>
      <td colspan="2">USB Zigbee*</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Standards</strong></td>
    </tr>
    <tr>
      <td rowspan="3">EMC</td>
      <td colspan="2">ESD: EN61000-4-2, Level 3</td>
    </tr>
    <tr>
      <td colspan="2">EFT: EN61000-4-4, Level 2</td>
    </tr>
    <tr>
      <td colspan="2">Surge: EN61000-4-5, Level 2</td>
    </tr>
    <tr>
      <td rowspan="4">Certification</td>
      <td colspan="2">CE, FCC</td>
    </tr>
    <tr>
      <td colspan="2">TELEC</td>
    </tr>
    <tr>
      <td colspan="2">RoHS</td>
    </tr>
    <tr>
      <td colspan="2">REACH</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Ambient Conditions</strong></td>
    </tr>
    <tr>
      <td>Ingress Protection</td>
      <td colspan="2">IP40</td>
    </tr>
    <tr>
      <td>Operating Temperature</td>
      <td colspan="2">-30~70 °C</td>
    </tr>
    <tr>
      <td>Operating Humidity</td>
      <td colspan="2">10~95% RH</td>
    </tr>
    <tr>
      <td>Storage Temperature</td>
      <td colspan="2">-40~80 °C</td>
    </tr>
    <tr>
      <td colspan="3"><strong>Others</strong></td>
    </tr>
    <tr>
      <td>Supercapacitor UPS</td>
      <td colspan="2">SuperCAP UPS LTC3350 Module*</td>
    </tr>
  </tbody>
</table>
