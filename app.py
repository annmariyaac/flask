from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return f"Welcome to Flask"
@app.route('/html')
def load_html():
    return render_template('index.html',
    name="Ann",class1="bca")

todos = ['Learn Flask','Build a project','Deploy the app']

@app.route('/todos')
def get_todos():
    return render_template('todos.html',
    todos =todos)

@app.route('/add', method=['POST'])
def add_todo():
    todo=request.form.get('todo')
    if todo:
        todos.append(todo)
    return render_template('index.html',
      name="Ann",class1="bca")

if __name__ == '__main__':
    app.run(debug=True)