#!/usr/bin/env python3
"""
build_civilizations.py
----------------------
Generates Wave 2: World Anvil Ethnicity articles for the public-facing
civilizations of Sideros, plus an overview hub article.

ALL content here is hand-authored public-safe text. The GM-only layers from the
canon civilization table (handoff master §10) are deliberately EXCLUDED:
  - the per-civilization "13th position" secret-force identities,
  - every Ashen Coil leader,
  - the truth that the Coil leaders embody the thirteenth force,
  - Antarctos (a secret continent -> staged later as a PRIVATE Wave 5 article),
  - any named Quint Bond member (so the Abyssal Sea regent is left unnamed).

The public stance on "the thirteenth" is included because it is genuinely public:
every culture independently chose NOT to build a tradition around the 13th sign.

Term usage follows current canon: "Game Master", not "Concordance".
"""
import os, re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "articles", "civilizations")
os.makedirs(OUT, exist_ok=True)

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# (title, tradition, homeland, peoples, lens, notable[list], thirteenth)
CIVS = [
    ("The Duchy Compact of Terra Firma", "Western — the Court of Lords and Ladies",
     "Terra Firma, the central continent and primary stage of the age",
     "A diverse, largely human-led society; the great institution-builders of the world",
     "The Western tradition reads the zodiac as a court: each sign a noble office held by a Lord or Lady who embodies that sign's cosmic character. Rule is legitimised by zodiacal resonance, not merely bloodline.",
     ["The dominant political power of the central continent, governed by zodiac-aligned Lords and Ladies — among them the Solar seat of Leo, the volcanic Aries, the haunted Sagittarius, the grain-rich Taurus, the analytical Virgo, the deep-earth Capricorn, and the Libran High Arbiter whose floating city of Equilibrium weighs the law from above.",
      "The Compact itself is remembered as a landmark act of cross-cultural diplomacy — an agreement brokered between traditions that do not naturally share a framework."],
     "The thirteenth seat of the court is left deliberately vacant. A throne is set for it, and no one claims it."),

    ("Shen-lì, the Jade Empire", "Chinese — the Twelve Animals",
     "The vast eastern empire of Shen-lì",
     "Home of the Gear-Forged and the Geode-Kin engineering tradition — the apex of Magi-Tech",
     "The twelve signs are reckoned as the Twelve Animals, each a year and a temperament. The Azure Dragon Emperor embodies the supreme Leo/Dragon seat.",
     ["The most technologically advanced civilization in Sideros: steam, clockwork, constructed sapience, and paper currency.",
      "An unresolved cold war runs through the Empire over the legal status of the Gear-Forged — whether constructed people are property or persons. The Free Construct movement grows quietly beneath the official position."],
     "The calendar holds an Excised Animal — a thirteenth sign sealed out of the reckoning two thousand years ago, named only to forbid it."),

    ("The Abyssal Sea Civilisation", "Babylonian — the Celestial Court of the Deep",
     "The great abyssal sea and its trading ports",
     "Maritime traders and navigators who read fate in the stars over open water",
     "Babylonian star-reckoning governs the Abyssal Sea, where 'The Great One' (Leo) reigns supreme over a celestial court of the other signs.",
     ["A civilization of harbours, tides, and long trade routes, ruled in its coastal regencies by tidal authorities who answer to the rhythm of the sea as much as to any throne.",
      "Its navigators are among the finest in the world, charting both water and sky."],
     "The thirteenth is the sea itself — vast, unnamed, and never personified. The Abyssal peoples do not give the deep a face."),

    ("The Boreal Expanse", "Norse — Twelve Hearths and the Thing",
     "The frozen northern reaches",
     "The homeland of the Giant-Kin; a harsh, honour-bound, martial people",
     "Twelve Hearths, runic and elemental, govern the Boreal cold. Disputes are settled in assembly — the Thing — where every free voice carries weight.",
     ["Jarl Skadi rules the Aquarius hearth: seven feet of sentient blizzard who has, by her own reckoning, never met a real threat.",
      "Survival is a virtue here, and oaths are made in earnest because winter keeps them."],
     "The Boreal peoples name the thirteenth as the World-Serpent coiled at the root of the world, and forbid its worship. A serpent-cult stirs at the edges all the same — a growing heresy that troubles the Hearths."),

    ("The Tuathan Archipelago", "Celtic — the Tree Calendar",
     "The misted isles of the western waters",
     "A people who live close to the Fade; keepers of thresholds and old pacts",
     "The Tree Calendar orders the Tuathan year, each sign a tree and a season. Noctilith Moon-Stone marks their rites.",
     ["The boundary between the world and the Fade is thin here, and the Fade-Guardians ward the places where it wears through.",
      "Bargains, hospitality, and the precise keeping of one's word carry real and dangerous weight."],
     "Their thirteenth is a door in the old wood — one the Fade-Guardians keep, and never open."),

    ("Khem-Ma'at", "Egyptian — the Solar Dragon Lords",
     "The great river and the surrounding desert",
     "A solar priesthood and the smiths who arm the world against the Void",
     "Khem-Ma'at reckons by thirteen solar Dragon Lords, with the sun as the axis of all order.",
     ["Khem-Ma'at forges Sun-Kissed Adamas — among the few materials in the world that bite into Void-corruption. Its weaponsmiths are sought across continents.",
      "Each night, by their myth, the sun does battle with the serpent of chaos and rises again at dawn — a cycle their rites re-enact."],
     "The serpent of the night — Apep — is named as the enemy of order, fought and never fed. It is the thirteenth they will not honour."),

    ("K'uh-la'an", "Mayan — the Day-Lords",
     "The jungle lowlands and their sacred cenotes",
     "The homeland of the Serpent-Kin",
     "The Day-Lords rule the K'uh-la'an calendar, each day a deity with its own demands.",
     ["Weep-Stone serves as both currency and sacred material. The Cenote of Dreams is a site of vision and pilgrimage, guarded by the Petal-Weaver castes.",
      "Time, debt, and prophecy are tracked with exacting care."],
     "An unnamed Lord of the underworld holds the thirteenth seat — a power spoken around, never directly addressed."),

    ("The Ashélands of Orsha-Anu", "Yoruba — the Orisha",
     "The savanna lands of Orsha-Anu",
     "The homeland of the Ashé-Touched, marked in body by the Orisha",
     "The Orisha are approached through Ifá divination, which reads the will of the cosmos in cast patterns. Power here is relational — a covenant with a living force, not a title.",
     ["The Ashélands hold what may be the longest unbroken contact with a Legendary Beast in the world: four thousand years of communion, through Ifá, with the fragment of the Great Roc.",
      "Its diviners are consulted far beyond their borders."],
     "Their thirteenth is a Silence — a reading the Ifá priests can begin but choose never to complete."),

    ("Mori-Ōkami", "Japanese — Kami-Binding across Twelve Uji",
     "The forested isles of the east",
     "The homeland of the Wolf-Shifters",
     "Twelve Uji (clans) each bind a kami, and the balance of inner natures is a discipline of daily life.",
     ["The Grove of Fallen Stars is a site of pilgrimage and old power.",
      "Honour, restraint, and the careful holding of one's two natures define Mori-Ōkami life."],
     "A thirteenth clan once existed and was purged — struck from the records three centuries ago, its name unspoken in polite company."),

    ("The Great Kurgan Bog", "Mongolian — Sky and Earth, the Twelve Böö",
     "The vast bog and the open steppe beyond it",
     "Ancestor-revering peoples led by their shaman-keepers",
     "Twelve Böö (shamans) bridge Sky and Earth, and the ancestors are present participants in the living world.",
     ["The Bog-Keeper Oshen Varr holds the Scorpio seat, tending the boundary between the remembered and the buried.",
      "The bog itself preserves — bodies, memories, and grudges alike."],
     "The thirteenth is the Silent Ancestor — the one no living shaman will call by name."),

    ("Chinvat", "Persian — Asha and the Twelve Eagle Clans",
     "The high bridge-realm of Chinvat",
     "The homeland of the Avian peoples",
     "Asha — truth and right order — is the organising principle, upheld by twelve Eagle Clans whose word is meant to be unbreakable.",
     ["Chinvat's builders engineered the truth-enforcement field that underwrites the Libran city of Equilibrium — a working that makes a lie struggle to stand.",
      "To cross a bridge in Chinvat is to be measured; the realm prizes the weighing of souls and statements alike."],
     "At the foot of the great bridge lies a Void the Eagle Clans guard. The crossing is watched; the thirteenth is not invited across."),

    ("The Scattered Temples", "Hindu — Rāśi-Siddha across Twelve Temples",
     "No homeland — twelve temples scattered across the world",
     "Ascetics and healers of the Siddha traditions, including many of the long-lived Eldren",
     "The Rāśi-Siddha order pursues power through Tapas — the ascetic heat of discipline, sacrifice, and meditation. Each of the twelve temples tends one sign's tradition.",
     ["The Temples hold no political authority and claim none. Yet the Kanya Sanctum (Virgo) preserves the only reliable cure for Void-energy illness in all of Sideros — a fact that makes the otherwise unworldly order quietly indispensable.",
      "Theirs is a path of restraint, and of paying the true cost of power."],
     "The thirteenth temple's seat is left intentionally empty — not forbidden, simply unfilled, by a discipline four thousand years deep."),
]

