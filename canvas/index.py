from flask import Flask, render_template, request
import base64


app= Flask(__name__)

@app.route("/")
def index():
    return render_template("canvas.html")

@app.route('/upload', methods=['GET','POST']) 
def upload_base64_file():
    if request.method == "POST": 
        # Upload image with base64 format and get car make model and year 
        # response 
        data = request.form
        if data is None:
            print("No valid request body, json missing!")
            return jsonify({'error': 'No valid request body, json missing!'})
        else:
            img_data = data['canvas']
            img_data = img_data.partition(",")[2]
            pad = len(img_data)%4
            img_data += "="*pad
            convert_and_save(img_data)
        return render_template("canvas.html")
def convert_and_save(b64_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))


# @app.route("/upload" , methods=['GET','POST'])
# def upload():
#     if request.method == "POST":
#           print(request.form['canvas'])
#     return render_template("canvas.html")

if __name__=='__main__':
    app.run(debug=True)