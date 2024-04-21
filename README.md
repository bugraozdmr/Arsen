<p align=center>
  <br>
  <a href="https://github.com/bugraozdmr/Arsen/blob/main/Arsen/images/sample-2.png" target="_blank"><img src="https://raw.githubusercontent.com/bugraozdmr/Arsen/main/Arsen/images/sample-2.png"/></a>
  <br>
  <span>Find social media profiles for a username</span>
  <br>
</p>




## Installation

```console
# clone the repo
$ git clone https://github.com/bugraozdmr/Arsen.git

# change the working directory to Arsen
$ cd Arsen

```

## Usage

```console
$ python Arsen.py --help
Arsen: Find profiles in popular websites

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Operation ends after n seconds. ** arsen.py -t 30 => this operation ends after 30 seconds
  -u USERNAME, --username USERNAME
                        After this parameter type username that you want to search
  -o OUTPUT, --output OUTPUT
                        After this parameter type filename only .Output will be in the same folder. ** arsen.py -u grant -o out.txt

```

To search for user:
```
python Arsen.py -u grant
```
Advanced search for user:
```
python Arsen.py -u grant -o grant.txt -t 20
```


Thank you for using Arsen 🎉🎉🎉
