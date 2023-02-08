from ros._base import BaseModule, BaseProps

from .interface import InterfaceQueue
from .simple import SimpleQueue


class QueueModule(BaseModule):
    _interface: BaseProps[InterfaceQueue] = None
    _simple: BaseProps[SimpleQueue] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self, self.url + "/interface", InterfaceQueue)
        return self._interface

    @property
    def simple(self):
        if not self._simple:
            self._simple = BaseProps(self, self.url + "/simple", SimpleQueue)
        return self._simple
