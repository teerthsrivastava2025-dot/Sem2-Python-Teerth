# Household Budget & Inflation Impact Analyzer (Personalized)

# -----------------------------
# 1. USER INPUT (PERSONALIZED)
# -----------------------------
monthly_income = int(input("Enter your monthly income (INR): "))

# -----------------------------
# 2. BASIC DATA TYPES
# -----------------------------
inflation_rate = 0.06           # float
currency = "INR"                # str
extra_income = None             # NoneType

# -----------------------------
# 3. TUPLE (Fixed categories)
# -----------------------------
categories = ("Food", "Rent", "Transport", "Utilities", "Entertainment")

# -----------------------------
# 4. LIST (Monthly expenses)
# -----------------------------
expenses = [12000, 18000, 6000, 4000, 3000]

# -----------------------------
# 5. DICTIONARY (Mapping)
# -----------------------------
expense_data = dict(zip(categories, expenses))

# -----------------------------
# 6. SET (Unique categories)
# -----------------------------
unique_categories = set(expense_data.keys())

# -----------------------------
# 7. CALCULATIONS
# -----------------------------
total_expense = sum(expenses)
savings = monthly_income - total_expense

# -----------------------------
# 8. BOOLEAN (IF–ELSE CONDITION)
# -----------------------------
is_budget_balanced = True if savings >= 0 else False

# -----------------------------
# 9. INFLATION ADJUSTMENT
# -----------------------------
inflation_adjusted = {}

for category, amount in expense_data.items():
    inflation_adjusted[category] = amount * (1 + inflation_rate)

inflation_total = sum(inflation_adjusted.values())
inflation_savings = monthly_income - inflation_total

# -----------------------------
# 10. OUTPUT
# -----------------------------
print("\nHOUSEHOLD BUDGET ANALYSIS")
print("--------------------------")
print("Income:", monthly_income, currency)
print("Total Expenses:", total_expense, currency)
print("Savings:", savings, currency)
print("Budget Balanced:", is_budget_balanced)

print("\nInflation Adjusted Expenses:")
for cat, amt in inflation_adjusted.items():
    print(cat, ":", round(amt, 2), currency)

print("\nSavings After Inflation:", round(inflation_savings, 2), currency)

# -----------------------------
# 11. ECONOMIC INTERPRETATION
# -----------------------------
if is_budget_balanced:
    print("\n✅ You are living within your means.")
else:
    print("\n❌ Your expenses exceed your income.")

if inflation_savings < savings:
    print("⚠️ Inflation reduces real purchasing power.")
else:
    print("✅ Inflation impact is manageable.")
