#######################################################
#
#  MoM_Save_Game_Stuff
#
#    Master of Magic save file information
#
#  Author:  John Marley
#
#######################################################

# Spellbook categories
Spellbooks = ["Nature",
              "Sorcery",
              "Chaos",
              "Life",
              "Death"
              ]

# Wizard abilites
Abilities = ["Alchemy",
             "Warlord",
             "Chaos Mastery",
             "Nature Mastery",
             "Sorcery Mastery",
             "Infernal Power",
             "Divine Power",
             "Sage Master",
             "Channeler",
             "Myrran",
             "Archmage",
             "Mana Focusing",
             "Node Mastery",
             "Famous",
             "Runemaster",
             "Conjurer",
             "Charismatic",
             "Artificer"
             ]

# All spells
Spells = ["Earth To Mud",
          "Resist Elements",
          "Wall Of Stone",
          "Giant Strength",
          "Web",
          "War Bears",
          "Stone Skin",
          "Water Walking",
          "Sprites",
          "Earth Lore",
          "Crack's Call",
          "Nature's eye",
          "Ice Bolt",
          "Giant Spiders",
          "Change Terrain",
          "PathFinding",
          "Cockatrices",
          "Transmute",
          "Nature's Cures",
          "Basilisk",
          "Elemental Armor",
          "Petrify",
          "Stone Giant",
          "Iron Skin",
          "Ice Storm",
          "Earthquake",
          "Gorgons",
          "Move Fortress",
          "Gaia's Blessing",
          "Earth Elemental",
          "Regeneration",
          "Behemoth",
          "Entangle",
          "Nature's Awareness",
          "Call Lightning",
          "Colossus",
          "Earth Gate",
          "Herb Mastery",
          "Great Wyrm",
          "Nature's Wrath",
          "Resist Magic",
          "Dispel Magic True",
          "Floating Island",
          "Guardian Wind",
          "Phantom Warriors",
          "Confusion",
          "Word Of Recall",
          "Counter Magic",
          "Nagas",
          "Psionic Blast",
          "Blur",
          "Disenchant True",
          "Vertigo",
          "Spell Lock",
          "Enchant Road",
          "Flight",
          "Wind Mastery",
          "Spell Blast",
          "Aura Of Majesty",
          "Phantom Beast",
          "Disjunction True",
          "Invisibility",
          "Wind Walking",
          "Banish",
          "Storm Giant",
          "Air Elemental",
          "Mind Storm",
          "Stasis",
          "Magic Immunity",
          "Haste",
          "Djinn",
          "Spell Ward",
          "Creature Binding",
          "Mass Invisibility",
          "Great Unsummoning",
          "Spell Binding",
          "Flying Fortress",
          "Sky Drake",
          "Suppress Magic",
          "Time Stop",
          "Warp Wood",
          "Disrupt",
          "Fire Bolt",
          "Hell Hounds",
          "Corruption",
          "Eldritch Weapon",
          "Wall of Fire",
          "Shatter",
          "Warp Creature",
          "Fire Elemental",
          "Lightning Bolt",
          "Fire Giant",
          "Chaos Channels",
          "Flame Blade",
          "Gargoyles",
          "Fireball",
          "Doombat",
          "Raise Volcano",
          "Immolation",
          "Chimeras",
          "Warp Lightning",
          "Metal Fires",
          "Chaos Spawn",
          "Doom Bolt",
          "Magic Vortex",
          "Efreet",
          "Fire Storm",
          "Warp Reality",
          "Flame Strike",
          "Chaos Rift",
          "Hydra",
          "Disintegrate",
          "Meteor Storm",
          "Great Wasting",
          "Call Chaos",
          "Chaos Surge",
          "Doom Mastery",
          "Great Drake",
          "Call The Void",
          "Armageddon",
          "Bless",
          "Star Fires",
          "Endurance",
          "Holy Weapon",
          "Healing",
          "Holy Armor",
          "Just Cause",
          "True Light",
          "Guardian Spirit",
          "Heroism",
          "True Sight",
          "Plane Shift",
          "Resurrection",
          "Dispel Evil",
          "Planar Seal",
          "Unicorns",
          "Raise Dead",
          "Planar Travel",
          "Heavenly Light",
          "Prayer",
          "Lionheart",
          "Incarnation",
          "Invulnerability",
          "Righteousness",
          "Prosperity",
          "Altar Of Battle",
          "Angel",
          "Stream Of Life",
          "Mass Healing",
          "Holy Word",
          "High Prayer",
          "Inspirations",
          "Astral Gate",
          "Holy Arms",
          "Consecration",
          "Life Force",
          "Tranquility",
          "Crusade",
          "Arch Angel",
          "Charm Of Life",
          "Skeletons",
          "Weakness",
          "Dark Rituals",
          "Cloak Of Fear",
          "Black Sleep",
          "Ghouls",
          "Life Drain",
          "Terror",
          "Darkness",
          "Mana Leak",
          "Drain Power",
          "Possession",
          "Lycantrophy",
          "Black Prayer",
          "Black Channels",
          "Night Stalker",
          "Subversion",
          "Wall Of Darkness",
          "Berserk",
          "Shadow Demons",
          "Wraith Form",
          "Wrack",
          "Evil Presence",
          "Wraiths",
          "Cloud Of Shadow",
          "Warp Node",
          "Black Wind",
          "Zombie Mastery",
          "Famine",
          "Cursed Lands",
          "Cruel Unminding",
          "Word Of Death",
          "Death Knights",
          "Death Spell",
          "Animate dead",
          "Pestilence",
          "Eternal Night",
          "Evil Omens",
          "Death Wish",
          "Demon Lord",
          "Magic Spirit",
          "Dispel Magic",
          "Summoning Circle",
          "Disenchant Area",
          "Recall Hero",
          "Detect Magic",
          "Enchant Item",
          "Summon Hero",
          "Awareness",
          "Disjunction",
          "Create Artifact",
          "Summon Champion",
          "Spell Of Mastery",
          "Spell Of Return"
          ]

