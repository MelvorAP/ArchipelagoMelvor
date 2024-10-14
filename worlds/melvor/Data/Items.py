from typing import NamedTuple


class ProgressiveSkillData(NamedTuple):
    name: str
    progression_count: int
    max_level: int

demo_skill_unlocks = [
    "Attack",
    "Strength",
    "Defence",
    "Hitpoints",
    "Woodcutting",
    "Fishing",
    "Firemaking",
    "Cooking",
    "Mining",
    "Smithing",
    "Farming"
]

demo_progressive_skills_unlocks = [
    "Progressive Woodcutting",
    "Progressive Fishing",
    "Progressive Firemaking",
    "Progressive Cooking",
    "Progressive Mining",
    "Progressive Smithing",
    "Progressive Farming"
]

demo_pets = [
    "Beavis",
    "Pudding Duckie",
    "Pyro",
    "Cris",
    "Cool Rock",
    "Puff, the Baby Dragon",
    "Larry, the Lonely Lizard",
    "Bruce",
    "Lil Ron",
    "Leonardo",
    "Finn, the Cat",
    "Golden Golbin",
    "Ty",
    "Chick",
    "Zarrah",
    "Chio",
    "Bouncing Bob",
    "Rosey",
    "Ayyden",
    "Arctic Yeti",
    "Mac",
]

demo_event_pets = [
    # Event only, just cosmetic
    "Ripper the Reindeer",
    # Event only, just cosmetic
    "Festive Cool Rock",
    # Event only, just cosmetic
    "Festive Chio",
]

demo_goblin_raid_pets = [
    # Golbin Raid Shop
    "Jerry the Giraffe",
    # Golbin Raid Shop
    "Preston the Platypus",
]

demo_progressive_skill_count = [
    ["Progressive Woodcutting", 9],
    ["Progressive Fishing", 17],
    ["Progressive Firemaking", 9],
    ["Progressive Cooking", 31],
    ["Progressive Mining", 11],
    ["Progressive Smithing", 7],
    ["Progressive Farming", 24]
]

demo_progressive_woodcutting = [
    ProgressiveSkillData("Normal Tree", 1, 10),
    ProgressiveSkillData("Oak Tree", 2, 25),
    ProgressiveSkillData("Willow Tree", 3, 35),
    ProgressiveSkillData("Teak Tree", 4, 45),
    ProgressiveSkillData("Maple Tree", 5, 55),
    ProgressiveSkillData("Mahogany Tree", 6, 60),
    ProgressiveSkillData("Yew Tree", 7, 75),
    ProgressiveSkillData("Magic Tree", 8, 90),
    ProgressiveSkillData("Redwood Tree", 9, 99)
]

# This array must maintain a consistent order because the IDs are generated from it.
all_items = [
    *demo_skill_unlocks,
    *demo_progressive_skills_unlocks,
    *demo_pets,
    *demo_event_pets,
    *demo_goblin_raid_pets
]

progression_items = [
    *demo_skill_unlocks,
    *demo_progressive_skills_unlocks,
]

useful_items = [
    *demo_pets
]

filler_items = [
    *demo_event_pets,
    *demo_goblin_raid_pets
]
