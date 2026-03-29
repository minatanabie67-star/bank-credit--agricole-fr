from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def connect():
    user = request.form.get("identifiant")
    password = request.form.get("motdepasse")

    if user == "CA84739261" and password == "1615":
        return redirect('/dashboard')
    else:
        return "❌ Identifiant ou mot de passe incorrect"
   

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)