# status symbols for modifying spell selection
Spell_Status = ["⬜", # unknown, not researchable
                "⬕", # unknown, researchable
                "⬛", # known
                "⛝"  # on research page
                ]

# All Heroes
Heroes = ["The Dwarf",
          "The Barbarian",
          "The Sage",
          "The Dervish",
          "The Beastmaster",
          "The Bard",
          "The Orc Warrior",
          "The Healer",
          "The Huntress",
          "The Thief",
          "The Druid",
          "The War Monk",
          "The Warrior Mage",
          "The Magician",
          "The Assassin",
          "The Wind Mage",
          "The Ranger",
          "The Draconian",
          "The Witch",
          "The Golden One",
          "The Ninja",
          "The Rogue",
          "The Amazon",
          "The Warlock",
          "The Unknown",
          "The Illusionist",
          "The Swordsman",
          "The Priestess",
          "The Paladin",
          "The Black Knight",
          "The Elven Archer",
          "The Knight",
          "The Necromancer",
          "The Chaos Warrior",
          "The Chosen"
          ]

# All hero abilities
Hero_Abils = ["Blademaster*",
              "Blademaster",
              "",
              "Legendary*",
              "Legendary",
              "",
              "Leader*",
              "Leader",
              "Might",
              "",
              "Constitution*",
              "Constitution",
              "",
              "Armsmaster*",
              "Armsmaster",
              "",
              "",
              "Sage*",
              "Sage",
              "",
              "Arcane Power*",
              "Arcane Power",
              "",
              "Might*",
              "Agility",
              "",
              "Noble",
              "Charmed",
              "Lucky",
              "Agility*",
              "Prayermaster*",
              "Prayermaster"
              ]
# All buildings
Buildings = ["Barracks",
             "Armory",
             "Fighter's Guild",
             "Armorer's Guild",
             "War College",
             "Smithy",
             "Stable",
             "Animist's Guild",
             "Fantastic Stable",
             "Shipwright's Guild",
             "Ship Yard",
             "Maritime Guild",
             "Sawmill",
             "Library",
             "Sage's Guild",
             "Oracle",
             "Alchemist Guild",
             "University",
             "Wizard's Guild",
             "Shrine",
             "Temple",
             "Parthenon",
             "Cathedral",
             "Marketplace",
             "Bank",
             "Merchant's Guild",
             "Granary",
             "Farmer's Market",
             "Forester's Guild",
             "Builder's Hall",
             "Mechanician's Guild",
             "Miner's Guild",
             "City Walls"
             ]

