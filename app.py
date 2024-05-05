from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']

    if password == '123':
        return redirect('https://eklase.lv/')
    elif password == '321':
        return redirect('https://uzdevumi.lv/')
    else:
        return 'Nepareiza parole'

if __name__ == '__main__':
    app.run(debug=True)
