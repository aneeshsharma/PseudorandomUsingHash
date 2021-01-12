import hashlib
import time

def calc_hash(x):
    return hashlib.sha256(str(x).encode()).hexdigest()

def random():
    t = time.time() * 1000
    h = calc_hash(t)
    s = sum([ord(_) for _ in h])
    r = float(s % 1000)
    return r / 1000

