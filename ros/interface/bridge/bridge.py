from attr import dataclass
from typing import Literal

from ros._literals import ARPLiteral

ProtocolModeLiteral = Literal["mstp", "rstp", "stp", "none"]
PortCostModeLiteral = Literal["long", "short"]

@dataclass
class Bridge:
    name: str
    arp: ARPLiteral = "enabled"
    ageing_time: str = "5m"
    mtu: str = None
    arp_timeout: str = None
    auto_mac: bool = True
    dhcp_snooping: bool = False
    igmp_snooping: bool = False
    admin_mac: str = None
    disabled: bool = None
    fast_forward: bool = True
    priority: str = "0x8000"
    protocol_mode: ProtocolModeLiteral = "rstp"
    port_cost_mode: PortCostModeLiteral = "long"
    max_message_age: str = "20s"
    forward_delay: str = "15s"
    transmit_hold_count: int = 6
    max_hops: int = 20
    vlan_filtering: bool = False
    comment: str = None
    mac_address: str = None
    actual_mtu: int = None
    l2mtu: int = None
    running: bool = None
    id: str = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
