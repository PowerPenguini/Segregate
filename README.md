# Segregate
Segregate is program which will make files segregation simpler.

### Working
Script can segregate files which are placed in "Classify" folder. Name of this cathalog can be changed ("base_dir" varialbe, 7 line).

### Configuration
You can configure script.

Configuration file syntax:

###### formats.json 
```
{"<Cathalog name 1>": ["<Cathalog name 1>", "<Extention 1>, "<Extention 2>", "<Extention 3>"], "<Cathalog name 2>": ["<Cathalog name 2>", "<Extention 1>", "<Extention 2>", "<Extention 3>"] ...}
```

Deflault configuration:
```
{"Documents": ["Documents", "odt", "doc", "docx", "xls", "xlsx", "txt", "ppt", "pptx"], "Audio": ["Audio", "wav", "mp1", "mp2", "mp3"], "Archives": ["Archives", "tar", "rar", "zip", "xz", "gz"], "Video": ["Video", "avi", "wmv", "mp4"], "Programming": ["Programming", "py", "pyc", "cpp", "c", "h", "html", "htm", "php", "css", "js", "kv", "apk", "bat", "exe", "o", "bin", "json", "asm", "cc", "hpp", "cs", "sh"], "Pictures": ["Pictures", "gif", "jpg", "jpeg", "png", "bmp", "psd", "mpeg"]}
```
