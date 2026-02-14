text = input("Введіть текст: ")

sentences = 0
for ch in text:
    if ch in ".!?":
        sentences += 1

print("Кількість речень:", sentences)

text = input("Введіть рядок: ")

clean = ""
for ch in text.lower():
    if ch.isalnum():
        clean += ch

if clean == clean[::-1]:
    print("Це паліндром")
else:
    print("Це НЕ паліндром")

    reserved = ["python", "code", "while", "for"]

text = input("Введіть текст: ")
words = text.split()

for i in range(len(words)):
    if words[i].lower() in reserved:
        words[i] = words[i].upper()

result = " ".join(words)
print(result)

text = input("Введіть рядок: ")
a = input("Перший символ: ")
b = input("Другий символ: ")

i = text.find(a)
j = text.find(b)

if i != -1 and j != -1 and i < j:
    result = text[:i] + text[j+1:]
    print(result)
else:
    print("Символи не знайдені або в неправильному порядку")

    text = input("Введіть текст: ")
bad_chars = input("Введіть набір символів: ")

words = text.split()
result = []

for word in words:
    ok = True
    for ch in bad_chars:
        if ch in word:
            ok = False
    if ok:
        result.append(word)

print(" ".join(result))

text = input("Введіть текст: ")
words = text.split()
words.reverse()
result = " ".join(words)
print(result)
