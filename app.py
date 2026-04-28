from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

#Criar banco
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS produtos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       preco REAL NOT NULL
                       )
                       """)
    conn.commit()
    conn.close()
    
# Página inicial
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    conn.close()
    return render_template("index.html", produtos=produtos)

# Adicionar produto
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
            (nome, preco)
        )
        
        conn.commit()
        conn.close()
        
        return redirect("/")
    
    return render_template("add.html")

#Editar produto
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        
        cursor.execute(
            "UPDATE produtos SET nome=?, preco=? WHERE id=?", (nome, preco, id)
        )
        
        conn.commit()
        conn.close()
        
        return redirect("/")
    
    cursor.execute("SELECT * FROM produtos WHERE id=?", (id,))
    produto = cursor.fetchone()
    
    conn.close()
    
    return render_template("edit.html", produto=produto)

# Excluir produto
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
    
    conn.commit()
    conn.close()
    
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    