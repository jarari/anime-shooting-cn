import json
import re

# Load the glossary
glossary = {}
with open("C:\Assets\GFL2\CN Translation\anime-shooting-cn\gfl_dict.csv", "r", encoding="utf-8") as f:
    for line in f.readlines()[1:]:
        zh, ko = line.strip().split(",")
        glossary[zh] = ko

# Load the source file
with open("C:\Assets\GFL2\CN Translation\anime-shooting-cn\Gemini\scenario_texts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# More sophisticated translation function
def translate(text):
    # Punctuation conversion
    text = text.replace("。", ".").replace("？", "?").replace("！", "!").replace("，", ", ").replace("：", ": ").replace("；", "; ").replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'").replace("…", "...")

    # Glossary replacement (longer matches first)
    for zh in sorted(glossary.keys(), key=len, reverse=True):
        text = text.replace(zh, glossary[zh])

    # Special cases
    text = re.sub(r"心智(?![螺旋])", "마인드맵", text)
    text = text.replace("闪电", "그로자")

    # Basic contextual adjustments (example)
    if "我" in text and "你" in text:
        text = text.replace("我", "나").replace("你", "너")

    return text

# Translate the data
translated_data = {k: translate(k) for k in data.keys()}

# Save the translated data
with open("C:\Assets\GFL2\CN Translation\anime-shooting-cn\Gemini\scenario_texts_translated.json", "w", encoding="utf-8") as f:
    json.dump(translated_data, f, ensure_ascii=False, indent=4)

print("Translation complete.")
