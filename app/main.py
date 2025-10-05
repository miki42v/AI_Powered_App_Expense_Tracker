# app/main.py
import streamlit as st
from ai_bot import AIBot
from text_summarizer import TextSummarizer
from expense_tracker import ExpenseTracker

# Initialize session state for the expense tracker
if 'expense_tracker' not in st.session_state:
    st.session_state.expense_tracker = ExpenseTracker()

def main():
    st.title("My AI-Powered App")

    # --- AI Q&A Bot ---
    st.header("1. AI Q&A Bot")
    ai_bot = AIBot()
    question = st.text_input("Ask the AI a question:")
    if st.button("Get Answer"):
        if question:
            with st.spinner("Thinking..."):
                answer = ai_bot.get_answer(question)
                st.write(f"**Answer:** {answer}")
        else:
            st.warning("Please enter a question.")

    # --- Text Summarizer ---
    st.header("2. Text Summarizer")
    text_summarizer = TextSummarizer()
    text_to_summarize = st.text_area("Enter text to summarize:")
    if st.button("Summarize"):
        if text_to_summarize:
            with st.spinner("Summarizing..."):
                summary = text_summarizer.summarize(text_to_summarize)
                st.write(f"**Summary:** {summary}")
        else:
            st.warning("Please enter text to summarize.")

    # --- Personal Expense Tracker ---
    st.header("3. Personal Expense Tracker")
    expense_tracker = st.session_state.expense_tracker
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.text_input("Expense Category (e.g., Food, Rent):")
    with col2:
        amount = st.number_input("Amount:", min_value=0.0, format="%.2f")

    if st.button("Add Expense"):
        if category and amount > 0:
            expense_tracker.add_expense(category, amount)
            st.success(f"Added expense: {category} - ${amount}")
        else:
            st.warning("Please enter a valid category and amount.")
            
    st.subheader("Expense Summary")
    summary = expense_tracker.get_summary()
    st.text(summary)

if __name__ == "__main__":
    main()