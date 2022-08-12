use pyo3::prelude::*;
use pyo3::{PyResult, Python};

#[pyfunction]
fn fibo(n: u64) -> u64 {
    if n == 0 {
        0
    } else if n == 1 || n == 2 {
        1
    } else {
        fibo(n - 1) + fibo(n - 2)
    }
}

#[pyfunction]
fn facto(n: u64) -> u64 {
    if n == 0 {
        0
    } else if n == 1 {
        1
    } else {
        facto(n - 1) * n }
}

#[pymodule]
fn fnum(_py:Python, m:&PyModule)-> PyResult<()>{
    m.add_wrapped(wrap_pyfunction!(fibo))?;
    m.add_wrapped(wrap_pyfunction!(facto))?;
    Ok(())
}
