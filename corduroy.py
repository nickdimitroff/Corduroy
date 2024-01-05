from dataclasses import dataclass
from typing import List, Optional

import matplotlib.pyplot as plt
import networkx

PERIPHERAL_DEFAULT_CORD = "USB-A"

@dataclass
class Mouse:
    name: str = "mouse"
    cord: Optional[str] = PERIPHERAL_DEFAULT_CORD
    port: Optional[str] = None
    protocol: Optional[str] = None

@dataclass
class Keyboard:
    name: str = "keyboard"
    cord: Optional[str] = PERIPHERAL_DEFAULT_CORD
    port: Optional[str] = None
    protocol: Optional[str] = None

@dataclass
class Computer:
    ports: List[str]
    name: str = "computer"

@dataclass
class Monitor:
    ports: List[str]
    name: str = "monitor"

@dataclass
class Adapter:
    name: str = "adapter"
    cord: Optional[str] = PERIPHERAL_DEFAULT_CORD
    port: Optional[str] = PERIPHERAL_DEFAULT_CORD

@dataclass
class Cord:
    cords: List[str]
    name: str = "cord"

def build_graph(listOfDevices) -> List[str]:
    ret: List = []
    # MultiGraph to allow parallel edges
    G = networkx.MultiGraph()
    for d in listOfDevices:
        G.add_node(d.name)
        print(d)
        if hasattr(d, 'port') and d.port is not None:
            G.add_edge(d.name, d.port, weight=0)
        if hasattr(d, 'cord') and d.cord is not None:
            G.add_edge(d.name, d.cord, weight=1)
        if hasattr(d, 'ports') and d.ports is not None:
            for port in d.ports:
                G.add_edge(d.name, port, weight=0)
        if hasattr(d, 'cords') and d.cords is not None:
            for cord in d.cords:
                G.add_edge(d.name, cord, weight=1)
    return(G)

def get_devices(somelist):
    devices = []
    with open("data/devices.txt") as input:
        for line in input:
            line = line.strip()
            for item in somelist:
                if item in line:
                    devices.append(eval(line))
    return(devices)

def display(G):
    networkx.draw(G, networkx.planar_layout(G), with_labels=True)

    edge_labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in G.edges(data=True)])

    networkx.draw_networkx_edge_labels(G, networkx.planar_layout(G), edge_labels=edge_labels,
                                font_color='red', font_weight='bold')

    ax = plt.gca()
    ax.margins(0.50)
    plt.axis("off")
    plt.show()
