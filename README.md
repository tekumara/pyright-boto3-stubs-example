# pyright with boto3-stubs

Demonstrates the use of pyright with [boto3-stubs](https://pypi.org/project/boto3-stubs/).

Create and activate a virtualenv, then install the stubs:

```bash
pip install 'boto3-stubs[ec2]==1.14.47.0'
make typings
```

When checking [ec2.py](ec2.py) pyright takes > 20 secs:

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
Found 14 source files
0 errors, 0 warnings
Completed in 23.731sec
pyright  39.58s user 5.38s system 187% cpu 23.921 total
```

Remove type_defs.pyi and the time drops to ~2 sec:

```
rm typings/mypy_boto3_ec2/type_defs.pyi
Loading configuration file at /Users/tekumara/code/pyright-boto3-stubs-example/pyrightconfig.json
Assuming Python version 3.7
Assuming Python platform Darwin
Auto-excluding **/node_modules
Auto-excluding **/__pycache__
Auto-excluding .git
The useLibraryCodeForTypes has been specified in both the config file and a command-line option. The value in the config file (false) will take precedence
Searching for source files
Found 13 source files
0 errors, 0 warnings
Completed in 1.93sec
pyright  2.84s user 0.14s system 148% cpu 2.015 total
```