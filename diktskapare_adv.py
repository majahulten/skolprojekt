

def create_poem():
	# skapa en lista
	sentence = []

	for i in range(4):
		# fråga användaren efter en mening
		# lägg till meningen i listan
		sentence.append(input('sentence number {}: '.format(i+1)))

		if sentence[0] <= 4 or sentence[i] < 3:
			print('En mening måste bestå av minst tre ord. (minst fem för första meningen)')
			# om sant avsluta programmet
			exit(1)

	# return'a hela listan
	return sentence


def write_poem(sentence):
	# första meningen
	first = sentence[0].split()
	# fyra första orden i första meningen
	first_four = first[:4]
	# allt utom fyra första i första meningen
	not_first_four = first[4:]
	# allt utom första meningen
	not_first = sentence[1:]

	# 1. first_four.uppercase
	# skapa en sträng och loopa fyra första orden i meningen
	title = ''
	for word in first_four:
		# gör om varje ord till stora bokstäver och lägg till i strängen
		title += word.upper() + ' '
	print(title)

	# 2. ""
	print('')

	# 3. first_four
	# gör om lista till sträng
	print(' '.join(first_four), '')

	# 4. not_first_four
	print(' '.join(not_first_four), '')

	# 5. first_four
	print(' '.join(first_four), '')

	# 6-8. for-loop not_first
	# loopa dom tre sista meningarna och gör om lista till sträng
	for text_row in not_first:
		text_rad = text_row.split()
		print(' '.join(text_rad), '')

	# 9. first
	print(' '.join(first_four), '')

# kör programmet
if __name__ == "__main__":
	# spara return värdet från funtionen i variablen lista
	lista = create_poem()
	write_poem(lista)
