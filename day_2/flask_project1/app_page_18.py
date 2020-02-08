from flask import Flask, abort, request, render_template #update this code

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') #update this code

@app.route('/hello/')
def hello(name=None):
    if name is None:
        name=request.args.get("name")
        if name:
            return render_template('user.html', name=name) #update this code
        else:
            abort(404)

if __name__ == '__main__':
    app.run(debug=True)