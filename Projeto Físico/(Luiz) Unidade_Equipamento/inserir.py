import pymongo

uri = "mongodb+srv://leal:<password>@cluster0.hk2pult.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cliente = pymongo.MongoClient(uri)

bd = cliente['academia']
unidade = bd['unidade']
equipamento = bd['equipamento']

# CASO 1 - Um documento (unidade) referenciando outro documento (equipamento)
userId = unidade.insert_one({
    "_id": 1,
    "cidade": "Recife",
    "CEP": "12345-678"
}).inserted_id

equipamento.insert_one({
    "_id": 1,
    "nome": "Leg press",
    "quantidade": 3,
    "id_unidade": userId
})

#CASO 2 - Um documento (equipamento) embutindo apenas um outro documento (unidade)
unidade_sao_paulo = {
    "_id": 2,
    "cidade": "São Paulo",
    "CEP": "11111-222"
}
unidade.insert_one(unidade_sao_paulo)

equipamento.insert_one({
    "_id": 2,
    "nome": "Esteira",
    "quantidade": 12,
    "unidade": unidade_sao_paulo 
})

# CASO 3 - Um documento (unidade) com um array de referências para documentos de equipamentos
equip1_id = equipamento.insert_one({
    "_id": 3,
    "nome": "Bicicleta",
    "quantidade": 5
}).inserted_id

equip2_id = equipamento.insert_one({
    "_id": 4,
    "nome": "Remo",
    "quantidade": 2
}).inserted_id

unidade.insert_one({
    "_id": 3,
    "cidade": "Fortaleza",
    "CEP": "22222-333",
    "equipamentos": [equip1_id, equip2_id]  # Array de referências
})

# CASO 4 - um documento (unidade) embuntindo varios documentos (equipamento)
equip_list = [{
    "_id": 5,
    "nome": "Halter",
    "quantidade": 40,
},{
    "_id": 6,
    "nome": "Barra fixa",
    "quantidade": 8,
}]
equipamento.insert_many(equip_list)

unidade.insert_one({
    "_id": 4,
    "cidade": "Rio de Janeiro",
    "CEP": "77777-888",
    "equipamentos": equip_list
})
