# Image Bank
<p align="left">
<img src="https://img.shields.io/badge/status-finalizado-brightgreen"/>
<img src="https://img.shields.io/badge/python-3.6-yellow"/>
<img src="https://img.shields.io/badge/linux-shell-orange"/>
<img src="https://img.shields.io/badge/HTML5--informational"/>
</p>

|* Endpoint              |* Methods |* Rule                                                                |
|------------------------|----------|----------------------------------------------------------------------|
|home                    |GET       |/                                                                     |
|upload                  |POST      |/upload                                                               |
|download_by_filename    |GET       |/download/<file_name>                                                 |
|download                |GET       |/download                                                             |
|download_zip            |GET       |/download-zip?file_extension= <EXTENSION> &compression_ratio= <RATIO> |
|list_files_by_extension |GET       |/files/<extension>                                                    |
|list_all_files          |GET       |/files                                                                |
