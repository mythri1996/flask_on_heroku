from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return '<h1>this is flask application <f1>'

if __name__=="__main__":
    app.run()