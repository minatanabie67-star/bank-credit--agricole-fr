from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🔥 toujours revenir à la connexion
@app.route('/')
def home():
    return redirect(url_for('login'))

# page connexion
@app.route('/login')
def login():
    return render_template('connexion.html')

# traitement du formulaire
@app.route('/login', methods=['POST'])
def connect():
    user = request.form.get('identifiant')
    password = request.form.get('motdepasse')

    if user == "CA84739261" and password == "1615":
        return render_template('tableau.html')
    else:
        return "❌ Identifiant ou mot de passe incorrect"

# sécurité : bloquer accès direct dashboard
@app.route('/dashboard')
def dashboard():
    return redirect(url_for('login'))
