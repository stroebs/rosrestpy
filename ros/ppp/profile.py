from attr import dataclass

from ._literals import YesNoDefault, YesNoDefaultRequired


@dataclass
class PPPProfile:
    name: str
    address_list: str = None
    bridge_learning: YesNoDefault = "default"
    change_tcp_mss: YesNoDefault = "yes"
    default: bool = False
    on_down: str = None
    on_up: str = None
    only_one: YesNoDefault = "default"
    use_compression: YesNoDefault = "default"
    use_encryption: YesNoDefaultRequired = "default"
    use_ipv6: YesNoDefaultRequired = "yes"
    use_mpls: YesNoDefaultRequired = "default"
    use_upnp: YesNoDefault = "default"
    bridge: str = None
    bridge_horizon: int = None
    bridge_path_cost: int = None
    bridge_port_priority: str = None
    comment: str = None
    dhcpv6_pd_pool: str = None
    dns_server: str = None
    idle_timeout: str = None
    incoming_filter: str = None
    insert_queue_before: str = None
    interface_list: str = None
    local_address: str = None
    outgoing_filter: str = None
    parent_queue: str = None
    queue_type: str = None
    rate_limit: str = None
    remote_address: str = None
    remote_ipv6_prefix_pool: str = None
    session_timeout: str = None
    wins_server: str = None
    id: str = None

    def __str__(self) -> str:
        return self.name
