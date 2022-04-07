
#Laoding a file
def read_file(enter):
	chat = []
	with open(enter, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

#Write output
def out_put(output, chat):
	with open(output, 'w', encoding = 'utf-8-sig') as f:
		for p in chat:
			if 'Allen' in p:
				person = 'Allen' 
				continue
			elif 'Tom' in p:
				person = 'Tom'
				continue
			f.write(person + ': ' + p + '\n')


def main():
	enter = 'input.txt'
	output = 'output.txt'
	chat = read_file(enter)
	for p in chat:
		print(p)
	out_put(output, chat)

main()