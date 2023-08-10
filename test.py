def test(name, values: dict):
    max_value = max(values.values())
    y = min(max(max_value, 1), 10)

    val = ""
    for i in range(10, 0, -1):
        for j in values:
            # Normaliser la valeur pour qu'elle soit comprise entre 1 et y en fonction de max_value
            normalized_value = min(int(values[j] * y / max_value), y)
            if normalized_value >= i:
                val += "█ "
            else:
                val += "▒ "
        val += f" {int(i * max_value / y)}\n"

    legend = "_"
    val += "---".join([f"{count}" for count, i in enumerate(values)])
    legend = " | ".join([f"{count}: {i}" for count, i in enumerate(values)])
    legend += "_"
    val += "\n" + legend
    return val


# print(test("Test",{"Test1":1,"Test2":10,"Test3":4,"Test4":20}))

import math
import random


def generate_legend(data):
    emojis = ["🔴", "🔵", "🟢", "🟡", "🟣"]
    total = sum(data)

    val: list = []
    for i, valeur in enumerate(data):
        pourcentage = (valeur / total) * 100
        num_emojis = int(pourcentage / 20)  # 20% correspond à un emoji
        emoji_rayon = emojis[i % len(emojis)]  # Choisir l'emoji pour ce "rayon"

        val.append(f"{emoji_rayon} {pourcentage:.1f}%")
    print(" | ".join(val))

def create_circle(radius,data):
    size = radius * 2 + 1
    grid = [["" for _ in range(size)] for _ in range(size)]
    x_centre, y_centre = radius, radius

    for x in range(size):
        for y in range(size):
            distance = math.sqrt((x - x_centre) ** 2 + (y - y_centre) ** 2)
            if distance <= radius:
                # Calculer l'angle en radians entre le centre du cercle et le point courant
                angle = math.atan2(y - y_centre, x - x_centre)
                # Transformer l'angle en degrés positifs
                angle = math.degrees(angle) % 360
                # Convertir en un angle entre 0 et 90 degrés
                angle = (angle + 360) % 360
                if angle <= 45:
                    grid[y][x] = "🟦"  # Bleu pour la partie découpée de la pizza
                else:
                    grid[y][x] = "🟥"  # Rouge pour le reste du cercle
            else:
                grid[y][x] = "⬛"

    for row in grid:
        print(" ".join(row))
    generate_legend(data)

data = [25, 40, 15, 10]
create_circle(5,data)



