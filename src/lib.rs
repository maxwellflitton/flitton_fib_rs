use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::PyDict;
use pyo3::exceptions::PyTypeError;


#[pyfunction]
pub fn add_numbers(one: i32, two: i32) -> PyResult<i32> {
    Ok(one + two)
}


#[pymodule]
fn rust_messaging(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    Ok(())
}