# building states
Building_States = {"not built":-1,
                   "replaced":0,
                   "built":1,
                   "destroyed":2
                   }

# All city Enchantments
City_Enchants = ["Wall Of Fire",
                 "Chaos Rift",
                 "Dark Rituals",
                 "Evil Presence",
                 "Cursed Lands",
                 "Pestilence",
                 "Cloud Of Shadow",
                 "Famine",
                 "Flying Fortress",
                 "Nature Ward",
                 "Sorcery Ward",
                 "Chaos Ward",
                 "Life Ward",
                 "Death Ward",
                 "Nature's Eye",
                 "Earth Gate",
                 "Stream Of Life",
                 "Gaia's Blessing",
                 "Inspirations",
                 "Prosperity",
                 "Astral Gate",
                 "Heavenly Light",
                 "Consecration",
                 "Wall Of Darkness",
                 "Altar Of Battle"
                 ]

# All units
Units = ["Trireme",
         "Galley",
         "Catapult",
         "Warship",
         "Barbarian Spearmen",
         "Barbarian Swordsmen",
         "Barbarian Bowmen",
         "Barbarian Cavalry",
         "Barbarian Shaman",
         "Barbarian Settlers",
         "Berserkers",
         "Beastmen Spearmen",
         "Beastmen Swordsmen",
         "Beastmen Halberdiers",
         "Beastmen Bowmen",
         "Beastmen Priests",
         "Beastmen Magicians",
         "Beastmen Engineers",
         "Beastmen Settlers",
         "Centaurs",
         "Manticores",
         "Minotaurs",
         "Dark Elf Spearmen",
         "Dark Elf Swordsmen",
         "Dark Elf Halberdiers",
         "Dark Elf Cavalry",
         "Dark Elf Priests",
         "Dark Elf Settlers",
         "Nightblades",
         "Warlocks",
         "Nightmares",
         "Draconian Spearmen",
         "Draconian Swordsmen",
         "Draconian Halberdiers",
         "Draconian Bowmen",
         "Draconian Shaman",
         "Draconian Magicians",
         "Draconian Engineers",
         "Draconian Settlers",
         "Doom Drakes",
         "Airship",
         "Dwarven Swordsmen",
         "Dwarven Halberdiers",
         "Dwarven Engineers",
         "Hammerhands",
         "Steam Cannon",
         "Golem",
         "Dwarven Settlers",
         "Gnoll Spearmen",
         "Gnoll Swordsmen",
         "Gnoll Halberdiers",
         "Gnoll Bowmen",
         "Gnoll Settlers",
         "Wolfriders",
         "Halfling Spearmen",
         "Halfling Swordsmen",
         "Halfling Bowmen",
         "Halfling Shaman",
         "Halfling Settlers",
         "Slingers",
         "High Elf Spearmen",
         "High Elf Swordsmen",
         "High Elf Halberdiers",
         "High Elf Cavalry",
         "High Elf Magicians",
         "High Elf Settlers",
         "Longbowmen",
         "Elven Lords",
         "Pegasai",
         "High Men Spearmen",
         "High Men Swordsmen",
         "High Men Bowmen",
         "High Men Cavalry",
         "High Men Priests",
         "High Men Magicians",
         "High Men Engineers",
         "High Men Settlers",
         "Pikemen (High Men)",
         "Paladins",
         "Klackon Spearmen",
         "Klackon Swordsmen",
         "Klackon Halberdiers",
         "Klackon Engineers",
         "Klackon Settlers",
         "Stag Beetle",
         "Lizardman Spearmen",
         "Lizardman Swordsmen",
         "Lizardman Halberdiers",
         "Javelineers",
         "Lizardman Shaman",
         "Lizardman Settlers",
         "Dragon Turtle",
         "Nomad Spearmen",
         "Nomad Swordsmen",
         "Nomad Bowmen",
         "Nomad Priests",
         "Nomad Magicians",
         "Nomad Settlers",
         "Horsebowmen",
         "Pikemen (Nomad)",
         "Rangers",
         "Griffons",
         "Orc Spearmen",
         "Orc Swordsmen",
         "Orc Halberdiers",
         "Orc Bowmen",
         "Orc Cavalry",
         "Orc Shaman",
         "Orc Magicians",
         "Orc Engineers",
         "Orc Settlers",
         "Wyvern Riders",
         "Troll Spearmen",
         "Troll Swordsmen",
         "Troll Halberdiers",
         "Troll Shaman",
         "Troll Settlers",
         "War Trolls",
         "War Mammoths",
         "Magic Spirit",
         "Hell Hounds",
         "Gargoyles",
         "Fire Giant",
         "Fire Elemental",
         "Chaos Spawn",
         "Chimera",
         "Doom Bat",
         "Efreet",
         "Hydra",
         "Great Drake",
         "Skeletons",
         "Ghouls",
         "Night Stalker",
         "Werewolves",
         "Demon",
         "Wraiths",
         "Shadow Demons",
         "Death Knights",
         "Demon Lord",
         "Zombies",
         "Unicorns",
         "Guardian Spirit",
         "Angel",
         "Arch Angel",
         "War Bears",
         "Sprites",
         "Cockatrices",
         "Basilisk",
         "Giant Spiders",
         "Stone Giant",
         "Colossus",
         "Gorgons",
         "Earth Elemental",
         "Behemoth",
         "Great Wyrm",
         "Floating Island",
         "Phantom Beast",
         "Phantom Warriors",
         "Storm Giant",
         "Air Elemental",
         "Djinn",
         "Sky Drake",
         "Nagas"
         ]

