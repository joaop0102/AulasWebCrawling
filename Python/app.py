from flask import *
import sqlite3

app = Flask(__name__)

#conexão com o banco de dados
conn = sqlite3.connect('gestao_hospitalar.db')
cursor = conn.cursor() 

#criação de tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, 
        idade INTEGER,
        sexo TEXT,
        cpf TEXT UNIQUE,
        endereco TEXT,
        telefone TEXT
    )
''')

conn.commit() #salvar
conn.close() #fechar

@app.route('/')
def index():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', pacientes=pacientes)

@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO pacientes(nome, idade, sexo, cpf, endereco, telefone)
                       VALUES(?, ?, ?, ?, ?, ?)
        ''', (nome, idade, sexo, cpf, endereco, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')
    
@app.route('/limpar_paciente')
def limpar_paciente():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('DELETE * FROM pacientes')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)