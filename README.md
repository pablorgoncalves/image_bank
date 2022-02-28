# Sample API - Image Bank 
<p align="left">
<img src="https://img.shields.io/static/v1?style=flat&logo=linux&label=status&message=gradewaiting&color=yellow"/>
<img src="https://img.shields.io/badge/status-gradewaiting-yellow"/>
<img src="https://img.shields.io/badge/python-3.6-blue"/>
<img src="https://img.shields.io/badge/linux-shell-lightgrey"/>
<img src="https://img.shields.io/badge/HTML5--red"/>
</p>

  
|*Endpoints              | *Methods | *Rules |
|------------------------|----------|-----------|
|home                    |GET       |/|
|upload                  |POST      |/upload|
|download_by_filename    |GET       |/download/<file_name>|
|download                |GET       |/download|
|download_zip            |GET       |/download-zip?file_extension=<FILE_EXTENSION>&compression_ratio=<COMPRESSION_RATIO>|
|list_files_by_extension |GET       |/files/<file_extension>|
|list_all_files          |GET       |/files|
