# O relacionamento utilizado nos casos abaixo foi o "1-contrata-N" entre as entidades Unidade e Funcionário.

from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://phra2:<senha>@bdprojectcluster.gjiliad.mongodb.net/?retryWrites=true&w=majority&appName=BDprojectCluster")

bd = cliente["rede"]
unidades = bd["unidades"]
funcionarios = bd["funcionarios"]

# Em todos os casos a seguir, será impresso os nomes dos funcionários contratados pela unidade de CEP "12345-678".

# Caso 1 - Um documento (funcionario) referenciando um outro documento (unidade):
unidade = {
    "id_u" : 1,
    "cidade" : "Recife",
    "CEP" : "12345-678"
}
unidades.insert_one(unidade)
funcionario = {
    "CPF" : "000.000.000-00",
    "nome" : "Pedro",
    "salario" : 3000,
    "id_u" : 1
}
funcionarios.insert_one(funcionario)
unidade = unidades.find_one({"CEP" : "12345-678"})
resultado = funcionarios.find({"id_u" : unidade["id_u"]})
print("\nCaso 1 - Nomes dos funcionários na unidade CEP = 12345-678:")
for i in resultado:
    print(i["nome"])

# Caso 2 - Um documento (funcionario) embutindo apenas um outro documento (unidade):
unidades.delete_many({})
funcionarios.delete_many({})
funcionario = {
    "CPF" : "100.000.000-00",
    "nome" : "augusto",
    "salario" : 5000,
    "unidade" : {
        "id_u" : 1,
        "cidade" : "Recife",
        "CEP" : "12345-678"
    }
}
funcionarios.insert_one(funcionario)
resultado = funcionarios.find({"unidade.CEP" : "12345-678"})
print("\nCaso 2 - Nomes dos funcionários na unidade CEP = 12345-678:")
for i in resultado:
    print(i["nome"])

# Caso 3 - Um documento (unidade) com um array de referências para documentos (funcionarios):
funcionarios.delete_many({})
funcionarios.insert_many([
    {
        "CPF" : "200.000.000-00",
        "nome" : "adriano",
        "salario" : 2000
    },
    {
        "CPF" : "300.000.000-00",
        "nome" : "felipe",
        "salario" : 4000
    }
])
unidade = {
    "id_u" : 1,
    "cidade" : "Recife",
    "CEP" : "12345-678",
    "funcionarios" : ["200.000.000-00","300.000.000-00"]
}
unidades.insert_one(unidade)
unidade = unidades.find_one({"CEP" : "12345-678"})
resultado = funcionarios.find({"CPF" : {"$in" : unidade["funcionarios"]}})
print("\nCaso 3 - Nomes dos funcionários na unidade CEP = 12345-678:")
for i in resultado:
    print(i["nome"])

# Caso 4 - Um documento (unidade) embutindo vários documentos (funcionarios):
unidades.delete_many({})
funcionarios.delete_many({})
unidade = {
    "id_u" : 1,
    "cidade" : "Recife",
    "CEP" : "12345-678",
    "funcionarios" : [
        {
            "CPF" : "400.000.000-00",
            "nome" : "sigurossom",
            "salario" : 10000
        },
        {
            "CPF" : "500.000.000-00",
            "nome" : "adeílton",
            "salario" : 30000
        }
    ]
}
unidades.insert_one(unidade)
unidade = unidades.find_one({"CEP" : "12345-678"})
print("\nCaso 4 - Nomes dos funcionários na unidade CEP = 12345-678")
for i in unidade["funcionarios"]:
    print(i["nome"])
print("\n")

cliente.drop_database("rede")