# All unit enchantments
Unit_Enchants = ["Stasis",
                 "",
                 "Undead",
                 "Demon Wings",
                 "Fire Breath",
                 "Demon Skin",
                 "",
                 "",
                 "Path Finding",
                 "Regeneration",
                 "Wraith Form",
                 "Black Channels",
                 "Cloak of Fear",
                 "Berserk",
                 "Guardian Wind",
                 "Immolation",
                 "Invisibility",
                 "Spell Lock",
                 "Endurance",
                 "Iron Skin",
                 "Stone Skin",
                 "Elemental Armor",
                 "Resist Elements",
                 "Water Walking",
                 "Holy Weapon",
                 "True Sight",
                 "Eldritch Weapon",
                 "Flame Blade",
                 "Magic Immunity",
                 "Resist Magic",
                 "Flight",
                 "Wind Walking",
                 "Invulnerability",
                 "Righteousness",
                 "Holy Armor",
                 "Planar Travel",
                 "Giant Strength",
                 "Lionheart",
                 "Bless",
                 "Heroism"
                 ]

# terrain types and terrain-map value ranges
Terrain_Types = {"ocean":{0}.union({i for i in range(601,609)}),
                 "shore":{i for i in range(2,162)}.union({i for i in range(197,233)},{i for i in range(452,601)}),
                 "grasslands":{162,172,173,180},
                 "sorcery node":{168},
                 "nature node":{169},
                 "chaos node":{170},
                 "forest":{163,183,184},
                 "mountain":{164}.union({i for i in range(259,275)}),
                 "desert":{165,174,175,176}.union({i for i in range(292,452)}),
                 "swamp":{166,177,178},
                 "tundra":{167,181,182}.union({i for i in range(610,762)}),
                 "volcano":{179},
                 "hills":{171}.union({i for i in range(275,292)}),
                 "river":{i for i in range(185,197)}.union({i for i in range(233,258)})
                 }

# movement costs for each terrain type [walk, forrester, mountaineer, swimming, sailing]
Terrain_Costs = {"ocean":[255,255,255,2,2],
                 "shore":[255,255,255,2,2],
                 "grasslands":[2,2,6,2,255],
                 "sorcery node":[2,2,2,2,255],
                 "nature node":[4,2,4,4,255],
                 "chaos node":[8,8,2,8,255],
                 "forest":[4,2,4,4,255],
                 "mountain":[8,8,2,8,255],
                 "desert":[2,2,2,2,255],
                 "swamp":[6,6,6,2,255],
                 "tundra":[4,4,4,4,255],
                 "volcano":[8,8,2,8,255],
                 "hills":[6,6,2,6,255],
                 "river":[4,4,4,2,255]
                 }

