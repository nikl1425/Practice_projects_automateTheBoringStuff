import sys
from pyperclip import copy




TEXT = {'agree': """yes, i agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next?""",
        'upsell': """would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]

if keyphrase in TEXT:
    copy(TEXT[keyphrase])
    print('text for' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

