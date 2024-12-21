# Ouvrir le fichier exporté depuis PulseView
with open("rxdata.txt", "r") as file:
    lines = file.readlines()

result = ""

# Parcourir chaque ligne et extraire les caractères après "UART: RX data:"
for line in lines:
    if "UART: RX data:" in line:
        result += line.split(":")[-1].strip()

# Écrire le texte reconstruit dans un nouveau fichier
with open("output_reconstruit.txt", "w") as output_file:
    output_file.write(result)

print("Fichier 'output_reconstruit.txt' généré avec succès.")
