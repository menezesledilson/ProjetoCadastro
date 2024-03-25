#o dicionario

personagens ={
    
    1: {
        "nome" :"Andre",
        "personagem" :"Harry ",
        "origem" :"Imperial"    
    },
    2: {
        "nome":"Tom",
        "personagem" :"Dragon ",
        "origem" :"Rhodoks"    
    },
    3: {
        "nome" :"Alan",
        "personagem" :"Severus ",
        "origem" :"Nórdicos"    
    }    
    
}
#esta função gera novoo id 
def gerar_id():
    id = len(personagens) + 1
    return id
def criar_personagem(nome,personagem,origem):
    personagens[gerar_id()] ={"nome":nome,"personagem":personagem,"origem":origem}
    
def retornar_personagens():
    return personagens

def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return{}
    
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens [id]=dados_personagem  
    
def remover_personagem  (id:int):
    del personagens[id]  

#print(retornar_personagens())
    
#criar_personagem("teste","teste1","imperial")

##print(retornar_personagem(1))

#atualizar_personagem(1,{'nome': 'Alex', 'personagem': 'Harry ', 'origem': 'Imperial'})

#print(retornar_personagem(1))

#remover_personagem(1)
#print(retornar_personagem(1))*/