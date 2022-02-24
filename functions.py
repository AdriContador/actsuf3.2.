MSG1 = "Introdueix el contingut del fitxer(inferior a 100 caracters): "
MSG2 = 'El contingut ha de ser inferior a 100 caracters, torna a introduir-lo: '

def file_add_st(fname):
  f = open(fname, "a+")
  str = input(MSG1)
  while len(str) > 100:
          str = input(MSG2)
  f.write(str)
  f.close()
