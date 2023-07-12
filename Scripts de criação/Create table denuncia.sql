CREATE TABLE Denúncia (
  idDenúncia INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Estudantes_id INTEGER UNSIGNED NOT NULL,
  Comentario VARCHAR(300) NULL,
  PRIMARY KEY(idDenúncia),
  INDEX Denúncia_FKIndex1(Estudantes_id)
);