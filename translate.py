from googletrans import Translator
translator = Translator()

with open("test.txt", 'r+') as my_file:
    translator = Translator()
    text = my_file.read()

jp_text = translator.translate(text, dest='ja').text

print(jp_text)
