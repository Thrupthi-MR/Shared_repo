from statistics import mean


def calculate_grade(student_name, marks):
    if not isinstance(student_name, str):
        raise TypeError("Student name must be a string")

    if not marks:
        raise ValueError("Marks list cannot be empty")

    if any(
        not isinstance(mark, (int, float)) 
        for mark in marks
        ):
        raise ValueError("All marks must be numeric")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    average_score = round(mean(marks), 2)

    if average_score >= 75:
        result = "Distinction"
    elif average_score >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return {
        "student_name": student_name,
        "average_score": average_score,
        "result": result
    }


def main():
    marks = [65, 78, 92, 88]

    student_report = calculate_grade(
        "Thrupthi",
        marks
    )

    print(student_report)


if __name__ == "__main__":
    main()