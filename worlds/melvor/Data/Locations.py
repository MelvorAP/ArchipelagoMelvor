from enum import Enum, IntEnum
from typing import NamedTuple, List, Dict


class LocationType(IntEnum):
    NONE = 0,
    PET = 1,
    ACTION = 2,
    STORE = 3,
    COMBAT = 4,


class CombatType(IntEnum):
    NONE = 0,
    MELEE = 1,
    RANGED = 2,
    MAGIC = 3,
    ALL = 4


class LocationData(NamedTuple):
    name: str
    region_name: str
    reqs: List[str] = []
    loot: List[str] = []
    location_type: LocationType = LocationType.NONE
    source_of_gp: bool = False
    source_of_sc: bool = False
    combat_easy: bool = False
    combat_type: CombatType = CombatType.NONE
    inverted_combat_tree: bool = False


# This array must maintain a consistent order because the IDs are generated from it.
all_locations: List[LocationData] = [
    # Combat Pets
    LocationData("Pet - Bruce",
                 "Attack",
                 ["Attack"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Lil Ron",
                 "Strength",
                 ["Strength"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Leonardo",
                 "Defence",
                 ["Defence"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Finn, the Cat",
                 "Hitpoints",
                 ["Hitpoints"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Finn, the Cat",
                 "Hitpoints",
                 ["Hitpoints"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Larry, the Lonely Lizard",
                 "Farming",
                 ["Farming"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Beavis",
                 "Woodcutting",
                 ["Woodcutting"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Pudding Duckie",
                 "Fishing",
                 ["Fishing"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Pyro",
                 "Firemaking",
                 ["Firemaking"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Cool Rock",
                 "Mining",
                 ["Mining"],
                 [],
                 location_type=LocationType.PET
                 ),
    LocationData("Pet - Puff, the Baby Dragon",
                 "Smithing",
                 ["Smithing"],
                 [],
                 location_type=LocationType.PET
                 ),
    # Combat
    LocationData("Combat - FarmLands - Plant",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Potatoes"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_easy=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - FarmLands - Chicken",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Bones",
                     "Feathers",
                     "Raw Chicken"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_easy=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - FarmLands - Cow",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Bones",
                     "Leather",
                     "Raw Beef"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - FarmLands - Junior Farmer",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Bones",
                     "Potato Seeds",
                     "Garum Seeds",
                     "Onion Seeds",
                     "Cabbage Seeds",
                     "Tomato Seeds"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - FarmLands - Adult Farmer",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Bones",
                     "Onion Seeds",
                     "Cabbage Seeds",
                     "Tomato Seeds",
                     "Sourweed Seeds",
                     "Mantalyme Seeds",
                     "Sweetcorn Seeds",
                     "Strawberry Seeds",
                     "Watermelon Seeds",
                     "Compost",
                     "Oak Tree Seeds",
                     "Snape Grass Seeds"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - FarmLands - Adult Farmer",
                 "Combat Area - Farmlands",
                 [],
                 [
                     "Bones",
                     "Tomato Seeds",
                     "Sweetcorn Seeds",
                     "Oak Tree Seeds",
                     "Lemontyle Seeds",
                     "Strawberry Seeds",
                     "Oxilyme Seeds",
                     "Willow Tree Seeds",
                     "Watermelon Seeds",
                     "Compost",
                     "Maple Tree Seeds",
                     "Snape Grass Seeds",
                     "Yew Tree Seeds",
                     "Magic Tree Seeds",
                     "Bob's Rake"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Goblin Village - Goblin",
                 "Combat Area - Goblin Village",
                 [],
                 [
                     "Bones",
                     "Water Rune",
                     "Body Rune",
                     "Raw Shrimp",
                     "Garum Seeds",
                     "Bronze Shield",
                     "Bronze Battleaxe",
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Goblin Village - Ranged Goblin",
                 "Combat Area - Goblin Village",
                 [],
                 [
                     "Bones",
                     "Bronze Arrows",
                     "Raw Shrimp",
                     "Garum Seeds",
                     "Normal Shortbow",
                     "Slingshot",
                     "Oak Shortbow",
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.RANGED
                 ),
    LocationData("Combat - Graveyard - Skeleton",
                 "Combat Area - Graveyard",
                 [],
                 [
                     "Bones",
                     "Headless Arrows"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Graveyard - Zombie Hand",
                 "Combat Area - Graveyard",
                 [],
                 [
                     "Bones",
                     "Bronze Platebody",
                     "Bronze Platelegs",
                     "Iron Platebody",
                     "Iron Platelegs"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Graveyard - Zombie",
                 "Combat Area - Graveyard",
                 [],
                 [
                     "Bones",
                     "Garum Seeds"
                     "Iron Platebody",
                     "Iron Platelegs",
                     "Steel Platebody",
                     "Steel Platelegs"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Graveyard - Ghost",
                 "Combat Area - Graveyard",
                 [],
                 [
                     "Bones",
                     "Oxilyme Seeds"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Sandy Shores - Seagull",
                 "Combat Area - Sandy Shores",
                 [],
                 [
                     "Bones",
                     "Feathers"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Sandy Shores - Tentacle",
                 "Combat Area - Sandy Shores",
                 [],
                 [
                     "Bones",
                     "Iron Ore",
                     "Coal Ore",
                     "Raw Sardine",
                     "Raw Herring",
                     "Burnt Cave Fish",

                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Sandy Shores - Giant Crab",
                 "Combat Area - Sandy Shores",
                 [],
                 [
                     "Raw Crab",
                     "Treasure Chest",

                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Sandy Shores - Confused Pirate",
                 "Combat Area - Sandy Shores",
                 [],
                 [
                     "Steel Scimitar",
                     "Black Scimitar",
                     "Mithril Scimitar",
                     "Adamant Scimitar",
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Wet Forest - Leech",
                 "Combat Area - Wet Forest",
                 [],
                 [
                     "Garum Seeds",
                     "Chest of Witwix"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
    LocationData("Combat - Wet Forest - Sweaty Monster",
                 "Combat Area - Wet Forest",
                 [],
                 [
                     "Raw Salmon",
                     "Raw Trout",
                     "Salmon",
                     "Silver Ore",
                     "Lobster",
                     "Maple Logs",
                     "Mithril Ore",
                     "Oxilyme Seeds",
                     "Raw Lobster",
                     "Steel Bar",
                     "Teak Logs",
                     "Gold Bar",
                     "Topaz",
                     "Mithril Bar",
                     "Adamantite Ore",
                     "Amulet of Accuracy",
                     "Shark",
                     "Yew Logs"
                 ],
                 location_type=LocationType.COMBAT,
                 source_of_gp=True, combat_type=CombatType.MELEE
                 ),
]

locations_by_name: Dict[str, LocationData] = {location.name: location for location in all_locations}


def build_locations_by_region_dict():
    result: Dict[str, List[LocationData]] = {}
    for location in all_locations:
        result.setdefault(location.region_name, []).append(location)
    return result


locations_by_region: Dict[str, List[LocationData]] = build_locations_by_region_dict()
