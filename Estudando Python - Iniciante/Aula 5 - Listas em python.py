Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lista=[1,4,7,"tiago",23,14]
print(lista)
[1, 4, 7, 'tiago', 23, 14]
lista.append("fraga")
print (lista)
[1, 4, 7, 'tiago', 23, 14, 'fraga']
[1, 4, 7, 'tiago', 23, 14, 'fraga']
[1, 4, 7, 'tiago', 23, 14, 'fraga']
lista.append(38)
print(lista)
[1, 4, 7, 'tiago', 23, 14, 'fraga', 38]
lista.index("tiago)
            
SyntaxError: unterminated string literal (detected at line 1)
lista.index("tiago")
            
3


lista.index(38)
            
7

lista.count(4)
            
1

lista.append (4)
            
lista.count(4)
            
2

print (lista)
            
[1, 4, 7, 'tiago', 23, 14, 'fraga', 38, 4]

lista.remove("fraga")
            
print(lista)
            
[1, 4, 7, 'tiago', 23, 14, 38, 4]
lista.reverse()
            
print(lista)
            
[4, 38, 14, 23, 'tiago', 7, 4, 1]

lista2=(1,9,3,4,2,7,6,8)
            
lista2.sort()
            
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
lista2.sort()
            
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
lista2=(1,9,3,4,2,7,6,8)
            
print(lista2)
            
(1, 9, 3, 4, 2, 7, 6, 8)
lista2.sort()
            
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
print(lista2)
            
(1, 9, 3, 4, 2, 7, 6, 8)
lista2.sort()
            
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
print(lista2)
            
(1, 9, 3, 4, 2, 7, 6, 8)
print(lista2)
            
(1, 9, 3, 4, 2, 7, 6, 8)
lista2=[1,9,3,4,2,7,6,8]
            
print (lista2)
            
[1, 9, 3, 4, 2, 7, 6, 8]
lista2.sort()
            
print(lista2)
            
[1, 2, 3, 4, 6, 7, 8, 9]
