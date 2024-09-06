from typing import NamedTuple, List


class ChestData(NamedTuple):
    name: str
    loot: List[str] = []


chests: List[ChestData] = [
    ChestData("Treasure Chest",
              [
                  "Old Boot",
                  "Shell",
                  "Rope ",
                  "Glass Bottle",
                  "Rusty Key",
                  "Old Hat",
                  "Seaweed",
                  "Rubber Ducky",
                  "Shark",
                  "Manta Ray",
                  "Steel Bar",
                  "Mithril Bar",
                  "Whale",
                  "Runite Bar",
                  "Dragonite Bar",
                  "Amulet of Fishing"
              ]),
    ChestData("Chest of Witwix",
              [
                  "Topaz",
                  "Ruby",
                  "Sapphire",
                  "Emerald",
                  "Diamond",
                  "Amulet of Fury"
              ])
]
