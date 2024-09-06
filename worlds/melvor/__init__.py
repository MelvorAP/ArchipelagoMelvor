import logging
import typing

from BaseClasses import Region, Location, Item, ItemClassification, CollectionState, Tutorial
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import WebWorld, World
from typing import List, Callable, Dict, Any, Set

from . import Constants
from .Options import MelvorGameOptions


class MelvorLocation(Location):
    game = "Melvor Idle"


class MelvorItem(Item):
    game = "Melvor Idle"


class MelvorWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Melvor Idle with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["PixieCatSupreme"]
    )]


class MelvorWorld(World):
    """
    Anodyne is a unique Zelda-like game, influenced by games such as Yume Nikki and Link's Awakening.
    In Anodyne, you'll visit areas urban, natural, and bizarre, fighting your way through dungeons
    and areas in Young's subconscious.
    """
    game = "Melvor Idle"  # name of the game/world
    web = MelvorWebWorld()

    options_dataclass = MelvorGameOptions
    options: MelvorGameOptions

    item_name_to_id = Constants.item_name_to_id
    location_name_to_id = Constants.location_name_to_id

    data_version = 1

    def fill_slot_data(self):
        return {
            "victory_condition": int(self.options.victory_condition),

            "useful_pet_locations": bool(self.options.useful_pet_locations),

            "is_permaDeath": bool(self.options.is_permaDeath),
            "item_doubling": bool(self.options.item_doubling),
            "preservation": bool(self.options.preservation),
            "has_regen": bool(self.options.has_regen),

            "exp_gain": int(self.options.exp_gain),
            "mastery_gain": int(self.options.mastery_gain),
            "currency_gain": int(self.options.currency_gain),
            "slayer_gain": int(self.options.slayer_gain),
            "max_mastery_pool_cap": int(self.options.max_mastery_pool_cap),
            "bank_space_increase": int(self.options.bank_space_increase),

            "death_link": bool(self.options.death_link.value)
        }

    # for the universal tracker, doesn't get called in standard gen
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
