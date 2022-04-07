def read_file(enter):
	with open(enter, 'r', encoding = 'utf-8-sig') as f:
		chat = []
		for line in f:
			chat.append(line.strip())
		# print(chat)
		return chat

def convert(enter):
	allen_sticker = 0
	allen_word = 0
	allen_image = 0
	viki_sticker = 0
	viki_word = 0
	viki_image = 0
	for line in enter:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_image += 1
			elif s[2] == '貼圖':
				allen_sticker += 1
			else:
				for m in s[2:]:
					allen_word += len(m)
		if name == 'Viki':
			if s[2] == '圖片':
				viki_image += 1
			elif s[2] == '貼圖':
				viki_sticker += 1
			else:
				for m in s[2:]:
					viki_word += len(m)
	print(allen_word, viki_word)
	print(allen_sticker, viki_sticker)
	print(allen_image, viki_image)



def write_file(out, new):
	with open(out, 'w', encoding = 'utf-8-sig') as f:
		for line in new:
			f.write(line)

def main():

	chat = read_file('LINE-Viki.txt')
	new = convert(chat)
	# write_file('output.txt', new)

main()