import logging
from typing import TYPE_CHECKING, List

from BaseClasses import CollectionState

from .Data import Items, Locations

if TYPE_CHECKING:
    from . import MelvorWorld

id_offset: int = 20201120

debug_mode: bool = False

item_name_to_id = {name: id for id, name in enumerate(Items.all_items, id_offset)}
location_name_to_id = {location.name: id for id, location in enumerate(Locations.all_locations, id_offset)}