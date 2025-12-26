// Shadow Slave Reader - by Guiltythree
// With AI Assistant and Comprehensive Wiki Sidebar

const WIKI_DATA = {
  "characters": [
    {
      "name": "Sunny",
      "first_appearance": 1,
      "aliases": [
        "Sunless",
        "Lord Shadow",
        "Mongrel",
        "Devil of Antarctica"
      ],
      "description": "The main protagonist. An orphan from the outskirts who awakens with the Shadow Aspect. Known for his cunning mind, dark humor, and ability to survive impossible situations.",
      "type": "protagonist",
      "aspect": "Shadow",
      "rank": "Awakened \u2192 Master",
      "clan": "None"
    },
    {
      "name": "Nephis",
      "first_appearance": 15,
      "aliases": [
        "Changing Star",
        "Neph"
      ],
      "description": "A brilliant Legacy from Clan Valor with an inner fire that literally burns within her. One of the most powerful Awakened of her generation.",
      "type": "main",
      "aspect": "Changing Star",
      "rank": "Awakened \u2192 Saint",
      "clan": "Valor"
    },
    {
      "name": "Cassie",
      "first_appearance": 20,
      "aliases": [
        "Cassia",
        "The Oracle",
        "Song's Prophetess"
      ],
      "description": "A blind prophet who can see visions of the future. Despite her gentle nature, her prophecies are incredibly accurate and sometimes terrifying.",
      "type": "main",
      "aspect": "Oracle",
      "rank": "Awakened \u2192 Master",
      "clan": "Song"
    },
    {
      "name": "Kai",
      "first_appearance": 25,
      "aliases": [
        "Nightingale"
      ],
      "description": "A handsome Sleeper with a beautiful singing voice. Comes from a wealthy background but harbors secrets about his past.",
      "type": "main",
      "aspect": "Nightingale",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Effie",
      "first_appearance": 30,
      "aliases": [
        "Athena",
        "Raised by Wolves"
      ],
      "description": "A fierce warrior with incredible physical strength and appetite. Despite her brash exterior, she's fiercely loyal to her cohort.",
      "type": "main",
      "aspect": "Raised by Wolves",
      "rank": "Awakened \u2192 Master",
      "clan": "None"
    },
    {
      "name": "Caster",
      "first_appearance": 35,
      "aliases": [
        "The Quiet One"
      ],
      "description": "A Legacy from Clan Song who initially seems arrogant but proves to be a capable leader. Has a complex relationship with Sunny.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "Song"
    },
    {
      "name": "Shadow",
      "first_appearance": 1,
      "aliases": [
        "Sunny's Shadow",
        "The Rogue"
      ],
      "description": "Sunny's sentient shadow with its own personality. Mischievous and sometimes defiant, but ultimately loyal.",
      "type": "companion",
      "aspect": "N/A",
      "rank": "N/A",
      "clan": "N/A"
    },
    {
      "name": "Mordret",
      "first_appearance": 400,
      "aliases": [
        "The Prince of Nothing",
        "Mirror Beast"
      ],
      "description": "A mysterious and terrifying figure with the ability to possess bodies. One of the most dangerous beings in the Dream Realm.",
      "type": "antagonist",
      "aspect": "Mirror",
      "rank": "Corrupted Saint",
      "clan": "Valor"
    },
    {
      "name": "Jet",
      "first_appearance": 50,
      "aliases": [
        "Soul Reaper",
        "Master Jet"
      ],
      "description": "A powerful Master who becomes Sunny's mentor. Cold and efficient, but deeply cares for her students.",
      "type": "mentor",
      "aspect": "Soul Reaper",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Teacher Julius",
      "first_appearance": 10,
      "aliases": [
        "Julius"
      ],
      "description": "An instructor at the Awakened Academy who teaches Sleepers about the Dream Realm and survival.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Rain",
      "first_appearance": 800,
      "aliases": [
        "Sunny's Sister"
      ],
      "description": "Sunny's younger sister who he's been trying to protect. Her awakening becomes a major plot point.",
      "type": "main",
      "aspect": "Unknown",
      "rank": "Sleeper \u2192 Awakened",
      "clan": "None"
    },
    {
      "name": "Saint Tyris",
      "first_appearance": 150,
      "aliases": [
        "The Bright Lord"
      ],
      "description": "A powerful Saint who rules over the Bright Castle in the Forgotten Shore.",
      "type": "historical",
      "aspect": "Light",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Nightmare",
      "first_appearance": 45,
      "aliases": [
        "The Spell",
        "First Nightmare"
      ],
      "description": "The manifestation of the Nightmare Spell that tests Sleepers in their First Nightmare.",
      "type": "entity",
      "aspect": "N/A",
      "rank": "N/A",
      "clan": "N/A"
    },
    {
      "name": "Serpent",
      "first_appearance": 200,
      "aliases": [
        "The Serpent King",
        "Beast of the Depths"
      ],
      "description": "A colossal Nightmare Creature that rules the waters of the Forgotten Shore.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Corrupted Titan",
      "clan": "N/A"
    },
    {
      "name": "Morgan",
      "first_appearance": 600,
      "aliases": [
        "Lady Morgan"
      ],
      "description": "A powerful figure from Clan Valor with connections to Nephis's past.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Master",
      "clan": "Valor"
    },
    {
      "name": "Anvil",
      "first_appearance": 500,
      "aliases": [
        "The Smith"
      ],
      "description": "A skilled craftsman who can forge powerful Memories and equipment.",
      "type": "supporting",
      "aspect": "Forge",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Fiend",
      "first_appearance": 300,
      "aliases": [
        "The Demon"
      ],
      "description": "A terrifying Nightmare Creature that hunts in the darkness.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "Ananke",
      "first_appearance": 1000,
      "aliases": [
        "The Weaver",
        "Fate"
      ],
      "description": "A mysterious entity associated with fate and destiny. One of the most enigmatic beings.",
      "type": "entity",
      "aspect": "Fate",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Hope",
      "first_appearance": 350,
      "aliases": [
        "The Lost One"
      ],
      "description": "A Nightmare Creature that appears almost human. Has a tragic backstory.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Awakened",
      "clan": "N/A"
    },
    {
      "name": "Siege Master Welthe",
      "first_appearance": 1200,
      "aliases": [
        "Welthe"
      ],
      "description": "A military commander in the war against the Nightmare Creatures.",
      "type": "supporting",
      "aspect": "Fortress",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Valor",
      "first_appearance": 100,
      "aliases": [
        "Clan Valor",
        "The Warborn"
      ],
      "description": "One of the Great Clans, known for producing powerful warriors. Nephis's clan.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Valor"
    },
    {
      "name": "Song",
      "first_appearance": 100,
      "aliases": [
        "Clan Song",
        "The Singers"
      ],
      "description": "One of the Great Clans, known for their prophecies and oracles. Cassie joins this clan.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Song"
    },
    {
      "name": "Night",
      "first_appearance": 120,
      "aliases": [
        "Clan Night",
        "The Shadow Walkers"
      ],
      "description": "One of the Great Clans, associated with darkness and shadow abilities.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Night"
    },
    {
      "name": "Sword Domain Saint",
      "first_appearance": 1500,
      "aliases": [
        "Sword Saint"
      ],
      "description": "A legendary Saint known for mastering sword techniques to divine levels.",
      "type": "legendary",
      "aspect": "Sword Domain",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Noctis",
      "first_appearance": 1800,
      "aliases": [
        "The Dark One",
        "Shadow Sovereign"
      ],
      "description": "An ancient Sovereign connected to shadow powers. May have connection to Sunny's Aspect.",
      "type": "legendary",
      "aspect": "Shadow",
      "rank": "Sovereign",
      "clan": "Unknown"
    },
    {
      "name": "Weaver",
      "first_appearance": 2000,
      "aliases": [
        "The First Weaver"
      ],
      "description": "A primordial being responsible for creating the fundamental laws of the Dream Realm.",
      "type": "entity",
      "aspect": "Creation",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Asterion",
      "first_appearance": 700,
      "aliases": [
        "The Bull",
        "Labyrinth King"
      ],
      "description": "A powerful beast that guards a labyrinth containing great treasures.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "Solvane",
      "first_appearance": 1600,
      "aliases": [
        "The Undying"
      ],
      "description": "A Saint who has achieved a form of immortality through their Aspect.",
      "type": "legendary",
      "aspect": "Immortality",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "The Spell",
      "first_appearance": 1,
      "aliases": [
        "Nightmare Spell",
        "The Curse"
      ],
      "description": "The mysterious force that brought Nightmare Creatures to Earth and grants humans the chance to become Awakened.",
      "type": "entity",
      "aspect": "N/A",
      "rank": "N/A",
      "clan": "N/A"
    },
    {
      "name": "Imp",
      "first_appearance": 1400,
      "aliases": [
        "Little Devil"
      ],
      "description": "A small but cunning Nightmare Creature known for trickery.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Dormant",
      "clan": "N/A"
    },
    {
      "name": "Serpent King",
      "first_appearance": 200,
      "aliases": [
        "King of the Deep"
      ],
      "description": "Ruler of the underwater domain in the Forgotten Shore.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Corrupted",
      "clan": "N/A"
    },
    {
      "name": "Stone Saint",
      "first_appearance": 180,
      "aliases": [
        "The Petrified"
      ],
      "description": "A Saint whose body turned to stone, leaving behind powerful Memories.",
      "type": "historical",
      "aspect": "Stone",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Belle",
      "first_appearance": 2200,
      "aliases": [
        "The Beauty"
      ],
      "description": "A mysterious Awakened with charm-based abilities.",
      "type": "supporting",
      "aspect": "Charm",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Aiko",
      "first_appearance": 2100,
      "aliases": [
        "The Swift"
      ],
      "description": "A speed-focused Awakened who joins later expeditions.",
      "type": "supporting",
      "aspect": "Wind",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Dire Beast",
      "first_appearance": 40,
      "aliases": [
        "Dire Wolf"
      ],
      "description": "A powerful wolf-like Nightmare Creature common in the Dream Realm.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Awakened",
      "clan": "N/A"
    },
    {
      "name": "Sailor Kai",
      "first_appearance": 250,
      "aliases": [
        "Sea Master"
      ],
      "description": "An Awakened skilled in naval combat and water navigation.",
      "type": "supporting",
      "aspect": "Sea",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Bloodfiend",
      "first_appearance": 550,
      "aliases": [
        "The Drinker"
      ],
      "description": "A vampire-like Nightmare Creature that feeds on blood.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "War Chief",
      "first_appearance": 1100,
      "aliases": [
        "The Conqueror"
      ],
      "description": "Leader of a tribe of Nightmare Creatures that have developed society.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Corrupted",
      "clan": "N/A"
    },
    {
      "name": "Plague Doctor",
      "first_appearance": 1700,
      "aliases": [
        "The Healer of Death"
      ],
      "description": "An Awakened with healing abilities that come at a dark cost.",
      "type": "supporting",
      "aspect": "Plague",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Titan",
      "first_appearance": 1900,
      "aliases": [
        "The Giant"
      ],
      "description": "An absolutely massive Nightmare Creature that can level cities.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Titan",
      "clan": "N/A"
    },
    {
      "name": "Queen of Shadows",
      "first_appearance": 2300,
      "aliases": [
        "Dark Queen"
      ],
      "description": "A legendary figure associated with the shadow domain.",
      "type": "legendary",
      "aspect": "Shadow",
      "rank": "Saint",
      "clan": "Night"
    },
    {
      "name": "Phoenix",
      "first_appearance": 2400,
      "aliases": [
        "The Reborn"
      ],
      "description": "A mythical creature that resurrects from its own ashes.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Titan",
      "clan": "N/A"
    },
    {
      "name": "Watcher",
      "first_appearance": 2500,
      "aliases": [
        "The All-Seeing"
      ],
      "description": "An entity that observes all events in the Dream Realm.",
      "type": "entity",
      "aspect": "Sight",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Final Guardian",
      "first_appearance": 2600,
      "aliases": [
        "The Last Defense"
      ],
      "description": "The ultimate protector standing between humanity and destruction.",
      "type": "legendary",
      "aspect": "Protection",
      "rank": "Sovereign",
      "clan": "Unknown"
    },
    {
      "name": "Dream Demon",
      "first_appearance": 2700,
      "aliases": [
        "Nightmare Incarnate"
      ],
      "description": "The manifestation of pure nightmare energy.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Titan",
      "clan": "N/A"
    }
  ],
  "terms": [
    {
      "name": "Nightmare Spell",
      "first_appearance": 1,
      "category": "world",
      "description": "The mysterious force that brought the Dream Realm to Earth and created the Nightmare Creatures. It grants humans the chance to become Awakened."
    },
    {
      "name": "Awakened",
      "first_appearance": 1,
      "category": "ranks",
      "description": "Humans who survived their First Nightmare and gained supernatural powers. The second rank after Sleeper."
    },
    {
      "name": "Sleeper",
      "first_appearance": 1,
      "category": "ranks",
      "description": "A human who has been marked by the Nightmare Spell but hasn't yet undergone their First Nightmare."
    },
    {
      "name": "First Nightmare",
      "first_appearance": 5,
      "category": "world",
      "description": "The trial every Sleeper must survive to become Awakened. Takes place in the Dream Realm."
    },
    {
      "name": "Aspect",
      "first_appearance": 5,
      "category": "powers",
      "description": "The unique supernatural ability granted to someone after becoming Awakened. Defines their powers and fighting style."
    },
    {
      "name": "Flaw",
      "first_appearance": 5,
      "category": "powers",
      "description": "A weakness or curse that comes with every Aspect. Can be deadly or merely inconvenient."
    },
    {
      "name": "Soul Core",
      "first_appearance": 10,
      "category": "powers",
      "description": "The source of an Awakened's power. Contains their essence and abilities."
    },
    {
      "name": "Memory",
      "first_appearance": 15,
      "category": "items",
      "description": "Magical items created from the remnants of defeated Nightmare Creatures or powerful beings."
    },
    {
      "name": "Echo",
      "first_appearance": 20,
      "category": "creatures",
      "description": "Creatures that can be bound to serve an Awakened, created from defeated Nightmare Creatures."
    },
    {
      "name": "Legacy",
      "first_appearance": 25,
      "category": "society",
      "description": "Descendants of powerful Awakened who inherit enhanced potential and resources."
    },
    {
      "name": "Dream Realm",
      "first_appearance": 1,
      "category": "world",
      "description": "A parallel dimension where Nightmare Creatures originate. Connected to Earth through the Nightmare Spell."
    },
    {
      "name": "Seed of Nightmare",
      "first_appearance": 30,
      "category": "world",
      "description": "Locations where the Dream Realm bleeds into the real world, spawning Nightmare Creatures."
    },
    {
      "name": "Ascension",
      "first_appearance": 50,
      "category": "ranks",
      "description": "The process of advancing to a higher rank. Requires specific trials and growth."
    },
    {
      "name": "Saint",
      "first_appearance": 100,
      "category": "ranks",
      "description": "The fifth rank of power. Saints possess god-like abilities and are extremely rare."
    },
    {
      "name": "Great Clans",
      "first_appearance": 100,
      "category": "society",
      "description": "Powerful families that control much of human society. Include Valor, Song, Night, and others."
    },
    {
      "name": "Irregulars",
      "first_appearance": 120,
      "category": "society",
      "description": "Awakened who don't belong to any Great Clan. Often face discrimination."
    },
    {
      "name": "Shadow Dance",
      "first_appearance": 80,
      "category": "powers",
      "description": "Sunny's signature ability to manipulate and become one with shadows."
    },
    {
      "name": "Soul Sea",
      "first_appearance": 60,
      "category": "powers",
      "description": "The inner realm where an Awakened's soul cores and Memories are stored."
    },
    {
      "name": "Forgotten Shore",
      "first_appearance": 45,
      "category": "locations",
      "description": "A dangerous region of the Dream Realm where many Sleepers are sent during their First Nightmare."
    },
    {
      "name": "Bright Castle",
      "first_appearance": 150,
      "category": "locations",
      "description": "A stronghold in the Forgotten Shore that offers safety from Nightmare Creatures."
    },
    {
      "name": "Dark City",
      "first_appearance": 300,
      "category": "locations",
      "description": "A massive ruined city in the Dream Realm filled with powerful Nightmare Creatures."
    },
    {
      "name": "Nightmare Creature",
      "first_appearance": 1,
      "category": "creatures",
      "description": "Monsters from the Dream Realm that invade Earth. Range from weak to god-like in power."
    },
    {
      "name": "Dormant",
      "first_appearance": 40,
      "category": "ranks",
      "description": "The lowest class of Nightmare Creatures. Weak individually but dangerous in numbers."
    },
    {
      "name": "Awakened Beast",
      "first_appearance": 60,
      "category": "ranks",
      "description": "Nightmare Creatures equivalent to human Awakened in power."
    },
    {
      "name": "Fallen",
      "first_appearance": 150,
      "category": "ranks",
      "description": "Powerful Nightmare Creatures that have 'fallen' from a higher state."
    },
    {
      "name": "Corrupted",
      "first_appearance": 200,
      "category": "ranks",
      "description": "Nightmare Creatures that were once something else but have been twisted by darkness."
    },
    {
      "name": "Titan",
      "first_appearance": 200,
      "category": "ranks",
      "description": "The most powerful class of Nightmare Creatures. Can destroy cities."
    },
    {
      "name": "Sovereign",
      "first_appearance": 500,
      "category": "ranks",
      "description": "The highest rank achievable. Sovereigns are god-like beings with reality-warping powers."
    },
    {
      "name": "Master",
      "first_appearance": 50,
      "category": "ranks",
      "description": "The fourth rank of power. Masters are elite Awakened with multiple soul cores."
    },
    {
      "name": "Ascended",
      "first_appearance": 100,
      "category": "ranks",
      "description": "The third rank of power. Represents significant growth from baseline Awakened."
    },
    {
      "name": "Soul Shards",
      "first_appearance": 30,
      "category": "items",
      "description": "Currency and power source obtained from killing Nightmare Creatures."
    },
    {
      "name": "Attribute",
      "first_appearance": 10,
      "category": "powers",
      "description": "Fundamental stats like Strength, Agility, Perception that define an Awakened's capabilities."
    },
    {
      "name": "Ability",
      "first_appearance": 20,
      "category": "powers",
      "description": "Special powers granted by an Aspect beyond base attributes."
    },
    {
      "name": "Enchantment",
      "first_appearance": 70,
      "category": "powers",
      "description": "Magical effects that can be applied to items or abilities."
    },
    {
      "name": "Divine Aspect",
      "first_appearance": 400,
      "category": "powers",
      "description": "Extremely rare and powerful Aspects with unique properties."
    },
    {
      "name": "True Name",
      "first_appearance": 500,
      "category": "powers",
      "description": "The fundamental name of a being that holds power over their existence."
    },
    {
      "name": "Shadow Familiar",
      "first_appearance": 80,
      "category": "powers",
      "description": "Sunny's ability to create and control shadow creatures."
    },
    {
      "name": "Weave",
      "first_appearance": 600,
      "category": "world",
      "description": "The fundamental structure underlying reality and the Dream Realm."
    },
    {
      "name": "Chains of the Abyss",
      "first_appearance": 350,
      "category": "items",
      "description": "A powerful Memory that Sunny acquires."
    },
    {
      "name": "Stone Saint's Legacy",
      "first_appearance": 180,
      "category": "locations",
      "description": "The tomb and treasures left behind by the Stone Saint."
    },
    {
      "name": "Antarctic Expedition",
      "first_appearance": 700,
      "category": "events",
      "description": "A major military expedition to fight Nightmare Creatures in Antarctica."
    },
    {
      "name": "Second Nightmare",
      "first_appearance": 300,
      "category": "world",
      "description": "The trial to advance from Awakened to Ascended. Even more dangerous than the First."
    },
    {
      "name": "Third Nightmare",
      "first_appearance": 600,
      "category": "world",
      "description": "The trial to advance from Ascended to Master. Survival rate is extremely low."
    },
    {
      "name": "Fourth Nightmare",
      "first_appearance": 1000,
      "category": "world",
      "description": "The trial to advance from Master to Saint. Few ever attempt it."
    },
    {
      "name": "Siege of the Forgotten Shore",
      "first_appearance": 250,
      "category": "events",
      "description": "A major battle where the cohort had to defend against waves of Nightmare Creatures."
    },
    {
      "name": "Fall of the Bright Castle",
      "first_appearance": 400,
      "category": "events",
      "description": "The destruction of the main safe haven in the Forgotten Shore."
    },
    {
      "name": "Government Awakened Forces",
      "first_appearance": 500,
      "category": "society",
      "description": "Military units composed of Awakened that defend human territories."
    },
    {
      "name": "Spell Academy",
      "first_appearance": 10,
      "category": "society",
      "description": "Schools that train Sleepers before their First Nightmare."
    },
    {
      "name": "Dream Shard",
      "first_appearance": 800,
      "category": "items",
      "description": "Fragments of the Dream Realm that contain concentrated power."
    },
    {
      "name": "Shadow Realm",
      "first_appearance": 900,
      "category": "locations",
      "description": "A domain within the Dream Realm associated with shadow powers."
    },
    {
      "name": "Citadel",
      "first_appearance": 1100,
      "category": "locations",
      "description": "Major human fortification designed to withstand Nightmare Creature attacks."
    },
    {
      "name": "Dreamer",
      "first_appearance": 1300,
      "category": "ranks",
      "description": "Rare individuals who can consciously enter and navigate the Dream Realm."
    },
    {
      "name": "Nightmare Gate",
      "first_appearance": 1500,
      "category": "world",
      "description": "Portals between the real world and Dream Realm."
    },
    {
      "name": "Ancient War",
      "first_appearance": 1700,
      "category": "events",
      "description": "A legendary conflict that shaped the current state of the Dream Realm."
    },
    {
      "name": "Six Chains",
      "first_appearance": 600,
      "category": "powers",
      "description": "Sunny's signature ability representing different aspects of his shadow power."
    },
    {
      "name": "Domain",
      "first_appearance": 1200,
      "category": "powers",
      "description": "An area of absolute control that Saints can manifest."
    },
    {
      "name": "Soul Flame",
      "first_appearance": 1400,
      "category": "powers",
      "description": "The inner fire that powers an Awakened's abilities."
    },
    {
      "name": "Core Compression",
      "first_appearance": 1600,
      "category": "powers",
      "description": "Technique to increase power by compressing soul cores."
    },
    {
      "name": "Reality Anchor",
      "first_appearance": 1800,
      "category": "powers",
      "description": "Ability to resist reality-warping effects."
    },
    {
      "name": "Soul Bond",
      "first_appearance": 1900,
      "category": "powers",
      "description": "Deep connection between two Awakened that shares power and fate."
    },
    {
      "name": "Oblivion",
      "first_appearance": 2000,
      "category": "world",
      "description": "The void beyond the Dream Realm where even gods fear to tread."
    },
    {
      "name": "Genesis",
      "first_appearance": 2100,
      "category": "events",
      "description": "The original creation event that spawned the Nightmare Spell."
    },
    {
      "name": "Twilight Sea",
      "first_appearance": 2200,
      "category": "locations",
      "description": "A vast ocean in the Dream Realm between major landmasses."
    },
    {
      "name": "World Tree",
      "first_appearance": 2300,
      "category": "locations",
      "description": "A legendary structure connecting different layers of the Dream Realm."
    },
    {
      "name": "Final Nightmare",
      "first_appearance": 2500,
      "category": "world",
      "description": "The prophesied event that will determine humanity's ultimate fate."
    },
    {
      "name": "Apotheosis",
      "first_appearance": 2600,
      "category": "ranks",
      "description": "The theoretical transcendence beyond Sovereign rank."
    },
    {
      "name": "God-King",
      "first_appearance": 2700,
      "category": "ranks",
      "description": "Beings who have achieved complete mastery over the Dream Realm."
    }
  ],
  "locations": [
    {
      "name": "Forgotten Shore",
      "first_appearance": 45,
      "description": "A dangerous coastal region in the Dream Realm where many Sleepers are sent for their First Nightmare. Features ruins, monsters, and the Bright Castle."
    },
    {
      "name": "Bright Castle",
      "first_appearance": 150,
      "description": "A fortified castle in the Forgotten Shore that serves as a refuge for survivors."
    },
    {
      "name": "Dark City",
      "first_appearance": 300,
      "description": "A massive ruined metropolis in the Dream Realm, filled with powerful Nightmare Creatures and ancient secrets."
    },
    {
      "name": "Spell Academy",
      "first_appearance": 10,
      "description": "Schools in the real world that train Sleepers before they undergo their First Nightmare."
    },
    {
      "name": "Outskirts",
      "first_appearance": 1,
      "description": "The poor districts on the edge of cities where Sunny grew up. Lawless and dangerous."
    },
    {
      "name": "Antarctic Citadel",
      "first_appearance": 700,
      "description": "A major human fortification in Antarctica, site of crucial battles against Nightmare Creatures."
    },
    {
      "name": "Valor Estate",
      "first_appearance": 100,
      "description": "The ancestral home of Clan Valor, one of the most powerful Great Clans."
    },
    {
      "name": "Song Tower",
      "first_appearance": 120,
      "description": "Headquarters of Clan Song, known for their oracles and prophecies."
    },
    {
      "name": "Night Palace",
      "first_appearance": 140,
      "description": "The shadowy domain of Clan Night."
    },
    {
      "name": "Stone Saint's Tomb",
      "first_appearance": 180,
      "description": "The burial place of the Stone Saint, containing powerful Memories."
    },
    {
      "name": "Labyrinth",
      "first_appearance": 700,
      "description": "A massive maze-like structure guarded by Asterion the Bull."
    },
    {
      "name": "Shadow Realm",
      "first_appearance": 900,
      "description": "A domain of pure darkness within the Dream Realm."
    },
    {
      "name": "Serpent's Domain",
      "first_appearance": 200,
      "description": "The underwater territory ruled by the Serpent King."
    },
    {
      "name": "Mountain of Trials",
      "first_appearance": 1000,
      "description": "A legendary peak where powerful Awakened go to advance."
    },
    {
      "name": "Twilight Sea",
      "first_appearance": 2200,
      "description": "A vast ocean separating major Dream Realm continents."
    },
    {
      "name": "World Tree",
      "first_appearance": 2300,
      "description": "A colossal tree connecting different planes of the Dream Realm."
    },
    {
      "name": "Abyss",
      "first_appearance": 1100,
      "description": "The deepest, most dangerous region of the Dream Realm."
    },
    {
      "name": "Eastern Wasteland",
      "first_appearance": 1300,
      "description": "A desolate region ravaged by ancient battles."
    },
    {
      "name": "Celestial Tower",
      "first_appearance": 1500,
      "description": "A tower reaching into the heavens of the Dream Realm."
    },
    {
      "name": "Nightmare Core",
      "first_appearance": 2500,
      "description": "The theoretical center of the Dream Realm."
    }
  ],
  "events": [
    {
      "name": "First Nightmare",
      "first_appearance": 45,
      "description": "Sunny's traumatic trial in the Forgotten Shore that awakened his powers."
    },
    {
      "name": "Battle of the Forgotten Shore",
      "first_appearance": 250,
      "description": "Major conflict where Sunny's cohort defended against waves of Nightmare Creatures."
    },
    {
      "name": "Fall of the Bright Castle",
      "first_appearance": 400,
      "description": "The destruction of the main safe haven, forcing survivors to flee."
    },
    {
      "name": "Escape from the Forgotten Shore",
      "first_appearance": 450,
      "description": "The cohort's desperate journey to return to the real world."
    },
    {
      "name": "Antarctic Campaign",
      "first_appearance": 700,
      "description": "A major military operation against Nightmare Creatures in Antarctica."
    },
    {
      "name": "Second Nightmare",
      "first_appearance": 850,
      "description": "Sunny's trial to advance from Awakened to Ascended."
    },
    {
      "name": "Rain's Awakening",
      "first_appearance": 900,
      "description": "Sunny's sister undergoes her transformation."
    },
    {
      "name": "Third Nightmare",
      "first_appearance": 1200,
      "description": "Sunny's trial to reach Master rank."
    },
    {
      "name": "Siege of the Citadel",
      "first_appearance": 1100,
      "description": "A massive battle defending human territory."
    },
    {
      "name": "Labyrinth Expedition",
      "first_appearance": 1300,
      "description": "Journey into the ancient Labyrinth."
    },
    {
      "name": "War of the Saints",
      "first_appearance": 1500,
      "description": "Conflict between powerful Saints."
    },
    {
      "name": "Discovery of the Weave",
      "first_appearance": 1700,
      "description": "Understanding the fundamental nature of reality."
    },
    {
      "name": "Shadow Sovereign's Trial",
      "first_appearance": 1900,
      "description": "Sunny's confrontation with his Aspect's origin."
    },
    {
      "name": "Genesis Revelation",
      "first_appearance": 2100,
      "description": "The truth about the Nightmare Spell's creation is revealed."
    },
    {
      "name": "Final Battle",
      "first_appearance": 2700,
      "description": "The climactic confrontation that determines humanity's fate."
    }
  ]
};

