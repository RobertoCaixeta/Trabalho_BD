CREATE TABLE Estudantes (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  matricula INTEGER UNSIGNED NULL,
  Curso VARCHAR(50) NULL,
  email VARCHAR(150) NULL,
  nome VARCHAR(100) NULL,
  senha VARCHAR(100) NOT NULL,
  Foto BLOB NULL,
  PRIMARY KEY(id)
);