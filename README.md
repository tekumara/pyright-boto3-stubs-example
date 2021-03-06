# pyright with boto3-stubs

Demonstrates the use of pyright with [boto3-stubs](https://pypi.org/project/boto3-stubs/).

Create and activate a virtualenv, then install the stubs:

```bash
pip install 'boto3-stubs[ec2]==1.14.47.0'
python -m mypy_boto3
make typings
```

When checking [ec2.py](ec2.py) pyright takes ~20 secs:

```
$ pyright --version
pyright 1.1.64

$ time pyright
Loading configuration file at /Users/tekumara/code/pyright-boto3-stubs-example/pyrightconfig.json
Assuming Python version 3.7
Assuming Python platform Darwin
Auto-excluding **/node_modules
Auto-excluding **/__pycache__
Auto-excluding .git
The useLibraryCodeForTypes has been specified in both the config file and a command-line option. The value in the config file (false) will take precedence
Searching for source files
Found 1 source file
0 errors, 0 warnings
Completed in 20.723sec
```

Remove _type_defs.pyi_ and the time drops to ~1 sec:

```
$ rm typings/mypy_boto3_ec2/type_defs.pyi
Loading configuration file at /Users/tekumara/code/pyright-boto3-stubs-example/pyrightconfig.json
Assuming Python version 3.7
Assuming Python platform Darwin
Auto-excluding **/node_modules
Auto-excluding **/__pycache__
Auto-excluding .git
The useLibraryCodeForTypes has been specified in both the config file and a command-line option. The value in the config file (false) will take precedence
Searching for source files
Found 1 source file
0 errors, 0 warnings
Completed in 0.824sec
pyright  1.05s user 0.09s system 125% cpu 0.910 total
```

## Notes

[typings/](typings/) can be regenerated by running `make typings`.
