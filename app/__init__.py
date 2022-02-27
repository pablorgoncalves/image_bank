from flask import Flask, render_template
from app.kenzie.image import upload
from app.kenzie.image import list_all_files
from app.kenzie.image import list_files_by_extension
from app.kenzie.image import download
from app.kenzie.image import download_by_filename
from app.kenzie.image import download_zip

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/upload')
def upload_call():
    return upload()

@app.get('/files')
def list_all_files_call():
    return list_all_files()

@app.get('/files/<extension>')
def list_files_by_extension_call(extension):
    return list_files_by_extension(extension)

@app.get('/download')
def download_call():
    return download()

@app.get('/download/<file_name>')
def download_by_filename_call(file_name):
    return download_by_filename(file_name)


@app.get('/download-zip')
def download_zip_call():
    return download_zip()
    
if __name__ == '__main__':
    app.run(debug=True)