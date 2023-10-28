'''
----- database -----
DROP DATABASE IF EXISTS escola;
CREATE DATABASE IF NOT EXISTS escola;
USE escola;
CREATE TABLE alunos (
	matricula VARCHAR(100) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    curso VARCHAR(100) NOT NULL,
    nota FLOAT NOT NULL
);
'''

