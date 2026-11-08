import subprocess
import sys
from calculator import add


def run_script(filename):
    return subprocess.run(
        [sys.executable, filename],
        capture_output=True,
        text=True,
    )


def test_helloworld_runs_and_prints_greeting():
    result = run_script("helloworld.py")
    assert result.returncode == 0
    assert "Hello World" in result.stdout


def test_profile_runs_and_prints_profile():
    result = run_script("profile.py")
    assert result.returncode == 0
    assert "profile" in result.stdout


def test_add_function():
    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(-5, 5) == 0


def test_calculator_runs_and_prints_result():
    result = run_script("calculator.py")
    assert result.returncode == 0
    assert "Calculator Program" in result.stdout
    assert "10 + 20 = 30" in result.stdout
