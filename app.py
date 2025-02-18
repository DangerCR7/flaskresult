## Integrate HTML with flask
## HTTP verb GET and POST

## Jinja 2 Template Engine
"""
{%........%} statements
{{    }}  Experssions to print outputs
{#.......#} THis is for internal Commends

"""


from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
        
    exp={'score':score, 'res': res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "FAIL"


## Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

## Result Checker Html page
@app.route('/submit',methods=["POST","GET"])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        math=float(request.form['maths'])
        data_science=float(request.form['datascience'])
        total_score=(science+math+data_science)/3
   
    return redirect(url_for('success', score=total_score))
        

if __name__ == '__main__':
    app.run(debug=True)
