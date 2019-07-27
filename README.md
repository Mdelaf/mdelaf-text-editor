# Mdelaf Text Editor

Simple text editor with password protection

### Download compiled binary files

Binary files are available for Windows in the [releases section](https://github.com/Mdelaf/mdelaf-text-editor/releases).

### Build binary file yourself

Use `pyinstaller` with the following command:

`pyinstaller --onefile --windowed --icon=icon.ico mdelaf_editor.py`

Using this command, a single binary file will be created and the whole Python library will be bundled within it. Because of this, the size may be quite large (> 30 MB).
