CREATE TABLE Avaliações (
  idAvaliações INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Estudantes_id INTEGER UNSIGNED NOT NULL,
  Comentario VARCHAR(300) NULL,
  PRIMARY KEY(idAvaliações),
  INDEX Avaliações_FKIndex1(Estudantes_id)
);
ALTER TABLE avaliações
ADD COLUMN turmas_id INTEGER UNSIGNED,
ADD CONSTRAINT fk_avaliacoes_turmas
FOREIGN KEY (turmas_id) REFERENCES turmas(idTurmas);