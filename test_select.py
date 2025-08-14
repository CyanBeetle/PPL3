#!/usr/bin/env python3
"""
HLang Project Selective Test Runner

This script allows you to run specific tests from any test suite.
It supports pattern matching and individual test selection.

Usage:
    # Run specific test by name
    python select.py test_007
    python select.py test_checker.py::test_007
    
    # Run multiple tests
    python select.py test_007 test_008 test_009
    
    # Run tests matching a pattern
    python select.py "test_0*"
    python select.py "*pipeline*"
    
    # Run from specific test file
    python select.py --file test_checker.py test_007
    python select.py --file test_lexer.py "test_*"
    
    # Run with verbose output
    python select.py -v test_007
    
    # Show only failures
    python select.py --tb=short test_007
"""

import argparse
import os
import platform
import subprocess
import sys
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output."""

    def __init__(self):
        # Check if we're on Windows and if ANSI is supported
        self.supported = (
            platform.system() != "Windows"
            or os.environ.get("TERM")
            or os.environ.get("ANSICON")
            or "ANSI" in os.environ.get("TERM_PROGRAM", "")
        )

        if self.supported:
            self.RED = "\033[31m"
            self.GREEN = "\033[32m"
            self.YELLOW = "\033[33m"
            self.BLUE = "\033[34m"
            self.MAGENTA = "\033[35m"
            self.CYAN = "\033[36m"
            self.RESET = "\033[0m"
        else:
            self.RED = self.GREEN = self.YELLOW = self.BLUE = self.MAGENTA = self.CYAN = self.RESET = ""

    def red(self, text):
        return f"{self.RED}{text}{self.RESET}"

    def green(self, text):
        return f"{self.GREEN}{text}{self.RESET}"

    def yellow(self, text):
        return f"{self.YELLOW}{text}{self.RESET}"

    def blue(self, text):
        return f"{self.BLUE}{text}{self.RESET}"

    def magenta(self, text):
        return f"{self.MAGENTA}{text}{self.RESET}"

    def cyan(self, text):
        return f"{self.CYAN}{text}{self.RESET}"


class SelectiveTestRunner:
    """Selective test runner for HLang project."""

    def __init__(self):
        self.root_dir = Path(__file__).parent.absolute()
        self.tests_dir = self.root_dir / "tests"
        self.venv_dir = self.root_dir / "venv"
        self.build_dir = self.root_dir / "build"
        self.report_dir = self.root_dir / "reports"

        self.colors = Colors()

        # Platform-specific paths
        if platform.system() == "Windows":
            self.venv_python3 = self.venv_dir / "Scripts" / "python.exe"
        else:
            self.venv_python3 = self.venv_dir / "bin" / "python"

        # Available test files
        self.test_files = {
            "lexer": "test_lexer.py",
            "parser": "test_parser.py", 
            "ast": "test_ast_gen.py",
            "checker": "test_checker.py",
            "codegen": "test_codegen.py"
        }

    def find_python(self):
        """Find appropriate Python executable."""
        # First try virtual environment python
        if self.venv_python3.exists():
            return str(self.venv_python3)
        
        # Fall back to system python
        candidates = ["python3.12", "python", "py"]
        for cmd in candidates:
            try:
                result = subprocess.run(
                    [cmd, "--version"], 
                    capture_output=True, 
                    text=True, 
                    check=False
                )
                if result.returncode == 0:
                    return cmd
            except:
                continue
        
        return "python"

    def run_command(self, cmd, cwd=None, check=True):
        """Run a shell command."""
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.root_dir,
                check=check,
                text=True,
            )
            return result
        except subprocess.CalledProcessError as e:
            print(self.colors.red(f"Command failed: {e}"))
            if check:
                sys.exit(1)
            return e

    def ensure_build(self):
        """Ensure build directory exists."""
        if not self.build_dir.exists():
            print(self.colors.yellow("Build directory not found. Please run 'python run.py build' first."))
            sys.exit(1)

    def detect_test_file(self, test_pattern):
        """Detect which test file contains the given test pattern."""
        for suite_name, filename in self.test_files.items():
            test_file = self.tests_dir / filename
            if test_file.exists():
                try:
                    with open(test_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if f"def {test_pattern}(" in content:
                            return filename
                except:
                    continue
        return None

    def list_available_tests(self, test_file=None):
        """List available tests in the specified file or all files."""
        print(self.colors.blue("Available tests:"))
        print()
        
        files_to_check = [test_file] if test_file else list(self.test_files.values())
        
        for filename in files_to_check:
            test_file_path = self.tests_dir / filename
            if not test_file_path.exists():
                continue
                
            print(self.colors.cyan(f"{filename}:"))
            try:
                with open(test_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    for line_num, line in enumerate(lines, 1):
                        line = line.strip()
                        if line.startswith('def test_') and '(' in line:
                            test_name = line.split('(')[0].replace('def ', '')
                            # Look for docstring in next few lines
                            doc = ""
                            for i in range(line_num, min(line_num + 3, len(lines))):
                                if i < len(lines) and '"""' in lines[i]:
                                    doc = lines[i].strip().replace('"""', '').strip()
                                    break
                            
                            if doc:
                                print(f"  {self.colors.green(test_name)} - {doc}")
                            else:
                                print(f"  {self.colors.green(test_name)}")
            except Exception as e:
                print(f"  {self.colors.red(f'Error reading file: {e}')}")
            print()

    def run_tests(self, test_patterns, test_file=None, verbose=False, tb_style="short", timeout=10):
        """Run selected tests."""
        self.ensure_build()
        
        python_cmd = self.find_python()
        
        # Build pytest command
        cmd = [
            python_cmd,
            "-m",
            "pytest",
            f"--timeout={timeout}",
            f"--tb={tb_style}",
        ]
        
        if verbose:
            cmd.append("-v")
        else:
            cmd.append("-q")
        
        # Determine test targets
        test_targets = []
        
        if test_file:
            # Specific test file provided
            test_file_path = self.tests_dir / test_file
            if not test_file_path.exists():
                print(self.colors.red(f"Test file not found: {test_file}"))
                sys.exit(1)
            
            for pattern in test_patterns:
                if "::" in pattern:
                    # Already contains file reference
                    test_targets.append(pattern)
                else:
                    # Add file reference
                    test_targets.append(f"tests/{test_file}::{pattern}")
        else:
            # Auto-detect test files or use patterns as-is
            for pattern in test_patterns:
                if "::" in pattern:
                    # Already contains file reference
                    test_targets.append(pattern)
                elif pattern.endswith(".py"):
                    # Test file name
                    test_targets.append(f"tests/{pattern}")
                else:
                    # Test function name - try to find it
                    detected_file = self.detect_test_file(pattern)
                    if detected_file:
                        test_targets.append(f"tests/{detected_file}::{pattern}")
                    else:
                        # Pattern matching across all files
                        test_targets.append(f"tests/ -k {pattern}")
        
        if not test_targets:
            print(self.colors.red("No test targets specified."))
            sys.exit(1)
        
        # Add test targets to command
        cmd.extend(test_targets)
        
        # Set up environment
        env = os.environ.copy()
        env["PYTHONPATH"] = str(self.root_dir)
        
        print(self.colors.blue(f"Running tests: {' '.join(test_targets)}"))
        print(self.colors.yellow(f"Command: {' '.join(cmd)}"))
        print()
        
        # Run the tests
        try:
            result = subprocess.run(
                cmd,
                cwd=self.root_dir,
                env=env,
                check=False  # Don't fail on test failures
            )
            
            print()
            if result.returncode == 0:
                print(self.colors.green("✓ All selected tests passed!"))
            else:
                print(self.colors.yellow(f"Tests completed with exit code {result.returncode}"))
                
        except KeyboardInterrupt:
            print(self.colors.yellow("\nTest run interrupted by user."))
        except Exception as e:
            print(self.colors.red(f"Error running tests: {e}"))
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="HLang Project Selective Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python select.py test_007                    # Run specific test (auto-detect file)
  python select.py test_007 test_008          # Run multiple tests
  python select.py "test_0*"                  # Run tests matching pattern
  python select.py --file test_checker.py test_007  # Run from specific file
  python select.py -v test_007                # Verbose output
  python select.py --list                     # List all available tests
  python select.py --list --file test_checker.py  # List tests in specific file
        """,
    )

    parser.add_argument(
        "patterns",
        nargs="*",
        help="Test patterns to run (test names, patterns, or file names)"
    )
    
    parser.add_argument(
        "--file", "-f",
        dest="test_file",
        help="Specific test file to run tests from"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "--tb",
        choices=["short", "long", "line", "no"],
        default="short",
        help="Traceback print mode"
    )
    
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Test timeout in seconds"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available tests"
    )

    args = parser.parse_args()

    runner = SelectiveTestRunner()

    if args.list:
        runner.list_available_tests(args.test_file)
        return

    if not args.patterns:
        print(runner.colors.red("No test patterns specified."))
        print("Use --list to see available tests, or specify test patterns.")
        parser.print_help()
        sys.exit(1)

    runner.run_tests(
        test_patterns=args.patterns,
        test_file=args.test_file,
        verbose=args.verbose,
        tb_style=args.tb,
        timeout=args.timeout
    )


if __name__ == "__main__":
    main()
