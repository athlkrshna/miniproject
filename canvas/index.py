from flask import Flask, render_template, request


app= Flask(__name__)

@app.route("/")
def index():
    return render_template("canvas.html")


@app.route("/upload" , methods=['GET','POST'])
def upload():
    if request.method == "POST":
          print(request.form['canvas'])
    return render_template("canvas.html")

if __name__=='__main__':
    app.run(debug=True)