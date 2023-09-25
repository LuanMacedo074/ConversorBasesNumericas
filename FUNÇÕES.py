def dec2bin(núm): #Iniciando a função dec2bin
    números = [] # aberta uma lista para salvar o resultado, visto que o resto da primeira divisão é na verdade o ultimo número
    bina = '' # str aberta para retornar o valor binário
    while núm != 0: # ciclo de repetição pra tratar o número fornecido até que ele chegue em 0.
        resto = núm % 2 # aplicando o processo da divisão por 2.
        números.insert(0,resto) # adicionando cada número na lista, sempre em primeira posição
        núm //= 2 # pegando a divisão inteira do número por 2 pra continuar o processo.
    for c in números: # percorrendo a lista para salvar os números
        bina += (str(c)) # salvando os números da lista em uma única str.
    return bina # retornando a str com o resultado.

def bin2dec(núm): #Iniciando a função bin2dec
    dec = 0 # abrindo uma variavel pra guardar o número decimal
    c = len(str(núm)) # pegando o comprimento do número para o tratamento
    bin = str(núm) # salvando o número como str para facilitar o tratamento de cada dígito
    while c != 0: # ciclo de repetição até acabar o comprimento da str
        c -= 1 # controlador do ciclo
        base = 2**c # pegando a base para a multiplicação como explicado no metódo
        núm = int(bin[0]) # pegando o dígito para a conversão
        bin = bin[1:] # salvando a str a partir do segundo dígito, tirando o dígito que já foi tratado
        dec += núm*base # multipliando o dígito pela base como explicado no metódo.
    return int(dec) # retornando o número decimal


def dec2hex(núm): #Iniciando a função dec2hex
    letra = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F') # Iniciando uma tupla pra converter os números com mais de 1 dígito como 10,11 etc
    final = [] # aberta uma lista para salvar o resultado, visto que o resto da primeira divisão é na verdade o ultimo número
    hex = '' # Iniciando uma str vazia pra retornar o resultado
    while núm != 0: # iniciando um ciclo até que o número seja 0
        resto = núm % 16 # iniciado o processo pegando o resto da divisão
        if 10 or 11 or 12 or 13 or 14 or 15 == resto: # caso o número tenha dois dígitos, ele tem que ser convertido.
            resto = letra[resto] # convertendo o número com dois dígitos em uma única letra, usando o número para saber a posição na tupla.
            final.insert(0, resto) # inserindo o dígito ná lista
        else: # caso o número for de um único dígito não precisa da conversão.
            final.insert(0, resto) # inserindo o dígito ná lista
        núm //= 16 # pegando a divisão inteira do número por 16 pra continuar o processo.
    for c in final: # percorrendo a lista pra salvar o número em uma única var
        hex += c # salvando o número em uma única var
    return hex # retornando o número hexadecimal

def hex2dec(núm): #Iniciando a função hex2dec
    letra = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F') # Iniciando uma tupla pra converter as letras em números.
    decimal = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15') # inciando a segunda tupla para a conversão.
    dec = 0 # inciado uma var pra salvar o valor decimal
    c = len(str(núm)) # uma var com o comprimento da string para executar a conversão.
    hex = str(núm).upper() # uma var transformando o número em string e botando todas as letras em maiúsculo para facilitar a manipulação.
    while c != 0: # iniciando um ciclo de repetição até que o comprimento do número seja 0.
        c -= 1 # controlador do ciclo, tirando 1 do comprimento sempre.
        base = 16**c # pegando a base do número como explicado no metódo
        núm = hex[0] # pegando o primeiro dígito do número
        hex = hex[1:] # salvando o número sem o primeiro dígito, que já foi tratado
        if 'A' or 'B' or 'C' or 'D' or 'E' or 'F' == núm: # caso o dígito selecionado for uma letra, é preciso converter
            núm = núm.replace(núm,decimal[letra.index(núm)]) # convertendo a letra em número usando as duas tuplas que eu criei
            dec += int(núm)*base # adicionando o número a var dec, utilizando o metódo de número vezes a base apresentado em aula
        else: # caso não seja uma letra
            dec += int(núm)*base # adicionando o número a var dec, utilizando o metódo de número vezes a base apresentado em aula
    return dec # retornando a var dec para o programa.


