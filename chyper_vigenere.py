# Hacer una función que tome un texto y una key. A partir de estos devolver el mensaje 
# cifrado. Para esto se debe tener una matriz de 27 x 27 cuyas coordenadas de filas y columnas sean las 
# letras del abecedario. El contenido de cada fila sera el propio abecedario con un desfasaje segun la 
# fila. Es decir la segunda fila la letra B sera la primera colmuna y la A la última, en la tercer la C sera
# la primera columna y B la última ya así sucesivamente hasta que la Z sea la primera.

def cypher_vigenere(text, key):
  formated_text = "".join(char for char in text if char.isalpha()).strip().upper()
  formated_key = "".join(char for char in key if char.isalpha()).strip().upper()
  count = 0
  alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
  cypher_text = ""

  while len(formated_key) < len(formated_text):
        formated_key += formated_key[count]
        count += 1
  
  # print(formated_text, formated_key, len(formated_key), len(formated_text))

  table = []
  for i in range(27):
      table.append(alphabet[i:] + alphabet[:i])
  
  # print(table)

  for i in range(len(formated_text)): 
    column = alphabet.index(formated_text[i])
    row = alphabet.index(formated_key[i])
    cypher_text += table[row][column]  

  return cypher_text

print(cypher_vigenere("hola", "sol") )