import math
import statistics


def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    if radius <= 0:
        return 0.0
    return math.pi * radius * radius


def calculate_statistics(numbers: list[int]) -> dict:
    """Return basic statistics (mean, median, variance)."""
    if not numbers:
        return {"mean": 0, "median": 0, "variance": 0}

    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "variance": statistics.variance(numbers),
    }


class Student:
    """Represents a student with grades."""

    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def average_grade(self) -> float:
        """Return the student's average grade."""
        if not self.grades:
            return 0.0
        return statistics.mean(self.grades)

    def performance(self) -> str:
        """Classify student performance based on average grade."""
        avg = self.average_grade()
        if avg >= 75:
            return "Excellent"
        elif avg >= 50:
            return "Good"
        else:
            return "Needs Improvement"
