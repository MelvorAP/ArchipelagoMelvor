import typing
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Type, List

from Options import (Choice, DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle, Range, OptionSet, TextChoice,
                     DefaultOnToggle)


class ExpGain(Range):
    """
    Set how much level experience you get in the game. This value is additive.
    """
    display_name = "Experience Gain Percentage"
    range_start = -90
    range_end = 900
    default = 0


class MasteryGain(Range):
    """
    Set how much mastery experience you get in the game. This value is additive.
    """
    display_name = "Mastery Gain Percentage"
    range_start = -90
    range_end = 900
    default = 0


class CurrencyGain(Range):
    """
    Set how much mastery experience you get in the game. This value is additive.
    """
    display_name = "Mastery Gain Percentage"
    range_start = -90
    range_end = 900
    default = 0


class SlayerCoinGain(Range):
    """
    Set how much mastery experience you get in the game. This value is additive.
    """
    display_name = "Mastery Gain Percentage"
    range_start = -90
    range_end = 900
    default = 0


class MaxMasteryPoolCap(Range):
    """
    Increase the cap of the mastery pool. The when set to 0 the value is 100.
    """
    display_name = "Increase Mastery Pool Cap"
    range_start = 0
    range_end = 900
    default = 0


class BankSpaceIncrease(Range):
    """
    Increase the starting bank space. The when set to 0 the value is 20.
    """
    display_name = "Increase Mastery Pool Cap"
    range_start = 0
    range_end = 980
    default = 0


@dataclass
class MelvorGameOptions(PerGameCommonOptions):
    exp_gain: ExpGain
    mastery_gain: MasteryGain
    currency_gain: CurrencyGain
    slayer_gain: SlayerCoinGain
    max_mastery_pool_cap: MaxMasteryPoolCap
    bank_space_increase: BankSpaceIncrease
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
