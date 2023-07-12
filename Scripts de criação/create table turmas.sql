CREATE TABLE Turmas (
  idTurmas INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Professores_idProfessores INTEGER UNSIGNED NOT NULL,
  Disciplinas_idDisciplinas INTEGER UNSIGNED NOT NULL,
  Número INTEGER UNSIGNED NULL,
  semestre varchar(255) NULL;
  PRIMARY KEY(idTurmas),
  INDEX Turmas_FKIndex1(Disciplinas_idDisciplinas),
  INDEX Turmas_FKIndex2(Professores_idProfessores)
);
