import json
import re
import os

# Load original PHB-style JSON
with open("data/10 magic items.json", "r", encoding="utf-8") as f:
    phb_data = json.load(f)

# Get inner content under "Magic Items"
items = phb_data.get("Magic Items", {})

# Output structure
grouped_by_rarity = {}

# Regex to extract all rarities from first line
rarity_regex = re.compile(r"\b(common|uncommon|rare|very rare|legendary)\b", re.IGNORECASE)

for name, content in items.items():
    if name == "content":
        continue  # skip the general description

    if not isinstance(content, dict) or "content" not in content:
        continue  # skip if not an item description

    entry = content.get("content", [])
    if not entry or not isinstance(entry, list):
        continue

    first_line = entry[0] if isinstance(entry[0], str) else ""
    description_lines = [line for line in entry[1:] if isinstance(line, str)]
    description = " ".join(description_lines)

    # Extract all rarities from the first line
    rarities = rarity_regex.findall(first_line)
    if not rarities:
        continue

    for rarity in rarities:
        rarity = rarity.lower()
        grouped_by_rarity.setdefault(rarity, []).append({
            "name": name,
            "description": description.strip()
        })

# Save result
with open("data/loot.json", "w", encoding="utf-8") as f:
    json.dump(grouped_by_rarity, f, ensure_ascii=False, indent=2)

print("✅ loot.json created successfully!")
