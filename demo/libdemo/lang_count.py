f = open("langs.txt", "rt")

langs = {}

for lang in f.readlines():
    lang = lang.strip()
    count = langs.get(lang, 0) + 1
    langs[lang] = count

f.close()

for lang, count in sorted(langs.items()):
    print(f"{lang:10} {count:3}")

print('-' * 50)

for lang, count in sorted(langs.items(), key=lambda t: t[1], reverse=True):
    print(f"{lang:10} {count:3}")