const Storage = {
    getProgress() { return JSON.parse(localStorage.getItem('readingProgress') || '{}'); },
    saveProgress(chapterNum) {
        const progress = this.getProgress();
        progress.lastChapter = chapterNum;
        progress.readChapters = progress.readChapters || [];
        if (!progress.readChapters.includes(chapterNum)) {
            progress.readChapters.push(chapterNum);
        }
        progress.lastRead = new Date().toISOString();
        localStorage.setItem('readingProgress', JSON.stringify(progress));
    },
    getLastChapter() { return this.getProgress().lastChapter || null; },
    isRead(chapterNum) { return (this.getProgress().readChapters || []).includes(chapterNum); },
    getReadCount() { return (this.getProgress().readChapters || []).length; },
    getMaxChapterRead() {
        const chapters = this.getProgress().readChapters || [];
        return chapters.length > 0 ? Math.max(...chapters) : 0;
    }
};

// Wiki Sidebar
const WikiSidebar = {
    currentChapter: 1,
    
    init(chapterNum) {
        this.currentChapter = chapterNum;
        this.render();
        this.initTabs();
        this.initMobileToggle();
    },
    
    render() {
        this.renderSection('characters', WIKI_DATA.characters, 'characters-list');
        this.renderSection('terms', WIKI_DATA.terms, 'terms-list');
        this.renderSection('locations', WIKI_DATA.locations, 'locations-list');
        this.renderSection('events', WIKI_DATA.events, 'events-list');
    },
    
    renderSection(type, items, containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        const visible = items.filter(item => item.first_appearance <= this.currentChapter);
        visible.sort((a, b) => b.first_appearance - a.first_appearance);
        
        if (visible.length === 0) {
            container.innerHTML = '<div class="wiki-empty">Nothing discovered yet in this chapter</div>';
            return;
        }
        
        container.innerHTML = visible.map(item => {
            const isNew = item.first_appearance === this.currentChapter;
            const newBadge = isNew ? '<span class="badge new">NEW!</span>' : '';
            const typeBadge = item.type ? `<span class="badge">${item.type}</span>` : '';
            const categoryBadge = item.category ? `<span class="badge">${item.category}</span>` : '';
            
            let aliases = '';
            if (item.aliases && item.aliases.length > 0) {
                aliases = `<div class="aliases">AKA: ${item.aliases.join(', ')}</div>`;
            }
            
            let meta = [];
            if (item.rank) meta.push(`<span>Rank: ${item.rank}</span>`);
            if (item.aspect && item.aspect !== 'N/A') meta.push(`<span>Aspect: ${item.aspect}</span>`);
            if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') meta.push(`<span>Clan: ${item.clan}</span>`);
            meta.push(`<span>Ch.${item.first_appearance}</span>`);
            
            const metaHtml = meta.length > 0 ? `<div class="meta">${meta.join('')}</div>` : '';
            
            return `
                <div class="wiki-item ${isNew ? 'new-this-chapter' : ''}">
                    <h4>${item.name} ${newBadge || typeBadge || categoryBadge}</h4>
                    ${aliases}
                    <div class="description">${item.description}</div>
                    ${metaHtml}
                </div>
            `;
        }).join('');
        
        // Update tab count
        const tab = document.querySelector(`[data-tab="${type}"]`);
        if (tab) {
            const newCount = visible.filter(i => i.first_appearance === this.currentChapter).length;
            const newIndicator = newCount > 0 ? ` (${newCount} new)` : '';
            tab.dataset.count = visible.length;
        }
    },
    
    initTabs() {
        const tabs = document.querySelectorAll('.wiki-tab');
        const sections = document.querySelectorAll('.wiki-section');
        
        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                tabs.forEach(t => t.classList.remove('active'));
                sections.forEach(s => s.classList.remove('active'));
                
                tab.classList.add('active');
                const target = tab.dataset.tab;
                document.getElementById(`${target}-section`)?.classList.add('active');
            });
        });
    },
    
    initMobileToggle() {
        const toggle = document.querySelector('.wiki-toggle');
        const sidebar = document.querySelector('.wiki-sidebar');
        
        if (toggle && sidebar) {
            toggle.addEventListener('click', () => {
                sidebar.classList.toggle('mobile-open');
                toggle.textContent = sidebar.classList.contains('mobile-open') ? '✕' : '📖';
            });
        }
    }
};

