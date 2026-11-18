from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Expense:
    amount: float
    category: str
    description: str = ''


def total_spent(expenses: Iterable[Expense]) -> float:
    '''Return the total amount spent across all expenses.'''
    return sum(e.amount for e in expenses)


def total_by_category(expenses: Iterable[Expense], category: str) -> float:
    '''Return total spending for a given category (case-insensitive).'''
    cat = category.strip().lower()
    return sum(e.amount for e in expenses if e.category.strip().lower() == cat)


def remaining_budget(budget: float, expenses: Iterable[Expense]) -> float:
    '''Return how much budget remains after subtracting all expenses.

    Example: budget=100, expenses totaling 30 -> 70.
    '''
    spent = total_spent(expenses)
    return budget - spent


def summarize_by_category(expenses: Iterable[Expense]) -> dict[str, float]:
    '''Return a mapping of category -> total spent.'''
    summary: dict[str, float] = {}
    for e in expenses:
        key = e.category.strip().lower()
        summary[key] = summary.get(key, 0.0) + e.amount
    return summary