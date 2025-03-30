from attr import dataclass

from typing import Literal

EdgeLiteral = Literal["auto", "no", "no discover", "yes", "yes discover"]
FrameTypesLiteral = Literal["admit-all", "admit-only-untagged-and-priority-tagged", "admit-only-vlan-tagged"]
LearnLiteral = Literal["auto", "no", "yes"]
MulticastRouterLiteral = Literal["temporary-query", "permanent", "disabled"]
PointToPointLiteral = Literal["auto", "no", "yes"]
MvrpRegistrarStateLiteral = Literal["normal", "fixed"]
MvrpApplicantStateLiteral = Literal["non-participant", "normal-participant"]


@dataclass
class BridgePort:
    interface: str
    bridge: str
    horizon: str = None
    learn: LearnLiteral = "auto"
    unknown_multicast_flood: bool = True
    unknown_unicast_flood: bool = True
    broadcast_flood: bool = True
    trusted: bool = False
    multicast_router: MulticastRouterLiteral = "temporary-query"
    fast_leave: bool = False
    priority: str = "0x80"
    path_cost: str = None
    internal_path_cost: int = None
    edge: EdgeLiteral = "auto"
    point_to_point: PointToPointLiteral = "auto"
    auto_isolate: bool = False
    restricted_role: bool = False
    restricted_tcn: bool = False
    bpdu_guard: bool = False
    pvid: int = 1
    frame_types: FrameTypesLiteral = "admit-all"
    ingress_filtering: bool = True
    tag_stacking: bool = False
    mvrp_registrar_state: MvrpRegistrarStateLiteral = "normal"
    mvrp_applicant_state: MvrpApplicantStateLiteral = "normal-participant"
    status: str = None
    disabled: bool = None
    dynamic: bool = None
    inactive: bool = None
    comment: str = None
    nextid: str = None
    id: str = None

    def __bool__(self) -> bool:
        return not self.disabled
