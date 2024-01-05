import corduroy
from corduroy import build_graph
from typing import List


devices: List = []

devices.append(Mouse(name="usb mouse", cord="USB-A"))
devices.append(Keyboard(name="usb keyboard", cord="USB-A"))
devices.append(Computer(name="test laptop", ports=["USB-A", "USB-A", "USB-C"]))
devices.append(Monitor(name="test monitor", ports=["USB-C", "Thunderbolt"]))
devices.append(Cord(name="usb cord", cords=["USB-C", "USB-C"]))

G = build_graph(devices)
print(G)