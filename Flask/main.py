from flask import Flask, redirect, url_for, request, render_template, make_response


app = Flask(__name__)
app.secret_key = "1233"

@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog number %d' % postID

@app.route('/rev/<float:revNo>/')
def revision(revNo):
    return 'Revsion number %f' % revNo

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('result.html', result = result)

# @app.route("/")
# def student():
#    return render_template("student.html")

# @app.route("/")
# def index():
#   return render_template('login.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']

   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)

   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)