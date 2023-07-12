from flask import Flask, render_template, redirect, url_for, request
from app import app
import mysql.connector


@app.route('/')
def main():
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    cursor = con.cursor(dictionary=True) 
    query = "SELECT turmas.idTurmas, turmas.Número, turmas.semestre, professores.Nome AS nome_professor, disciplinas.Nome AS nome_disciplinas FROM turmas JOIN professores ON turmas.Professores_idProfessores = professores.idProfessores JOIN disciplinas ON turmas.Disciplinas_idDisciplinas = disciplinas.idDisciplinas;"
    cursor.execute(query)
    turmas = cursor.fetchall()
    print(turmas)

    cursor.close()
    con.close()
    

    return render_template('turmas.html', turmas=turmas)

@app.route('/avaliations', methods = ['GET', 'POST', 'DELETE', 'UPDATE'])
def mainAvaliacoes():
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    cursor = con.cursor(dictionary=True) 
    query = "SELECT a.idAvaliações,a.Comentario, e.nome, e.curso, e.matricula, e.email, t.Número, t.semestre, p.nome AS nomeProfessor, d.nome as nomeDisciplina FROM avaliações a JOIN estudantes e ON a.Estudantes_id = e.id JOIN turmas t ON a.turmas_id = t.idTurmas JOIN professores p ON t.Professores_idProfessores  = p.idProfessores JOIN disciplinas d ON t.Disciplinas_idDisciplinas = d.idDisciplinas;"
    cursor.execute(query)
    avaliacoes = cursor.fetchall()
    print("avaliacoes")

    cursor.close()
    con.close()
    

    return render_template('avaliacoes.html', avaliacoes=avaliacoes)

@app.route('/DeleteAvaliations/<int:id>', methods=['DELETE'])
def deleteAvaliation(id):
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )
    cursor = con.cursor()
    query = 'DELETE FROM avaliações where idAvaliações = %s;'
    cursor.execute(query, (id,))
    print("query =", cursor.statement)
    con.commit()
    cursor.close()
    con.close()

    return redirect(url_for('mainAvaliacoes'))


@app.route('/UpdateAvaliations/<int:id>', methods=['GET', 'PUT', 'PATCH', 'POST'])
def UpdateAvaliation(id):
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    if request.method == 'POST':
        estudante = request.form.get('estudante')
        turma = request.form.get('turma')
        comentario = request.form.get('comentario')
        cursor = con.cursor() 
        query = 'UPDATE `trabalho_bd`.`avaliações` SET `idAvaliações` = %s, `Estudantes_id` = %s, `Comentario` ="%s", `turmas_id` = %s WHERE `idAvaliações` = %s;' % (id, estudante,comentario,turma, id)
        
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for('mainAvaliacoes'))


    cursor = con.cursor(dictionary=True)
    query = "SELECT a.idAvaliações,a.Comentario, e.nome, e.curso,e.id,t.idTurmas, e.matricula, e.email, t.Número, t.semestre, p.nome AS nomeProfessor, d.nome as nomeDisciplina FROM avaliações a JOIN estudantes e ON a.Estudantes_id = e.id JOIN turmas t ON a.turmas_id = t.idTurmas JOIN professores p ON t.Professores_idProfessores  = p.idProfessores JOIN disciplinas d ON t.Disciplinas_idDisciplinas = d.idDisciplinas where idAvaliações = %s;"
    cursor.execute(query, (id,))
    avaliacao = cursor.fetchall()
    cursor = con.cursor(dictionary=True) 
    query = "SELECT * from estudantes;"
    cursor.execute(query)
    estudantes = cursor.fetchall()

    cursor = con.cursor(dictionary=True) 
    query = "SELECT turmas.idTurmas, turmas.Número, turmas.semestre, professores.Nome AS nome_professor, disciplinas.Nome AS nome_disciplinas FROM turmas JOIN professores ON turmas.Professores_idProfessores = professores.idProfessores JOIN disciplinas ON turmas.Disciplinas_idDisciplinas = disciplinas.idDisciplinas;"

    cursor.execute(query)
    turmas = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template('EditarAvaliacoes.html', avaliacao=avaliacao, estudantes=estudantes, turmas= turmas)

@app.route('/CreateAvaliations', methods = ['GET', 'POST'])
def CreateAvaliacoes():
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    if request.method == 'POST':
        estudante = request.form.get('estudante')
        turma = request.form.get('turma')
        comentario = request.form.get('comentario')
        cursor = con.cursor() 
        query = 'INSERT INTO `trabalho_bd`.`avaliações` (`Estudantes_id`, `Comentario`,`turmas_id`) VALUES( %s,"%s", %s);' % (estudante,comentario,turma)
        
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for('mainAvaliacoes'))


    cursor = con.cursor(dictionary=True) 
    query = "SELECT * from estudantes;"
    cursor.execute(query)
    estudantes = cursor.fetchall()

    cursor = con.cursor(dictionary=True) 
    query = "SELECT turmas.idTurmas, turmas.Número, turmas.semestre, professores.Nome AS nome_professor, disciplinas.Nome AS nome_disciplinas FROM turmas JOIN professores ON turmas.Professores_idProfessores = professores.idProfessores JOIN disciplinas ON turmas.Disciplinas_idDisciplinas = disciplinas.idDisciplinas;"

    cursor.execute(query)
    turmas = cursor.fetchall()
    cursor.close()
    con.close()
    

    return render_template('CriarAvaliacoes.html', estudantes=estudantes, turmas= turmas)



