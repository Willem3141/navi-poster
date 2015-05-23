
import re
import navi_alphabet

from string import Template

word_path = 'word_list.txt'
output_path = 'poster/words.tex'

word_template = Template(r'\wordtype{$wtype} \wordgroup{$wgroups} \naviword{$word}')
word_group_template = Template(r'\wordgroup{$wgroup}')

def main():

	def sub(w):
		word, wtype, wgroups = w
		word = word.replace(navi_alphabet.tiftang1, "'").replace(navi_alphabet.tiftang2, "'").strip()
		wtype = wtype.replace('.', '')
		if wgroups:
			wgroups = ' '.join( word_group_template.substitute(wgroup=wg) for wg in wgroups.split(',') )
		return word_template.substitute(word=word, wtype=wtype, wgroups=wgroups)

	outfile = open(output_path, 'w', encoding='utf-8')

	words = [ w.split(';') for w in open(word_path, encoding='utf-8') ]
	words.sort(key=lambda w: navi_alphabet.sort_key(w[0]))
	words = [ sub(w) for w in words ]

	words_tex = '\n'.join(words)
	
	print(words_tex, file=outfile)	

if __name__ == '__main__':
	main()