import gc
import network

import esp

from configuration import WIFI_CREDENTIALS


esp.osdebug(None)

gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_CREDENTIALS.get("ssid"), WIFI_CREDENTIALS.get("password"))
wlan.config(dhcp_hostname=WIFI_CREDENTIALS.get("hostname"))

while not wlan.isconnected():
    pass

print("successfully connected to WIFI")

wifi_ap = network.WLAN(network.AP_IF)
wifi_ap.active(False)

print("wifi access point disabled")
