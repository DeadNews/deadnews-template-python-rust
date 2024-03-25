import ctypes
import os

# Load the shared library
rust_lib = ctypes.cdll.LoadLibrary(os.path.abspath("target/release/librust_python_lib.so"))

# Use the add function
result = rust_lib.add(2, 3)
print(f"2 + 3 = {result}")
