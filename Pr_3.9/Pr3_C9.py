with open("sample.txt",'r') as f:
    word=f.read()
word=word.replace("donkey","¥€¢¢")
with open("sample.txt",'w') as f:
    f.write(word)
    