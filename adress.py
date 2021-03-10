book = {}
book['Akash']={
    'name':'Akash',
    'Adress':'Arrah Bihar bhojpur',
    'phone':852150
}
book['Vikrant']={
    'name':'Vikrant',
    'Adress':'Chhapra Bihar bhojpur',
    'phone':8085
}
import json
s=json.dump(book)

with open("D://SEMINAR//book.txt","w") as f:
    f.write(s)