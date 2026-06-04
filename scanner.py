import json

autos = [
    {
        "title": "BMW E46 320i",
        "price": "2500 €",
        "km": "197000 km",
        "distance": "18 km entfernt",
        "url": "https://www.kleinanzeigen.de/s-autos/sinzig/c216l5395"
    }
]

with open("autos.json", "w", encoding="utf-8") as f:
    json.dump(autos, f, ensure_ascii=False, indent=2)

print("Autos gespeichert")
