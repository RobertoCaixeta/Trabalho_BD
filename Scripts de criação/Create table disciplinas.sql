CREATE TABLE Disciplinas (
  idDisciplinas INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Departamentos_idDepartamentos INTEGER UNSIGNED NOT NULL,
  Nome VARCHAR(100) NULL,
  PRIMARY KEY(idDisciplinas),
  INDEX Disciplinas_FKIndex1(Departamentos_idDepartamentos)
);