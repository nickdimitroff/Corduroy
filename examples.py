from typing import List

from corduroy import (Computer, Cord, Keyboard, Monitor, Mouse, build_graph,
                      get_devices, segments)

def use_existing_devices():
    """ Use existing devices from data/devices.txt to build your list """
    devices: List = []
    devices = get_devices(["test laptop", "usb mouse"])
    G = build_graph(devices)
    print(G)
    segments(G)

def use_custom_devices():
    """ Create custom devices directly to build your list """
    devices: List = []
    devices.append(Mouse(name="mouse", cord="USB-A"))
    devices.append(Keyboard(name="keyboard", cord="USB-A"))
    devices.append(Computer(name="laptop", ports=["USB-A", "USB-A", "USB-C"]))
    devices.append(Monitor(name="monitor", ports=["USB-C"]))
    G = build_graph(devices)
    print(G)


use_existing_devices()