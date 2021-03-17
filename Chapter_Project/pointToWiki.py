import pyperclip


# run this from terminal "python3 pointToWiki.py"
text = pyperclip.paste()



lines = text.split('\n')

for i in range(len(lines)):
    lines[i] ='hej ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)


