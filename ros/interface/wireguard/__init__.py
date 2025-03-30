from typing import Any, List

from ros._base import BaseProps
from .wireguard import Wireguard
from .peers import WireguardPeer


class WireguardModule(BaseProps[Wireguard]):
    _peers: BaseProps[WireguardPeer] = None

    @property
    def peers(self) -> BaseProps[WireguardPeer]:
        if not self._peers:
            self._peers = BaseProps(self.ros, "/interface/wireguard/peers", WireguardPeer)
        return self._peers

    def print(self, **kwds: Any) -> List[Wireguard]:
        return self.ros.get_as("/interface/wireguard", List[Wireguard], kwds)


__all__ = [
    "Wireguard",
    "WireguardPeer",
    "WireguardModule",
]
