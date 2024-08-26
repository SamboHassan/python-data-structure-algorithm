"""
Custom Exception Handling with Traceback Manipulation
You can use the traceback module to manipulate and format 
tracebacks, excluding the system paths.

"""

import traceback
import sys


def custom_traceback(exc_type, exc_value, exc_traceback):
    tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    filtered_tb = []
    for line in tb_lines:
        if sys.prefix not in line:  # Filter out system paths
            filtered_tb.append(line)
    return "".join(filtered_tb)


def faulty_function():
    return 1 / 0  # This will cause a ZeroDivisionError


try:
    faulty_function()
except Exception as e:
    tb_str = custom_traceback(*sys.exc_info())
    print("Custom Traceback (without system paths):")
    print(tb_str)


# Using traceback.format_exc with Filtering
# You can also filter out specific lines from the traceback
# string returned by traceback.format_exc():

import traceback
import sys


def faulty_function():
    return 1 / 0  # This will cause a ZeroDivisionError


try:
    faulty_function()
except Exception as e:
    tb_str = traceback.format_exc()
    filtered_tb = "\n".join(
        line for line in tb_str.splitlines() if sys.prefix not in line
    )
    print("Custom Traceback (without system paths):")
    print(filtered_tb)


# Using traceback.extract_tb for Fine-Grained Control
# traceback.extract_tb() can be used to extract the traceback
# details as a list of FrameSummary objects, allowing you to
# selectively include or exclude certain paths:

import traceback
import sys


def custom_traceback(exc_type, exc_value, exc_traceback):
    tb_list = traceback.extract_tb(exc_traceback)
    filtered_tb_list = [frame for frame in tb_list if sys.prefix not in frame.filename]
    formatted_tb = traceback.format_list(filtered_tb_list)
    return "".join(formatted_tb)


def faulty_function():
    return 1 / 0  # This will cause a ZeroDivisionError


try:
    faulty_function()
except Exception as e:
    tb_str = custom_traceback(*sys.exc_info())
    print("Custom Traceback (without system paths):")
    print(tb_str)


# Simplifying Tracebacks Using traceback.TracebackException
# Python 3.5 introduced traceback.TracebackException, which allows
# or more customizable traceback formatting.

import traceback
import sys


def custom_traceback(exc_type, exc_value, exc_traceback):
    tb_exc = traceback.TracebackException(exc_type, exc_value, exc_traceback)
    tb_exc.stack = [frame for frame in tb_exc.stack if sys.prefix not in frame.filename]
    return "".join(tb_exc.format())


def faulty_function():
    return 1 / 0  # This will cause a ZeroDivisionError


try:
    faulty_function()
except Exception as e:
    tb_str = custom_traceback(*sys.exc_info())
    print("Custom Traceback (without system paths):")
    print(tb_str)
