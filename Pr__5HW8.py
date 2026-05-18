#Strip function remove the blank spaces avilable on sides  of a function
this="    Harry is a good boy   "
print(this)
print(this.strip())
def remove_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
    
This="    Harry is a good boy   "
n=remove_split(this,"Harry")
print(n)