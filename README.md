# Image Bank

|* Endpoint              |* Methods |* Rule                                                 |
|------------------------|----------|-------------------------------------------------------|
|home                    |GET       |/                                                      |
|upload                  |POST      |/upload                                                |
|download_by_filename    |GET       |/download/<file_name>                                  |
|download                |GET       |/download                                              |
|download_zip            |GET       |/download-zip?file_extension=###&compression_ratio=### |
|list_all_files          |GET       |/files                                                 |
|list_files_by_extension |GET       |/files/<extension>                                     |
