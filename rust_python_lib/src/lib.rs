extern crate cpython;

use cpython::{PyResult, Python, py_module_initializer, py_fn};

// add function
fn add(a: i32, b: i32) -> PyResult<i32> {
    Ok(a + b)
}

// PyMODINIT_FUNC is a macro which will be used to tell Python about our module
py_module_initializer!(rust_python_lib, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "add", py_fn!(py, add(a: i32, b: i32)))?;
    Ok(())
});
