import typing
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Type, List

from Options import (DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle, Range, Choice)


class ProgressiveSkills(Toggle):
    """
    Select whether the skill action unlocks are progressive or not. If turned on, you will unlock all skill actions
    in order. If turned off, you will unlock all skill actions in a random order. Do note that unlock requirements still
    apply.
    """
    display_name = "Pet Location Items"
    default = 1


class RemoveSkillActionLevels(Toggle):
    """
    Select whether skill actions allow to be done on level 1. This way you don't need to grind to use unlocked
    skill actions.
    """
    display_name = "Remove Skill Action Level Requirements"
    default = 1


class VictoryCondition(Choice):
    """
    Select the end goal of your game.
    [Max Level] Reach the maximum level in every skill.
    [Max Level and Mastery] Reach the maximum level and mastery in every skill.
    [All Kills] Kill every enemy in the game at least once.
    [Completion] Get 100% completion in the Completion Log.
    """
    display_name = "Victory Condition"
    option_max_level = 0
    # option_max_level_and_mastery = 1
    # option_max_all_kills = 2
    # option_max_completion = 3
    default = 0


class UsefulPetLocations(Toggle):
    """
    Pet locations can have progression items or useful items. Pets usually take a while to unlock.
    """
    display_name = "Pet Location Items"
    default = 0


class Difficulty(Choice):
    """
    Set how difficult the game is.
    [Easy] No permadeath and no items lost on death.
    [Normal] No permadeath, but a random item is lost on death.
    [Hard] When you die, you lose your save. Be aware of death link.
    """
    display_name = "Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1


class ItemDoubling(Toggle):
    """
    Set if items can be doubles when crafting.
    """
    display_name = "Item Doubling"
    default = 1


class Preservation(Toggle):
    """
    Set if ingredients can be preserved in crafting.
    """
    display_name = "Ingredient Doubling"
    default = 1


class HasRegen(Toggle):
    """
    Set if not being in combat automatically heals the player.
    """
    display_name = "Has Regen"
    default = 1


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
    Set how much currency you get in the game. This value is additive.
    """
    display_name = "Mastery Gain Percentage"
    range_start = -90
    range_end = 900
    default = 0


class SlayerCoinGain(Range):
    """
    Set how much slayer coins you get in the game. This value is in percentage and is additive.
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
    range_end = 500
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
    progressive_skills: ProgressiveSkills
    remove_skill_action_levels: RemoveSkillActionLevels

    victory_condition: VictoryCondition

    useful_pet_locations: UsefulPetLocations

    difficulty: Difficulty
    item_doubling: ItemDoubling
    preservation: Preservation
    has_regen: HasRegen

    exp_gain: ExpGain
    mastery_gain: MasteryGain
    currency_gain: CurrencyGain
    slayer_gain: SlayerCoinGain
    max_mastery_pool_cap: MaxMasteryPoolCap
    bank_space_increase: BankSpaceIncrease

    start_inventory_from_pool: StartInventoryPool

    death_link: DeathLink
