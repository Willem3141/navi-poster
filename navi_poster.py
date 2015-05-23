
import re
import navi_alphabet

from string import Template

word_path = 'word_list2.txt'
output_path = 'poster/words.tex'

word_template = Template(r"\naviword{$word}")

def main():

	def sub(s):
		return word_template.substitute(word=s.replace(navi_alphabet.tiftang1, "'").replace(navi_alphabet.tiftang2, "'").strip())

	outfile = open(output_path, 'w', encoding="utf-8")

	words = [ w for w in open(word_path, encoding="utf-8") ]
	words.sort(key=navi_alphabet.sort_key)
	words = [ sub(l) for l in words ]

	words_spaced = '\n'.join(words)
	
	print(words_spaced, file=outfile)	

if __name__ == '__main__':
	main()