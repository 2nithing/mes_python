from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['GET','POST'])
def hi():
    if request.method=='POST':
        num1 = request.form['num1']
        result = factorial(int(num1))
    return render_template('name.html',num2=result,num1=num1)

def factorial(num):
    i=1
    fact=1
    while i<=num:
        fact = fact*i
        i+=1
    return fact



if __name__=='__main__':
    app.run()