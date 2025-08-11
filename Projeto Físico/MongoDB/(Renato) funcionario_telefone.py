print(    
    """

        CONNECTING TO MONGO DB

    """
)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
uri = "mongodb+srv://renato:12144@cluster0.y1crybf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# create database
bd = client["set"]
# create documents
funcionario = bd["funcionario"]
telefone = bd["telefone"]

telefone.insert_many([
    {"numero": "123"},
    {"numero": "456"},
    {"numero": "789"},
    {"numero": "1011"},
    {"numero": "1213"},
    {"numero": "1415"}
])


#############################################################
print(
    """

        REFERÊNCIA 1-1

    """
)

telefone_ref1 = telefone.find_one({"numero": "123"})
telefone_ref2 = telefone.find_one({"numero": "789"})

funcionario.insert_many([
    {"nome": "Renato", "ref_telefone": telefone_ref1['_id']},
    {"nome": "Robson", "ref_telefone": telefone_ref2['_id']}
])

# Nome → Telefone
nome_buscado = "Renato"
f = funcionario.find_one({"nome": nome_buscado})
t = telefone.find_one({"_id": f["ref_telefone"]})
print(f"Telefone de {nome_buscado}: {t['numero']}")

# Telefone → Nome
numero_buscado = "789"
t = telefone.find_one({"numero": numero_buscado})
f = funcionario.find_one({"ref_telefone": t["_id"]})
print(f"Funcionário com telefone {numero_buscado}: {f['nome']}")

funcionario.drop()


#############################################################
print(
    """

        EMBUTIDO 1-1

    """
)

funcionario.insert_many([
    {"nome": "Renato", "telefone": {"numero": "123"}},
    {"nome": "Robson", "telefone": {"numero": "456"}}
])

# Nome → Telefone
nome_buscado = "Robson"
f = funcionario.find_one({"nome": nome_buscado})
print(f"Telefone de {nome_buscado}: {f['telefone']['numero']}")

# Telefone → Nome
numero_buscado = "123"
f = funcionario.find_one({"telefone.numero": numero_buscado})
print(f"Funcionário com telefone {numero_buscado}: {f['nome']}")

funcionario.drop()


#############################################################
print(
    """

        REFERÊNCIA 1-N

    """
)

telefones_refs1 = [
    telefone.find_one({"numero": "123"})['_id'],
    telefone.find_one({"numero": "456"})['_id'],
    telefone.find_one({"numero": "789"})['_id'],
]
telefones_refs2 = [
    telefone.find_one({"numero": "1011"})['_id'],
]

funcionario.insert_many([
    {"nome": "Renato", "telefones_refs": telefones_refs1},
    {"nome": "Robson", "telefones_refs": telefones_refs2}
])

# Nome → Telefones
nome_buscado = "Renato"
f = funcionario.find_one({"nome": nome_buscado})
telefones_refs = telefone.find({"_id": {"$in": f["telefones_refs"]}})
print(f"Telefones de {nome_buscado}: {[t['numero'] for t in telefones_refs]}")

# Telefone → Nome
numero_buscado = "1011"
t = telefone.find_one({"numero": numero_buscado})
f = funcionario.find_one({"telefones_refs": t["_id"]})
print(f"Funcionário com telefone {numero_buscado}: {f['nome']}")

funcionario.drop()


#############################################################
print(
    """

        EMBUTIDO 1-N

    """
)

funcionario.insert_many([
    {"nome": "Renato", "telefone": [
        {"numero": "123"},
        {"numero": "456"},
        {"numero": "789"}
    ]},
    {"nome": "Robson", "telefone": [
        {"numero": "1011"}
    ]}
])

# Nome → Telefones
nome_buscado = "Renato"
f = funcionario.find_one({"nome": nome_buscado})
print(f"Telefones de {nome_buscado}: {[t['numero'] for t in f['telefone']]}")

# Telefone → Nome
numero_buscado = "456"
f = funcionario.find_one({"telefone.numero": numero_buscado})
print(f"Funcionário com telefone {numero_buscado}: {f['nome']}")

funcionario.drop()
