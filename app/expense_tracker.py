# app/expense_tracker.py
import pandas as pd
from io import StringIO

class ExpenseTracker:
    """
    A class to track and summarize personal expenses.
    """
    def __init__(self):
        """
        Initializes the ExpenseTracker with an empty DataFrame.
        """
        self.expenses = pd.DataFrame(columns=["Category", "Amount"])

    def add_expense(self, category: str, amount: float):
        """
        Adds a new expense.
        """
        new_expense = pd.DataFrame([{"Category": category, "Amount": amount}])
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)

    def get_summary(self) -> str:
        """
        Returns a summary of all expenses.
        """
        if self.expenses.empty:
            return "No expenses recorded yet."
        
        total_expenses = self.expenses["Amount"].sum()
        summary_by_category = self.expenses.groupby("Category")["Amount"].sum()

        summary_str = f"Total Expenses: ${total_expenses:,.2f}\n\n"
        summary_str += "Expenses by Category:\n"
        summary_str += summary_by_category.to_string()
        
        return summary_str