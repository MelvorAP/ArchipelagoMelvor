from typing import NamedTuple


class ProgressiveSkillData(NamedTuple):
    name: str
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
    # These pets are just cosmetic
    "Ripper the Reindeer",
    "Festive Cool Rock",
    "Festive Chio",
]

demo_goblin_raid_pets = [
    "Jerry the Giraffe",
    "Preston the Platypus",
]

demo_progressive_woodcutting = [
    ProgressiveSkillData("Normal Tree", 10),
    ProgressiveSkillData("Oak Tree", 25),
    ProgressiveSkillData("Willow Tree", 35),
    ProgressiveSkillData("Teak Tree", 45),
    ProgressiveSkillData("Maple Tree", 55),
    ProgressiveSkillData("Mahogany Tree", 60),
    ProgressiveSkillData("Yew Tree", 75),
    ProgressiveSkillData("Magic Tree", 90),
    ProgressiveSkillData("Redwood Tree", 99)
]

demo_progressive_fishing = [
	ProgressiveSkillData("Raw Sardine", 5),
	ProgressiveSkillData("Raw Blowfish", 8),
	ProgressiveSkillData("Raw Herring", 10),
	ProgressiveSkillData("Raw Seahorse", 15),
	ProgressiveSkillData("Raw Trout", 20),
	ProgressiveSkillData("Leaping Trout", 20),
	ProgressiveSkillData("Raw Poison Fish", 30),
	ProgressiveSkillData("Raw Salmon", 35),
	ProgressiveSkillData("Leaping Salmon", 35),
	ProgressiveSkillData("Raw Lobster", 40),
	ProgressiveSkillData("Raw Skeleton Fish", 45),
	ProgressiveSkillData("Raw Swordfish", 50),
	ProgressiveSkillData("Raw Anglerfish", 50),
	ProgressiveSkillData("Raw Fanfish", 55),
	ProgressiveSkillData("Raw Crab", 60),
	ProgressiveSkillData("Raw Carp", 65),
	ProgressiveSkillData("Raw Shark", 70),
	ProgressiveSkillData("Leaping Broad Fish", 70),
	ProgressiveSkillData("Raw Cave Fish", 75),
	ProgressiveSkillData("Raw Magic Fish", 80),
	ProgressiveSkillData("Raw Manta Ray", 85),
	ProgressiveSkillData("Raw Whale", 95),
]

demo_progressive_firemaking = [
    ProgressiveSkillData("Oak Logs", 10),
    ProgressiveSkillData("Willow Logs", 25),
    ProgressiveSkillData("Teak Logs", 35),
    ProgressiveSkillData("Maple Logs", 45),
    ProgressiveSkillData("Mahogany Logs", 55),
    ProgressiveSkillData("Yew Logs", 60),
    ProgressiveSkillData("Magic Logs", 75),
    ProgressiveSkillData("Redwood Logs", 90),
]

demo_progressive_cooking = [
    ProgressiveSkillData("Chicken", 4),
    ProgressiveSkillData("Sardine", 5),
    ProgressiveSkillData("Plain Pizza Slice", 9),
    ProgressiveSkillData("Herring", 10),
    ProgressiveSkillData("Seahorse", 15),
    ProgressiveSkillData("Beef Pie", 17),
    ProgressiveSkillData("Trout", 20),
    ProgressiveSkillData("Meat Pizza Slice", 25),
    ProgressiveSkillData("Basic Soup", 33),
    ProgressiveSkillData("Salmon", 35),
    ProgressiveSkillData("Lobster", 40),
    ProgressiveSkillData("Strawberry Cupcake", 41),
    ProgressiveSkillData("Hearty Soup", 49),
    ProgressiveSkillData("Swordfish", 50),
    ProgressiveSkillData("Anglerfish", 50),
    ProgressiveSkillData("Fanfish", 55),
    ProgressiveSkillData("Cherry Cupcake", 57),
    ProgressiveSkillData("Crab", 60),
    ProgressiveSkillData("Carp", 65),
    ProgressiveSkillData("Cream Corn Soup", 65),
    ProgressiveSkillData("Shark", 70),
    ProgressiveSkillData("Cave Fish", 75),
    ProgressiveSkillData("Chicken Soup", 81),
    ProgressiveSkillData("Manta Ray", 85),
    ProgressiveSkillData("Strawberry Cake", 89),
    ProgressiveSkillData("Whale", 95),
    ProgressiveSkillData("Carrot Cake", 97),
]

demo_progressive_mining = [
    ProgressiveSkillData("Iron", 15),
    ProgressiveSkillData("Coal", 30),
    ProgressiveSkillData("Silver", 30),
    ProgressiveSkillData("Gold", 40),
    ProgressiveSkillData("Mithril", 50),
    ProgressiveSkillData("Adamantite", 70),
    ProgressiveSkillData("Runite", 80),
    ProgressiveSkillData("Dragonite", 95),
]

demo_progressive_smithing = [
    ProgressiveSkillData("Iron Bar", 10),
    ProgressiveSkillData("Steel Bar", 25),
    ProgressiveSkillData("Silver Bar", 30),
    ProgressiveSkillData("Gold Bar", 40),
    ProgressiveSkillData("Mithril Bar", 40),
    ProgressiveSkillData("Adamantite Bar", 55),
    ProgressiveSkillData("Runite Bar", 70),
    ProgressiveSkillData("Dragonite Bar", 85),
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
