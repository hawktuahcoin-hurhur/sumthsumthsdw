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
        "Devil of Antarctica",
        "Lost from Light"
      ],
      "description": "The main protagonist. A frail orphan from the outskirts with dark circles under his eyes. He awakens with the Shadow Slave Aspect, granting him control over shadows. Known for his cunning mind, dark humor, and survival instinct. His flaw is that he cannot lie.",
      "type": "protagonist",
      "aspect": "Shadow Slave",
      "rank": "Sleeper \u2192 Awakened \u2192 Ascended \u2192 Master",
      "clan": "None"
    },
    {
      "name": "Nephis",
      "first_appearance": 24,
      "aliases": [
        "Changing Star",
        "Neph",
        "Princess of Valor"
      ],
      "description": "A beautiful silver-haired girl with burning eyes from Clan Valor. Daughter of the Broken Sword. Her Aspect allows her to ignite with inner fire. One of the most powerful Awakened of her generation. Forms a deep bond with Sunny.",
      "type": "main",
      "aspect": "Changing Star",
      "rank": "Awakened \u2192 Saint",
      "clan": "Valor"
    },
    {
      "name": "Cassie",
      "first_appearance": 22,
      "aliases": [
        "Cassia",
        "The Oracle",
        "Song's Prophetess",
        "Blind Oracle"
      ],
      "description": "A blind girl with the gift of prophecy. Her visions of the future are terrifyingly accurate. Despite her gentle and kind nature, she carries a heavy burden. Later becomes associated with Clan Song.",
      "type": "main",
      "aspect": "Oracle",
      "rank": "Awakened \u2192 Master",
      "clan": "Song"
    },
    {
      "name": "Kai",
      "first_appearance": 115,
      "aliases": [
        "Nightingale",
        "The Singer"
      ],
      "description": "A handsome young man with a beautiful singing voice and charming personality. Comes from a wealthy background but harbors dark secrets about his past. His voice has special powers.",
      "type": "main",
      "aspect": "Nightingale",
      "rank": "Awakened \u2192 Ascended",
      "clan": "None"
    },
    {
      "name": "Effie",
      "first_appearance": 126,
      "aliases": [
        "Athena",
        "Raised by Wolves",
        "The Glutton"
      ],
      "description": "A fierce warrior with incredible physical strength and an even more incredible appetite. Despite her brash and lazy exterior, she is fiercely loyal and surprisingly perceptive. One of Sunny's closest friends.",
      "type": "main",
      "aspect": "Raised by Wolves",
      "rank": "Awakened \u2192 Master",
      "clan": "None"
    },
    {
      "name": "Caster",
      "first_appearance": 21,
      "aliases": [
        "The Quiet One",
        "Legacy of Song"
      ],
      "description": "A Legacy from Clan Song who initially seems arrogant and calculating. Proves to be a capable leader with his own complex motivations. Has complicated relationships with the cohort.",
      "type": "main",
      "aspect": "Unknown",
      "rank": "Awakened \u2192 Ascended",
      "clan": "Song"
    },
    {
      "name": "Shadow",
      "first_appearance": 2,
      "aliases": [
        "The Rogue",
        "Sunny's Shadow",
        "Sentient Shadow"
      ],
      "description": "Sunny's own shadow which gained sentience due to his Aspect. Mischievous and sometimes defiant, but ultimately loyal. Can act independently and has its own distinct personality.",
      "type": "companion",
      "aspect": "N/A",
      "rank": "N/A",
      "clan": "N/A"
    },
    {
      "name": "Saint",
      "first_appearance": 9,
      "aliases": [
        "The Stone Saint",
        "Shadow Saint"
      ],
      "description": "A powerful Echo that Sunny obtains. Once a great Saint in life, now serves as one of Sunny's most powerful combat assets. Silent but deadly.",
      "type": "echo",
      "aspect": "Stone",
      "rank": "Saint",
      "clan": "N/A"
    },
    {
      "name": "Serpent",
      "first_appearance": 217,
      "aliases": [
        "Soul Serpent",
        "The Serpent",
        "Nightmare"
      ],
      "description": "A massive serpentine Nightmare Creature that Sunny bonds with. Serves as transportation and a powerful ally.",
      "type": "echo",
      "aspect": "N/A",
      "rank": "Corrupted",
      "clan": "N/A"
    },
    {
      "name": "Nightmare",
      "first_appearance": 1,
      "aliases": [
        "The Steed",
        "Shadow Horse"
      ],
      "description": "A fearsome nightmare creature that becomes one of Sunny's shadows. A terrifying steed that can traverse impossible terrain.",
      "type": "echo",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "Gunlaug",
      "first_appearance": 82,
      "aliases": [
        "The Host",
        "Bright Lord",
        "King of the Castle"
      ],
      "description": "The tyrannical ruler of the Bright Castle on the Forgotten Shore. Once a hero, corrupted by power and desperation. Maintains order through fear and control.",
      "type": "antagonist",
      "aspect": "Unknown",
      "rank": "Ascended",
      "clan": "None"
    },
    {
      "name": "Harus",
      "first_appearance": 143,
      "aliases": [
        "The Hunchback",
        "Gunlaug's Advisor"
      ],
      "description": "Gunlaug's cunning advisor with a hunched back. Despite his unassuming appearance, he is dangerous and calculating. One of the main obstacles on the Forgotten Shore.",
      "type": "antagonist",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Gemma",
      "first_appearance": 141,
      "aliases": [
        "The Huntress"
      ],
      "description": "A skilled hunter from the Bright Castle who becomes an ally to Sunny's cohort.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Harper",
      "first_appearance": 134,
      "aliases": [
        "The Mender"
      ],
      "description": "A healer at the Bright Castle who helps Sunny and his companions.",
      "type": "supporting",
      "aspect": "Healing",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Scholar",
      "first_appearance": 3,
      "aliases": [
        "The Teacher"
      ],
      "description": "An older slave during Sunny's First Nightmare who appears kind but is calculating. Teaches Sunny valuable lessons about trust.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Sleeper",
      "clan": "None"
    },
    {
      "name": "Shifty",
      "first_appearance": 2,
      "aliases": [
        "The Thief"
      ],
      "description": "A fellow slave during the First Nightmare. Meets a tragic end early in the story.",
      "type": "minor",
      "aspect": "Unknown",
      "rank": "Sleeper",
      "clan": "None"
    },
    {
      "name": "Auro",
      "first_appearance": 6,
      "aliases": [
        "Hero",
        "Auro of the Nine"
      ],
      "description": "A legendary Sleeper who fought valiantly during the First Nightmare. Sunny witnesses his heroic death.",
      "type": "historical",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "Unknown"
    },
    {
      "name": "Jet",
      "first_appearance": 17,
      "aliases": [
        "Soul Reaper",
        "Master Jet"
      ],
      "description": "A powerful Master who becomes Sunny's mentor in the waking world. Cold and efficient in battle, but deeply cares for her students. Teaches Sunny essential combat skills.",
      "type": "mentor",
      "aspect": "Soul Reaper",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Teacher Julius",
      "first_appearance": 25,
      "aliases": [
        "Julius",
        "The Professor"
      ],
      "description": "An instructor at the Awakened Academy who teaches Sleepers about the Dream Realm and survival. Knowledgeable and somewhat eccentric.",
      "type": "mentor",
      "aspect": "Unknown",
      "rank": "Awakened",
      "clan": "None"
    },
    {
      "name": "Saint Tyris",
      "first_appearance": 384,
      "aliases": [
        "The Bright Lord",
        "Lord of Light"
      ],
      "description": "A legendary Saint who once ruled over the Forgotten Shore from the Bright Castle. His legacy and memories scattered across the Dream Realm.",
      "type": "historical",
      "aspect": "Light",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Stone Saint",
      "first_appearance": 102,
      "aliases": [
        "The Petrified",
        "Guardian of Stone"
      ],
      "description": "An ancient Saint whose body turned to stone, leaving behind powerful Memories. The source of Sunny's Saint Echo.",
      "type": "historical",
      "aspect": "Stone",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Mordret",
      "first_appearance": 438,
      "aliases": [
        "Prince of Nothing",
        "Mirror Beast",
        "The Reflection"
      ],
      "description": "A terrifying and mysterious figure with the ability to possess bodies through reflections. One of the most dangerous beings Sunny encounters. Has connections to Clan Valor.",
      "type": "antagonist",
      "aspect": "Mirror",
      "rank": "Corrupted Saint",
      "clan": "Valor"
    },
    {
      "name": "Noctis",
      "first_appearance": 381,
      "aliases": [
        "The Dark One",
        "Shadow Sovereign",
        "Lord of Night"
      ],
      "description": "An ancient Sovereign connected to shadow powers. May have deep connections to Sunny's Aspect and the nature of shadows themselves.",
      "type": "legendary",
      "aspect": "Shadow",
      "rank": "Sovereign",
      "clan": "Night"
    },
    {
      "name": "Valor Matriarch",
      "first_appearance": 223,
      "aliases": [
        "Matriarch",
        "Lady of Valor"
      ],
      "description": "The powerful leader of Clan Valor. Nephis's grandmother and a key political figure among the Great Clans.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Saint",
      "clan": "Valor"
    },
    {
      "name": "Dread Lord",
      "first_appearance": 1309,
      "aliases": [
        "Lord of Dread",
        "The Tyrant"
      ],
      "description": "A powerful and fearsome ruler encountered in later arcs. Commands respect and fear from all who know of him.",
      "type": "antagonist",
      "aspect": "Dread",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Soul Stealer",
      "first_appearance": 1309,
      "aliases": [
        "The Thief of Souls"
      ],
      "description": "A terrifying being with the power to steal souls. One of the major threats in the later story.",
      "type": "antagonist",
      "aspect": "Soul",
      "rank": "Saint",
      "clan": "Unknown"
    },
    {
      "name": "Weaver",
      "first_appearance": 81,
      "aliases": [
        "The First Weaver",
        "Creator",
        "Fate Weaver"
      ],
      "description": "A primordial entity responsible for weaving the fundamental fabric of reality. Connected to fate and destiny.",
      "type": "entity",
      "aspect": "Weave",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Ananke",
      "first_appearance": 1284,
      "aliases": [
        "The Weaver of Fate",
        "Inevitability"
      ],
      "description": "A mysterious entity associated with fate and inevitability. One of the most enigmatic beings in the Dream Realm.",
      "type": "entity",
      "aspect": "Fate",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Rain",
      "first_appearance": 1,
      "aliases": [
        "Sunny's Sister",
        "Little Rain"
      ],
      "description": "Sunny's younger sister whom he desperately tries to protect. Her potential awakening is a major plot point. Sunny's main motivation for surviving.",
      "type": "main",
      "aspect": "Unknown",
      "rank": "Sleeper \u2192 Awakened",
      "clan": "None"
    },
    {
      "name": "Morgan",
      "first_appearance": 545,
      "aliases": [
        "Lady Morgan"
      ],
      "description": "A powerful figure from Clan Valor with connections to Nephis's past. Plays a significant role in clan politics.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Master",
      "clan": "Valor"
    },
    {
      "name": "Anvil",
      "first_appearance": 263,
      "aliases": [
        "The Smith",
        "The Forger"
      ],
      "description": "A skilled craftsman who can forge powerful Memories and equipment. An invaluable ally for enhancing gear.",
      "type": "supporting",
      "aspect": "Forge",
      "rank": "Master",
      "clan": "None"
    },
    {
      "name": "Belle",
      "first_appearance": 777,
      "aliases": [
        "The Beauty",
        "Charmer"
      ],
      "description": "A mysterious Awakened with charm-based abilities encountered in later arcs.",
      "type": "supporting",
      "aspect": "Charm",
      "rank": "Ascended",
      "clan": "None"
    },
    {
      "name": "Ariel",
      "first_appearance": 869,
      "aliases": [
        "Wind Spirit"
      ],
      "description": "A being associated with wind and air. Encountered during major expeditions.",
      "type": "supporting",
      "aspect": "Wind",
      "rank": "Unknown",
      "clan": "None"
    },
    {
      "name": "Sid",
      "first_appearance": 1607,
      "aliases": [
        "The Warrior"
      ],
      "description": "A fierce warrior who crossed paths with Sunny on the Forgotten Shore and again in later battles.",
      "type": "supporting",
      "aspect": "Unknown",
      "rank": "Ascended",
      "clan": "None"
    },
    {
      "name": "Felise",
      "first_appearance": 1998,
      "aliases": [
        "The Rival"
      ],
      "description": "An Awakened whose path has led her to conflict with Sid. Their final confrontation spans battlefields.",
      "type": "antagonist",
      "aspect": "Unknown",
      "rank": "Ascended",
      "clan": "None"
    },
    {
      "name": "Covet",
      "first_appearance": 2229,
      "aliases": [
        "The Envious"
      ],
      "description": "A being representing greed and desire. Encountered in the later stages of the story.",
      "type": "entity",
      "aspect": "Desire",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Carapace Demon",
      "first_appearance": 31,
      "aliases": [
        "Shell Demon",
        "Armored Beast"
      ],
      "description": "Nightmare Creatures with hard armored shells. Common but dangerous foes on the Forgotten Shore.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Dormant",
      "clan": "N/A"
    },
    {
      "name": "Scavenger",
      "first_appearance": 33,
      "aliases": [
        "Scavengers"
      ],
      "description": "Pack creatures that feed on corpses. Common Nightmare Creatures that hunt in groups.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Dormant",
      "clan": "N/A"
    },
    {
      "name": "Carapace Centurion",
      "first_appearance": 51,
      "aliases": [
        "Centurion",
        "Elite Shell Beast"
      ],
      "description": "A more powerful variant of the Carapace Demon. Commands lesser creatures.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Awakened",
      "clan": "N/A"
    },
    {
      "name": "Fallen Titan",
      "first_appearance": 23,
      "aliases": [
        "Titan",
        "The Giant"
      ],
      "description": "Massive Nightmare Creatures of devastating power. Encountering one is often a death sentence.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Titan",
      "clan": "N/A"
    },
    {
      "name": "Spire Messenger",
      "first_appearance": 132,
      "aliases": [
        "Messenger",
        "Flying Horror"
      ],
      "description": "Flying Nightmare Creatures that carry messages or hunt from the sky.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Awakened",
      "clan": "N/A"
    },
    {
      "name": "Fiend",
      "first_appearance": 86,
      "aliases": [
        "The Demon",
        "Dark Beast"
      ],
      "description": "A terrifying Nightmare Creature that hunts in the darkness. One of the most feared creatures.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "Imp",
      "first_appearance": 176,
      "aliases": [
        "Little Devil"
      ],
      "description": "Small but cunning Nightmare Creatures known for trickery and mischief.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Dormant",
      "clan": "N/A"
    },
    {
      "name": "Gate Guardian",
      "first_appearance": 491,
      "aliases": [
        "Guardian",
        "The Gatekeeper"
      ],
      "description": "Massive creatures that guard important passages and gates in the Dream Realm.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Fallen",
      "clan": "N/A"
    },
    {
      "name": "Winter Beast",
      "first_appearance": 902,
      "aliases": [
        "Ice Horror",
        "Frost Monster"
      ],
      "description": "Terrifying creatures adapted to frozen environments. Major threats during the Antarctic campaign.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Corrupted",
      "clan": "N/A"
    },
    {
      "name": "Defiled",
      "first_appearance": 845,
      "aliases": [
        "The Corrupted Ones",
        "Twisted Creatures"
      ],
      "description": "Nightmare Creatures that have been twisted and corrupted beyond their original forms. Especially dangerous.",
      "type": "creature",
      "aspect": "N/A",
      "rank": "Corrupted",
      "clan": "N/A"
    },
    {
      "name": "Demon of Imagination",
      "first_appearance": 330,
      "aliases": [
        "Mirage",
        "The Illusionist"
      ],
      "description": "A powerful daemon with the ability to create illusions and imaginary constructs. Creator of fantastical kingdoms.",
      "type": "creature",
      "aspect": "Imagination",
      "rank": "Titan",
      "clan": "N/A"
    },
    {
      "name": "Terror",
      "first_appearance": 5,
      "aliases": [
        "The Fear",
        "Living Nightmare"
      ],
      "description": "Manifestation of pure fear. One of the most primal and dangerous forces.",
      "type": "entity",
      "aspect": "Fear",
      "rank": "Unknown",
      "clan": "N/A"
    },
    {
      "name": "Clan Valor",
      "first_appearance": 42,
      "aliases": [
        "The Warborn",
        "House Valor"
      ],
      "description": "One of the Great Clans, known for producing powerful warriors. Nephis's clan. Values strength and honor above all.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Valor"
    },
    {
      "name": "Clan Song",
      "first_appearance": 88,
      "aliases": [
        "The Singers",
        "House Song"
      ],
      "description": "One of the Great Clans, known for their prophecies and oracles. Cassie becomes associated with them. Masters of foresight.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Song"
    },
    {
      "name": "Clan Night",
      "first_appearance": 2,
      "aliases": [
        "The Shadow Walkers",
        "House Night"
      ],
      "description": "One of the Great Clans, associated with darkness and shadow abilities. Mysterious and secretive.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Night"
    },
    {
      "name": "Great Clans",
      "first_appearance": 353,
      "aliases": [
        "The Seven Clans",
        "Noble Houses"
      ],
      "description": "The most powerful families that control much of human society. Include Valor, Song, Night, and others. Command enormous resources.",
      "type": "organization",
      "aspect": "Various",
      "rank": "N/A",
      "clan": "Various"
    },
    {
      "name": "Government",
      "first_appearance": 17,
      "aliases": [
        "The Authority",
        "Human Government"
      ],
      "description": "The governing body of human civilization. Manages Awakened forces and defends against Nightmare Creatures.",
      "type": "organization",
      "aspect": "N/A",
      "rank": "N/A",
      "clan": "N/A"
    },
    {
      "name": "Nightmare Creatures",
      "first_appearance": 1,
      "aliases": [
        "Monsters",
        "Beasts",
        "Abominations"
      ],
      "description": "Creatures from the Dream Realm that invade the waking world. Range from weak Dormant to god-like Titans.",
      "type": "organization",
      "aspect": "N/A",
      "rank": "Various",
      "clan": "N/A"
    },
    {
      "name": "Shadow Lantern",
      "first_appearance": 653,
      "aliases": [
        "The Lantern",
        "Light of Shadows"
      ],
      "description": "A powerful divine Memory that Sunny acquires. Can open gates to other realms.",
      "type": "memory",
      "aspect": "Shadow/Light",
      "rank": "Divine",
      "clan": "N/A"
    },
    {
      "name": "Dying Wish",
      "first_appearance": 730,
      "aliases": [
        "Last Wish",
        "Final Memory"
      ],
      "description": "A Memory containing the last wish of a powerful being. Grants significant power.",
      "type": "memory",
      "aspect": "Unknown",
      "rank": "Ascended",
      "clan": "N/A"
    },
    {
      "name": "Sin of Solace",
      "first_appearance": 869,
      "aliases": [
        "Solace",
        "The Sword"
      ],
      "description": "A powerful weapon Memory with its own consciousness. One of Sunny's signature weapons.",
      "type": "memory",
      "aspect": "Unknown",
      "rank": "Transcendent",
      "clan": "N/A"
    },
    {
      "name": "Chain Breaker",
      "first_appearance": 741,
      "aliases": [
        "Liberator",
        "The Chains"
      ],
      "description": "A Memory associated with breaking bonds and chains. Represents freedom.",
      "type": "memory",
      "aspect": "Liberation",
      "rank": "Ascended",
      "clan": "N/A"
    }
  ],
  "terms": [
    {
      "name": "Nightmare Spell",
      "first_appearance": 1,
      "category": "world",
      "description": "The mysterious force that descended upon Earth, bringing the Dream Realm and Nightmare Creatures. It grants humans the chance to become Awakened through surviving Nightmares. The fundamental change that altered humanity forever."
    },
    {
      "name": "Awakened",
      "first_appearance": 1,
      "category": "ranks",
      "description": "Humans who survived their First Nightmare and gained supernatural powers. The second rank of power after Sleeper. Can use Aspects and Memories."
    },
    {
      "name": "Sleeper",
      "first_appearance": 17,
      "category": "ranks",
      "description": "A human who has been marked by the Nightmare Spell but hasn't yet undergone their First Nightmare. Training at academies to prepare for their trial."
    },
    {
      "name": "First Nightmare",
      "first_appearance": 1,
      "category": "world",
      "description": "The trial every Sleeper must survive to become Awakened. Takes place in the Dream Realm. Many die, but survivors gain powers."
    },
    {
      "name": "Aspect",
      "first_appearance": 1,
      "category": "powers",
      "description": "The unique supernatural ability granted to someone after becoming Awakened. Defines their powers and fighting style. Each Aspect is unique."
    },
    {
      "name": "Flaw",
      "first_appearance": 8,
      "category": "powers",
      "description": "A weakness or curse that comes with every Aspect. Can be deadly or merely inconvenient. Sunny's flaw is that he cannot lie."
    },
    {
      "name": "Soul Core",
      "first_appearance": 2,
      "category": "powers",
      "description": "The source of an Awakened's power. Contains their essence and abilities. More cores mean more power."
    },
    {
      "name": "Memory",
      "first_appearance": 1,
      "category": "items",
      "description": "Magical items created from the remnants of defeated Nightmare Creatures or powerful beings. Can be weapons, armor, or tools."
    },
    {
      "name": "Echo",
      "first_appearance": 16,
      "category": "powers",
      "description": "Creatures that can be bound to serve an Awakened, created from defeated Nightmare Creatures. Loyal companions in battle."
    },
    {
      "name": "Legacy",
      "first_appearance": 21,
      "category": "society",
      "description": "Descendants of powerful Awakened who inherit enhanced potential and resources. Often members of Great Clans."
    },
    {
      "name": "Dream Realm",
      "first_appearance": 1,
      "category": "world",
      "description": "A parallel dimension where Nightmare Creatures originate. Connected to Earth through the Nightmare Spell. Contains countless dangers and treasures."
    },
    {
      "name": "Seed of Nightmare",
      "first_appearance": 458,
      "category": "world",
      "description": "Locations where the Dream Realm bleeds into the real world, spawning Nightmare Creatures. Must be destroyed or contained."
    },
    {
      "name": "Ascended",
      "first_appearance": 9,
      "category": "ranks",
      "description": "The third rank of power. Represents significant growth from baseline Awakened. Can begin to challenge Fallen creatures."
    },
    {
      "name": "Master",
      "first_appearance": 15,
      "category": "ranks",
      "description": "The fourth rank of power. Masters are elite Awakened with multiple soul cores. Can fight Corrupted creatures."
    },
    {
      "name": "Saint",
      "first_appearance": 9,
      "category": "ranks",
      "description": "The fifth rank of power. Saints possess god-like abilities and are extremely rare. Can reshape reality in limited ways."
    },
    {
      "name": "Sovereign",
      "first_appearance": 368,
      "category": "ranks",
      "description": "The highest known rank. Sovereigns are god-like beings with reality-warping powers. Only a handful exist."
    },
    {
      "name": "Titan",
      "first_appearance": 23,
      "category": "ranks",
      "description": "The most powerful class of Nightmare Creatures. Can destroy cities and challenge Saints."
    },
    {
      "name": "Dormant",
      "first_appearance": 2,
      "category": "ranks",
      "description": "The lowest class of Nightmare Creatures. Weak individually but dangerous in numbers."
    },
    {
      "name": "Fallen",
      "first_appearance": 8,
      "category": "ranks",
      "description": "Powerful Nightmare Creatures. Challenging for most Awakened to face alone."
    },
    {
      "name": "Corrupted",
      "first_appearance": 15,
      "category": "ranks",
      "description": "Nightmare Creatures that were once something else but have been twisted by darkness. Especially dangerous."
    },
    {
      "name": "Shadow Slave",
      "first_appearance": 15,
      "category": "powers",
      "description": "Sunny's unique Aspect. Allows him to control shadows, create shadow copies, and eventually command shadow servants."
    },
    {
      "name": "Shadow Fragments",
      "first_appearance": 34,
      "category": "powers",
      "description": "Resources Sunny collects by defeating enemies. Used to enhance his shadow abilities."
    },
    {
      "name": "Shadow Dance",
      "first_appearance": 187,
      "category": "powers",
      "description": "Sunny's signature combat technique. Allows him to merge with and move through shadows."
    },
    {
      "name": "Shadow Control",
      "first_appearance": 16,
      "category": "powers",
      "description": "The ability to manipulate shadows and dark areas. Range and power increase with rank."
    },
    {
      "name": "Shadow Manifestation",
      "first_appearance": 744,
      "category": "powers",
      "description": "Advanced shadow technique allowing creation of solid shadow constructs."
    },
    {
      "name": "Shadow Bond",
      "first_appearance": 15,
      "category": "powers",
      "description": "The connection between Sunny and his shadow servants. Allows communication and power sharing."
    },
    {
      "name": "True Name",
      "first_appearance": 2,
      "category": "powers",
      "description": "The fundamental name of a being that holds power over their existence. Knowing one grants influence."
    },
    {
      "name": "Soul Shards",
      "first_appearance": 9,
      "category": "items",
      "description": "Currency and power source obtained from killing Nightmare Creatures. Can be absorbed for power."
    },
    {
      "name": "Attribute",
      "first_appearance": 1,
      "category": "powers",
      "description": "Fundamental stats like Strength, Agility, Perception that define an Awakened's capabilities."
    },
    {
      "name": "Enchantment",
      "first_appearance": 8,
      "category": "powers",
      "description": "Magical effects that can be applied to items or abilities. Enhance or modify their properties."
    },
    {
      "name": "Essence",
      "first_appearance": 5,
      "category": "powers",
      "description": "The energy that powers Awakened abilities. Must be managed carefully in combat."
    },
    {
      "name": "Rune",
      "first_appearance": 2,
      "category": "powers",
      "description": "Mystical symbols that describe an Awakened's abilities, flaws, and attributes."
    },
    {
      "name": "Divine Aspect",
      "first_appearance": 15,
      "category": "powers",
      "description": "Extremely rare and powerful Aspects with unique divine properties."
    },
    {
      "name": "Domain",
      "first_appearance": 61,
      "category": "powers",
      "description": "An area of absolute control that Saints can manifest. Within a Domain, the Saint is supreme."
    },
    {
      "name": "Weave",
      "first_appearance": 83,
      "category": "world",
      "description": "The fundamental structure underlying reality and the Dream Realm. Can be perceived and manipulated by some."
    },
    {
      "name": "Blood Weave",
      "first_appearance": 83,
      "category": "powers",
      "description": "A technique involving the manipulation of blood and life force. Dangerous but powerful."
    },
    {
      "name": "Lineage",
      "first_appearance": 85,
      "category": "society",
      "description": "Inherited traits and powers from ancestors. Important for Legacy families."
    },
    {
      "name": "Second Nightmare",
      "first_appearance": 17,
      "category": "world",
      "description": "The trial to advance from Awakened to Ascended. More dangerous than the First, with lower survival rates."
    },
    {
      "name": "Third Nightmare",
      "first_appearance": 15,
      "category": "world",
      "description": "The trial to advance from Ascended to Master. Survival rate is extremely low."
    },
    {
      "name": "Fourth Nightmare",
      "first_appearance": 81,
      "category": "world",
      "description": "The trial to advance from Master to Saint. Few ever attempt it, fewer survive."
    },
    {
      "name": "Nightmare Gate",
      "first_appearance": 484,
      "category": "world",
      "description": "Portals between the real world and Dream Realm. Can appear randomly or be created."
    },
    {
      "name": "Ascension",
      "first_appearance": 368,
      "category": "ranks",
      "description": "The process of advancing to a higher rank. Requires surviving specific trials."
    },
    {
      "name": "Great Clans",
      "first_appearance": 353,
      "category": "society",
      "description": "The most powerful families in human society. Control vast resources and political power."
    },
    {
      "name": "Cohort",
      "first_appearance": 55,
      "category": "society",
      "description": "A group of Awakened who survived together. Bonds forged in the Dream Realm are strong."
    },
    {
      "name": "Outskirts",
      "first_appearance": 1,
      "category": "locations",
      "description": "The poor districts on the edges of cities. Lawless and dangerous, where Sunny grew up."
    },
    {
      "name": "Citadel",
      "first_appearance": 23,
      "category": "locations",
      "description": "Major human fortification designed to withstand Nightmare Creature attacks."
    },
    {
      "name": "Great War",
      "first_appearance": 500,
      "category": "events",
      "description": "A legendary conflict that shaped the current state of humanity and the Dream Realm."
    },
    {
      "name": "Gates",
      "first_appearance": 14,
      "category": "world",
      "description": "Passages between locations in the Dream Realm or between realms entirely."
    },
    {
      "name": "Sacrifice",
      "first_appearance": 11,
      "category": "powers",
      "description": "The act of giving up something precious for power. A common theme in gaining strength."
    },
    {
      "name": "Temple",
      "first_appearance": 2,
      "category": "locations",
      "description": "Sacred structures in the Dream Realm, often containing powerful beings or treasures."
    },
    {
      "name": "Chain",
      "first_appearance": 2,
      "category": "powers",
      "description": "Bonds that can restrict or empower. Sunny's ability involves chains of shadow."
    },
    {
      "name": "Divine",
      "first_appearance": 6,
      "category": "powers",
      "description": "The highest quality of Memories and abilities. Incredibly rare and powerful."
    },
    {
      "name": "Void",
      "first_appearance": 15,
      "category": "world",
      "description": "The emptiness between realms. Dangerous to traverse."
    },
    {
      "name": "Twilight",
      "first_appearance": 36,
      "category": "world",
      "description": "A state between light and dark. A significant location and concept in the story."
    },
    {
      "name": "Daemon",
      "first_appearance": 277,
      "category": "creatures",
      "description": "Powerful beings, neither fully Nightmare Creature nor human. Often ancient and mysterious."
    },
    {
      "name": "Soul Sea",
      "first_appearance": 16,
      "category": "powers",
      "description": "The inner realm where an Awakened's soul cores and Memories are stored."
    },
    {
      "name": "Sundered",
      "first_appearance": 616,
      "category": "world",
      "description": "Something that has been broken or separated. Often refers to realms or beings split apart."
    },
    {
      "name": "Spell",
      "first_appearance": 1,
      "category": "world",
      "description": "Another name for the Nightmare Spell. The force that changed everything."
    }
  ],
  "locations": [
    {
      "name": "Dream Realm",
      "first_appearance": 1,
      "description": "A parallel dimension where Nightmare Creatures originate. Connected to Earth through the Nightmare Spell. Contains countless dangers, treasures, and mysteries."
    },
    {
      "name": "Forgotten Shore",
      "first_appearance": 34,
      "description": "A dangerous coastal region in the Dream Realm where many Sleepers are sent for their First Nightmare. Features ruins of an ancient civilization, deadly creatures, and the Bright Castle."
    },
    {
      "name": "Bright Castle",
      "first_appearance": 124,
      "description": "A fortified castle in the Forgotten Shore that serves as a refuge for survivors. Ruled tyrannically by Gunlaug until its fall."
    },
    {
      "name": "Dark City",
      "first_appearance": 126,
      "description": "A massive ruined metropolis in the Forgotten Shore, filled with powerful Nightmare Creatures and ancient secrets. Built by a lost civilization."
    },
    {
      "name": "Labyrinth",
      "first_appearance": 31,
      "description": "A massive maze-like structure in the Dream Realm. Contains valuable treasures but is extremely dangerous to navigate."
    },
    {
      "name": "Shadow Realm",
      "first_appearance": 729,
      "description": "A domain of pure darkness within the Dream Realm. Connected to shadow powers and Sunny's abilities."
    },
    {
      "name": "Twilight Sea",
      "first_appearance": 1279,
      "description": "A vast ocean separating major Dream Realm continents. Contains its own horrors and wonders."
    },
    {
      "name": "Abyss",
      "first_appearance": 3,
      "description": "The deepest, most dangerous region of the Dream Realm. Few who enter ever return."
    },
    {
      "name": "Kingdom of Hope",
      "first_appearance": 601,
      "description": "A realm created by the Demon of Imagination. Beautiful but ultimately tragic."
    },
    {
      "name": "Ivory Tower",
      "first_appearance": 382,
      "description": "A significant structure in the Dream Realm associated with knowledge and power."
    },
    {
      "name": "Red Colosseum",
      "first_appearance": 611,
      "description": "An arena in the Dream Realm where battles are fought for various purposes."
    },
    {
      "name": "Stone Forest",
      "first_appearance": 2270,
      "description": "A region of petrified trees, remnants of an ancient catastrophe."
    },
    {
      "name": "Verge",
      "first_appearance": 9,
      "description": "The edge between realms or states of being. A place of transition."
    },
    {
      "name": "Waking World",
      "first_appearance": 319,
      "description": "The real world, as opposed to the Dream Realm. Where humanity struggles to survive."
    },
    {
      "name": "Outskirts",
      "first_appearance": 1,
      "description": "The poor, lawless districts on the edges of cities. Sunny's birthplace and childhood home."
    },
    {
      "name": "Spell Academy",
      "first_appearance": 18,
      "description": "Schools in the real world that train Sleepers before they undergo their First Nightmare."
    },
    {
      "name": "Antarctic",
      "first_appearance": 816,
      "description": "The frozen continent, site of crucial battles against Nightmare Creatures. Location of the Falcon Scott siege."
    },
    {
      "name": "NQSC",
      "first_appearance": 754,
      "description": "National Quadrant Service Center. A government facility for Awakened."
    },
    {
      "name": "Police Station",
      "first_appearance": 1,
      "description": "Where Sunny sat before being taken to the Academy. Beginning of his journey."
    },
    {
      "name": "Slums",
      "first_appearance": 129,
      "description": "Impoverished areas of cities where life is hard and danger is constant."
    },
    {
      "name": "Citadel",
      "first_appearance": 23,
      "description": "Major fortified human settlements designed to withstand Nightmare Creature attacks."
    },
    {
      "name": "Bastion",
      "first_appearance": 127,
      "description": "Defensive positions in the Dream Realm or waking world."
    },
    {
      "name": "Castle",
      "first_appearance": 24,
      "description": "Various castles exist in both the Dream Realm and waking world, serving as strongholds."
    },
    {
      "name": "Palace",
      "first_appearance": 14,
      "description": "Grand structures in the Dream Realm, often belonging to powerful beings."
    },
    {
      "name": "Mountain",
      "first_appearance": 2,
      "description": "Various mountain ranges in both realms, often containing secrets."
    },
    {
      "name": "Tomb",
      "first_appearance": 325,
      "description": "Burial places of powerful beings, often containing their Memories and Echoes."
    },
    {
      "name": "Sanctuary",
      "first_appearance": 232,
      "description": "Safe havens in the Dream Realm, rare and precious."
    },
    {
      "name": "Serpent's Domain",
      "first_appearance": 30,
      "description": "The underwater territory in the Forgotten Shore, ruled by the Soul Serpent."
    },
    {
      "name": "Falcon Scott",
      "first_appearance": 843,
      "description": "A research station in Antarctica that became the site of a massive siege against Nightmare Creatures."
    }
  ],
  "events": [
    {
      "name": "First Nightmare",
      "first_appearance": 1,
      "description": "Sunny's traumatic trial in the Forgotten Shore that awakened his Shadow Slave Aspect. The beginning of his journey."
    },
    {
      "name": "Battle of the Forgotten Shore",
      "first_appearance": 250,
      "description": "Major conflict where Sunny's cohort defended the Bright Castle against waves of Nightmare Creatures."
    },
    {
      "name": "Fall of the Bright Castle",
      "first_appearance": 400,
      "description": "The destruction of the main safe haven on the Forgotten Shore, forcing survivors to flee into the wilderness."
    },
    {
      "name": "Escape from the Forgotten Shore",
      "first_appearance": 450,
      "description": "The cohort's desperate journey across the Dream Realm to return to the waking world."
    },
    {
      "name": "Sunny's Awakening",
      "first_appearance": 1,
      "description": "The moment Sunny gained his Shadow Slave Aspect and began his transformation."
    },
    {
      "name": "Second Nightmare Trial",
      "first_appearance": 600,
      "description": "Sunny's trial to advance from Awakened to Ascended, facing greater horrors than before."
    },
    {
      "name": "Antarctic Campaign",
      "first_appearance": 843,
      "description": "A major military operation against Nightmare Creatures in Antarctica. The Siege of Falcon Scott."
    },
    {
      "name": "Siege of Falcon Scott",
      "first_appearance": 843,
      "description": "Desperate battle at the Antarctic research station. Sunny earns the title 'Devil of Antarctica'."
    },
    {
      "name": "Third Nightmare Trial",
      "first_appearance": 1000,
      "description": "Sunny's trial to reach Master rank, facing impossibly powerful foes."
    },
    {
      "name": "Discovery of the Weave",
      "first_appearance": 83,
      "description": "Revelation about the fundamental nature of reality and the Dream Realm."
    },
    {
      "name": "Meeting Mordret",
      "first_appearance": 438,
      "description": "First encounter with the Prince of Nothing, one of the most dangerous beings."
    },
    {
      "name": "Rain's Awakening",
      "first_appearance": 900,
      "description": "Sunny's sister undergoes her transformation, changing the stakes dramatically."
    },
    {
      "name": "The Great Battle",
      "first_appearance": 2001,
      "description": "A massive conflict where hundreds of thousands of Awakened fight, with Sid and Felise's final confrontation."
    },
    {
      "name": "Confrontation with Noctis",
      "first_appearance": 381,
      "description": "Encounter with the Shadow Sovereign, revealing connections to Sunny's Aspect."
    },
    {
      "name": "Twilight Expedition",
      "first_appearance": 1500,
      "description": "Journey to Twilight to rescue allies and uncover truths about the Dread Lord and Soul Stealer."
    },
    {
      "name": "Hunt in the Labyrinth",
      "first_appearance": 31,
      "description": "Early expedition into the dangerous maze-like structure."
    },
    {
      "name": "Serpent's Defeat",
      "first_appearance": 217,
      "description": "Battle against and subsequent binding of the Soul Serpent."
    },
    {
      "name": "Stone Saint's Legacy",
      "first_appearance": 102,
      "description": "Discovery of the Stone Saint's remains and acquisition of the Saint Echo."
    },
    {
      "name": "Demon of Imagination's End",
      "first_appearance": 330,
      "description": "Confrontation with Mirage and the fate of her imaginary kingdom."
    },
    {
      "name": "Pursuit of Mortality",
      "first_appearance": 2701,
      "description": "Late-game events involving the nature of life and death."
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
