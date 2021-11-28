from typing import Match
import getmac
for i in range(255):
    mac = getmac.get_mac_address(ip="10.0.0."+str(i))
    print(mac)