def bin2oct(núm): #Iniciando a função bin2oct
    oct = '' # inciado uma var pra salvar o valor em octal
    octal = ('0', '1', '2', '3', '4', '5', '6', '7') # Iniciando uma tupla pra converter os números octais
    bin = ('000', '001', '010', '011', '100', '101', '110', '111') # iniciando uma tupla com os respectivos números, da pra fazer usando dicionário
    núm = str(núm) # convertendo o número pra uma var do tipo str, pra facilitar o tratamento
    while len(núm) % 3 != 0: # nessa parte, como cada número binário na minha tupla tem 3 digitos, eu tive que garantir que sempre teria um múltiplo de 3 nó comprimento da str.
            núm = '0' + núm # acrescentando um zero no começo da str até que o comprimento sejá 3
    while len(núm) != 0: # enquanto o número não acabar, ou seja seu comprimento for 0, eu tenho que continuar fazendo a conversão
        algarismo = núm[0:3] # pegando o algrismo, do primeiro até o 3 dígito
        núm = núm[3:] # salvando o número sem a parte que eu já tirei
        oct += algarismo.replace(algarismo, octal[bin.index(algarismo)]) # fazendo a substituição usando as tuplas, dá para fazer usando dicionário
    return int(oct) # retonando o valor octal


def oct2bin(núm): #Iniciando a função oct2bin
    bina = '' # criando uma var pra salvar o resultado binário
    octal = ('0', '1', '2', '3', '4', '5', '6', '7') # usando as mesmas tuplas pra conversãos
    bin = ('000', '001', '010', '011', '100', '101', '110', '111') # usando a mesma tupla com os respectivos números.
    núm = str(núm) # convertendo pra str, pra facilitar o tratamento
    while len(núm) != 0: # enquanto o número não acabar, ou seja seu comprimento for 0, eu tenho que continuar fazendo a conversão
        algarismo = núm[0] # pegando o primeiro dígito
        núm = núm[1:] # salvando o número sem o dígito q eu peguei
        bina += algarismo.replace(algarismo, bin[octal.index(algarismo)]) # fazendo a substituição usando as tuplas
    return int(bina) # retornando o valor em binário


def bin2hex(núm): #Iniciando a função bin2hex
    hex = '' # iniciando uma var pra armazenar o valor hexadecimal
    letra = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F') # Iniciando uma tupla pra converter os números hexadecimais
    bin = ('0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111') # iniciando uma tupla com os respectivos números, da pra fazer usando dicionário
    núm = str(núm) # convertendo o número pra str pra facilitar o tratamento
    while len(núm) % 4 != 0: # como na minha tupla todos os números binários têm 4 dígitos, tive que garantir que o número que o usuário informou também tenha.
            núm = '0' + núm # acrescentando um zero no início do número até atingir os dígitos multiplos de 4
    while len(núm) != 0:  # enquanto o número não acabar, ou seja seu comprimento for 0, eu tenho que continuar fazendo a conversão
        algarismo = núm[:4] # pegando do começo até o quarto dígito.
        núm = núm[4:] # salvando o número tirando o os dígitos q eu já peguei
        hex += algarismo.replace(algarismo, letra[bin.index(algarismo)]) # substituindo os 4 dígitos binários por um único dígito hexadecimal.
    return hex # retornando o valor hexadecimal


def hex2bin(núm): #Iniciando a função hex2bin
    bina = ''  # iniciando uma var pra armazenar o valor binario
    letra = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F') # Iniciando uma tupla pra converter os números hexadecimais
    bin = ('0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111') # iniciando uma tupla com os respectivos números em bínario
    núm = str(núm).upper() # transformando o número em str pra facilitar a manipulação, e botando todas as letras para maiúsculo
    while len(núm) != 0: # iniciando o ciclo de repetição até q o número acabe
        algarismo = núm[0] # pegando o primeiro dígito
        núm = núm[1:] # salvando o número sem o dígito que eu peguei
        bina += algarismo.replace(algarismo, bin[letra.index(algarismo)]) # fazendo a substituição usando as tuplas
    return bina # retornando o valor binario
