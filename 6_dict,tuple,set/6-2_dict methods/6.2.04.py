morze = {".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д", ".": "Е", "...-": "Ж", "--..": "З", "..": "И", ".---": "Й", "-.-": "К", ".-..": "Л", "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р", "...": "С", "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч", "----": "Ш", "--.-": "Щ", ".--.-": "Ъ", "-.--": "Ы", "-..-": "Ь", "...-...": "Э", "..--": "Ю", ".-.-": "Я", "-...-": " "}
data_in = input().split()

for i in data_in:
    print(morze[i].lower(), end = "")