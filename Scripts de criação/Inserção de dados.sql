INSERT INTO `trabalho_bd`.`estudantes`
(`matricula`,
`Curso`,
`email`,
`nome`,
`senha`,
`Foto`)
VALUES
(
190067455,
"Engenharia",
"pedro@unb.br",
"Pedro",
"123456789",
NULL),
(
190189098,
"Enfermagem",
"lucas@unb.br",
"Lucas",
"123456789",
NULL),
(
192896541,
"Economia",
"gustavo@unb.br",
"Gustavo",
"123456789",
NULL);

INSERT INTO `trabalho_bd`.`denúncia`
(
`Estudantes_id`,
`Comentario`)
VALUES
(1,
"Denuncia em flagrante 1"),
(2,
"Denuncia em flagrante 1"),
(3,
"Denuncia em flagrante 1");

INSERT INTO `trabalho_bd`.`departamentos`
(`Nome`,
`Sigla`)
VALUES
("Departamento de Engenharia Elétrica","ENE"),
("Departamento de Economia","ECO"),
("Departamento de Enfermagem","ENF");


INSERT INTO `trabalho_bd`.`disciplinas`
(`Departamentos_idDepartamentos`,
`Nome`)
VALUES
(1,"Circuitos Elétricos"),
(2,"Cálculo 1"),
(3,"Fundamentos Téoricos");

INSERT INTO `trabalho_bd`.`professores`
(
`Departamentos_idDepartamentos`,
`Nome`)
VALUES
(1,"João"),
(2,"José"),
(3,"Ana");

INSERT INTO `trabalho_bd`.`turmas`
(`Professores_idProfessores`,
`Disciplinas_idDisciplinas`,
`Número`,
`semestre`)
VALUES
(1,
1,
3,
"2023.2"),
(2,
2,
4,
"2023.2"),
(3,
3,
5,
"2023.2");



INSERT INTO `trabalho_bd`.`avaliações`
(`Estudantes_id`,
`Comentario`,
`turmas_id`)
VALUES
(1,
"Comentário legal1",
1),
(1,
"Comentário legal2",
1),
(1,
"Comentário legal3",
1);
