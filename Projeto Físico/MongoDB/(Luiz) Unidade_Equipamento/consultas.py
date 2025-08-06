import pymongo

uri = "mongodb+srv://leal:<password>@cluster0.hk2pult.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cliente = pymongo.MongoClient(uri)
bd = cliente["academia"]

equipamento = bd["equipamento"]
unidade = bd["unidade"]

# CASO 1
# Quais são as cidades das unidades que possuem o equipamento com o nome="Leg press"
print("Caso 1:")
equipamentos_leg_press = equipamento.find({"nome": "Leg press"})

for eq in equipamentos_leg_press:
    unidade_doc = unidade.find_one({"_id": eq["id_unidade"]})
    print(unidade_doc["cidade"])

# CASO 2
# Quais sao os nomes dos equipamentos da unidade da cidade ="São Paulo"
print()
print("Caso 2:")
equipamento_sao_paulo = equipamento.find({"unidade.cidade": "São Paulo"})

for eq in equipamento_sao_paulo:
    print(eq["nome"])

#Caso 3
#Quais são os nomes dos equipamentos da unidade da cidade = "Fortaleza"
print()
print("Caso 3:")
unidade_fortaleza = unidade.find_one({"cidade": "Fortaleza"})

for equip_id in unidade_fortaleza["equipamentos"]:
    eq = equipamento.find_one({"_id": equip_id})
    if eq:
        print(eq["nome"])


# CASO 4
# Quais são os nomes dos equipamentos da unidade da cidade = "Rio de Janeiro"
print()
print("Caso 4:")
unidade_rio = unidade.find_one({"cidade": "Rio de Janeiro"})

for eq in unidade_rio["equipamentos"]:
    print(eq["nome"])
