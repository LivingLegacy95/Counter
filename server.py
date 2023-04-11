from flask import Flask, render_template, redirect, session
app = Flask(__name__)

app.secret_key = 'Valaar Morghulis'

@app.route('/')
def make_table():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)