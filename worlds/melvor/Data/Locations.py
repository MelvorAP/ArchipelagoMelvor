from typing import NamedTuple, List, Dict


class LocationData(NamedTuple):
    name: str
    region_name: str
    reqs: List[str] = []
    combat_melee: bool = False
    combat_ranged: bool = False
    combat_magic: bool = False


# This array must maintain a consistent order because the IDs are generated from it.
all_locations: List[LocationData] = [
    LocationData("Combat - FarmLands - Plant", "Combat", ["Farmlands"], combat_melee=True),
]

locations_by_name: Dict[str, LocationData] = {location.name: location for location in all_locations}


def build_locations_by_region_dict():
    result: Dict[str, List[LocationData]] = {}
    for location in all_locations:
        result.setdefault(location.region_name, []).append(location)
    return result


locations_by_region: Dict[str, List[LocationData]] = build_locations_by_region_dict()
