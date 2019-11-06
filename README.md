### Hard Space Replacer Script

Script replaces whitespace with the non-breaking space after each `n`-letters-length word in a text fetched from 1+ files. Script outputs the processed text to a new created file for every processed file.

Make the script file executable:

`chmod +x hard_space_replacer_script.py`

Usage example:

`python3 hard_space_replacer_script.py 2 \
	/path/input_text_1.txt \
	/path/input_text_2.txt \
	/path/input_text_3.txt \
	/path/input_text_4.txt \
	/path/input_text_5.txt \
	/path/input_text_6.txt`

Pattern:

```
python3 hard_space_replacer_script.py param1 param2 param3 ...

param1 - number, length of the word after which the whitespace is replaced
param2, param3, ..., paramN - input files (filepaths)
```
