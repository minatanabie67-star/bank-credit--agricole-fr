from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# toujours revenir à la connexion
@app.route('/')
def home():
    return redirect(url_for('login'))

# page connexion
@app.route('/login')
def login():
    return render_template('login.html')

# traitement du formulaire
@app.route('/login', methods=['POST'])
def connect():
    user = request.form.get('identifiant')
    password = request.form.get('motdepasse')

    if user == "CA84739261" and password == "1615":
    return redirect(url_for('dashboard'))
    else:
        return "❌ Identifiant ou mot de passe incorrect"

# sécurité : empêcher accès direct au dashboard


    @app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        nom="nathalie hodemon",
        solde="2.000.000,00"
    )
