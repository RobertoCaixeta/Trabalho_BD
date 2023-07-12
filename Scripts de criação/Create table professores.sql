CREATE TABLE Professores (
  idProfessores INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Departamentos_idDepartamentos INTEGER UNSIGNED NOT NULL,
  Nome VARCHAR(100) NULL,
  PRIMARY KEY(idProfessores),
  INDEX Professores_FKIndex1(Departamentos_idDepartamentos)
);