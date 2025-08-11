from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://kant:InCCQPbCPTFvNv6y@cluster0.7dkw9xi.mongodb.net/?retryWrites=true&w=majority")

bd = cliente["set"]
treino = bd["treino"]
exercicios = bd["exercicios"]

#Caso 1: Documento referenciando apenas um documento
print("\nReferência a um documento")
treino.insert_one({
    "_id": 1,
    "nome": "Treino de pernas",
    "ref_exercicio": 2,
})

exercicios.insert_one({
    "_id": 2,
    "nome": "Leg Press"
})
exercicio_ref = exercicios.find_one({"_id": 2})
achou = treino.find({"ref_exercicio": exercicio_ref["_id"]})
treino_encontrado = treino.find_one({"_id" : 1})
for doc in achou:
    print(f"Treino encontrado: {doc['nome']}")
exercicio_ref = exercicios.find_one({"_id": treino_encontrado['ref_exercicio']})

print("Exercício referenciado:")
print(f"- Nome: {exercicio_ref['nome']}")
exercicios.drop()
treino.drop()

#Caso 2: Documento embutindo apenas um documento
print("\nDocumento embutido")
treino.insert_one({
    "_id": 3,
    "nome": "Treino de Costas",
    "exercicio": {
        "_id": 4,
        "nome": "Elevação Frontal"
    }
})

achou = treino.find({"exercicio.nome": "Elevação Frontal"})
doc = achou[0]
print(f"Treino: {doc['nome']}")
for doc in achou:
    print(f"Exercício embutido: {doc['exercicio']['nome']}")


treino.drop()

#Caso 3: Documento com array de referências
print("\nArray de referências")
exercicios.insert_many([
    {"_id": 5, "nome": "Halteres"},
    {"_id": 6, "nome": "Supino"},
    {"_id": 7, "nome": "Supino inclinado"},
    {"_id": 8, "nome": "Barra fixa"}
])

treino.insert_one({
    "_id": 9,
    "nome": "Treino de peito",
    "exercicios_ref": [5, 6, 7, 8]
})

treino_doc = treino.find_one({"_id": 9})
achou = exercicios.find({"_id": {"$in": treino_doc["exercicios_ref"]}})
print("Exercícios referenciados:")
for ex in achou:
    print(f"- {ex['nome']}")

treino.drop()
exercicios.drop()

#Caso 4: Documento embutindo vários documentos
print("\nArray de documentos embutidos")
treino.insert_one({
    "_id": 10,
    "nome": "Treino Completo",
    "exercicios_emb": [ 
        {"_id": 11, "nome": "Agachamento"},
        {"_id": 12, "nome": "Flexão"},
        {"_id": 13, "nome": "Prancha"}
    ]
})

achou = treino.find({"exercicios_emb.nome": "Agachamento"})
for doc in achou:
    print(f"{doc['nome']} contém:")
    for ex in doc["exercicios_emb"]:
        print(f"  - {ex['nome']}")

treino.drop()