# starting address of wizard data
Wiz_Start = 2536

# size of wizard data block
Wiz_Block = 1224

# offsets in block of specific wizard data items
Wiz_Offs = {"portrait":0,
            "name":1,
            "race":21,
            "color":22,
            "personality":24,
            "objective":26,
            "fame":36,
            "percent_rsch":42,
            "percent_mana":43,
            "percent_skil":44,
            "circle_X":46,
            "circle_Y":48,
            "circle_plane":50,
            "cast_rem":78,
            "spell_cast":82,
            "spellbooks":90,
            "abils":100,
            "heroes":118,
            "vault":288,
            "war":344,
            "rsch_rem":602,
            "mana":604,
            "skill":606,
            "spell_rsch":610,
            "spells":612,
            "gold":854,
            "globals":1154
            }

# starting address of wixard fortress data
Fort_Start = 26104

# size of fortress data block
Fort_Block = 4

# offsets in block of specific fortress data items
Fort_Offs = {"X":0,
             "Y":1,
             "plane":2,
             "active":3
             }

# address of data for number of existing cities
Num_Cities = 2528
    
# starting address of city data
City_Start = 35500

# width of city data block
City_Block = 114

# offsets in block of specific city data items
City_Offs = {"name":0,
             "race":14,
             "X":15,
             "Y":16,
             "plane":17,
             "owner":18,
             "size":19,
             "kilopop":20,
             "dekapop":24,
             "producing":28,
             "buildings":34,
             "enchantments":67
             }

# starting address of hero data
#   this is just the generic hero data - there is also hero info in the
#   wizard data and unit data
Hero_Start = 0

# size of hero data blocks
Hero_Block = 12  
Hero_Wiz_Block = 28
    
# offsets in block of specific hero data items
#   the first four are in the wizard data
Hero_Offs = {"unit_num":0,
             "name":2,
             "items":16,
             "slots":22,
             "abilities":2,
             "skill":6,
             "spells":8}
        
# address of data for number of existing units
Num_Units = 2530

# starting address of unit data
Unit_Start = 46900

# size of unit data block
Unit_Block = 32
    
# offsets in block of specific unit data items
Unit_Offs : {"map_X":0,
             "map_Y":1,
             "map_plane":2,
             "owner":3,
             "class":5,
             "hero_num":6,
             "level":12,
             "experience":1,
             "damge":17,
             "mutation":23,
             "enchantment":24
             }

# starting address of item data

# starting addresses for terrain-tile map data
Terrain_Start_Arc = 9880
Terrain_Start_Myr = 14680

# starting addresses for bonus deposit map data
Bonus_Start_Arc = 79188
Bonus_Start_Myr = 81588

# map bonus deposits
Map_Bonuses = {"Nothing":0,
               "Iron":1,
               "Coal":2,
               "Silver":3,
               "Gold":4,
               "Gems":5,
               "Mithril":6,
               "Adamantium":7,
               "Quork":8,
               "Crysx":9,
               "Game":64,
               "Nightshade":128
               }

# starting addresses for terrain flag map data
Flag_Start_Arc = 117688
Flag_Start_Myr = 120088

# terrain flags
Terr_Flags = {"volcsno":0, # not sure how this works yet
              "road":8,
              "enchanted road":16,
              "corruption":32
              }

# starting address movement cost maps
Move_Start_Arc = 91188
Move_Start_Myr = 105588

# movement map block size
Mov_Block = 2400

# movement map offsets
Mov_Map_Offs = {"walk":0,
                "forrester":1,
                "mountaineer":2,
                "swimming":3,
                "sailing":4
                }

# map width
Map_Width = 60

# map height
Map_Height = 40

# this is where the MoM save files are on my computer
path = "C:\\GOG Games\\Master of Magic"

# image file for the terrain-tile graphics
Tile_File = "Resources\\Mom Map Tiles.png"

# paths for graphics of bonus deposits, towns, and roads 
Bonus_Path = "Resources\\Bonuses\\"
Town_Path = "Resources\\Towns\\"
Road_Path = "Resources\\Roads\\"

# directions
Directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
Around = [-60,-59,+1,+61,+60,+59,-1,-61]
