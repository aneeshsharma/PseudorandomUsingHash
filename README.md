# Pseudorandom Number Generator using Hash

This program generates pseudo-random numbers by calculating a hash of the current time in milliseconds.
It first generates the SHA256 hash of the timestamp then adds the ASCII values of the hexadecimal digits of the hash and finally takes its modulos with 1000.
The final result is divided by 1000 to get a random number between 0 and 1.

## Usage

Clone the repo and then simply run the program `test.py` using python. It outputs the first 100 random numbers generated.

```
$ git clone https://github.com/aneeshsharma/PseudorandomUsingHash
$ cd PseudorandomUsingHash
$ python test.py
```

> Use Python 3.x
