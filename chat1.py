def read_file(enter):
	with open(enter, 'r', encoding = 'utf-8-sig') as f:
		chat = []
		for line in f:
			chat.append(line.strip())
		print(chat)
		return chat

def convert(enter):
	new = []
	person = None
	for line in enter:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line + '\n')
	print(new)
	return new

def write_file(out, new):
	with open(out, 'w', encoding = 'utf-8-sig') as f:
		for line in new:
			f.write(line)

def main():

	chat = read_file('input.txt')
	new = convert(chat)
	write_file('output.txt', new)

main()