OVERVIEW = (
    "The World of Sideros", "civilizations-overview",
    "[h2]Thirteen Cultures, One Shattered Sky[/h2]\n"
    "Before the Pantheonic Fall, the thirteen zodiac forces governed the cosmos through pure "
    "divine aether, and every people perceived them identically. After the Fall, that single "
    "signal fractured — and each surviving culture came to read the same forces through its own "
    "lens. This is why a Lord of Terra Firma, an Animal of the Jade Empire, an Orisha of the "
    "Ashélands, and a Day-Lord of K'uh-la'an can all be the [i]same[/i] cosmic power wearing "
    "different cultural faces.\n\n"
    "[h2]How the Lens Shapes the Power[/h2]\n"
    "The cultural framework a practitioner is raised in is not mere flavour: it determines which "
    "facets of a sign's power they can reach. A practitioner trained in two or more traditions "
    "of the same sign can access aspects no single-tradition practitioner ever touches — which "
    "is why the rare cross-cultural adept is among the most capable people alive.\n\n"
    "[h2]The Thirteenth Problem[/h2]\n"
    "Every cultural system in Sideros handles the twelve forces with its own precision and "
    "emphasis. And every one of them, independently and without consulting the others, arrived "
    "at the same conclusion about the thirteenth: [b]do not build a tradition around it.[/b] "
    "Western astrologers leave a throne empty. The Jade Empire excised an Animal from its "
    "calendar. The Babylonians refuse to give the deep a face. Across the whole world, the "
    "thirteenth seat is left vacant — a consensus no one organised, and the closest thing "
    "Sideros has to a universal truth.\n\n"
    "[i]The civilizations below are the twelve a traveller may openly walk among. What lies "
    "beneath the empty thirteenth seat is another matter, and another story.[/i]"
)

