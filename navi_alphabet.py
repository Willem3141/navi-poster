import re

tiftang1 = '‘'
tiftang2 = '’'

alphabet_map = [
	('['+tiftang1+tiftang2+']', 'A'),
	('a', 'B'),
	('ä', 'C'),
	('e', 'D'),
	('f', 'E'),
	('h', 'F'),
	('i', 'G'),
	('ì', 'H'),
	('k', 'I'),
	('kx', 'J'),
	('l', 'K'),
	('ll', 'L'),
	('m', 'M'),
	('n', 'N'),
	('ng', 'O'),
	('o', 'P'),
	('p', 'Q'),
	('px', 'R'),
	('r', 'S'),
	('rr', 'T'),
	('sä', 'U'),
	('t', 'V'),
	('tx', 'W'),
	('ts', 'X'),
	('u', 'Y'),
	('v', 'Z'),
	('w', 'a'),
	('y', 'b'),
	('z', 'c')
]

alphabet_map.sort(key=lambda e: len(e[0]), reverse=True)
alphabet_map = [ (re.compile(letter), replacement) for letter, replacement in alphabet_map ]

def sort_key(s):
	s = s.lower()
	for reg, replacement in alphabet_map:
		s = reg.sub(replacement, s)
	return s