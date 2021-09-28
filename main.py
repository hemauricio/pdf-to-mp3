import argparse

from pdfminer import high_level, pdfparser
from gtts import gTTS


parser = argparse.ArgumentParser(description = 'PDF to Audio converter')
parser.add_argument('path',
                    help = 'Path to the PDF file')
parser.add_argument('-l', '--lang',
                    required = False,
                    help = 'language to read the PDF. Default is en',
                    default = 'en')
parser.add_argument('-s', '--slow',
                    required = False,
                    help = 'Reads the text more slowly. Defaults to False.',
                    action = 'store_true',
                    default = False)
parser.add_argument('-o', '--output',
                    required = False,
                    help = 'Output filename (w/ .mp3; e.g. -o filename.mp3)')

args = parser.parse_args()

# Path to the PDF file.
pdf_filename = args.path

# Extract the text from the PDF.
try:
    extracted_text = high_level.extract_text(pdf_filename)
except FileNotFoundError as _:
    exit('File not found')
except pdfparser.PDFSyntaxError as _:
    exit('Is this really a PDF?')

# Language in which you want to convert
language = args.lang
slow = args.slow
output = args.output if args.output else pdf_filename + '.mp3'

'''
text (string) – The text to be read.
lang (string, optional) – The language (IETF language tag) to read the text in. Default is en.
slow (bool, optional) – Reads text more slowly. Defaults to False.
'''

try:
    myobj = gTTS(text = extracted_text, lang = language, slow = slow)
except AssertionError as _:
    exit('Text is None or empty; there’s nothing left to speak after pre-precessing, tokenizing and cleaning.')

'''
save(savefile)[source]
Do the TTS API request and write result to file.

Parameters
savefile (string) – The path and file name to save the mp3 to.

Raises
gTTSError – When there’s an error with the API request.
'''

myobj.save(output)
