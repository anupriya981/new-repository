a={
"name" :"diya",
"age" :32,
"age":30,
"place":"kakkanad"
}
print(a)
print('------------')

print('  ')#just for space

a.update({'class':'diploma'})
print(a)
print('------------')

a.pop('age')#delete
print(a)
print('------------')

print('  ')#space
a['name']='user'#update
print(a)
print('------------')