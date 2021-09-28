# PDF to MP3 converter

## PDF to audio converter using [**Google Text-to-Speech.**](https://gtts.readthedocs.io/en/latest/module.html)


### Requirements
```
pip install -r requirements
```

### Usage
```
python3 main.py [-h] [-l LANG] [-s] [-o OUTPUT] path
```

**Positional arguments:**
```
  path                  Path to the PDF file
```

**Optional arguments:**

```
  -h, --help            shows the help message and exits.

  -l LANG, --lang LANG  language to read the PDF. Default is 'en'

  -s, --slow            Reads the text more slowly. Defaults to False.

  -o OUTPUT, --output OUTPUT
                        Output filename (w/ .mp3; e.g. -o filename.mp3) Defaults to the original
                        filename + '.mp3'.
```
