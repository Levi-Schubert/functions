def main(list, num, str="Hello, "):
	for item in list[0:num]:
		print(str + item)
	
names = ["Jonny", "Deanna", "Cashew", "Erin", "Jess", "Josh", "Meghan", "Daniel"]

main(names, 4)
main(names, len(names), "I think you're pretty neat, ")