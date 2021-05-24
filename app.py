from flask import Flask, render_template, request, flash, url_for,redirect
import base64
import model
import time
import rgb2grey
import calc
import urllib.request
import os

path_img = './static/image.jpg'
path_img = os.path.relpath(path_img)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg',])
UPLOAD_FOLDER = 'static/'

app= Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['TEMPLATES_AUTO_RELOAD'] = True

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/canvas")
def index():
    return render_template("canvas.html")

@app.route('/upload')
def upload_form():
	return render_template('upload.html')


@app.route('/upload' , methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = "image.jpg"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        rgb2grey.imgTogrey()


            # input to model
        final=model.predict()
        ans=calc.eval_expr(final)
        print('string ',final)
        print('ans ',ans)
        return render_template('upload.html', filename=filename ,final=final,ans=ans)


    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)



# @app.route('/upload', methods=['POST'])
# def upload_image():
# 	if 'file' not in request.files:
# 		flash('No file part')
# 		return redirect(request.url)
# 	file = request.files['file']
# 	if file.filename == '':
# 		flash('No image selected for uploading')
# 		return redirect(request.url)
# 	if file and allowed_file(file.filename):
# 		filename = "image.jpg"
# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 		#print('upload_image filename: ' + filename)
# 		flash('Image successfully uploaded and displayed below')     
# 		return render_template('upload.html', filename=filename)
# 	else:
# 		flash('Allowed image types are -> png, jpg, jpeg, gif')
# 		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename= filename), code=301)







@app.route('/save_canvas', methods=['GET','POST']) 
def upload_base64_file():
    if request.method == "POST": 
        # Upload image with base64 format and get car make model and year 
        # response 
        data = request.form
        if data is None:
            print("No valid request body, missing!")
            
        else:
            img_data = data['canvas']
            img_data = img_data.partition(",")[2]
            pad = len(img_data)%4
            img_data += "="*pad
            
            convert_and_save(img_data)


            # convert to grey scale 
            rgb2grey.imgTogrey()


            # input to model
            final=model.predict()
            ans=calc.eval_expr(final)
            print('string ',final)
            print('ans ',ans)
            time.sleep(3)
            
        return render_template("canvas.html" , final=final,ans=ans)




def convert_and_save(b64_string):
    with open(path_img, "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))



if __name__=='__main__':
    app.run(debug=True , host="0.0.0.0")

    