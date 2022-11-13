Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tipos=("Tiago","Karen","Rebeca")
tipos
('Tiago', 'Karen', 'Rebeca')

tipos[0]
'Tiago'
tipos[1]
'Karen'
tipos[2]
'Rebeca'

tipos[3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tipos[3]
IndexError: tuple index out of range

tipos[0:2]
('Tiago', 'Karen')
tipos[0:1]
('Tiago',)
tipos[0]
'Tiago'

len(tipos)
3

tipos+tipos
('Tiago', 'Karen', 'Rebeca', 'Tiago', 'Karen', 'Rebeca')

tipos*5
('Tiago', 'Karen', 'Rebeca', 'Tiago', 'Karen', 'Rebeca', 'Tiago', 'Karen', 'Rebeca', 'Tiago', 'Karen', 'Rebeca', 'Tiago', 'Karen', 'Rebeca')

4 in tipos
False

Rebeca in tipos
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Rebeca in tipos
NameError: name 'Rebeca' is not defined
"Rebeca" in tipos
True

lista=[1,4,"Tiago"]
lista
[1, 4, 'Tiago']
tipos2=tipos(lista)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tipos2=tipos(lista)
TypeError: 'tuple' object is not callable
tipos2=tuple(lista)
tipos2
(1, 4, 'Tiago')
