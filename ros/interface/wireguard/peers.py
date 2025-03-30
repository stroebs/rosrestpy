from attr import dataclass


@dataclass
class WireguardPeer:
    interface: str
    public_key: str
    allowed_address: str
    name: str = None
    private_key: str = None
    endpoint: str = None
    endpoint_port: str = None
    preshared_key: str = None
    persistent_keepalive: str = None
    responder: bool = False
    client_address: str = None
    client_dns: str = None
    client_endpoint: str = None
    client_keepalive: str = None
    client_listen_port: str = None
    current_endpoint_address: str = None
    current_endpoint_port: str = None
    tx: str = None
    rx: str = None
    comment: str = None
    disabled: bool = False
    copy_from: str = None
    dynamic: bool = None
    id: str = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
