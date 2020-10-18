## Gendiff

[![Maintainability](https://api.codeclimate.com/v1/badges/e72cf6c566954f9d6477/maintainability)](https://codeclimate.com/github/Andrka/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e72cf6c566954f9d6477/test_coverage)](https://codeclimate.com/github/Andrka/python-project-lvl2/test_coverage) [![Build Status](https://travis-ci.org/Andrka/python-project-lvl2.svg?branch=master)](https://travis-ci.org/Andrka/python-project-lvl2) [![Github Actions Status](https://github.com/Andrka/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/Andrka/python-project-lvl2/actions)

"Gendiff" is a written in Python utility, which finds differences between two .json or two .yml files.

#### Installation with pip:

Before you start, you will need Python and pip on your computer. To install "Gendiff", run the following command in your terminal:

`pip install --user -i https://test.pypi.org/simple andrka-gendiff --extra-index-url https://pypi.org/simple`

[![asciicast](https://asciinema.org/a/G1Y8WYji4M2xTMUJXDQx5NIrR.svg)](https://asciinema.org/a/G1Y8WYji4M2xTMUJXDQx5NIrR)

#### Start utility:

To get help with utility after installation, print and run in the terminal:

`gendiff -h`

`gendiff --help`

[![asciicast](https://asciinema.org/a/aIEtaf1uD9IDGAeGpTppNnr2g.svg)](https://asciinema.org/a/aIEtaf1uD9IDGAeGpTppNnr2g)

To start this utility print and run in the terminal:

`gendiff first_json_file.json second_json_file.json`

[![asciicast](https://asciinema.org/a/TRZ5eB1s5rDIKBHIF2yHzHJBl.svg)](https://asciinema.org/a/TRZ5eB1s5rDIKBHIF2yHzHJBl)

or

`gendiff first_yaml_file.yml second_yaml_file.yml`

[![asciicast](https://asciinema.org/a/KdHOQQQS3SJN382vLEQrfyR8J.svg)](https://asciinema.org/a/KdHOQQQS3SJN382vLEQrfyR8J)

(where first_\*.\* and second_\*.\* are paths to compared files).

This way you will see json-like text diff between two files (default output format: -f default (--format default)).

Also you can set plain text output by choosing -f plain (--format plain) option:

`gendiff -f plain first_json_file.json second_json_file.json`

`gendiff --format plain first_json_file.json second_json_file.json`


`gendiff -f plain first_yaml_file.yml second_yaml_file.yml`

`gendiff --format plain first_yaml_file.yml second_yaml_file.yml`

[![asciicast](https://asciinema.org/a/UIKomNCBFr3tGD53w7yh1bIOK.svg)](https://asciinema.org/a/UIKomNCBFr3tGD53w7yh1bIOK)

or json output by choosing -f json (--format json) option:

`gendiff -f json first_json_file.json second_json_file.json`

`gendiff --format json first_json_file.json second_json_file.json`


`gendiff -f json first_yaml_file.yml second_yaml_file.yml`

`gendiff --format json first_yaml_file.yml second_yaml_file.yml`

[![asciicast](https://asciinema.org/a/RBExLUmBdQpCyo3z3L0vV9cib.svg)](https://asciinema.org/a/RBExLUmBdQpCyo3z3L0vV9cib)