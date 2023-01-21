#dictionary={"name":"mayu"}

import json
file= json.load(open('data1.json'))


word=input("enter the word : ")
def check(d):
    return file[d]

print(check(word))