@echo off
echo Compiling the Security Signing Utility...
gcc sign.c -o sign.exe
if %errorlevel% equ 0 (
    echo Compilation successful!
) else (
    echo Compilation failed. Check your GCC installation.
)
pause