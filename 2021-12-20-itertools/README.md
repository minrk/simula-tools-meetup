# Python itertools module  
  
## Pre-requisits
* Iterable objects

  Objects that one can iterate over

* Iterators

  Objects that provide one element of an iterable at a time using `next()` method. 
  To create an iterator of an object `o`, use `iter(o)`.

* Generators

  Custom functions that `yeild` an element at a time instead of returning the full iterable.
  
  
  
 ## Itertools
  * Combinatorial operators
    * cartesian product
    * combinations
    * combinations with replacement
    * permutations
  * Operations on iterators
    * chain two iterables
    * compress - choose elements of one iterable using a condition on another iterable
    * starmap - apply a function on every element of a sequence
    * cycle an iterable
    * repeat an element n times 

Documentation
https://docs.python.org/3/library/itertools.html

More advanced functions than itertools:
* complex functions based on itertools: https://github.com/more-itertools/more-itertools
* toolz - a useful extension of itertools: https://github.com/pytoolz/toolz
    
## Why is itertools worth discussing?
* A module to work with basic iterators (counts) or to form more complex iterators
* Memory and time-efficient iterations
* Combinatorial operations
