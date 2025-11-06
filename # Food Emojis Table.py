# Food Emojis Table
print("Food Emojis Table\n")

emojis = {
    r"\U0001F347": "\U0001F347",
    r"\U0001F348": "\U0001F348",
    r"\U0001F349": "\U0001F349",
    r"\U0001F34A": "\U0001F34A",
    r"\U0001F34B": "\U0001F34B",
    r"\U0001F34C": "\U0001F34C",
    r"\U0001F34D": "\U0001F34D",
    r"\U0001F96D": "\U0001F96D",
    r"\U0001F34E": "\U0001F34E",
    r"\U0001F34F": "\U0001F34F",
    r"\U0001F350": "\U0001F350",
    r"\U0001F351": "\U0001F351",
    r"\U0001F352": "\U0001F352",
    r"\U0001F353": "\U0001F353",
    r"\U0001F95D": "\U0001F95D",
    r"\U0001F345": "\U0001F345",
    r"\U0001F346": "\U0001F346",
    r"\U0001F951": "\U0001F951",
    r"\U0001F33D": "\U0001F33D",
    r"\U0001F966": "\U0001F966",
    r"\U0001F955": "\U0001F955",
    r"\U0001F9C4": "\U0001F9C4",
    r"\U0001F9C5": "\U0001F9C5",
    r"\U0001F954": "\U0001F954",
    r"\U0001F360": "\U0001F360",
    r"\U0001F950": "\U0001F950",
    r"\U0001F96F": "\U0001F96F",
    r"\U0001F35E": "\U0001F35E",
    r"\U0001F956": "\U0001F956",
    r"\U0001F968": "\U0001F968",
    r"\U0001F95E": "\U0001F95E",
    r"\U0001F9C7": "\U0001F9C7",
}

# Print the table with two emojis per line
table = "{:<5} {:12} {:<5} {:12}"
separator = "-" * 32

print(table.format("Emoji", "Unicode", "Emoji", "Unicode"))
print(separator)

emoji_pairs = [(emoji, unicode_value) for emoji, unicode_value in emojis.items()]

for i in range(0, len(emoji_pairs), 2):
    emoji1, unicode1 = emoji_pairs[i]
    emoji2, unicode2 = emoji_pairs[i + 1]
    print(table.format(emoji1, unicode1, emoji2, unicode2))