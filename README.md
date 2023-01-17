# Hello
# fnum
## a python library by rust
  
contains some math functions.

This project is to show making Python library by Rust, especially via [maturin](https://github.com/PyO3/maturin.git) and pyo3.  
Look carefully at 'Cargo.toml',  'lib.rs' and project structure.



## build
1. activate virtual env (venv, conda)     
2. on terminal,
```
pip install maturin
```
```
maturin develop
```
3. and then, you can use fnum library in your python project on virtual env above.  
```python
from fnum import facto, fibo

x = facto(5)
y = fibo(10)
print(f"{x} {y}")
```


## facto
Calculate factorial, n!
```
parameter: n:int
return : n!
```

## fibo
Calculate fibonacci numbers
```
parameters: n:
int
return: fibonacci number
```