// AI Assistant
const AIAssistant = {
    responses: {
        greetings: [
            "Hello, Sleeper! How can I help you on your journey through the Dream Realm?",
            "Greetings! I'm your guide through Shadow Slave. Ask me anything!",
            "Welcome back! Ready to continue the adventure?"
        ],
        sunny: "Sunny (Sunless) is the protagonist - an orphan from the outskirts who becomes an Awakened. His Aspect is Shadow, allowing him to control shadows and eventually become the 'Lord Shadow'. He's known for his cunning mind and dark humor.",
        nephis: "Nephis (Changing Star) is a brilliant Legacy from Clan Valor. She possesses an inner fire that literally burns within her. She's one of the most powerful Awakened of her generation.",
        cassie: "Cassie is a blind prophet who can see visions of the future. Despite her gentle nature, her prophecies are incredibly accurate and sometimes terrifying.",
        nightmare: "The Nightmare Spell is the mysterious force that brought the Dream Realm to Earth. It grants humans the chance to become Awakened through surviving Nightmares.",
        awakened: "Awakened are humans who survived their First Nightmare and gained supernatural powers called Aspects. They rank from Sleeper → Awakened → Ascended → Master → Saint → Sovereign.",
        aspect: "An Aspect is the unique supernatural ability granted to someone after becoming Awakened. Each Aspect comes with a Flaw - a weakness or curse.",
        shadow: "Sunny's shadow is sentient and has its own personality. It's one of the most mysterious elements of his power.",
        progress: () => {
            const last = Storage.getLastChapter();
            const count = Storage.getReadCount();
            return last ? `You've read ${count} chapters so far. You were last on Chapter ${last}. Keep going!` : "You haven't started reading yet. Begin with Chapter 1!";
        },
        wiki: "Check the Wiki sidebar on the right! It shows characters, terms, locations, and events that have appeared up to your current chapter.",
        help: "I can help with: character info, world terms, your progress, navigation. Try asking about Sunny, Nephis, the Nightmare Spell, or your reading progress!",
        unknown: [
            "I'm not sure about that. Try asking about specific characters or concepts!",
            "That's beyond my knowledge. Ask me about characters, the Nightmare Spell, or Aspects!",
            "Hmm, I don't have info on that. Want to know about the main characters?"
        ]
    },
    
    processQuery(query) {
        const q = query.toLowerCase();
        
        if (q.match(/hello|hi|hey|greet/)) return this.random(this.responses.greetings);
        if (q.match(/sunny|sunless|protagonist|main character|lord shadow/)) return this.responses.sunny;
        if (q.match(/nephis|neph|changing star|valor/)) return this.responses.nephis;
        if (q.match(/cassie|cassia|blind|oracle|prophet/)) return this.responses.cassie;
        if (q.match(/nightmare spell|spell|dream realm|world/)) return this.responses.nightmare;
        if (q.match(/awakened|sleeper|master|saint|rank/)) return this.responses.awakened;
        if (q.match(/aspect|flaw|power|ability/)) return this.responses.aspect;
        if (q.match(/shadow|sentient shadow/)) return this.responses.shadow;
        if (q.match(/progress|reading|chapter|where|last/)) return this.responses.progress();
        if (q.match(/wiki|character|spoiler/)) return this.responses.wiki;
        if (q.match(/help|what can|how to/)) return this.responses.help;
        
        return this.random(this.responses.unknown);
    },
    
    random(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
};

// Initialize chat
function initChat() {
    const btn = document.querySelector('.ai-chat-button');
    const panel = document.querySelector('.ai-chat-panel');
    const closeBtn = document.querySelector('.ai-chat-close');
    const input = document.querySelector('.ai-chat-input input');
    const sendBtn = document.querySelector('.ai-chat-input button');
    const messages = document.querySelector('.ai-chat-messages');
    
    if (!btn) return;
    
    btn.onclick = () => panel.classList.toggle('open');
    closeBtn.onclick = () => panel.classList.remove('open');
    
    function sendMessage() {
        const text = input.value.trim();
        if (!text) return;
        
        const userMsg = document.createElement('div');
        userMsg.className = 'ai-message user';
        userMsg.textContent = text;
        messages.appendChild(userMsg);
        
        input.value = '';
        
        setTimeout(() => {
            const botMsg = document.createElement('div');
            botMsg.className = 'ai-message bot';
            botMsg.textContent = AIAssistant.processQuery(text);
            messages.appendChild(botMsg);
            messages.scrollTop = messages.scrollHeight;
        }, 500);
        
        messages.scrollTop = messages.scrollHeight;
    }
    
    sendBtn.onclick = sendMessage;
    input.onkeypress = (e) => { if (e.key === 'Enter') sendMessage(); };
    
    const greeting = document.createElement('div');
    greeting.className = 'ai-message bot';
    greeting.textContent = "Hello! I'm your Shadow Slave guide. Ask me about characters, concepts, or your reading progress!";
    messages.appendChild(greeting);
}

// Chapter page
function initChapterPage() {
    const match = window.location.pathname.match(/chapters\/([0-9]+)\.html/);
    if (match) {
        const chapterNum = parseInt(match[1]);
        Storage.saveProgress(chapterNum);
        WikiSidebar.init(chapterNum);
    }
}

// Index page
function initIndexPage() {
    const lastChapter = Storage.getLastChapter();
    const resumeSection = document.getElementById('resume-section');
    if (lastChapter && resumeSection) {
        resumeSection.classList.add('visible');
        const link = resumeSection.querySelector('a');
        if (link) {
            link.href = `chapters/${lastChapter}.html`;
            link.textContent = `Continue Chapter ${lastChapter}`;
        }
        const readCount = document.getElementById('read-count');
        if (readCount) readCount.textContent = Storage.getReadCount();
    }
}

// Chapter list
function initChapterList() {
    document.querySelectorAll('.chapter-card').forEach(card => {
        const match = card.href.match(/chapters\/([0-9]+)\.html/);
        if (match && Storage.isRead(parseInt(match[1]))) {
            card.classList.add('read');
        }
    });
    
    const searchBox = document.getElementById('chapter-search');
    if (searchBox) {
        searchBox.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.chapter-card').forEach(card => {
                card.style.display = card.textContent.toLowerCase().includes(query) ? 'block' : 'none';
            });
        });
    }
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        const next = document.querySelector('.chapter-nav a:last-child:not(.disabled)');
        if (next) next.click();
    } else if (e.key === 'ArrowLeft') {
        const prev = document.querySelector('.chapter-nav a:first-child:not(.disabled)');
        if (prev) prev.click();
    }
});

// Init
document.addEventListener('DOMContentLoaded', () => {
    initChat();
    
    if (document.querySelector('.chapter-content')) initChapterPage();
    else if (document.querySelector('.hero')) initIndexPage();
    else if (document.querySelector('.chapters-grid')) initChapterList();
});
