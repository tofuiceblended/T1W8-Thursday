# T1W8 Thursday

# 4 Pillars of OOP (contd..)
- Banking System

# __repr__ method
- Special method, like __init__, which is used to define a string representation for an object.
- Particularly used for debugging and development because it can give detailed info about an object.

# Composition of OOP
- Design principle where a class is composed of one or more objects from other classes.
- It's an alternative to Inheritance and is often times more flexible and modular
- Avoids inheritance's pitfall: Changes in base class can unintentionally affect the dericed class, which may break their functionality.
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interfaces.

using inheritance has a few pitfalls, you can have multiple child classes under 1 parent class, changes in parent will apply in child.
however this is a pitfall, because if you make changes in base class, it can accidental changes in child class

# Error Handling
## Taxonomy of Python Errors
- Silent Logical Errors - Codes that run fine, but are logically incorrect.
- Assertion Errors - Raised when 'assert' statement fails. If condition is True, nothing happens, if false, assertion error is raised.
- Syntax Errors - Errors in the written syntax, that Python interpreter cannot understand. 
- Exceptions - Runtime errors, that occurs during program execution. Python has built-in exception to handle common errors.

 # Stack Trace Interpretation
 - Text that appears when Python encounters an exception, "stack tree"
- When exception occurs, the interpreter prints a stack trace that shows where the error happened and how the code reached that point.
- Start with: Exception, then the trace.

 

### Always start from the bottom line when debugging code
