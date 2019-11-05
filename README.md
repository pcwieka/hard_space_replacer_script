### Hard Space Replacer Script

Script replaces whitespace with the non-breaking space after each `n`-letters-length word in a text fetched from file. Script outputs the processed text to a new file.

Make the script file executable:

`chmod +x hard_space_replacer_script.sh`

Usage example:

`./hard_space_replacer_script.sh /path/input_text.txt /path/output_text.txt 3`

Pattern:

```
./hard_space_replacer_script.sh param1 param2 param3

param1 - input file path
param2 - output file path (no need to create one manually)
param3 - number, length of the word after which the whitespace is replaced

```
