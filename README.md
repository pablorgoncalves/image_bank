# Sample API - Image Bank 
<p align="left">
<img src="https://img.shields.io/static/v1?style=plastic&logo=python&label=Python&message=3.6&color=blue"/>
<img src="https://img.shields.io/static/v1?style=plastic&logo=linux&label=Linux&message=Shell&color=lightgrey"/>
<img src="https://img.shields.io/static/v1?style=plastic&logo=html5&label=HTML5&message= &color=red"/>
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
