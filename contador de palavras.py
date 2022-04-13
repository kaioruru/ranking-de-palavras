def adicionarPalavras(frase):
    frase = frase.replace(',','').replace('.','').replace('"','').replace('!','').replace('?','').replace('”','').replace('“','').replace('-','').replace('|','').replace('—','').replace('’','')
    lista_de_palavras = frase.split(' ')
    with open('palavras.txt','a',encoding='UTF-8') as arquivo:
        for _ in lista_de_palavras:
            i = _.upper()
            arquivo.write(i.upper()+',')
def contarPalavras():
    with open('palavras.txt','r', encoding='UTF-8') as arquivo: # abre o arquivo em leitura
        ler = (arquivo.read()).split(',') #converte o texto do arquivo em lista 
        ordem ={}
        for _ in ler: #cria um laço que vai 
            word = int(ler.count(_))
            ordem.update({_:word})
    for i in sorted(ordem, key = ordem.get):
        print(i, ordem[i])
while True:
    adicionarPalavras(str(input('frase: ')))
    contarPalavras()
    x = str(input('que digitar mais frases (S/N): ')).upper()
    if x == 'N':
        break