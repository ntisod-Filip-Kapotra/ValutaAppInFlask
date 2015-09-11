from flask import Flask, render_template, request

import forex
app = Flask(__name__)



messages = []


#default methods is GET



# ordinary route
@app.route('/')
def hello_world():
    return render_template('index.html')


# route with restful
@app.route('/user/<username>/')
def user(username):
    #reuse variables in your tempalate
    if username == "Bosse":
        os = "Linux"
    elif username == "Daniel":
        os = "Mac"
    else:
        os = "Windows"
    return render_template('user.html', username=username, os=os)


@app.route('/sqrt/<int:number>')
def sqrt(number):
    return str(number** 0.5)


# route vid args
@app.route('/forex')
def args():

    tocurrency = request.args.get("to")
    fromcurrency = request.args.get("from")
    amount = request.args.get("amount")

    res = forex.convert(fromcurrency,tocurrency,int(amount))

    return str(res)


# method post (and get)
@app.route('/message',methods = ['GET', 'POST'])
def message():

    if request.method == 'POST':

        if len(messages) == 0:
            id=1
        else:
            id = messages[-1]['id'] + 1

        newmessage = {'id':id,'text':request.form.get('message')}
        messages.append(newmessage)

        return render_template("messages.html", messages=messages)

    elif request.method == 'GET':

        return render_template("messages.html", messages=messages)
    else:

        return "unsupported method"


if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0")
