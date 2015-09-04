from flask import Flask, render_template, request

app = Flask(__name__)


#default methods is GET


# ordinary route
@app.route('/')
def hello_world():
    return render_template('index.html')


# route with restful
@app.route('/user/<username>/')
def user(username):
    #reuse variables in your tempalate
    if username == "bosse":
        os = "linux"
    elif username == "daniel":
        os = "mac"
    else:
        os = "windows"
    return render_template('user.html',username=username,os=os)


@app.route('/sqrt/<int:number>')
def sqrt(number):
    return str(number** 0.5)


# route vid args
@app.route('/args')
def args():
    return "malin is %s" % request.args.get("malin","missing")


# method post (and get)
@app.route('/message',methods = ['GET', 'POST'])
def message():
    if request.method == 'POST':

        newmessage = request.form.get('message')

        return newmessage

    elif request.method == 'GET':

        return "write a form"
    else:

        return "unsupported method"




if __name__ == '__main__':
    app.debug=True
    app.run()
