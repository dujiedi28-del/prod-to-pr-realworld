from expense_tracker import Expense, remaining_budget, summarize_by_category, total_by_category, total_spent


def sample_expenses():
    return [
        Expense(20.0, "food", "lunch"),
        Expense(15.5, "transport", "bus pass"),
        Expense(10.0, "food", "snacks"),
        Expense(50.0, "rent", "partial"),
    ]


def test_total_spent():
    assert total_spent(sample_expenses()) == 95.5


def test_total_by_category_case_insensitive():
    expenses = sample_expenses()
    assert total_by_category(expenses, "food") == 30.0
    assert total_by_category(expenses, "FOOD") == 30.0
    assert total_by_category(expenses, "transport") == 15.5
    assert total_by_category(expenses, "missing") == 0.0


def test_remaining_budget():
    expenses = sample_expenses()
    assert remaining_budget(100.0, expenses) == 4.5
    assert remaining_budget(200.0, expenses) == 104.5
    assert remaining_budget(0.0, []) == 0.0


def test_summarize_by_category():
    summary = summarize_by_category(sample_expenses())
    assert summary == {"food": 30.0, "transport": 15.5, "rent": 50.0}
