# Day 13 - Debugging

## What I Learned
- **Understand the intent:** know what the code is supposed to do before hunting for what's wrong
- **Reproduce the error:** trigger the bug consistently to find the root cause
- **Play computer:** step through the code line by line, tracking each variable by hand
- **Find where it breaks:** use the output and logic flow to locate the failing line
- **Debugger tools:** `pdb` or an IDE debugger to inspect variable state while the code runs
- **Run code often:** test in small increments to catch errors early
- **Use the community:** Stack Overflow for common issues
- **Take breaks:** come back with fresh eyes

## Extra Techniques
- **`print()` debugging:** check variable values at different stages, and tag output (e.g. `[DEBUG]`) so it's easy to spot and remove
- **`try-except`:** catch errors like `ZeroDivisionError` or `TypeError` without crashing, and give clear error messages
