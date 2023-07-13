import mysql.connector

con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password=''
    )

cursor = con.cursor(dictionary=True) 
query = "CREATE VIEW Avaliacoes_view AS SELECT a.idAvaliações,a.Comentario, e.nome, e.curso, e.matricula, e.email, t.Número, t.semestre, p.nome AS nomeProfessor, d.nome as nomeDisciplina FROM avaliações a JOIN estudantes e ON a.Estudantes_id = e.id JOIN turmas t ON a.turmas_id = t.idTurmas JOIN professores p ON t.Professores_idProfessores  = p.idProfessores JOIN disciplinas d ON t.Disciplinas_idDisciplinas = d.idDisciplinas;"
cursor.execute(query)
avaliacoes = cursor.fetchall()
con.commit()
cursor.close()
con.close()