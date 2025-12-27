// Shadow Slave Reader - by Guiltythree
// With AI Assistant and Comprehensive Wiki Sidebar

const WIKI_DATA = {
  "characters": [
    {
      "name": "Sunny",
      "first_appearance": 1,
      "aliases": [
        "Sunless",
        "Lost from Light",
        "Lord Shadow",
        "Mongrel",
        "Devil of Antarctica",
        "Master Sunless"
      ],
      "search_terms": [
        "Sunny",
        "Sunless",
        "Lost from Light",
        "Lord Shadow",
        "Mongrel",
        "Devil of Antarctica",
        "Master Sunless"
      ],
      "description": "Protagonist from the outskirts with the Shadow Slave Aspect. His Flaw 'Clear Conscience' prevents lying.",
      "attributes": [
        "Strategist under pressure",
        "Dry humor and pragmatic",
        "Protective of cohort",
        "Shadow techniques specialist"
      ],
      "echoes": [
        "Stone Saint",
        "Soul Serpent"
      ],
      "memories": [
        "Puppeteer's Shroud",
        "Midnight Shard",
        "Weaver's Mask",
        "Mantle of the Underworld",
        "Cruel Sight",
        "Covetous Coffer",
        "Shadow Lantern",
        "Sin of Solace"
      ],
      "explicit_powers": [
        "Shadow Step",
        "Shadow Dance",
        "Bone Weave",
        "Shadow Manifestation",
        "Soul Weave",
        "Soul Sea",
        "Soul Core",
        "True Name"
      ],
      "description_progression": [
        {
          "from_chapter": 1,
          "text": "Born in the lawless outskirts, Sunny enters the First Nightmare on the Black Mountain as a slave. Resourceful and sardonic, he survives by studying enemies, exploiting terrain, and masking his fear behind dry humor. The Spell reveals his Aspect\u2014Shadow Slave\u2014and the Flaw 'Clear Conscience', a constraint that forbids him from lying. His earliest victories are small but defining: reading people accurately, making ruthless decisions when cornered, and discovering that his shadow is more than a silhouette."
        },
        {
          "from_chapter": 34,
          "text": "On the Forgotten Shore, Sunny forms a fragile cohort as the stakes escalate from survival to strategy. He acquires the Stone Saint Echo, turning an ancient statue into his stalwart guardian, and begins to think in terms of assets, risk, and long-term outcomes. Bright Castle politics test his patience and morality, while his bond with Nephis, Cassie, Kai, and Effie deepens through shared hardship. These chapters forge his leadership\u2014not out of idealism, but out of relentless necessity and the willingness to bear difficult choices."
        },
        {
          "from_chapter": 351,
          "text": "After becoming Awakened, Sunny graduates from improvisation to systematized mastery: training, Memory curation, Echo integration, and refinement of shadow techniques. He learns to leverage Domains, Soul Sea logistics, and the delicate economy of fragments. The Second Nightmare pushes him into Ascended, expanding both his capabilities and the burden of his decisions. Friends become responsibilities; plans become labyrinths; and every gain costs something invisible but lasting."
        },
        {
          "from_chapter": 751,
          "text": "Earning the title 'Master Sunless' coincides with the Antarctic Campaign, where tactics scale from skirmishes to sieges. Sunny operates amid collapsing timelines and mass-casualty calculus, earning the epithet 'Devil of Antarctica' not out of cruelty, but from executing grim necessities. Leadership sharpens into a blade: precise, cold when required, protective when possible. His shadow repertoire expands, and the distinction between man and legend starts to blur."
        },
        {
          "from_chapter": 1022,
          "text": "In the Tomb of Ariel, time itself becomes a variable. Sunny navigates anomalies with disciplined paranoia, using Memory configurations and Echo deployments like chess pieces. He confronts entities tied to fate and inevitability, probing the boundaries of Weave and Name. The past and future press inward, demanding clarity he barely possesses. Yet he adapts, stacking contingencies and keeping his cohort alive through insight and grit."
        },
        {
          "from_chapter": 1309,
          "text": "The Twilight expedition is a crucible for everything Sunny has become: a strategist with shadows for soldiers, a friend who carries the weight of choices, and a survivor confronting rulers whose domains rewrite reality. His humor persists\u2014quieter now, edged by memory. He is not a hero by design; he is a practitioner of victory under constraints, shaping outcomes in worlds designed to break the stubborn."
        }
      ],
      "type": "protagonist",
      "aspect": "Shadow Slave",
      "flaw": "Clear Conscience",
      "clan": "None",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 1
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 640
        },
        {
          "rank": "Master",
          "from_chapter": 751
        }
      ]
    },
    {
      "name": "Nephis",
      "first_appearance": 24,
      "aliases": [
        "Changing Star",
        "Neph",
        "Light Bringer"
      ],
      "search_terms": [
        "Nephis",
        "Changing Star",
        "Neph",
        "Light Bringer"
      ],
      "description": "Legacy of Clan Valor whose inner fire burns with purpose. Her power exacts a personal cost.",
      "attributes": [
        "Disciplined leadership",
        "Endures personal cost",
        "Mission-focused",
        "Radiant combat style"
      ],
      "echoes": [],
      "memories": [],
      "explicit_powers": [
        "Domain"
      ],
      "description_progression": [
        {
          "from_chapter": 24,
          "text": "Introduced as a composed, silver-haired Legacy from Clan Valor, Nephis carries an aura of resolve. Her Aspect manifests as inner fire\u2014radiant and disciplined\u2014while the price of power is suffering borne quietly. At the Academy, her focus is absolute, hinting at a mission larger than prestige or rank."
        },
        {
          "from_chapter": 34,
          "text": "On the Forgotten Shore, Nephis becomes the axis of fragile order. She guides through crisis, makes measured sacrifices, and holds fast when fear should win. The cohort orbits her discipline; Sunny\u2019s cynicism learns to respect her burden. Her strength is not only in flame\u2014it is in choosing pain when ease would betray the goal."
        },
        {
          "from_chapter": 351,
          "text": "Awakened and ascending, Nephis\u2019s power refines into luminous precision. Hints of her family\u2019s complicated legacy surface\u2014debts owed, oaths kept, and a father known as Broken Sword whose shadow shapes her path. Valor\u2019s politics surround her, but she remains a sovereign mind, wielding duty like a blade."
        },
        {
          "from_chapter": 804,
          "text": "As alliances shift and threats mature, Nephis navigates the expectations of Clan Valor and the realities of war. Her decisions are rarely soft, but never empty; every choice advances a line she refuses to break. The cohort\u2019s faith in her is earned\u2014not by warmth, but by the integrity of outcomes."
        },
        {
          "from_chapter": 1700,
          "text": "By the time Saints enter the board, Nephis has become a study in radiance under constraint. Her inner fire is no longer spectacle\u2014it is governance, a principle turned power. She stands where others would kneel, paying costs measured not in pain, but in permanence."
        }
      ],
      "type": "main",
      "aspect": "Changing Star",
      "flaw": "Pristine Soul",
      "clan": "Valor",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 24
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 500
        },
        {
          "rank": "Master",
          "from_chapter": 1100
        },
        {
          "rank": "Saint",
          "from_chapter": 1700
        }
      ]
    },
    {
      "name": "Cassie",
      "first_appearance": 36,
      "aliases": [
        "Cassia",
        "Blind Oracle",
        "The Seer"
      ],
      "search_terms": [
        "Cassie",
        "Cassia",
        "blind girl",
        "oracle"
      ],
      "description": "Blind oracle whose visions thread danger and hope. Closely tied to Clan Song.",
      "attributes": [
        "Prophetic insight",
        "Gentle but resolute",
        "Advises with caution"
      ],
      "echoes": [],
      "memories": [],
      "explicit_powers": [
        "Soul Sea"
      ],
      "description_progression": [
        {
          "from_chapter": 36,
          "text": "Cassie enters as a quiet presence with sight shaped by prophecy rather than light. Her warnings are precise yet fragmentary, guiding the cohort through hazards that should be fatal. She trusts carefully, speaks sparingly, and pays for clarity with exhaustion that feels older than she is."
        },
        {
          "from_chapter": 55,
          "text": "Within the cohort, Cassie becomes the conscience of caution. Her visions map routes through ruin, but never promise safety. The group learns to treat her foresight as a tool\u2014not a crutch\u2014because fate bends, but rarely breaks. She grows from survivor to guide, shouldering the weight of being right too often."
        },
        {
          "from_chapter": 351,
          "text": "As an Awakened aligned with Clan Song, Cassie refines the discipline of reading futures without drowning in them. Her role broadens: negotiating, advising, and anchoring decisions with the humility of someone who knows how wrong right can feel. Mastery later adds authority, but her gentleness remains deliberate."
        },
        {
          "from_chapter": 1022,
          "text": "In places where time misbehaves, Cassie\u2019s sight complicates and clarifies in the same breath. She becomes a compass that points through paradox, reminding the cohort that progress is not linear and survival is both a choice and an art."
        }
      ],
      "type": "main",
      "aspect": "Oracle",
      "clan": "Song",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 36
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 800
        },
        {
          "rank": "Master",
          "from_chapter": 1132
        }
      ]
    },
    {
      "name": "Kai",
      "first_appearance": 115,
      "aliases": [
        "Nightingale",
        "The Singer"
      ],
      "search_terms": [
        "Kai",
        "Nightingale"
      ],
      "description": "Singer found on the Forgotten Shore whose voice carries power. Charming, loyal, and braver than he looks.",
      "attributes": [
        "Voice-based support",
        "Loyal teammate",
        "Morale stabilizer"
      ],
      "echoes": [],
      "memories": [],
      "explicit_powers": [],
      "description_progression": [
        {
          "from_chapter": 115,
          "text": "First discovered trapped in a well, Kai brings music to a world of stone and hunger. His Nightingale Aspect weaves resonance into words, turning songs into tools\u2014comfort, distraction, and subtle control. He bonds quickly, offering levity where silence would fester."
        },
        {
          "from_chapter": 200,
          "text": "Kai proves he is more than morale: he scouts, negotiates, and fights when he must. His courage is practical, not performative, and his loyalty survives deprivation intact. The cohort learns to rely on him for the human moments that keep strategy humane."
        },
        {
          "from_chapter": 351,
          "text": "As an Awakened, Kai refines control over voice\u2014calibrating influence, focus, and emotional balance. He becomes a bridge among strong personalities, turning friction into coordination. The Nightingale\u2019s song grows from survival tactic into battlefield instrument."
        }
      ],
      "type": "main",
      "aspect": "Nightingale",
      "clan": "None",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 115
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 750
        }
      ]
    },
    {
      "name": "Effie",
      "first_appearance": 126,
      "aliases": [
        "Athena",
        "Raised by Wolves",
        "The Glutton"
      ],
      "search_terms": [
        "Effie",
        "Athena",
        "Raised by Wolves"
      ],
      "description": "A fierce warrior with incredible strength and appetite. First encountered in Dark City. One of Sunny's closest friends.",
      "attributes": [
        "Relentless frontline fighter",
        "High endurance and strength",
        "Loyal and protective",
        "Tactical aggression"
      ],
      "type": "main",
      "aspect": "Raised by Wolves",
      "clan": "None",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 126
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 650
        },
        {
          "rank": "Master",
          "from_chapter": 1100
        }
      ]
    },
    {
      "name": "Caster",
      "first_appearance": 21,
      "aliases": [
        "Legacy of Song"
      ],
      "search_terms": [
        "Caster"
      ],
      "description": "A Legacy from Clan Song. Initially seems arrogant but proves to be a capable leader during the Forgotten Shore.",
      "attributes": [
        "Leadership under pressure",
        "Clan Song discipline",
        "Strategic planner",
        "Growth from arrogance to reliability"
      ],
      "type": "main",
      "clan": "Song",
      "rank_progression": [
        {
          "rank": "Sleeper",
          "from_chapter": 21
        },
        {
          "rank": "Awakened",
          "from_chapter": 351
        },
        {
          "rank": "Ascended",
          "from_chapter": 600
        }
      ]
    },
    {
      "name": "Rain",
      "first_appearance": 1,
      "aliases": [
        "Sunny's Sister"
      ],
      "search_terms": [
        "Rain",
        "sister"
      ],
      "description": "Sunny's younger sister. Living in the outskirts, she represents Sunny's main motivation for surviving.",
      "attributes": [
        "Sunny's core motivation",
        "Resilient despite hardship",
        "Symbol of hope"
      ],
      "type": "main",
      "clan": "None",
      "rank_progression": [
        {
          "rank": "Human",
          "from_chapter": 1
        },
        {
          "rank": "Sleeper",
          "from_chapter": 800
        },
        {
          "rank": "Awakened",
          "from_chapter": 1000
        }
      ]
    },
    {
      "name": "Shadow",
      "first_appearance": 2,
      "aliases": [
        "Sunny's Shadow",
        "Sentient Shadow"
      ],
      "search_terms": [
        "shadow",
        "his shadow"
      ],
      "description": "Sunny's own shadow which gained sentience. Mischievous and sometimes defiant, but ultimately loyal.",
      "attributes": [
        "Sentient shadow",
        "Mischievous but loyal",
        "Acts independently"
      ],
      "type": "companion"
    },
    {
      "name": "Stone Saint",
      "first_appearance": 103,
      "aliases": [
        "Saint"
      ],
      "search_terms": [
        "Stone Saint",
        "stone statue",
        "stone woman"
      ],
      "description": "Sunny's most powerful Echo. An ancient female Saint whose body turned to stone, now serves as Sunny's primary combat shadow.",
      "attributes": [
        "Ancient Saint",
        "Stone body",
        "Primary combat echo"
      ],
      "type": "echo"
    },
    {
      "name": "Soul Serpent",
      "first_appearance": 358,
      "aliases": [
        "Serpent",
        "The Serpent"
      ],
      "search_terms": [
        "Soul Serpent",
        "Serpent"
      ],
      "description": "A massive serpentine creature that Sunny binds as an Echo. Serves as transportation and a powerful ally.",
      "attributes": [
        "Massive serpent",
        "Transport and support",
        "Powerful ally"
      ],
      "type": "echo"
    },
    {
      "name": "Scholar",
      "first_appearance": 3,
      "aliases": [
        "The Teacher",
        "Old Man"
      ],
      "search_terms": [
        "Scholar",
        "old man",
        "teacher"
      ],
      "description": "An older slave during Sunny's First Nightmare on the Black Mountain. Appears kind but calculating.",
      "attributes": [
        "Calculating mentor",
        "Pragmatic survivor"
      ],
      "type": "supporting"
    },
    {
      "name": "Shifty",
      "first_appearance": 2,
      "aliases": [
        "The Thief"
      ],
      "search_terms": [
        "Shifty"
      ],
      "description": "A fellow slave during the First Nightmare. Meets a tragic end early in the story.",
      "attributes": [
        "Resourceful",
        "Tragic arc"
      ],
      "type": "minor"
    },
    {
      "name": "Hero",
      "first_appearance": 6,
      "aliases": [
        "Auro",
        "Auro of the Nine"
      ],
      "search_terms": [
        "Hero",
        "Auro"
      ],
      "description": "A legendary Sleeper who fought valiantly during the First Nightmare on the Black Mountain.",
      "attributes": [
        "Valiant Sleeper",
        "Inspires resolve"
      ],
      "type": "historical"
    },
    {
      "name": "Mountain King",
      "first_appearance": 4,
      "aliases": [
        "The Tyrant",
        "Black Mountain Tyrant"
      ],
      "search_terms": [
        "Mountain King",
        "tyrant"
      ],
      "description": "A massive Nightmare Creature that rules the Black Mountain. The main antagonist of Sunny's First Nightmare.",
      "attributes": [
        "Tyrant of Black Mountain",
        "Colossal strength",
        "Territorial ruler"
      ],
      "type": "creature"
    },
    {
      "name": "Gunlaug",
      "first_appearance": 98,
      "aliases": [
        "The Host",
        "Bright Lord"
      ],
      "search_terms": [
        "Gunlaug",
        "Bright Lord",
        "Host"
      ],
      "description": "The tyrannical ruler of the Bright Castle on the Forgotten Shore. Maintains order through fear.",
      "attributes": [
        "Tyrant of Bright Castle",
        "Uses fear for control",
        "Ascended"
      ],
      "type": "antagonist",
      "rank_progression": [
        {
          "rank": "Ascended",
          "from_chapter": 98
        }
      ]
    },
    {
      "name": "Harus",
      "first_appearance": 143,
      "aliases": [
        "The Hunchback"
      ],
      "search_terms": [
        "Harus",
        "hunchback"
      ],
      "description": "Gunlaug's cunning advisor. Despite his unassuming appearance, he is dangerous and calculating.",
      "attributes": [
        "Cunning strategist",
        "Behind-the-scenes manipulator"
      ],
      "type": "antagonist"
    },
    {
      "name": "Gemma",
      "first_appearance": 141,
      "aliases": [
        "The Huntress"
      ],
      "search_terms": [
        "Gemma"
      ],
      "description": "A skilled hunter from the Bright Castle who becomes an ally to Sunny's cohort.",
      "attributes": [
        "Skilled huntress",
        "Reliable ally"
      ],
      "type": "supporting"
    },
    {
      "name": "Harper",
      "first_appearance": 134,
      "aliases": [
        "The Healer"
      ],
      "search_terms": [
        "Harper"
      ],
      "description": "A healer at the Bright Castle who helps Sunny and his companions.",
      "attributes": [
        "Competent healer",
        "Compassionate"
      ],
      "type": "supporting"
    },
    {
      "name": "Jet",
      "first_appearance": 17,
      "aliases": [
        "Soul Reaper",
        "Master Jet"
      ],
      "search_terms": [
        "Jet",
        "Soul Reaper"
      ],
      "description": "A powerful Master who becomes Sunny's mentor. Cold in battle but cares for her students.",
      "attributes": [
        "Cold in battle, warm in duty",
        "Mentor to future elites",
        "Precise combat doctrine"
      ],
      "type": "mentor",
      "aspect": "Soul Reaper",
      "rank_progression": [
        {
          "rank": "Master",
          "from_chapter": 17
        }
      ]
    },
    {
      "name": "Teacher Julius",
      "first_appearance": 25,
      "aliases": [
        "Julius",
        "The Professor"
      ],
      "search_terms": [
        "Julius",
        "Teacher Julius"
      ],
      "description": "An instructor at the Awakened Academy who teaches about the Dream Realm.",
      "attributes": [
        "Academic instructor",
        "Explains Dream Realm fundamentals"
      ],
      "type": "mentor"
    },
    {
      "name": "Mordret",
      "first_appearance": 438,
      "aliases": [
        "Prince of Nothing",
        "Mirror Beast",
        "The Reflection"
      ],
      "search_terms": [
        "Mordret",
        "Prince of Nothing"
      ],
      "description": "A terrifying figure with the ability to possess bodies through reflections. Has connections to Clan Valor.",
      "attributes": [
        "Reflection possession",
        "Strategic and ruthless",
        "Clan Valor ties"
      ],
      "type": "antagonist",
      "aspect": "Reflection",
      "rank_progression": [
        {
          "rank": "Corrupted",
          "from_chapter": 438
        },
        {
          "rank": "Saint",
          "from_chapter": 1500
        }
      ]
    },
    {
      "name": "Noctis",
      "first_appearance": 381,
      "aliases": [
        "Shadow Lord",
        "Lord of Night"
      ],
      "search_terms": [
        "Noctis"
      ],
      "description": "An ancient Sovereign connected to shadow powers. Has deep connections to Sunny's Aspect.",
      "attributes": [
        "Shadow Sovereign",
        "Ancient and enigmatic",
        "Reality-adjacent influence"
      ],
      "type": "legendary",
      "rank_progression": [
        {
          "rank": "Sovereign",
          "from_chapter": 381
        }
      ]
    },
    {
      "name": "Ki Song",
      "first_appearance": 367,
      "aliases": [
        "The Song Patriarch",
        "Lord Song"
      ],
      "search_terms": [
        "Ki Song"
      ],
      "description": "The patriarch of Clan Song. A powerful figure who leads one of the Great Clans.",
      "attributes": [
        "Patriarch of Clan Song",
        "Saint of prophecy",
        "Measured authority"
      ],
      "type": "supporting",
      "rank_progression": [
        {
          "rank": "Saint",
          "from_chapter": 367
        }
      ]
    },
    {
      "name": "Whispering Blade",
      "first_appearance": 804,
      "aliases": [
        "The Blade"
      ],
      "search_terms": [
        "Whispering Blade"
      ],
      "description": "A powerful Saint of Clan Valor. Known for deadly blade techniques.",
      "attributes": [
        "Saint of Valor",
        "Deadly blade techniques",
        "Strict discipline"
      ],
      "type": "supporting",
      "rank_progression": [
        {
          "rank": "Saint",
          "from_chapter": 804
        }
      ]
    },
    {
      "name": "Broken Sword",
      "first_appearance": 27,
      "aliases": [
        "Nephis's Father"
      ],
      "search_terms": [
        "Broken Sword"
      ],
      "description": "Nephis's father, a disgraced warrior of Clan Valor. His story is intertwined with Nephis's motivation.",
      "attributes": [
        "Disgraced Valor warrior",
        "Central to Nephis's resolve"
      ],
      "type": "historical"
    },
    {
      "name": "Weaver",
      "first_appearance": 81,
      "aliases": [
        "The First Weaver",
        "Fate Weaver"
      ],
      "search_terms": [
        "Weaver"
      ],
      "description": "A primordial entity responsible for weaving the fundamental fabric of reality. Connected to fate and destiny.",
      "attributes": [
        "Primordial weaver",
        "Fate and Weave architect"
      ],
      "type": "entity"
    },
    {
      "name": "Ananke",
      "first_appearance": 1284,
      "aliases": [
        "Inevitability"
      ],
      "search_terms": [
        "Ananke"
      ],
      "description": "A mysterious entity associated with fate and inevitability. Encountered in the Tomb of Ariel.",
      "attributes": [
        "Entity of inevitability",
        "Tomb of Ariel encounter"
      ],
      "type": "entity"
    },
    {
      "name": "Sun God",
      "first_appearance": 353,
      "aliases": [
        "Lord of Light"
      ],
      "search_terms": [
        "Sun God",
        "Lord of Light"
      ],
      "description": "An ancient deity of immense power associated with light and fire. One of the divine beings of the old world.",
      "attributes": [
        "Divinity of light and fire",
        "Ancient world god"
      ],
      "type": "entity"
    },
    {
      "name": "War God",
      "first_appearance": 2,
      "aliases": [],
      "search_terms": [
        "War God"
      ],
      "description": "An ancient deity associated with battle and conflict. Worshipped in ancient times.",
      "attributes": [
        "Divinity of war",
        "Ancient worship"
      ],
      "type": "entity"
    },
    {
      "name": "Dread Lord",
      "first_appearance": 1309,
      "aliases": [
        "The Tyrant of Twilight"
      ],
      "search_terms": [
        "Dread Lord"
      ],
      "description": "A powerful ruler encountered in Twilight. Commands fear from all who know of him.",
      "attributes": [
        "Twilight tyrant",
        "Commands fear",
        "Saint-level threat"
      ],
      "type": "antagonist",
      "rank_progression": [
        {
          "rank": "Saint",
          "from_chapter": 1309
        }
      ]
    },
    {
      "name": "Soul Stealer",
      "first_appearance": 1309,
      "aliases": [
        "Thief of Souls"
      ],
      "search_terms": [
        "Soul Stealer"
      ],
      "description": "A terrifying being with the power to steal souls. Found in Twilight.",
      "attributes": [
        "Steals souls",
        "Twilight presence"
      ],
      "type": "antagonist"
    },
    {
      "name": "Undying Slaughter",
      "first_appearance": 1309,
      "aliases": [
        "The Immortal"
      ],
      "search_terms": [
        "Undying Slaughter"
      ],
      "description": "A fearsome being that cannot be killed by conventional means. Encountered in Twilight.",
      "attributes": [
        "Effectively immortal",
        "Relentless combatant"
      ],
      "type": "antagonist"
    },
    {
      "name": "Morgan",
      "first_appearance": 545,
      "aliases": [
        "Lady Morgan"
      ],
      "search_terms": [
        "Morgan"
      ],
      "description": "A powerful figure from Clan Valor with connections to Nephis's past.",
      "attributes": [
        "Master of Valor",
        "Influence on Nephis"
      ],
      "type": "supporting",
      "rank_progression": [
        {
          "rank": "Master",
          "from_chapter": 545
        }
      ]
    },
    {
      "name": "Solvane",
      "first_appearance": 520,
      "aliases": [],
      "search_terms": [
        "Solvane"
      ],
      "description": "A character encountered in the Chained Isles. Provides information about the Kingdom of Hope.",
      "attributes": [
        "Informed guide",
        "Chained Isles native"
      ],
      "type": "supporting"
    },
    {
      "name": "Belle",
      "first_appearance": 777,
      "aliases": [],
      "search_terms": [
        "Belle"
      ],
      "description": "An Awakened with charm-based abilities encountered during Sunny's work.",
      "attributes": [
        "Charm-based abilities",
        "Social intuition"
      ],
      "type": "supporting"
    },
    {
      "name": "Samara",
      "first_appearance": 822,
      "aliases": [],
      "search_terms": [
        "Samara"
      ],
      "description": "A skilled warrior who joins Sunny's team during the Antarctic campaign.",
      "attributes": [
        "Skilled Antarctic fighter",
        "Team-oriented"
      ],
      "type": "supporting"
    },
    {
      "name": "Naeve",
      "first_appearance": 831,
      "aliases": [
        "Master Naeve"
      ],
      "search_terms": [
        "Naeve"
      ],
      "description": "A Master-rank Awakened encountered during government operations.",
      "attributes": [
        "Government Master",
        "Operational discipline"
      ],
      "type": "supporting",
      "rank_progression": [
        {
          "rank": "Master",
          "from_chapter": 831
        }
      ]
    },
    {
      "name": "Sybil",
      "first_appearance": 1021,
      "aliases": [],
      "search_terms": [
        "Sybil"
      ],
      "description": "A character with prophetic abilities encountered in the later story.",
      "attributes": [
        "Prophetic insight",
        "Reserved presence"
      ],
      "type": "supporting"
    },
    {
      "name": "Asterion",
      "first_appearance": 367,
      "aliases": [
        "The Bull"
      ],
      "search_terms": [
        "Asterion"
      ],
      "description": "A powerful being associated with ancient labyrinths and protection.",
      "attributes": [
        "Labyrinth guardian",
        "Protective force"
      ],
      "type": "supporting"
    },
    {
      "name": "Dire Fang",
      "first_appearance": 1102,
      "aliases": [],
      "search_terms": [
        "Dire Fang"
      ],
      "description": "A fearsome creature or warrior encountered in the later arcs.",
      "attributes": [
        "Relentless",
        "High-impact combatant"
      ],
      "type": "supporting"
    },
    {
      "name": "Sid",
      "first_appearance": 1607,
      "aliases": [],
      "search_terms": [
        "Sid"
      ],
      "description": "A warrior whose battles take place during the Great War arc.",
      "attributes": [
        "Great War combatant",
        "Persistent fighter"
      ],
      "type": "supporting"
    },
    {
      "name": "Felise",
      "first_appearance": 1998,
      "aliases": [],
      "search_terms": [
        "Felise"
      ],
      "description": "A warrior locked in combat with Sid during the Great War.",
      "attributes": [
        "Opposes Sid",
        "Determined adversary"
      ],
      "type": "antagonist"
    },
    {
      "name": "Revel",
      "first_appearance": 237,
      "aliases": [],
      "search_terms": [
        "Revel"
      ],
      "description": "A character encountered in the story.",
      "attributes": [
        "Brief appearance",
        "Context-dependent role"
      ],
      "type": "supporting"
    },
    {
      "name": "Carapace Scavenger",
      "first_appearance": 33,
      "aliases": [
        "Scavenger"
      ],
      "search_terms": [
        "Carapace Scavenger",
        "scavenger"
      ],
      "description": "The weakest variant of Carapace creatures. Pack hunters that feed on corpses.",
      "type": "creature"
    },
    {
      "name": "Carapace Centurion",
      "first_appearance": 52,
      "aliases": [
        "Centurion"
      ],
      "search_terms": [
        "Carapace Centurion",
        "centurion"
      ],
      "description": "A more powerful variant of the Carapace. Commands lesser creatures.",
      "type": "creature"
    },
    {
      "name": "Carapace Demon",
      "first_appearance": 63,
      "aliases": [
        "Shell Demon"
      ],
      "search_terms": [
        "Carapace Demon"
      ],
      "description": "Nightmare Creatures with hard armored shells. Common foes on the Forgotten Shore.",
      "type": "creature"
    },
    {
      "name": "Blood Fiend",
      "first_appearance": 97,
      "aliases": [],
      "search_terms": [
        "Blood Fiend",
        "Fiend"
      ],
      "description": "A terrifying Nightmare Creature that hunts in the darkness. Extremely dangerous.",
      "type": "creature"
    },
    {
      "name": "Spire Messenger",
      "first_appearance": 132,
      "aliases": [
        "Messenger"
      ],
      "search_terms": [
        "Spire Messenger",
        "messenger"
      ],
      "description": "Flying Nightmare Creatures that soar through the Dream Realm.",
      "type": "creature"
    },
    {
      "name": "Fallen Titan",
      "first_appearance": 953,
      "aliases": [
        "Titan"
      ],
      "search_terms": [
        "Fallen Titan",
        "Titan"
      ],
      "description": "Massive Nightmare Creatures of devastating power. Can destroy cities.",
      "type": "creature"
    },
    {
      "name": "Clan Valor",
      "first_appearance": 24,
      "aliases": [
        "House Valor"
      ],
      "search_terms": [
        "Clan Valor",
        "Valor"
      ],
      "description": "One of the Great Clans. Nephis's clan. Values strength and honor.",
      "type": "organization"
    },
    {
      "name": "Clan Song",
      "first_appearance": 21,
      "aliases": [
        "House Song"
      ],
      "search_terms": [
        "Clan Song",
        "Song"
      ],
      "description": "One of the Great Clans. Known for prophecies and oracles. Cassie and Caster's clan.",
      "type": "organization"
    },
    {
      "name": "Great Clans",
      "first_appearance": 353,
      "aliases": [
        "Seven Clans"
      ],
      "search_terms": [
        "Great Clan",
        "seven clan"
      ],
      "description": "The most powerful families that control much of human society.",
      "type": "organization"
    },
    {
      "name": "Government",
      "first_appearance": 17,
      "aliases": [
        "The Authority"
      ],
      "search_terms": [
        "government",
        "authority"
      ],
      "description": "The governing body of human civilization. Manages Awakened forces.",
      "type": "organization"
    },
    {
      "name": "First Irregular Company",
      "first_appearance": 814,
      "aliases": [
        "The Irregulars"
      ],
      "search_terms": [
        "First Irregular",
        "Irregular Company"
      ],
      "description": "A special military unit formed for the Antarctic Campaign.",
      "type": "organization"
    },
    {
      "name": "Night Temple",
      "first_appearance": 403,
      "aliases": [],
      "search_terms": [
        "Night Temple"
      ],
      "description": "A mysterious organization or location associated with shadow and darkness.",
      "type": "organization"
    },
    {
      "name": "Song Army",
      "first_appearance": 1844,
      "aliases": [],
      "search_terms": [
        "Song Army"
      ],
      "description": "The military forces of Clan Song, deployed during the Great War.",
      "type": "organization"
    },
    {
      "name": "Puppeteer's Shroud",
      "first_appearance": 15,
      "aliases": [
        "The Shroud",
        "Silk Armor"
      ],
      "search_terms": [
        "Puppeteer's Shroud",
        "Shroud",
        "silk armor"
      ],
      "description": "Sunny's signature armor Memory. A silk armor that can transform and protect.",
      "type": "memory"
    },
    {
      "name": "Midnight Shard",
      "first_appearance": 74,
      "aliases": [
        "The Shard"
      ],
      "search_terms": [
        "Midnight Shard"
      ],
      "description": "A dark blade Memory that Sunny wields. One of his primary weapons.",
      "type": "memory"
    },
    {
      "name": "Weaver's Mask",
      "first_appearance": 278,
      "aliases": [
        "The Mask"
      ],
      "search_terms": [
        "Weaver's Mask"
      ],
      "description": "A mysterious Memory connected to the Weaver. Grants unique abilities.",
      "type": "memory"
    },
    {
      "name": "Mantle of the Underworld",
      "first_appearance": 377,
      "aliases": [
        "The Mantle"
      ],
      "search_terms": [
        "Mantle of the Underworld"
      ],
      "description": "A Memory associated with the underworld and death.",
      "type": "memory"
    },
    {
      "name": "Cruel Sight",
      "first_appearance": 415,
      "aliases": [
        "The Eye"
      ],
      "search_terms": [
        "Cruel Sight"
      ],
      "description": "A Memory that enhances Sunny's perception. Allows him to see through deceptions.",
      "type": "memory"
    },
    {
      "name": "Covetous Coffer",
      "first_appearance": 428,
      "aliases": [
        "The Coffer"
      ],
      "search_terms": [
        "Covetous Coffer"
      ],
      "description": "A Memory that provides extra-dimensional storage.",
      "type": "memory"
    },
    {
      "name": "Shadow Lantern",
      "first_appearance": 653,
      "aliases": [
        "The Lantern"
      ],
      "search_terms": [
        "Shadow Lantern"
      ],
      "description": "A powerful Divine-rank Memory. Can open gates between realms.",
      "type": "memory"
    },
    {
      "name": "Sin of Solace",
      "first_appearance": 869,
      "aliases": [
        "Solace"
      ],
      "search_terms": [
        "Sin of Solace",
        "Solace"
      ],
      "description": "A powerful sword Memory with its own consciousness. Has a dark history.",
      "type": "memory"
    }
  ],
  "terms": [
    {
      "name": "Nightmare Spell",
      "first_appearance": 1,
      "category": "world",
      "search_terms": [
        "Nightmare Spell",
        "Spell"
      ],
      "description": "The mysterious force that brought the Dream Realm and Nightmare Creatures to Earth."
    },
    {
      "name": "Dream Realm",
      "first_appearance": 1,
      "category": "world",
      "search_terms": [
        "Dream Realm"
      ],
      "description": "A parallel dimension where Nightmare Creatures originate. Contains dangers and treasures."
    },
    {
      "name": "Nightmare Creature",
      "first_appearance": 1,
      "category": "creatures",
      "search_terms": [
        "Nightmare Creature",
        "creature",
        "monster"
      ],
      "description": "Monstrous beings from the Dream Realm that threaten humanity."
    },
    {
      "name": "Awakened",
      "first_appearance": 1,
      "category": "ranks",
      "search_terms": [
        "Awakened"
      ],
      "description": "Humans who survived their First Nightmare and gained supernatural powers."
    },
    {
      "name": "First Nightmare",
      "first_appearance": 1,
      "category": "world",
      "search_terms": [
        "First Nightmare"
      ],
      "description": "The trial every Sleeper must survive to become Awakened."
    },
    {
      "name": "Aspect",
      "first_appearance": 1,
      "category": "powers",
      "search_terms": [
        "Aspect"
      ],
      "description": "The unique supernatural ability granted after becoming Awakened."
    },
    {
      "name": "Soul Core",
      "first_appearance": 2,
      "category": "powers",
      "search_terms": [
        "soul core",
        "core"
      ],
      "description": "The source of an Awakened's power. More cores mean more power."
    },
    {
      "name": "True Name",
      "first_appearance": 2,
      "category": "powers",
      "search_terms": [
        "True Name",
        "true name"
      ],
      "description": "The fundamental name of a being that holds power over their existence."
    },
    {
      "name": "Dormant",
      "first_appearance": 2,
      "category": "ranks",
      "search_terms": [
        "Dormant"
      ],
      "description": "The lowest rank of Nightmare Creatures and Memories."
    },
    {
      "name": "Memory",
      "first_appearance": 5,
      "category": "items",
      "search_terms": [
        "Memory"
      ],
      "description": "Magical items from defeated Nightmare Creatures. Can be weapons, armor, or tools."
    },
    {
      "name": "Divine",
      "first_appearance": 6,
      "category": "powers",
      "search_terms": [
        "Divine"
      ],
      "description": "The highest rank of Memories. Incredibly rare and powerful."
    },
    {
      "name": "Flaw",
      "first_appearance": 8,
      "category": "powers",
      "search_terms": [
        "Flaw"
      ],
      "description": "A weakness or curse that comes with every Aspect. Sunny cannot lie."
    },
    {
      "name": "Fallen",
      "first_appearance": 8,
      "category": "ranks",
      "search_terms": [
        "Fallen"
      ],
      "description": "Third rank of Nightmare Creatures. Challenging for Awakened."
    },
    {
      "name": "Ascended",
      "first_appearance": 9,
      "category": "ranks",
      "search_terms": [
        "Ascended"
      ],
      "description": "Third rank of power for humans. Requires completing Second Nightmare."
    },
    {
      "name": "Saint",
      "first_appearance": 9,
      "category": "ranks",
      "search_terms": [
        "Saint"
      ],
      "description": "Fifth rank of power. Saints possess god-like abilities. Extremely rare."
    },
    {
      "name": "Shadow Slave",
      "first_appearance": 15,
      "category": "powers",
      "search_terms": [
        "Shadow Slave"
      ],
      "description": "Sunny's unique Aspect. Allows control over shadows and shadow Echoes."
    },
    {
      "name": "Master",
      "first_appearance": 15,
      "category": "ranks",
      "search_terms": [
        "Master"
      ],
      "description": "Fourth rank of power. Elite Awakened with multiple soul cores."
    },
    {
      "name": "Corrupted",
      "first_appearance": 15,
      "category": "ranks",
      "search_terms": [
        "Corrupted"
      ],
      "description": "Fourth rank of Nightmare Creatures. Twisted and especially dangerous."
    },
    {
      "name": "Echo",
      "first_appearance": 16,
      "category": "powers",
      "search_terms": [
        "Echo"
      ],
      "description": "Creatures bound to serve an Awakened. Sunny's include Saint and Serpent."
    },
    {
      "name": "Soul Sea",
      "first_appearance": 16,
      "category": "powers",
      "search_terms": [
        "Soul Sea"
      ],
      "description": "Inner realm where Memories and Echoes are stored."
    },
    {
      "name": "Sleeper",
      "first_appearance": 17,
      "category": "ranks",
      "search_terms": [
        "Sleeper"
      ],
      "description": "Human marked by the Spell but who hasn't survived First Nightmare yet."
    },
    {
      "name": "Second Nightmare",
      "first_appearance": 17,
      "category": "world",
      "search_terms": [
        "Second Nightmare"
      ],
      "description": "Trial to advance from Awakened to Ascended. More dangerous."
    },
    {
      "name": "Clear Conscience",
      "first_appearance": 17,
      "category": "powers",
      "search_terms": [
        "Clear Conscience",
        "cannot lie"
      ],
      "description": "Sunny's Flaw. He cannot lie."
    },
    {
      "name": "Legacy",
      "first_appearance": 21,
      "category": "society",
      "search_terms": [
        "Legacy"
      ],
      "description": "Descendants of powerful Awakened with enhanced potential."
    },
    {
      "name": "Titan",
      "first_appearance": 23,
      "category": "ranks",
      "search_terms": [
        "Titan"
      ],
      "description": "Most powerful normal Nightmare Creatures. Can challenge Saints."
    },
    {
      "name": "Shadow Step",
      "first_appearance": 28,
      "category": "powers",
      "search_terms": [
        "Shadow Step"
      ],
      "description": "Sunny's ability to move instantly through shadows."
    },
    {
      "name": "Shadow Fragment",
      "first_appearance": 34,
      "category": "powers",
      "search_terms": [
        "shadow fragment"
      ],
      "description": "Resources Sunny collects to enhance shadow abilities."
    },
    {
      "name": "Cohort",
      "first_appearance": 55,
      "category": "society",
      "search_terms": [
        "cohort"
      ],
      "description": "A group of Awakened who survived together. Strong bonds."
    },
    {
      "name": "Domain",
      "first_appearance": 61,
      "category": "powers",
      "search_terms": [
        "Domain"
      ],
      "description": "Area of absolute control that Saints can manifest."
    },
    {
      "name": "Fourth Nightmare",
      "first_appearance": 81,
      "category": "world",
      "search_terms": [
        "Fourth Nightmare"
      ],
      "description": "Trial to advance from Master to Saint. Few survive."
    },
    {
      "name": "Weave",
      "first_appearance": 83,
      "category": "world",
      "search_terms": [
        "Weave"
      ],
      "description": "The fundamental structure underlying reality."
    },
    {
      "name": "Blood Weave",
      "first_appearance": 83,
      "category": "powers",
      "search_terms": [
        "Blood Weave"
      ],
      "description": "Manipulation of blood and life force. Dangerous but powerful."
    },
    {
      "name": "Lineage",
      "first_appearance": 85,
      "category": "society",
      "search_terms": [
        "Lineage"
      ],
      "description": "Inherited traits and powers from ancestors."
    },
    {
      "name": "Shadow Dance",
      "first_appearance": 187,
      "category": "powers",
      "search_terms": [
        "Shadow Dance"
      ],
      "description": "Sunny's signature combat technique using shadows."
    },
    {
      "name": "Daemon",
      "first_appearance": 277,
      "category": "creatures",
      "search_terms": [
        "Daemon",
        "daemon"
      ],
      "description": "Powerful ancient beings. Neither Nightmare Creature nor human."
    },
    {
      "name": "Great Clans",
      "first_appearance": 353,
      "category": "society",
      "search_terms": [
        "Great Clan"
      ],
      "description": "The most powerful families controlling human society."
    },
    {
      "name": "Sovereign",
      "first_appearance": 368,
      "category": "ranks",
      "search_terms": [
        "Sovereign"
      ],
      "description": "Highest known rank. God-like beings with reality-warping powers."
    },
    {
      "name": "Bone Weave",
      "first_appearance": 450,
      "category": "powers",
      "search_terms": [
        "Bone Weave"
      ],
      "description": "Reinforces Sunny's body with shadow power. Incredible durability."
    },
    {
      "name": "Nightmare Gate",
      "first_appearance": 484,
      "category": "world",
      "search_terms": [
        "Nightmare Gate",
        "Gate"
      ],
      "description": "Portals between real world and Dream Realm."
    },
    {
      "name": "Shadow Manifestation",
      "first_appearance": 744,
      "category": "powers",
      "search_terms": [
        "Shadow Manifestation"
      ],
      "description": "Advanced technique creating solid shadow constructs."
    },
    {
      "name": "Soul Weave",
      "first_appearance": 787,
      "category": "powers",
      "search_terms": [
        "Soul Weave"
      ],
      "description": "Advanced manipulation of soul energy."
    }
  ],
  "locations": [
    {
      "name": "Dream Realm",
      "first_appearance": 1,
      "search_terms": [
        "Dream Realm"
      ],
      "description": "A parallel dimension where Nightmare Creatures originate."
    },
    {
      "name": "Outskirts",
      "first_appearance": 1,
      "search_terms": [
        "Outskirts",
        "outskirts"
      ],
      "description": "The poor, lawless districts on the edges of cities. Sunny's birthplace."
    },
    {
      "name": "Black Mountain",
      "first_appearance": 4,
      "search_terms": [
        "Black Mountain"
      ],
      "description": "Location of Sunny's First Nightmare. Ruled by the Mountain King."
    },
    {
      "name": "Spell Academy",
      "first_appearance": 18,
      "search_terms": [
        "Academy",
        "Spell Academy"
      ],
      "description": "Schools that train Sleepers before their First Nightmare."
    },
    {
      "name": "Citadel",
      "first_appearance": 23,
      "search_terms": [
        "Citadel"
      ],
      "description": "Major fortified human settlements designed to withstand attacks."
    },
    {
      "name": "Labyrinth",
      "first_appearance": 31,
      "search_terms": [
        "Labyrinth",
        "labyrinth"
      ],
      "description": "A massive maze-like structure in the Dream Realm."
    },
    {
      "name": "Forgotten Shore",
      "first_appearance": 34,
      "search_terms": [
        "Forgotten Shore"
      ],
      "description": "A dangerous coastal region where Sleepers are sent for First Nightmare."
    },
    {
      "name": "Twilight",
      "first_appearance": 36,
      "search_terms": [
        "Twilight"
      ],
      "description": "A mysterious region between light and darkness. Home to powerful beings."
    },
    {
      "name": "Bright Castle",
      "first_appearance": 124,
      "search_terms": [
        "Bright Castle",
        "castle"
      ],
      "description": "Fortified castle on the Forgotten Shore. Ruled by Gunlaug."
    },
    {
      "name": "Dark City",
      "first_appearance": 126,
      "search_terms": [
        "Dark City"
      ],
      "description": "Massive ruined metropolis on the Forgotten Shore filled with secrets."
    },
    {
      "name": "Chained Isles",
      "first_appearance": 378,
      "search_terms": [
        "Chained Isles"
      ],
      "description": "Region of floating islands held by seven ancient chains."
    },
    {
      "name": "Sky Below",
      "first_appearance": 380,
      "search_terms": [
        "Sky Below"
      ],
      "description": "The vast emptiness beneath the Chained Isles. Falling means death."
    },
    {
      "name": "Ivory Tower",
      "first_appearance": 382,
      "search_terms": [
        "Ivory Tower"
      ],
      "description": "Significant structure in the Chained Isles."
    },
    {
      "name": "Night Temple",
      "first_appearance": 403,
      "search_terms": [
        "Night Temple"
      ],
      "description": "A mysterious temple associated with darkness and shadow."
    },
    {
      "name": "Kingdom of Hope",
      "first_appearance": 601,
      "search_terms": [
        "Kingdom of Hope"
      ],
      "description": "Beautiful realm created by the Demon of Hope. Setting of Second Nightmare."
    },
    {
      "name": "Estuary",
      "first_appearance": 630,
      "search_terms": [
        "Estuary"
      ],
      "description": "A significant landmark where waters meet."
    },
    {
      "name": "Antarctic",
      "first_appearance": 754,
      "search_terms": [
        "Antarctic",
        "Antarctica"
      ],
      "description": "Frozen continent, site of crucial battles. Devil of Antarctica title earned here."
    },
    {
      "name": "Great River",
      "first_appearance": 812,
      "search_terms": [
        "Great River"
      ],
      "description": "A massive river in the Tomb of Ariel where time flows strangely."
    },
    {
      "name": "Falcon Scott",
      "first_appearance": 843,
      "search_terms": [
        "Falcon Scott"
      ],
      "description": "Research station in Antarctica. Site of massive siege."
    },
    {
      "name": "Tomb of Ariel",
      "first_appearance": 1022,
      "search_terms": [
        "Tomb of Ariel"
      ],
      "description": "Ancient structure where time flows differently."
    }
  ],
  "events": [
    {
      "name": "Nightmare Spell Descends",
      "first_appearance": 1,
      "search_terms": [
        "Nightmare Spell",
        "Spell descended"
      ],
      "description": "The cataclysmic event that changed humanity forever."
    },
    {
      "name": "First Nightmare Begins",
      "first_appearance": 1,
      "search_terms": [
        "First Nightmare"
      ],
      "description": "Sunny enters the Dream Realm as a slave on the Black Mountain."
    },
    {
      "name": "Meeting Shifty",
      "first_appearance": 2,
      "search_terms": [
        "Shifty"
      ],
      "description": "Sunny meets his fellow slave Shifty in the caravan."
    },
    {
      "name": "Mountain King Defeated",
      "first_appearance": 6,
      "search_terms": [
        "Mountain King"
      ],
      "description": "Sunny escapes the tyrant of the Black Mountain."
    },
    {
      "name": "Shadow Slave Revealed",
      "first_appearance": 15,
      "search_terms": [
        "Shadow Slave"
      ],
      "description": "The Spell reveals Sunny's unique Aspect."
    },
    {
      "name": "Meeting Jet",
      "first_appearance": 17,
      "search_terms": [
        "Jet"
      ],
      "description": "Sunny meets his mentor Master Jet."
    },
    {
      "name": "Meeting Caster",
      "first_appearance": 21,
      "search_terms": [
        "Caster"
      ],
      "description": "Sunny meets the Legacy from Clan Song."
    },
    {
      "name": "Meeting Nephis",
      "first_appearance": 24,
      "search_terms": [
        "Nephis",
        "Changing Star"
      ],
      "description": "Sunny first encounters Nephis at the Academy."
    },
    {
      "name": "Arrival on Forgotten Shore",
      "first_appearance": 34,
      "search_terms": [
        "Forgotten Shore"
      ],
      "description": "Sunny's true First Nightmare begins on the desolate coast."
    },
    {
      "name": "Meeting Cassie",
      "first_appearance": 36,
      "search_terms": [
        "Cassie"
      ],
      "description": "Sunny meets the blind oracle."
    },
    {
      "name": "Cohort Formation",
      "first_appearance": 55,
      "search_terms": [
        "cohort"
      ],
      "description": "The cohort comes together to survive."
    },
    {
      "name": "Stone Saint Acquired",
      "first_appearance": 103,
      "search_terms": [
        "Stone Saint"
      ],
      "description": "Sunny binds his most powerful Echo."
    },
    {
      "name": "Meeting Kai",
      "first_appearance": 115,
      "search_terms": [
        "Kai",
        "Nightingale"
      ],
      "description": "Sunny finds Kai trapped in a well."
    },
    {
      "name": "Meeting Effie",
      "first_appearance": 126,
      "search_terms": [
        "Effie"
      ],
      "description": "Sunny encounters Effie in Dark City."
    },
    {
      "name": "Fall of Gunlaug",
      "first_appearance": 280,
      "search_terms": [
        "Gunlaug"
      ],
      "description": "The tyrant of Bright Castle is defeated."
    },
    {
      "name": "Escape from Shore",
      "first_appearance": 350,
      "search_terms": [
        "escape",
        "Forgotten Shore"
      ],
      "description": "The cohort escapes the Forgotten Shore."
    },
    {
      "name": "Sunny Becomes Awakened",
      "first_appearance": 351,
      "search_terms": [
        "Awakened",
        "survived"
      ],
      "description": "Sunny officially becomes an Awakened."
    },
    {
      "name": "Soul Serpent Bound",
      "first_appearance": 358,
      "search_terms": [
        "Soul Serpent"
      ],
      "description": "Sunny binds the massive serpent."
    },
    {
      "name": "Encountering Noctis",
      "first_appearance": 381,
      "search_terms": [
        "Noctis"
      ],
      "description": "Sunny learns of the Shadow Sovereign."
    },
    {
      "name": "Meeting Mordret",
      "first_appearance": 438,
      "search_terms": [
        "Mordret"
      ],
      "description": "First encounter with the Prince of Nothing."
    },
    {
      "name": "Second Nightmare Complete",
      "first_appearance": 640,
      "search_terms": [
        "Second Nightmare",
        "Ascended"
      ],
      "description": "Sunny becomes Ascended."
    },
    {
      "name": "Master Sunless",
      "first_appearance": 751,
      "search_terms": [
        "Master Sunless",
        "Master"
      ],
      "description": "Sunny achieves Master rank."
    },
    {
      "name": "Antarctic Campaign",
      "first_appearance": 816,
      "search_terms": [
        "Antarctic"
      ],
      "description": "Major military operation against Nightmare Creatures."
    },
    {
      "name": "Siege of Falcon Scott",
      "first_appearance": 843,
      "search_terms": [
        "Falcon Scott",
        "siege"
      ],
      "description": "Desperate battle at the research station."
    },
    {
      "name": "Devil of Antarctica",
      "first_appearance": 871,
      "search_terms": [
        "Devil of Antarctica"
      ],
      "description": "Sunny earns his fearsome title."
    },
    {
      "name": "Entering Tomb of Ariel",
      "first_appearance": 1022,
      "search_terms": [
        "Tomb of Ariel"
      ],
      "description": "Sunny enters the ancient tomb."
    },
    {
      "name": "Meeting Ananke",
      "first_appearance": 1284,
      "search_terms": [
        "Ananke"
      ],
      "description": "Encounter with the entity of fate."
    },
    {
      "name": "Twilight Expedition",
      "first_appearance": 1309,
      "search_terms": [
        "Twilight",
        "Dread Lord"
      ],
      "description": "Journey to confront the Dread Lord."
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
    chapterContent: '',
    allItems: [],
    
    init(chapterNum, chapterContent) {
        this.currentChapter = chapterNum;
        this.chapterContent = (chapterContent || '').toLowerCase();
        this.allItems = [
            ...WIKI_DATA.characters.map(i => ({...i, itemType: 'character'})),
            ...WIKI_DATA.terms.map(i => ({...i, itemType: 'term'})),
            ...WIKI_DATA.locations.map(i => ({...i, itemType: 'location'})),
            ...WIKI_DATA.events.map(i => ({...i, itemType: 'event'}))
        ];
        this.createModal();
        this.render();
        this.initTabs();
        this.initMobileToggle();
    },
    
    createModal() {
        if (document.getElementById('wiki-modal-overlay')) return;
        const overlay = document.createElement('div');
        overlay.id = 'wiki-modal-overlay';
        overlay.className = 'wiki-modal-overlay';
        overlay.innerHTML = `
            <div class="wiki-modal">
                <div class="wiki-modal-header">
                    <div>
                        <h2 id="wiki-modal-title"></h2>
                        <div class="badges" id="wiki-modal-badges"></div>
                    </div>
                    <button class="wiki-modal-close" onclick="WikiSidebar.closeModal()">✕</button>
                </div>
                <div class="wiki-modal-body">
                    <div id="wiki-modal-aliases" class="wiki-modal-aliases"></div>
                    <div id="wiki-modal-description" class="wiki-modal-description"></div>
                    <div id="wiki-modal-meta" class="wiki-modal-meta"></div>
                    <div id="wiki-modal-ranks"></div>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) this.closeModal();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') this.closeModal();
        });
    },
    
    getTerms(item) {
        const base = [item.name, ...(item.aliases || [])];
        const terms = (item.search_terms && item.search_terms.length > 0) ? item.search_terms : base;
        return terms.map(t => t.toLowerCase());
    },
    
    coMentionedItems(subjectItem, targetType) {
        const subjectTerms = this.getTerms(subjectItem);
        const items = this.allItems.filter(i => i.itemType === targetType && i.first_appearance <= this.currentChapter);
        return items.filter(it => {
            const itTerms = this.getTerms(it);
            const subjectMentioned = subjectTerms.some(t => this.chapterContent.includes(t));
            const itMentioned = itTerms.some(t => this.chapterContent.includes(t));
            return subjectMentioned && itMentioned;
        });
    },

    openModal(itemName) {
        const item = this.allItems.find(i => i.name === itemName);
        if (!item) return;
        
        const overlay = document.getElementById('wiki-modal-overlay');
        const isNew = item.first_appearance === this.currentChapter;
        
        // Title
        document.getElementById('wiki-modal-title').textContent = item.name;
        
        // Badges
        let badges = [];
        if (isNew) badges.push('<span class="badge new">FIRST APPEARANCE!</span>');
        if (item.type) badges.push(`<span class="badge">${item.type}</span>`);
        if (item.category) badges.push(`<span class="badge">${item.category}</span>`);
        
        // Current rank badge
        let currentRank = '';
        if (item.rank_progression && item.rank_progression.length > 0) {
            const applicableRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
            if (applicableRanks.length > 0) {
                currentRank = applicableRanks[applicableRanks.length - 1].rank;
                badges.push(`<span class="badge rank">${currentRank}</span>`);
            }
        }
        document.getElementById('wiki-modal-badges').innerHTML = badges.join('');
        
        // Aliases
        const aliasesEl = document.getElementById('wiki-modal-aliases');
        if (item.aliases && item.aliases.length > 0) {
            aliasesEl.innerHTML = `Also known as: ${item.aliases.join(', ')}`;
            aliasesEl.style.display = 'block';
        } else {
            aliasesEl.style.display = 'none';
        }
        
        // Description (progressive, stacked up to current chapter)
        const descEl = document.getElementById('wiki-modal-description');
        if (item.description_progression && Array.isArray(item.description_progression)) {
            const visible = item.description_progression
                .filter(p => p.from_chapter <= this.currentChapter)
                .sort((a, b) => a.from_chapter - b.from_chapter);
            if (visible.length > 0) {
                descEl.innerHTML = visible.map(p => `<p>${p.text}</p>`).join('');
            } else {
                descEl.innerHTML = `<p>${item.description}</p>`;
            }
        } else {
            descEl.innerHTML = `<p>${item.description}</p>`;
        }
        
        // Meta info
        let metaItems = [];
        metaItems.push(`<div class="wiki-modal-meta-item"><label>First Appearance</label><span>Chapter ${item.first_appearance}</span></div>`);
        if (item.aspect && item.aspect !== 'N/A') {
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Aspect</label><span>${item.aspect}</span></div>`);
        }
        if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') {
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Clan</label><span>${item.clan}</span></div>`);
        }
        if (item.itemType) {
            metaItems.push(`<div class="wiki-modal-meta-item"><label>Type</label><span style="text-transform:capitalize">${item.itemType}</span></div>`);
        }
        document.getElementById('wiki-modal-meta').innerHTML = metaItems.join('');
        
        // Rank history
        const ranksEl = document.getElementById('wiki-modal-ranks');
        if (item.rank_progression && item.rank_progression.length > 0) {
            const visibleRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
            if (visibleRanks.length > 0) {
                ranksEl.innerHTML = `
                    <div class="wiki-modal-rank-history">
                        <h4>⚔️ Rank Progression</h4>
                        <div class="wiki-modal-rank-list">
                            ${visibleRanks.map(r => `
                                <div class="wiki-modal-rank-entry ${r.from_chapter === this.currentChapter ? 'current' : ''}">
                                    <span class="rank">${r.rank}</span>
                                    <span class="chapter">Ch.${r.from_chapter}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
                ranksEl.style.display = 'block';
            } else {
                ranksEl.style.display = 'none';
            }
        } else {
            ranksEl.style.display = 'none';
        }

        // Power System: Aspect, Flaw, co-mentioned powers terms (up to current chapter)
        const powerChips = [];
        if (item.aspect && item.aspect !== 'N/A') {
            powerChips.push(`Aspect: ${item.aspect}`);
        }
        if (item.flaw && item.flaw !== 'N/A') {
            powerChips.push(`Flaw: ${item.flaw}`);
        }
        if (currentRank) {
            powerChips.push(`Rank: ${currentRank}`);
        }
        // Co-mentioned terms in category "powers"
        const coTerms = this.coMentionedItems(item, 'term').filter(t => (t.category || '') === 'powers');
        coTerms.forEach(t => powerChips.push(t.name));
        // Explicit powers mapping to terms (if present), filtered by current chapter
        if (Array.isArray(item.explicit_powers) && item.explicit_powers.length > 0) {
            const explicit = item.explicit_powers
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'term' && (i.category || '') === 'powers'))
                .filter(t => t && t.first_appearance <= this.currentChapter);
            explicit.forEach(t => powerChips.push(`${t.name} (Ch.${t.first_appearance})`));
        }

        const body = document.querySelector('.wiki-modal-body');
        body.querySelectorAll('.wiki-modal-section.dynamic').forEach(el => el.remove());
        if (powerChips.length > 0) {
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Power System</h3>
                <div class="chip-list">${powerChips.map(c => `<span class="chip">${c}</span>`).join('')}
                </div>
            `;
            body.appendChild(sec);
        }

        // Attributes (explicit or fallback from meta)
        let attributes = Array.isArray(item.attributes) ? item.attributes.slice() : [];
        if (attributes.length === 0) {
            const auto = [];
            if (item.type) auto.push(`Type: ${item.type}`);
            if (currentRank) auto.push(`Rank: ${currentRank}`);
            if (item.aspect && item.aspect !== 'N/A') auto.push(`Aspect: ${item.aspect}`);
            if (item.flaw && item.flaw !== 'N/A') auto.push(`Flaw: ${item.flaw}`);
            if (item.clan && item.clan !== 'N/A' && item.clan !== 'None') auto.push(`Clan: ${item.clan}`);
            attributes = auto;
        }
        // Echoes
        let echoes = [];
        if (Array.isArray(item.echoes) && item.echoes.length > 0) {
            echoes = item.echoes
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'echo'))
                .filter(e => e && e.first_appearance <= this.currentChapter);
        } else if (item.itemType === 'character') {
            echoes = this.coMentionedItems(item, 'echo');
        }
        // Memories
        let memories = [];
        if (Array.isArray(item.memories) && item.memories.length > 0) {
            memories = item.memories
                .map(name => this.allItems.find(i => i.name === name && i.itemType === 'memory'))
                .filter(m => m && m.first_appearance <= this.currentChapter);
        } else if (item.itemType === 'character') {
            memories = this.coMentionedItems(item, 'memory');
        }

        // Render sections (Attributes, Echoes, Memories)
        if (attributes.length > 0) {
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Attributes</h3>
                <div class="chip-list">${attributes.map(a => `<span class="chip">${a}</span>`).join('')}
                </div>
            `;
            body.appendChild(sec);
        }
        if (echoes.length > 0) {
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Echoes</h3>
                <div class="chip-list">${echoes.map(e => `<span class="chip">${e.name}<span class="meta">Ch.${e.first_appearance}</span></span>`).join('')}
                </div>
            `;
            body.appendChild(sec);
        }
        if (memories.length > 0) {
            const sec = document.createElement('div');
            sec.className = 'wiki-modal-section dynamic';
            sec.innerHTML = `
                <h3>Memories</h3>
                <div class="chip-list">${memories.map(m => `<span class="chip">${m.name}<span class="meta">Ch.${m.first_appearance}</span></span>`).join('')}
                </div>
            `;
            body.appendChild(sec);
        }
        
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    },
    
    closeModal() {
        const overlay = document.getElementById('wiki-modal-overlay');
        if (overlay) {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    },
    
    isItemMentioned(item) {
        // Hard gate: never show items before their first appearance
        if (typeof item.first_appearance === 'number' && item.first_appearance > this.currentChapter) {
            return false;
        }
        if (!item.search_terms || item.search_terms.length === 0) {
            const terms = [item.name, ...(item.aliases || [])];
            return terms.some(term => this.chapterContent.includes(term.toLowerCase()));
        }
        return item.search_terms.some(term => this.chapterContent.includes(term.toLowerCase()));
    },
    
    truncate(text, maxLen = 80) {
        if (text.length <= maxLen) return text;
        return text.substring(0, maxLen).trim() + '...';
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
        
        const visible = items.filter(item => this.isItemMentioned(item));
        visible.sort((a, b) => b.first_appearance - a.first_appearance);
        
        if (visible.length === 0) {
            container.innerHTML = '<div class="wiki-empty">No wiki entries mentioned in this chapter</div>';
            return;
        }
        
        container.innerHTML = visible.map(item => {
            const isNew = item.first_appearance === this.currentChapter;
            const newBadge = isNew ? '<span class="badge new">NEW</span>' : '';
            const typeBadge = item.type ? `<span class="badge">${item.type}</span>` : '';
            const categoryBadge = item.category ? `<span class="badge">${item.category}</span>` : '';
            
            // Get current rank if applicable
            let rankBadge = '';
            if (item.rank_progression && item.rank_progression.length > 0) {
                const applicableRanks = item.rank_progression.filter(r => r.from_chapter <= this.currentChapter);
                if (applicableRanks.length > 0) {
                    const currentRank = applicableRanks[applicableRanks.length - 1].rank;
                    const isUpgrade = applicableRanks[applicableRanks.length - 1].from_chapter === this.currentChapter && applicableRanks.length > 1;
                    rankBadge = isUpgrade ? `<span class="badge" style="background:#fbbf24;color:#1a1a2e">⬆️ ${currentRank}</span>` : '';
                }
            }
            
            // Progressive preview: latest paragraph up to current chapter or base description
            let previewText = item.description;
            if (item.description_progression && Array.isArray(item.description_progression)) {
                const visible = item.description_progression
                    .filter(p => p.from_chapter <= this.currentChapter)
                    .sort((a, b) => a.from_chapter - b.from_chapter);
                if (visible.length > 0) {
                    previewText = visible[visible.length - 1].text;
                }
            }
            const preview = this.truncate(previewText, 100);
            
            return `
                <div class="wiki-item ${isNew ? 'new-this-chapter' : ''}" onclick="WikiSidebar.openModal('${item.name.replace(/'/g, "\'")}')">
                    <h4>${item.name} ${newBadge || rankBadge || typeBadge || categoryBadge}</h4>
                    <div class="description-preview">${preview}</div>
                    <div class="click-hint">Click for more →</div>
                </div>
            `;
        }).join('');
        
        const tab = document.querySelector(`[data-tab="${type}"]`);
        if (tab) {
            const newCount = visible.filter(i => i.first_appearance === this.currentChapter).length;
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

// Text-to-Speech (Chapter pages)
const TTS = {
    utterance: null,
    paragraphs: [],
    index: 0,
    supported: () => (typeof window !== 'undefined' && 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window),

    clearHighlight() {
        this.paragraphs.forEach(p => p.classList.remove('tts-active'));
    },

    setHighlight(i) {
        this.clearHighlight();
        const el = this.paragraphs[i];
        if (!el) return;
        el.classList.add('tts-active');
        // Keep it visible without being too jumpy
        try { el.scrollIntoView({ block: 'nearest' }); } catch (e) { /* ignore */ }
    },

    loadParagraphs() {
        const nodes = Array.from(document.querySelectorAll('.chapter-content .chapter-paragraph'));
        this.paragraphs = nodes;
    },

    getText() {
        // Kept for backwards compatibility; paragraph-based TTS uses DOM paragraphs
        const container = document.querySelector('.chapter-content');
        if (!container) return '';
        const text = (container.innerText || container.textContent || '').trim();
        return text.replace(/\s+/g, ' ');
    },

    clearHighlight() {
        // Clear word-by-word highlights
        document.querySelectorAll('.tts-word-active').forEach(span => {
            const parent = span.parentNode;
            if (!parent) return;
            const text = span.textContent;
            parent.replaceChild(document.createTextNode(text), span);
            parent.normalize();
        });
        // Clear paragraph highlights
        if (this.paragraphs) {
            this.paragraphs.forEach(p => p.classList.remove('tts-active'));
        }
    },

    highlightWord(wordIndex) {
        // Find and highlight the word at wordIndex
        const container = document.querySelector('.chapter-content');
        if (!container) return;
        
        let currentWord = 0;
        const targetWord = wordIndex;
        
        const walkDOM = (node) => {
            if (node.nodeType === 3) { // Text node
                const text = node.textContent;
                const words = text.match(/\b\w+\b|\s+/g) || [];
                const newSpans = [];
                
                for (const word of words) {
                    if (word.match(/\s/)) {
                        newSpans.push(document.createTextNode(word));
                    } else {
                        if (currentWord === targetWord) {
                            const span = document.createElement('span');
                            span.className = 'tts-word-active';
                            span.textContent = word;
                            newSpans.push(span);
                        } else {
                            newSpans.push(document.createTextNode(word));
                        }
                        currentWord++;
                    }
                }
                
                if (newSpans.length > 0) {
                    node.parentNode.replaceChild(newSpans[0], node);
                    let prev = newSpans[0];
                    for (let i = 1; i < newSpans.length; i++) {
                        prev.parentNode.insertBefore(newSpans[i], prev.nextSibling);
                        prev = newSpans[i];
                    }
                }
            } else if (node.nodeType === 1) { // Element node
                Array.from(node.childNodes).forEach(child => walkDOM(child));
            }
        };
        
        walkDOM(container);
    },

    stop() {
        if (!this.supported()) return;
        window.speechSynthesis.cancel();
        this.utterance = null;
        this.index = 0;
        this.wordIndex = 0;
        this.clearHighlight();
    },

    speakCurrent(rate = 1.0) {
        if (!this.supported()) return;
        if (!this.paragraphs || this.paragraphs.length === 0) this.loadParagraphs();
        if (!this.paragraphs || this.paragraphs.length === 0) return;
        if (this.index < 0) this.index = 0;
        if (this.index >= this.paragraphs.length) {
            this.stop();
            return;
        }

        const text = (this.paragraphs[this.index].innerText || this.paragraphs[this.index].textContent || '').trim();
        if (!text) {
            this.index += 1;
            this.speakCurrent(rate);
            return;
        }

        const u = new SpeechSynthesisUtterance(text);
        u.rate = Math.max(0.5, Math.min(2.0, Number(rate) || 1.0));
        u.pitch = 1.0;
        u.volume = 1.0;

        this.utterance = u;
        this.setHighlight(this.index);
        this.wordIndex = 0;

        u.onboundary = (event) => {
            if (event.name === 'word') {
                this.clearHighlight();
                this.setHighlight(this.index);
                this.highlightWord(this.wordIndex);
                this.wordIndex++;
            }
        };

        u.onend = () => {
            this.wordIndex = 0;
            this.index += 1;
            this.speakCurrent(rate);
        };
        u.onerror = () => {
            this.stop();
        };

        window.speechSynthesis.speak(u);
    },

    speak(rate = 1.0) {
        if (!this.supported()) return;
        this.stop();
        this.loadParagraphs();
        this.index = 0;
        this.wordIndex = 0;
        this.speakCurrent(rate);
    },

    pause() {
        if (!this.supported()) return;
        if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) window.speechSynthesis.pause();
    },

    resume() {
        if (!this.supported()) return;
        if (window.speechSynthesis.paused) window.speechSynthesis.resume();
    }
};

// AI Assistant
const AIAssistant = {
    responses: {
        greetings: [
            "Hello, Sleeper! Welcome to your journey through the Dream Realm. I'm here to help you navigate this dark and twisted world. Feel free to ask me about characters, the power system, world lore, or your reading progress. What would you like to know?",
            "Greetings, fellow traveler! I'm your guide through Shadow Slave's intricate world. Whether you want to learn about the Nightmare Spell, understand the Awakened ranks, or get info on specific characters like Sunny and Nephis - just ask. How can I assist you today?",
            "Welcome back to the Dream Realm! Ready to continue your adventure? I can help you with character backgrounds, world-building concepts, the complex power system, or help you pick up where you left off. What's on your mind?"
        ],
        sunny: "Sunny, also known as Sunless, is the protagonist of Shadow Slave. He grew up as an orphan in the outskirts - the slums outside the protective walls of human cities. After surviving his First Nightmare, he Awakened with the Shadow Aspect, granting him control over shadows and eventually earning him the title 'Lord Shadow'. What makes Sunny unique is his cunning intellect and dark, sarcastic humor. He's a pragmatic survivor who relies on wit rather than brute strength. His journey from a powerless outcast to one of the most formidable beings is the heart of the story. His sentient shadow companion adds another layer of mystery to his already complex abilities.",
        nephis: "Nephis, known by her True Name 'Changing Star', is one of the most compelling characters in Shadow Slave. She's a Legacy - someone born into one of the great clans (Clan Valor) that have shaped humanity's survival against the Nightmare Spell. Nephis possesses an extraordinary inner fire that literally burns within her, making her one of the most powerful Awakened of her generation. Despite her noble background, she's driven by complex motivations that often put her at odds with her own family. Her relationship with Sunny is central to the story - a mix of mutual respect, tension, and something deeper that evolves throughout the chapters.",
        cassie: "Cassie, sometimes called Cassia, is a blind prophet whose abilities are both a gift and a curse. After becoming Awakened, she gained the power to see visions of the future - glimpses of what's to come that are remarkably accurate. Despite her gentle, kind nature, her prophecies often reveal terrifying truths about the world and its fate. Being blind in the physical world but able to 'see' the future creates a fascinating duality in her character. She's one of Sunny's closest companions, and her prophecies have saved the group countless times - though the burden of knowing what's coming weighs heavily on her.",
        nightmare: "The Nightmare Spell is the catastrophic event that changed humanity forever. It brought the Dream Realm - a dimension of monsters, ancient gods, and unimaginable horrors - crashing into Earth's reality. But it also gave humanity a chance: those who survive their First Nightmare in the Dream Realm return as Awakened, gaining supernatural Aspects and powers. The Spell is mysterious - no one fully understands its origins or true purpose. Some believe it's a curse, others a twisted form of evolution. What's certain is that it created the entire power structure of the world: the great clans, the Citadel, the constant war against Nightmare Creatures, and the desperate struggle for humanity's survival.",
        awakened: "The Awakened are humans who survived their First Nightmare and emerged with supernatural powers called Aspects. The ranking system goes: Sleeper (before awakening) → Awakened (first rank) → Ascended → Master → Saint → Sovereign (the highest known rank). Each rank represents an exponential increase in power. Awakened protect humanity from Nightmare Creatures and explore the Dream Realm for resources and knowledge. The higher ranks become almost godlike in their abilities. Most Awakened never progress beyond the first few ranks - reaching Master is exceptional, and Saints are legendary figures. The journey through these ranks, the trials required, and the transformations involved are central to the story's progression.",
        aspect: "An Aspect is the unique supernatural ability granted to someone after becoming Awakened - it defines their power, fighting style, and often their fate. Each Aspect is different: some grant control over elements, others enhance physical abilities, some provide utility powers. But every Aspect comes with a Flaw - an inherent weakness or curse that balances the power. Flaws can be debilitating or even lethal. For example, Sunny's Shadow Aspect gives him incredible abilities, but his Flaw creates significant complications in his life. The interplay between Aspect powers and their Flaws creates strategic depth in combat and character development throughout the story.",
        shadow: "Sunny's sentient shadow is one of the most intriguing mysteries of the series. Unlike normal shadows, his has its own personality, thoughts, and sometimes even seems to act independently. It can express emotions through gestures and movements, often in humorous or sarcastic ways that mirror Sunny's own personality. The shadow's sentience is connected to his Shadow Aspect, but the full extent of their relationship and the shadow's true nature unfolds gradually through the story. It serves as both a companion and an extension of Sunny's powers, adding depth to his abilities and creating memorable comedic and dramatic moments.",
        progress: () => {
            const last = Storage.getLastChapter();
            const count = Storage.getReadCount();
            if (last) {
                const percent = Math.round((last / 2720) * 100);
                return `Great progress! You've read ${count} chapters so far (${percent}% of the story). You were last reading Chapter ${last}. The journey continues - there's still so much to discover about Sunny's path through the Dream Realm. Ready to continue?`;
            }
            return "You haven't started reading yet! Shadow Slave is an epic journey of over 2,700 chapters following Sunny's transformation from an outcast to a legend. Begin with Chapter 1 and experience the Nightmare Spell for yourself!";
        },
        wiki: "The Wiki sidebar on the right is your companion through the story! It dynamically shows characters, terms, locations, and events that have appeared up to your current chapter - so you won't encounter spoilers for content you haven't read yet. Click on any entry to see more details. It's perfect for refreshing your memory on who's who or understanding the complex terminology of the Dream Realm. Note: The wiki information is approximate and may not be 100% accurate for all entries.",
        help: "I'm here to help you navigate Shadow Slave! Here's what I can assist with:\n\n• Character info - Ask about Sunny, Nephis, Cassie, or other characters\n• World lore - The Nightmare Spell, Dream Realm, great clans\n• Power system - Aspects, Flaws, Awakened ranks (Sleeper to Sovereign)\n• Your progress - Where you left off, chapters read\n• Wiki guide - How to use the spoiler-free sidebar\n\nJust type your question naturally. For example: 'Tell me about Sunny' or 'What are Aspects?'",
        unknown: [
            "I don't have specific information on that topic, but I'd love to help with something else! Try asking about the main characters (Sunny, Nephis, Cassie), the power system (Aspects, Awakened ranks), or the world lore (Nightmare Spell, Dream Realm). What interests you?",
            "That's beyond my current knowledge base. I'm best at explaining Shadow Slave's core concepts - the Nightmare Spell, character backgrounds, the Awakened ranking system, Aspects and Flaws. Would you like to know about any of these?",
            "Hmm, I'm not sure about that particular topic. How about I tell you about one of the main characters? Sunny's journey from outcast to legend is fascinating, or I could explain how the Awakened power system works. What sounds interesting?"
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
        // Get chapter content from the page for wiki filtering
        const chapterContent = document.querySelector('.chapter-content')?.textContent || '';
        WikiSidebar.init(chapterNum, chapterContent);

        // Init Text-to-Speech controls
        const ttsRoot = document.querySelector('[data-tts]');
        if (ttsRoot) {
            const playBtn = ttsRoot.querySelector('.tts-play');
            const pauseBtn = ttsRoot.querySelector('.tts-pause');
            const resumeBtn = ttsRoot.querySelector('.tts-resume');
            const stopBtn = ttsRoot.querySelector('.tts-stop');
            const rateSel = ttsRoot.querySelector('.tts-rate');
            const unsupported = ttsRoot.querySelector('.tts-unsupported');

            const isSupported = TTS.supported();
            if (!isSupported) {
                if (unsupported) unsupported.style.display = '';
                [playBtn, pauseBtn, resumeBtn, stopBtn, rateSel].forEach(el => { if (el) el.disabled = true; });
            } else {
                if (unsupported) unsupported.style.display = 'none';
                if (playBtn) playBtn.addEventListener('click', () => TTS.speak(rateSel?.value || 1));
                if (pauseBtn) pauseBtn.addEventListener('click', () => TTS.pause());
                if (resumeBtn) resumeBtn.addEventListener('click', () => TTS.resume());
                if (stopBtn) stopBtn.addEventListener('click', () => TTS.stop());

                window.addEventListener('beforeunload', () => TTS.stop());
            }
        }
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

// Firebase Integration
const FirebaseConfig = {
    apiKey: "YOUR_FIREBASE_API_KEY",
    authDomain: "YOUR_FIREBASE_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_FIREBASE_PROJECT_ID",
    storageBucket: "YOUR_FIREBASE_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

let currentUser = null;
let db = null;

async function initFirebase() {
    try {
        firebase.initializeApp(FirebaseConfig);
        db = firebase.firestore();
        
        firebase.auth().onAuthStateChanged(user => {
            currentUser = user;
            updateAuthUI();
            if (user) {
                loadComments();
            }
        });
    } catch (e) {
        console.log('Firebase not configured. To enable auth & comments, set up Firebase config in the code.');
    }
}

function updateAuthUI() {
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const userDisplay = document.getElementById('user-display');
    const authContainer = document.getElementById('auth-container');
    
    if (!authContainer) return;
    
    if (currentUser) {
        loginBtn.style.display = 'none';
        logoutBtn.style.display = 'block';
        userDisplay.textContent = currentUser.email ? currentUser.email.split('@')[0] : 'User';
        authContainer.style.display = 'flex';
    } else {
        loginBtn.style.display = 'block';
        logoutBtn.style.display = 'none';
        userDisplay.textContent = '';
    }
}

async function handleLogin() {
    if (!firebase) {
        alert('Firebase not configured');
        return;
    }
    const provider = new firebase.auth.GoogleAuthProvider();
    try {
        await firebase.auth().signInWithPopup(provider);
    } catch (e) {
        alert('Login failed: ' + e.message);
    }
}

async function handleLogout() {
    try {
        await firebase.auth().signOut();
    } catch (e) {
        alert('Logout failed: ' + e.message);
    }
}

let currentCommentChapter = null;
let currentCommentParagraph = null;

function showCommentModal(chapterNum, paragraphIndex) {
    if (!currentUser) {
        alert('Please sign in to comment');
        return;
    }
    currentCommentChapter = chapterNum;
    currentCommentParagraph = paragraphIndex;
    document.getElementById('comment-text').value = '';
    document.getElementById('comment-modal').style.display = 'block';
}

async function submitComment() {
    const text = document.getElementById('comment-text').value.trim();
    if (!text || !currentUser || !db) {
        alert('Error: Could not submit comment');
        return;
    }
    
    try {
        await db.collection('comments').add({
            chapter: currentCommentChapter,
            paragraph: currentCommentParagraph,
            userId: currentUser.uid,
            email: currentUser.email,
            text: text,
            timestamp: new Date(),
            likes: 0
        });
        document.getElementById('comment-modal').style.display = 'none';
        loadComments();
    } catch (e) {
        alert('Error posting comment: ' + e.message);
    }
}

async function loadComments() {
    if (!db) return;
    
    const chapterNum = document.querySelector('[data-chapter]')?.dataset.chapter;
    if (!chapterNum) return;
    
    try {
        const snapshot = await db.collection('comments')
            .where('chapter', '==', parseInt(chapterNum))
            .orderBy('timestamp', 'desc')
            .get();
        
        const paragraphs = document.querySelectorAll('.chapter-paragraph');
        paragraphs.forEach((p, idx) => {
            const commentsBucket = p.querySelector('.paragraph-comments');
            if (commentsBucket) commentsBucket.remove();
            
            const paraComments = snapshot.docs.filter(doc => doc.data().paragraph === idx);
            if (paraComments.length > 0) {
                const container = document.createElement('div');
                container.className = 'paragraph-comments';
                container.style.cssText = `
                    margin-top: 1rem;
                    padding: 1rem;
                    background: rgba(255, 255, 255, 0.03);
                    border-left: 2px solid var(--secondary);
                    border-radius: 0;
                    font-size: 0.9rem;
                `;
                
                paraComments.forEach(doc => {
                    const data = doc.data();
                    const commentEl = document.createElement('div');
                    commentEl.style.marginBottom = '0.75rem';
                    commentEl.innerHTML = `
                        <div style="color: var(--primary); font-weight: 500;">${data.email.split('@')[0]}</div>
                        <div style="color: var(--text-light); font-size: 0.8rem; margin-bottom: 0.25rem;">${new Date(data.timestamp.toDate()).toLocaleDateString()}</div>
                        <div>${data.text}</div>
                    `;
                    container.appendChild(commentEl);
                });
                
                p.parentNode.insertBefore(container, p.nextSibling);
            }
        });
    } catch (e) {
        console.log('Comments not available:', e.message);
    }
}

// Setup event listeners and handlers
document.addEventListener('DOMContentLoaded', () => {
    // Auth handlers
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    if (loginBtn) loginBtn.addEventListener('click', handleLogin);
    if (logoutBtn) logoutBtn.addEventListener('click', handleLogout);
    
    // Comment system: add click handlers to paragraphs
    document.querySelectorAll('.chapter-paragraph').forEach((p, idx) => {
        p.style.cursor = 'pointer';
        p.addEventListener('click', () => {
            showCommentModal(document.querySelector('[data-chapter]')?.dataset.chapter, idx);
        });
    });
    
    // Initialize Firebase
    initFirebase();
});

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
