import sqlite3


def populate_tables():

	# Conecta com bd já criado
	conn = sqlite3.connect("academia.db")
	cursor = conn.cursor()
	cursor.executescript("""
	
	-- Unidades
	INSERT INTO Unidade VALUES (1, 'Rua das Flores, 123', '12345-678', 'São Paulo');
	INSERT INTO Unidade VALUES (2, 'Av. Central, 456', '87654-321', 'Rio de Janeiro');
	
	-- Funcionários
	INSERT INTO Funcionário VALUES ('12345678900', 'Carlos Silva', 5000.00, NULL, 1);
	INSERT INTO Funcionário VALUES ('23456789011', 'Ana Souza', 3000.00, '12345678900', 1);
	INSERT INTO Funcionário VALUES ('34567890122', 'João Lima', 3200.00, '12345678900', 2);
	
	-- Gerente
	INSERT INTO Gerente VALUES ('12345678900', 1);
	
	-- Professor
	INSERT INTO Professor VALUES ('23456789011');
	
	-- Telefones
	INSERT INTO TelefoneFunc VALUES ('12345678900', '11999990000');
	INSERT INTO TelefoneFunc VALUES ('12345678900', '11988887777');
	INSERT INTO TelefoneFunc VALUES ('23456789011', '21999995555');
	
	-- Alunos
	INSERT INTO Aluno VALUES ('11122233344', 'Pedro Henrique');
	INSERT INTO Aluno VALUES ('55566677788', 'Juliana Alves');
	INSERT INTO Aluno VALUES ('88899900011', 'Luiz Eduardo');
	
	-- Planos
	INSERT INTO Plano VALUES (1, 150.00);
	INSERT INTO Plano VALUES (2, 200.00);
	
	-- Promoções
	INSERT INTO Promoção VALUES (1, 0.10); -- 10%
	INSERT INTO Promoção VALUES (2, 0.15); -- 15%
	
	-- Assinaturas
	INSERT INTO Assina VALUES (1, '11122233344', 1);
	INSERT INTO Assina VALUES (2, '55566677788', 2);
	
	-- Frequência
	INSERT INTO Frequência VALUES ('11122233344', '2025-08-05', '08:00', '09:00');
	INSERT INTO Frequência VALUES ('11122233344', '2025-08-06', '08:10', '09:15');
	INSERT INTO Frequência VALUES ('55566677788', '2025-08-06', '10:00', '11:00');
	
	-- Treinos
	INSERT INTO Treino VALUES (1, 'Treino A');
	INSERT INTO Treino VALUES (2, 'Treino B');
	
	-- Exercícios
	INSERT INTO Exercício VALUES (1, 'Supino');
	INSERT INTO Exercício VALUES (2, 'Agachamento');
	INSERT INTO Exercício VALUES (3, 'Remada');
	
	-- TreinoExercício
	INSERT INTO TreinoExercício VALUES (1, 1);
	INSERT INTO TreinoExercício VALUES (1, 2);
	INSERT INTO TreinoExercício VALUES (2, 3);
	
	-- Equipamentos
	INSERT INTO Equipamento VALUES (1, 'Banco de supino', 3, 1);
	INSERT INTO Equipamento VALUES (2, 'Barra olímpica', 5, 2);
	INSERT INTO Equipamento VALUES (3, 'Máquina remada', 2, 1);
	
	-- TreinoEquipamento
	INSERT INTO TreinoEquipamento VALUES (1, 1);
	INSERT INTO TreinoEquipamento VALUES (2, 1);
	INSERT INTO TreinoEquipamento VALUES (3, 2);
	
	-- Atribuição de treino a aluno
	INSERT INTO Atribui VALUES ('11122233344', 1, '23456789011');
	INSERT INTO Atribui VALUES ('55566677788', 2, '23456789011');
	
	""")

	print("Tabelas povoadas.")
