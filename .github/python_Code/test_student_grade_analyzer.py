import pytest
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent)
)

from student_grade_analyzer import calculate_grade


def test_distinction_result():
    result = calculate_grade(
        "John",
        [80, 90, 85]
    )

    assert result["result"] == "Distinction"


def test_pass_result():
    result = calculate_grade(
        "John",
        [55, 60, 65]
    )

    assert result["result"] == "Pass"


def test_fail_result():
    result = calculate_grade(
        "John",
        [20, 30, 40]
    )

    assert result["result"] == "Fail"


def test_empty_marks():
    with pytest.raises(ValueError):
        calculate_grade("John", [])


def test_invalid_student_name():
    with pytest.raises(TypeError):
        calculate_grade(123, [80, 90])


def test_marks_above_limit():
    with pytest.raises(ValueError):
        calculate_grade("John", [101, 80])


def test_negative_marks():
    with pytest.raises(ValueError):
        calculate_grade("John", [-5, 80])