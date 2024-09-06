base_skill_unlocks = [
    "Attack",
    "Strength",
    "Defence",
    "Hitpoints",
    "Ranged",
    "Magic",
    "Prayer",
    "Slayer",
    "Woodcutting",
    "Fishing",
    "Firemaking",
    "Cooking",
    "Mining",
    "Smithing",
    "Thieving",
    "Farming",
    "Fletching",
    "Crafting",
    "Runecrafting",
    "Herblore",
    "Agility",
    "Summoning",
    "Astrology",
    "Township"
]

base_pets = [
    # Woodcutting
    "Beavis",
    # Fishing
    "Pudding Duckie",
    # Firemaking
    "Pyro",
    # Cooking
    "Cris",
    # Mining
    "CoolRock",
    # Smithing
    "Puff, the Baby Dragon",
    # Farming
    "Larry,the Lonely Lizard",
    # Attack
    "Bruce",
    # Strength
    "Lil Ron",
    # Defence
    "Leonardo",
    # Hitpoints
    "Finn, the Cat",
    # Kill 42,069 goblins
    "Golden Golbin",
    # Mastery
    "Ty",
    # Chicken Coop
    "Chick",
    # Undead Graveyard
    "Zarrah",
    # Bandit Base
    "Chio",
    # Hall of Wizards
    "Bouncing Bob",
    # Spider Forest
    "Rosey",
    # Deep Sea Ship
    "Ayyden",
    # Frozen Cove
    "Arctic Yeti",
    # Volcanic Cave
    "Mac",
    # Thieving
    "Snek",
    # Fletching
    "Quill",
    # Crafting
    "Caaarrrlll",
    # Runecrafting
    "Gunter",
    # Herblore
    "Gronk",
    # Ranged
    "Marahute",
    # Magic
    "Salem",
    # Prayer
    "Monk-ey",
    # Slayer
    "Asura",
    # Perilous Peaks
    "Peri",
    # Dark Waters
    "Otto",
    # Miolite Caves
    "Jelly Jim",
    # Dragons Den
    "Harley",
    # Infernal Stronghold
    "Singe",
    # Air God Dungeon
    "Aquarias",
    # Water God Dungeon
    "Norman",
    # Earth God Dungeon
    "Erran",
    # Fire God Dungeon
    "Ren"
    # Into the Mist
    "Pablo",
    # Summoning
    "Tim the Wolf",
    # Summoning
    "Mark",
    # Impending Darkness Event
    "Bone",
    # Astrology
    "Astro",
    # Township, Malcs Cats
    "Marcy",
    # Township, Malcs Cats
    "Roger",
    # Township, Malcs Cats
    "Layla",
    # Township, Malcs Cats
    "Mister Fuzzbutt",
    # Township, Malcs Cats
    "Octavius Lepidus VIII",
    # Mastery level 120
    "Saki",
    # Stronghold of the Undead
    "Hades",
    # Stronghold of Magic
    "Caleb",
    # Stronghold of Dragons
    "Cindar",
    # Stronghold of the Gods
    "Maxwell"
]

base_event_pets = [
    # Event only, just cosmetic
    "Ripper the Reindeer",
    # Event only, just cosmetic
    "Festive Cool Rock",
    # Event only, just cosmetic
    "Festive Chio",
]

base_goblin_raid_pets = [
    # Golbin Raid Shop
    "Jerry the Giraffe",
    # Golbin Raid Shop
    "Preston the Platypus",
]

# This array must maintain a consistent order because the IDs are generated from it.
all_items = [
    *base_skill_unlocks,
    *base_pets,
    *base_event_pets,
    *base_goblin_raid_pets
]

progression_items = [
    *base_skill_unlocks
]

useful_items = [
    *base_pets
]

filler_items = [
    *base_event_pets,
    *base_goblin_raid_pets
]
