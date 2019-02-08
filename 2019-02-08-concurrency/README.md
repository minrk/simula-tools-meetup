# Concurrency in Python

In this workshop we will look at how to do concurrency in python.

The workshop will mostly be based on the article "[Speed up your
Python Program with
Concurrency](https://realpython.com/python-concurrency-overview/)",
and the code in [Realpython's github
repo](https://github.com/realpython/materials/tree/master/concurrency-overview)

To run the code here, first create a virtual environment
	
	python3 -m virtualenv venv
	
Activate the environement

	source venv/bin/activate
	
and install the required packages:

    pip install -r requirements.txt

I will also go through some basics of asyncio, where I will borrow
some
[slides](https://speakerdeck.com/pycon2017/miguel-grinberg-asynchronous-python-for-the-complete-beginner)
from a [talk](https://www.youtube.com/watch?v=iG6fr81xHKA) given by
Miguel Grinberg at PyCon2017.

## Extra

I recently came across a library
called[`parse`](https://pypi.org/project/parse/) which provides a way
to search for specific patterns in a string. This is basically an
inverse operation of the `string.format` method.

The forward problem
```
pattern = 'Hello {name}! Welcome to {place}'
s = pattern.format(name='Henrik', place='Simula')
print(s)
```
The inverse
```
# Say we have `s` and `pattern` and want to find `name` and `place`
import parse
res = parse.search(pattern, s)
print(res.named)
```
The specific problem I has was to extract info about an experiment
from the filename
```
# My example (getting information about experiment from the filename)
filename = '20181116_10uM_1hz/Point2A_MM_ChannelCyan_VC_Seq0007.nd2'
pattern = '{date}_{dose}_{pacing_frequency}/Point{chip}_{media}_Channel{channel}_{roi}_Seq{seq_nr}.nd2'
res = parse.search(pattern, filename)
print(res.named)
```
