from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('example_upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
    app.config['UPLOAD_FLODER'] = '/Users/yoonjoonlee/Dropbox/SWKorea/SKFLY-AI_Python교육/PythonCodes/Part4/TestFlask'
    app.run(debug = True)
