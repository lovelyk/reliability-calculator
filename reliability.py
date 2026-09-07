import math


def calculate_reliability(failure_rate: float, operating_time: float) -> float:
    """Calculate reliability using R(t) = exp(-failure_rate * operating_time)."""
    if failure_rate < 0:
        raise ValueError("Failure rate cannot be negative.")

    if operating_time < 0:
        raise ValueError("Operating time cannot be negative.")

    return math.exp(-failure_rate * operating_time)


if __name__ == "__main__":
    result = calculate_reliability(0.001, 100)
    print(f"Reliability: {result:.4f}")