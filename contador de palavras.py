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
def pegarLegenda(link):
    from youtube_transcript_api import YouTubeTranscriptApi 
    link= YouTubeTranscriptApi.get_transcript((link.split('?v='))[1],languages=['en'])
    for _ in link:
        i = _['text']+','
        adicionarPalavras(i)
print('-='*20,'\n1-adicionar um texto\n2-adicionar a legenda de um video\n3-consultar palavras')
x = int(input('>>'))
while True:
    if x == 1:
        texto = str(input('digite o seu texto:  '))
        adicionarPalavras(texto)
        print('-='*20,'\n1-adicionar um texto\n2-adicionar a legenda de um video\n3-consultar palavras')
        x = int(input('>>'))
    elif x == 2:
        link = str(input('digite o link: '))
        pegarLegenda(link)
        print('-='*20,'\n1-adicionar um texto\n2-adicionar a legenda de um video\n3-consultar palavras')
        x = int(input('>>'))
    elif x == 3:
        contarPalavras()
        print('-='*20,'\n1-adicionar um texto\n2-adicionar a legenda de um video\n3-consultar palavras')
        x = int(input('>>'))
    else:
        x = str(input('que continuar no progama?(S/N):  '))
        if x == 'N':
            break
