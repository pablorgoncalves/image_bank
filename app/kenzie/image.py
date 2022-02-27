from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from zipfile import ZipFile
from datetime import datetime
from dotenv import load_dotenv
# import os
from os import getenv, getcwd, listdir, mkdir, chdir, path
load_dotenv()

BASE_DIRECTORY = getcwd()
MAX_CONTENT_LENGTH = getenv('MAX_CONTENT_LENGTH')
ALLOWED_EXTENSIONS = getenv('ALLOWED_EXTENSIONS')
FILES_DIRECTORY = getenv('FILES_DIRECTORY')

if 'upload' not in listdir(path.join(BASE_DIRECTORY, 'app')):
    mkdir(FILES_DIRECTORY)
    
def allowed_extensions(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_image_filesize(filesize):
    if int(filesize) <= int(MAX_CONTENT_LENGTH):
        return True
    else:
        return False

def upload():
    if request.files:
        file_size_mb = request.content_length / 1024 / 1024
        file = request.files['file']
        save_path = path.join(FILES_DIRECTORY, secure_filename(file.filename))
        if allowed_image_filesize(request.content_length):
            if allowed_extensions(file.filename):
                if '_'.join(file.filename.split(' ')) in \
                    listdir(FILES_DIRECTORY):
                    return {'error': 'A file with that name already exists'}, 409
                file.save(save_path)
                return {'success': f'The file {file.filename} was successfully saved'}, 201
            return {'error': 'Extension not allowed'}, 415
        return {'error': f'Size file {file_size_mb:.2f}MB - Maximum allowed: 1MB'}, 413

def list_all_files():
    list_files = listdir(FILES_DIRECTORY)
    return jsonify(list_files), 200

def list_files_by_extension(extension):
    list_files = listdir(FILES_DIRECTORY)
    filtered_list_file = [file for file \
        in list_files if file[-3:] == extension \
        or file[-4:] == extension ]
    if filtered_list_file:
        return jsonify(filtered_list_file) ,200
    return {'error': 'Extension not found'}, 404

def download():
    return {'msg': 'Pagina de DOWNLOAD'}

def download_by_filename(file_name):
    list_files = listdir(FILES_DIRECTORY)
    found_filename = [filename for filename \
        in list_files if filename == file_name]
    if found_filename:
        return send_from_directory(
        directory="../app/upload", 
        path=found_filename[0], 
        as_attachment=True
        )
    return {'error': 'File does not exist'}, 404

def download_zip():
    query_params = request.args
    filename_zip = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filtered_list_file = [file for file in listdir(path.join(BASE_DIRECTORY, FILES_DIRECTORY)) \
        if file[-3:] == query_params['extension'] \
        or file[-4:] == query_params['extension'] ]
    if filtered_list_file:
        chdir(path.join(BASE_DIRECTORY, FILES_DIRECTORY))
        with ZipFile(f'/tmp/{filename_zip}.zip', 'w') as zip_file:
            for line in filtered_list_file:
                zip_file.write(line)
            return {'success': f'The file {filename_zip}.zip was created'}, 200
    return {'error': 'There are no files to compress'}, 404
