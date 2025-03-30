from ros import Ros, InterfaceModule
from ros.interface.bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from ros.interface.eoip import EoIP
from ros.interface.ethernet import InterfaceEthernet
from ros.interface.list import InterfaceListModule, InterfaceList, InterfaceListMember
from ros.interface.veth import Veth
from ros.interface.vlan import Vlan
from ros.interface.vrrp import Vrrp
from ros.interface.wireguard import WireguardModule, Wireguard, WireguardPeer


class TestInterface:
    def test_module(self, ros: Ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_module(self, ros: Ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge(self, ros: Ros):
        for item in ros.bridge():
            assert isinstance(item, Bridge)

    def test_msti(self, ros: Ros):
        for item in ros.bridge.msti():
            assert isinstance(item, BridgeMsti)

    def test_port(self, ros: Ros):
        for item in ros.bridge.port():
            assert isinstance(item, BridgePort)

    def test_vlan(self, ros: Ros):
        for item in ros.bridge.vlan():
            assert isinstance(item, BridgeVlan)


class TestEoIP:
    def test_eoip(self, ros: Ros):
        for item in ros.interface.eoip():
            assert isinstance(item, EoIP)


class TestEthernet:
    def test_ethernet(self, ros: Ros):
        assert ros.interface.ethernet.cl == InterfaceEthernet

    def test_list(self, ros: Ros):
        for item in ros.interface.ethernet():
            assert isinstance(item, InterfaceEthernet)


class TestList:
    def test_module(self, ros: Ros):
        assert isinstance(ros.interface.list, InterfaceListModule)

    def test_list(self, ros: Ros):
        for item in ros.interface.list.print():
            assert isinstance(item, InterfaceList)

    def test_member(self, ros: Ros):
        for item in ros.interface.list.member():
            assert isinstance(item, InterfaceListMember)


class TestVeth:
    def test_veth(self, ros: Ros):
        for item in ros.interface.veth():
            assert isinstance(item, Veth)


class TestVlan:
    def test_vlan(self, ros: Ros):
        for item in ros.interface.vlan():
            assert isinstance(item, Vlan)


class TestVrrp:
    def test_vrrp(self, ros: Ros):
        for item in ros.interface.vrrp():
            assert isinstance(item, Vrrp)


class TestWireguard:
    def test_module(self, ros: Ros):
        assert isinstance(ros.interface.wireguard, WireguardModule)
        assert isinstance(ros.wireguard, WireguardModule)
        assert isinstance(ros.interface.wireguard.peers, WireguardPeer)

    def test_wireguard(self, ros: Ros):
        for item in ros.interface.wireguard():
            assert isinstance(item, Wireguard)
