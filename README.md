## Gendiff

[![Maintainability](https://api.codeclimate.com/v1/badges/e72cf6c566954f9d6477/maintainability)](https://codeclimate.com/github/Andrka/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e72cf6c566954f9d6477/test_coverage)](https://codeclimate.com/github/Andrka/python-project-lvl2/test_coverage) [![Build Status](https://travis-ci.org/Andrka/python-project-lvl2.svg?branch=master)](https://travis-ci.org/Andrka/python-project-lvl2) [![Github Actions Status](https://github.com/Andrka/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/Andrka/python-project-lvl2/actions)

"Gendiff" is a written in Python utility, which finds differences between two .json or two .yml files.

#### Installation with pip:

Before you start, you will need Python and pip on your computer. To install "Gendiff", run the following command in your terminal:

`pip install --user -i https://test.pypi.org/simple andrka-gendiff --extra-index-url https://pypi.org/simple`

[![asciicast](https://asciinema.org/a/LcGT6OPf6QuD3iKCwef5XXkTd.svg)](https://asciinema.org/a/LcGT6OPf6QuD3iKCwef5XXkTd)

#### Start utility:

To start this utility after installation, print and run in the terminal:

`gendiff first_json_file.json second_json_file.json`

[![asciicast](https://asciinema.org/a/u3JvS82zTSWRtC5DEnyjnD9ai.svg)](https://asciinema.org/a/u3JvS82zTSWRtC5DEnyjnD9ai)

or

`gendiff first_yaml_file.yml second_yaml_file.yml`

[![asciicast](https://asciinema.org/a/dftuzIBseoRNiT1svBRICO0UH.svg)](https://asciinema.org/a/dftuzIBseoRNiT1svBRICO0UH)

This way you will see json-like diff between two files.

Also you can set plain text output by choosing -f plain (--format plain) option:

`gendiff -f plain first_json_file.json second_json_file.json`

`gendiff --format plain first_json_file.json second_json_file.json`

`gendiff -f plain first_yaml_file.yml second_yaml_file.yml`

`gendiff --format plain first_yaml_file.yml second_yaml_file.yml`

[![asciicast](https://asciinema.org/a/NtLJIat5JJ67P5SxVbxt6vJ4M.svg)](https://asciinema.org/a/NtLJIat5JJ67P5SxVbxt6vJ4M)