def front_matter(title, slug_, wave=2, template="ethnicity", category="Civilizations"):
    return ("---\n"
            f"title: {title}\n"
            f"template: {template}\n"
            f"category: {category}\n"
            "privacy: public\n"
            f"wave: {wave}\n"
            f"slug: {slug_}\n"
            "tags: [civilization, culture, player-facing]\n"
            "status: drafted\n"
            "source: handoff master §10 (secrets-stripped) + zodiac_cultures\n"
            "---\n\n")

def civ_body(c):
    title, trad, home, peoples, lens, notable, thirteenth = c
    b = [f"[b]Cultural Tradition:[/b] {trad}\n[b]Homeland:[/b] {home}\n[b]Peoples:[/b] {peoples}"]
    b.append("[h2]The Cultural Lens[/h2]\n" + lens)
    b.append("[h2]Notable Features[/h2]\n" + "\n\n".join(notable))
    b.append("[h2]The Thirteenth[/h2]\n" + thirteenth)
    return "\n\n".join(b)

def main():
    written = []
    # overview hub
    t, s, body = OVERVIEW
    fn = "00-civilizations-overview.md"
    open(os.path.join(OUT, fn), "w").write(
        front_matter(t, s, template="article") + body + "\n")
    written.append((fn, t))
    # civilizations
    for i, c in enumerate(CIVS, 1):
        title = c[0]
        s = slug(re.sub(r"^The\s+", "", title))
        fn = f"{i:02d}-{s}.md"
        open(os.path.join(OUT, fn), "w").write(front_matter(title, s) + civ_body(c) + "\n")
        written.append((fn, title))
    for fn, t in written:
        print(f"  wrote {fn:34s} {t}")
    print(f"\nTotal Wave 2 articles: {len(written)} (overview + {len(CIVS)} civilizations)")
    print("Excluded from public wave: Antarctos (secret continent -> Wave 5 private).")

if __name__ == "__main__":
    main()
