words_list = ["bottle", "computer mouse", "sun"] 

for word in words_list:
    count = len(word.replace(" ", ""))
    print(f"{word}\n{count}")
