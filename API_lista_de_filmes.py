import requests
import json

def requisicao(titulo):
    try:
        req = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey=d78ae2b5')
        # pega o texto e transforma em um dicionário
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def requisicao2(aux):
    try:
        req = requests.get(f'http://www.omdbapi.com/?s={aux}&apikey=d78ae2b5')
        d = json.loads(req.text)
        return d
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print(f"\033[32mTítulo:\033[m {filme['Title']}")
    print(f"\033[32mAno:\033[m {filme['Year']}")
    print(f"\033[32mDiretor:\033[m {filme['Director']}")
    print(f"\033[32mAtores:\033[m {filme['Actors']}")
    print(f"\033[32mNota:\033[m {filme['imdbRating']}")
    print(f"\033[32mPremios:\033[m {filme['Awards']}")
    print(f"\033[32mPoster:\033[m {filme['Poster']}")

def printar_saga(saga):
    for i in range(len(saga['Search'])):
        print('\033[37m<->\033[m' * 30)
        print(f"\033[32mTítulo:\033[m {saga['Search'][i]['Title']}")
        print(f"\033[32mAno:\033[m {saga['Search'][i]['Year']}")
        print(f"\033[32mPoster:\033[m {saga['Search'][i]['Poster']}")
        print(f"\033[32mTipo do poster:\033[m {saga['Search'][i]['Type']} ")

sair = False
while not sair:
    print("\033[35m*\033[m"*50)
    print("\033[1;35mConsumindo uma API".center(55))
    print("\033[35m*\033[m" * 50)
    print("Instruções:\n\033[1m1- Pesquisa por título ou ID\n2- Pesquisa sobre as sagas\n3- Sair\033[m")
    n = int(input("Digite o que deseja: "))
    if n == 1:
        op = str(input("Escreva o nome de um filme: "))
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('\033[31mFilme não encontrado\033[m')
        else:
            printar_detalhes(filme)
    elif n == 2:
        op = str(input("Digite a saga que você quer procurar: "))
        saga = requisicao2(op)
        if saga['Response'] == 'False':
            print('\033[31mSaga não encontrada\033[m')
        else:
            printar_saga(saga)
    elif n == 3:
        print('\033[36mSaindo... Volte sempre\033[m')
        break
    else:
        print('\033[31mOperação indiponível\033[m')


