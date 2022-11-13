Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

telefones={"tiago":965181785,"karen:951066314", "nunes":941900079}
SyntaxError: ':' expected after dictionary key
telefones={"tiago":965181785,"karen":951066314, "nunes":941900079}
telefones
{'tiago': 965181785, 'karen': 951066314, 'nunes': 941900079}
telefones{"junior"}=965656577
SyntaxError: invalid syntax
telefones["junior"]=965656577
telefones
{'tiago': 965181785, 'karen': 951066314, 'nunes': 941900079, 'junior': 965656577}

del telefones[junior]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del telefones[junior]
NameError: name 'junior' is not defined
del telefones["junior"]
telefones
{'tiago': 965181785, 'karen': 951066314, 'nunes': 941900079}
