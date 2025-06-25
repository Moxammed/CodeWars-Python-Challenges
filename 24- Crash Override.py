'''
------Instructions------

Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film Hackers.

Your task is to create a function that, given a proper first and last name, will return the correct alias.

Notes:
Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given. See the examples below for further details.

If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."

Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.

Examples
# These two dictionaries are preloaded, you need to use them in your code
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

The Dictionaries are as below:
 FIRST_NAME = {
    'A': 'Alpha',     'B': 'Beta',        'C': 'Cache',
    'D': 'Data',      'E': 'Energy',      'F': 'Function',
    'G': 'Glitch',    'H': 'Half-life',   'I': 'Ice',
    'J': 'Java',      'K': 'Keystroke',   'L': 'Logic',
    'M': 'Malware',   'N': 'Nagware',       'O': 'OS',
    'P': 'Phishing',   'Q': 'Quantum',     'R': 'RAD',
    'S': 'Strike',    'T': 'Trojan',      'U': 'Ultraviolet',
    'V': 'Vanilla',    'W': 'WiFi',        'X': 'Xerox',
    'Y': 'Y',     'Z': 'Zero'}

    SURNAME = {
    'A': 'Analogue',  'B': 'Bomb',        'C': 'Catalyst',
    'D': 'Discharge', 'E': 'Electron',      'F': 'Faraday',
    'G': 'Gig',     'H': 'Hacker',      'I': 'IP',
    'J': 'Jabber',    'K': 'Killer',      'L': 'Lazer',
    'M': 'Mike',      'N': 'n00b',       'O': 'Overclock',
    'P': 'Payload',   'Q': 'Quark',      'R': 'Roy',
    'S': 'Spy',    'T': 'T-Rex',       'U': 'Unit',
    'V': 'Virus',     'W': 'Worm',        'X': 'X',
    'Y': 'Yob',      'Z': 'Zombie'}
  
------Solution------
'''

def alias_gen(f_name, l_name):
    FIRST_NAME = {
    'A': 'Alpha',     'B': 'Beta',        'C': 'Cache',
    'D': 'Data',      'E': 'Energy',      'F': 'Function',
    'G': 'Glitch',    'H': 'Half-life',   'I': 'Ice',
    'J': 'Java',      'K': 'Keystroke',   'L': 'Logic',
    'M': 'Malware',   'N': 'Nagware',       'O': 'OS',
    'P': 'Phishing',   'Q': 'Quantum',     'R': 'RAD',
    'S': 'Strike',    'T': 'Trojan',      'U': 'Ultraviolet',
    'V': 'Vanilla',    'W': 'WiFi',        'X': 'Xerox',
    'Y': 'Y',     'Z': 'Zero'}

    SURNAME = {
    'A': 'Analogue',  'B': 'Bomb',        'C': 'Catalyst',
    'D': 'Discharge', 'E': 'Electron',      'F': 'Faraday',
    'G': 'Gig',     'H': 'Hacker',      'I': 'IP',
    'J': 'Jabber',    'K': 'Killer',      'L': 'Lazer',
    'M': 'Mike',      'N': 'n00b',       'O': 'Overclock',
    'P': 'Payload',   'Q': 'Quark',      'R': 'Roy',
    'S': 'Spy',    'T': 'T-Rex',       'U': 'Unit',
    'V': 'Virus',     'W': 'Worm',        'X': 'X',
    'Y': 'Yob',      'Z': 'Zombie'}
    
    def alias_gen(f_name, l_name):
    FIRST_NAME = {
    'A': 'Alpha',     'B': 'Beta',        'C': 'Cache',
    'D': 'Data',      'E': 'Energy',      'F': 'Function',
    'G': 'Glitch',    'H': 'Half-life',   'I': 'Ice',
    'J': 'Java',      'K': 'Keystroke',   'L': 'Logic',
    'M': 'Malware',   'N': 'Nagware',       'O': 'OS',
    'P': 'Phishing',   'Q': 'Quantum',     'R': 'RAD',
    'S': 'Strike',    'T': 'Trojan',      'U': 'Ultraviolet',
    'V': 'Vanilla',    'W': 'WiFi',        'X': 'Xerox',
    'Y': 'Y',     'Z': 'Zero'}

    SURNAME = {
    'A': 'Analogue',  'B': 'Bomb',        'C': 'Catalyst',
    'D': 'Discharge', 'E': 'Electron',      'F': 'Faraday',
    'G': 'Gig',     'H': 'Hacker',      'I': 'IP',
    'J': 'Jabber',    'K': 'Killer',      'L': 'Lazer',
    'M': 'Mike',      'N': 'n00b',       'O': 'Overclock',
    'P': 'Payload',   'Q': 'Quark',      'R': 'Roy',
    'S': 'Spy',    'T': 'T-Rex',       'U': 'Unit',
    'V': 'Virus',     'W': 'Worm',        'X': 'X',
    'Y': 'Yob',      'Z': 'Zombie'}
    
    if not (f_name or l_name):
        return "First and last name cannot be empty."

    if not (f_name[0].isalpha() and l_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."
    
    f_name = f_name[0].upper()
    l_name = l_name[0].upper()
    
    full_Name=""
    if f_name in FIRST_NAME:
        full_Name=FIRST_NAME[f_name]
    if l_name in SURNAME:
        full_Name+=" "+ SURNAME[l_name]
    return full_Name


'''
If Dictionary was preload then and Another Solution

def alias_gen(f_name, l_name):

    if not (f_name or l_name):
        return "First and last name cannot be empty."

    if not (f_name[0].isalpha() and l_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."

    f_initial = f_name[0].upper()
    l_initial = l_name[0].upper()

    return f"{FIRST_NAME[f_initial]} {SURNAME[l_initial]}"

'''