@app.route('/CreateClass', methods = ['GET', 'POST'])
def CreateTurmas():
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    if request.method == 'POST':
        professor = request.form.get('professor')
        disciplina = request.form.get('disciplina')
        numero = request.form.get('numero')
        semestre = request.form.get('semestre')


        cursor = con.cursor() 
        query = 'INSERT INTO `trabalho_bd`.`turmas` (`Professores_idProfessores`,`Disciplinas_idDisciplinas`,`Número`,`semestre`) VALUES( %s,%s, %s,"%s");' % (professor,disciplina,numero,semestre)
        
        print("query = ", query)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for('main'))


    cursor = con.cursor(dictionary=True) 
    query = "SELECT * from professores;"
    cursor.execute(query)
    professores = cursor.fetchall()

    cursor = con.cursor(dictionary=True) 
    query = "SELECT * from disciplinas;"
    cursor.execute(query)
    disciplinas = cursor.fetchall()
    cursor.close()
    con.close()
    

    return render_template('CriarTurmas.html', professores=professores, disciplinas= disciplinas)

@app.route('/DeleteClass/<int:id>', methods=['DELETE'])
def deleteClass(id):
    print("idaqaaaa = ", id)
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )
    cursor = con.cursor()
    query = 'DELETE FROM turmas where idTurmas = %s;'
    cursor.execute(query, (id,))
    print("query =", cursor.statement)
    con.commit()
    cursor.close()
    con.close()

    return redirect(url_for('main'))


@app.route('/UpdateClass/<int:id>', methods=['GET', 'PUT', 'PATCH', 'POST'])
def UpdateClasses(id):
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    if request.method == 'POST':
        professor = request.form.get('professor')
        disciplina = request.form.get('disciplina')
        numero = request.form.get('numero')
        semestre = request.form.get('semestre')
        cursor = con.cursor() 
        query = 'UPDATE `trabalho_bd`.`turmas` SET `idTurmas` = %s, `Professores_idProfessores` = %s, `Disciplinas_idDisciplinas` = %s, `Número` = %s, `semestre` = "%s" WHERE `idTurmas` = %s;' % (id, professor,disciplina,numero,semestre, id)
        
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for('main'))


    cursor = con.cursor(dictionary=True)
    query = "SELECT t.idTurmas,t.Número, t.semestre, p.Nome AS nome_professor, p.idProfessores AS id_professor, d.Nome AS nome_disciplina, d.idDisciplinas AS id_disciplina FROM turmas AS t JOIN professores AS p ON t.Professores_idProfessores = p.idProfessores JOIN disciplinas AS d ON t.Disciplinas_idDisciplinas = d.idDisciplinas where  t.idTurmas = %s;"
    cursor.execute(query, (id,))
    turma = cursor.fetchall()
    print("turma = ", turma )
    cursor = con.cursor(dictionary=True) 
    query = "SELECT * from professores;"
    cursor.execute(query)
    professores = cursor.fetchall()

    cursor = con.cursor(dictionary=True) 
    #query = "SELECT turmas.idTurmas, turmas.Número, turmas.semestre, professores.Nome AS nome_professor, disciplinas.Nome AS nome_disciplinas FROM turmas JOIN professores ON turmas.Professores_idProfessores = professores.idProfessores JOIN disciplinas ON turmas.Disciplinas_idDisciplinas = disciplinas.idDisciplinas;"
    query = "SELECT * from disciplinas"
    cursor.execute(query)
    disciplinas = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template('EditarTurmas.html', turma=turma, professores=professores, disciplinas= disciplinas)

@app.route('/user', methods = ['GET', 'POST'])
def CreateUser():
    con = mysql.connector.connect(
        host='localhost',
        database='trabalho_bd',
        user='root',
        password='Imcormrorcro123*'
    )

    if request.method == 'POST':
        nome = request.form.get('nome')
        matricula = request.form.get('matricula')
        curso = request.form.get('curso')
        email = request.form.get('email')
        senha = request.form.get('senha')


        cursor = con.cursor() 
        query = 'INSERT INTO `trabalho_bd`.`estudantes` (`matricula`,`Curso`,`email`,`nome`,`senha`,`Foto`) VALUES( %s,"%s","%s","%s","%s",null);' % (matricula,curso,email,nome,senha)
        
        print("query = ", query)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for('main'))

    

    return render_template('CriarEstudante.html')