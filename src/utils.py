"""
Utility functions for the Day 1 Python-for-AI assignment.

Three small, reusable functions: scaling features, summarising metrics,
and dividing numbers safely without crashing the whole pipeline.
"""


def normalise(values, minimum=None, maximum=None):
    """
    Scale a list of numbers into the 0-1 range.

    Args:
        values (list[float]): the numbers to scale.
        minimum (float, optional): lower bound to scale against.
            If None, the minimum of `values` is used.
        maximum (float, optional): upper bound to scale against.
            If None, the maximum of `values` is used.

    Returns:
        list[float]: each value rescaled to 0-1. If every value in
        `values` is identical, the span would be zero, so we treat it
        as 1 instead to avoid a divide-by-zero crash.
    """
    lo = min(values) if minimum is None else minimum
    hi = max(values) if maximum is None else maximum
    span = (hi - lo) or 1  # never divide by zero when all values are equal
    return [(v - lo) / span for v in values]


def summarise_scores(scores):
    """
    Summarise a list of numeric scores.

    Args:
        scores (list[float]): the scores to summarise.

    Returns:
        dict: with keys 'count', 'mean', 'minimum', 'maximum', and
        'above_threshold' (how many scores are >= 0.8). If `scores` is
        empty, we return zeros/None rather than raising an error.
    """
    if not scores:
        return {
            "count": 0,
            "mean": None,
            "minimum": None,
            "maximum": None,
            "above_threshold": 0,
        }

    return {
        "count": len(scores),
        "mean": sum(scores) / len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
        "above_threshold": sum(1 for s in scores if s >= 0.8),
    }


def safe_divide(numerator, denominator, default=0.0):
    """
    Divide two numbers, never raising an exception.

    Args:
        numerator (float): the value to divide.
        denominator (float): the value to divide by.
        default (float): value returned if the division is impossible.

    Returns:
        float: numerator / denominator, or `default` if that division
        fails (ZeroDivisionError) or the inputs aren't numeric (TypeError).
    """
    try:
        return numerator / denominator
    except (ZeroDivisionError, TypeError):
        return default