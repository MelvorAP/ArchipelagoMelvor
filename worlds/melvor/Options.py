import typing
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Type, List

from Options import (Choice, DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle, Range, OptionSet, TextChoice,
                     DefaultOnToggle)


class ExpGain(Range):
    """
    Set how much level experience you get in the game.
    """
    display_name = "Experience Gain Percentage"
    range_start = 10
    range_end = 1000
    default = 100

class MasteryGain(Range):
    """
    Set how much mastery experience you get in the game.
    """
    display_name = "Mastery Gain Percentage"
    range_start = 10
    range_end = 1000
    default = 100

@dataclass
class MelvorGameOptions(PerGameCommonOptions):
    exp_gain: ExpGain
    mastery_gain: MasteryGain
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
