from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page d'accueil → redirige vers login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Page login
@app.route('/login')
def login():
    return render_template('login.html')

# Traitement du formulaire
@app.route('/login', methods=['POST'])
def connect():
    user = request.form.get('identifiant')
    password = request.form.get('motdepasse')

    if user == "CA84739261" and password == "1615":
        return redirect(url_for('dashboard'))
    else:
        return "❌ Identifiant ou mot de passe incorrect"

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        nom="CHANTAL CAUMONT",
        solde="2.000.000,00"
    )

# Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
