import sqlite3


def create_tables():

	# Cria bd
	conn = sqlite3.connect("academia.db")
	cursor = conn.cursor()

	# Criação tabelas
	cursor.executescript("""
	CREATE TABLE Unidade (
		ID_uni INTEGER PRIMARY KEY,
		endereco TEXT,
		CEP TEXT,
		Cidade TEXT
	);
	
	CREATE TABLE Funcionário (
		CPF_func TEXT PRIMARY KEY,
		nome TEXT,
		salário REAL,
		CPF_supervisor TEXT,
		ID_uni INTEGER,
		FOREIGN KEY (CPF_supervisor) REFERENCES Funcionário(CPF_func),
		FOREIGN KEY (ID_uni) REFERENCES Unidade(ID_uni)
	);
	
	CREATE TABLE Gerente (
		CPF_func TEXT,
		ID_uni INTEGER,
		PRIMARY KEY (CPF_func, ID_uni),
		FOREIGN KEY (CPF_func) REFERENCES Funcionário(CPF_func),
		FOREIGN KEY (ID_uni) REFERENCES Unidade(ID_uni)
	);
	
	CREATE TABLE Professor (
		CPF_func TEXT PRIMARY KEY,
		FOREIGN KEY (CPF_func) REFERENCES Funcionário(CPF_func)
	);
	
	CREATE TABLE TelefoneFunc (
		CPF_func TEXT,
		Numero TEXT,
		PRIMARY KEY (CPF_func, Numero),
		FOREIGN KEY (CPF_func) REFERENCES Funcionário(CPF_func)
	);
	
	CREATE TABLE Aluno (
		CPF_aluno TEXT PRIMARY KEY,
		nome TEXT
	);
	
	CREATE TABLE Plano (
		ID_plano INTEGER PRIMARY KEY,
		valor REAL
	);
	
	CREATE TABLE Promoção (
		ID_promo INTEGER PRIMARY KEY,
		tx_desconto REAL
	);
	
	CREATE TABLE Assina (
		ID_plano INTEGER,
		CPF_aluno TEXT,
		ID_promo INTEGER,
		PRIMARY KEY (ID_plano, CPF_aluno, ID_promo),
		FOREIGN KEY (ID_plano) REFERENCES Plano(ID_plano),
		FOREIGN KEY (CPF_aluno) REFERENCES Aluno(CPF_aluno),
		FOREIGN KEY (ID_promo) REFERENCES Promoção(ID_promo)
	);
	
	CREATE TABLE Frequência (
		CPF_aluno TEXT,
		data TEXT,
		hora_entrada TEXT,
		hora_saida TEXT,
		PRIMARY KEY (CPF_aluno, data, hora_entrada),
		FOREIGN KEY (CPF_aluno) REFERENCES Aluno(CPF_aluno)
	);
	
	CREATE TABLE Treino (
		ID_treino INTEGER PRIMARY KEY,
		nome TEXT
	);
	
	CREATE TABLE Exercício (
		ID_exercício INTEGER PRIMARY KEY,
		nome TEXT
	);
	
	CREATE TABLE TreinoExercício (
		ID_treino INTEGER,
		ID_exercício INTEGER,
		PRIMARY KEY (ID_treino, ID_exercício),
		FOREIGN KEY (ID_treino) REFERENCES Treino(ID_treino),
		FOREIGN KEY (ID_exercício) REFERENCES Exercício(ID_exercício)
	);
	
	CREATE TABLE Equipamento (
		ID_equipamento INTEGER PRIMARY KEY,
		nome TEXT,
		qt_equip INTEGER,
		ID_uni INTEGER,
		FOREIGN KEY (ID_uni) REFERENCES Unidade(ID_uni)
	);
	
	CREATE TABLE TreinoEquipamento (
		ID_equip INTEGER,
		ID_treino INTEGER,
		PRIMARY KEY (ID_equip, ID_treino),
		FOREIGN KEY (ID_equip) REFERENCES Equipamento(ID_equipamento),
		FOREIGN KEY (ID_treino) REFERENCES Treino(ID_treino)
	);
	
	CREATE TABLE Atribui (
		CPF_aluno TEXT,
		ID_treino INTEGER,
		CPF_func TEXT,
		PRIMARY KEY (CPF_aluno, ID_treino, CPF_func),
		FOREIGN KEY (CPF_aluno) REFERENCES Aluno(CPF_aluno),
		FOREIGN KEY (ID_treino) REFERENCES Treino(ID_treino),
		FOREIGN KEY (CPF_func) REFERENCES Funcionário(CPF_func)
	);
	""")

	conn.commit()
	conn.close()
	print("Tabelas criadas.")
