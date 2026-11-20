"""Your code. One stub per milestone; build them in order and keep each one small."""

def milestone_1():
    """Generate mock medical procedure supply data."""
    procedures = [
        {"procedure_id": "P001", "supplies": ["Gloves", "Syringe", "Gauze"]},
        {"procedure_id": "P002", "supplies": ["Gloves", "Syringe", "IV Set"]},
        {"procedure_id": "P003", "supplies": ["Gloves", "Gauze", "Bandage"]},
        {"procedure_id": "P004", "supplies": ["Gloves", "Syringe", "Gauze"]},
        {"procedure_id": "P005", "supplies": ["Syringe", "IV Set", "Gloves"]},
        {"procedure_id": "P006", "supplies": ["Gloves", "Gauze", "Bandage"]},
        {"procedure_id": "P007", "supplies": ["Gloves", "Syringe", "Gauze"]},
        {"procedure_id": "P008", "supplies": ["Syringe", "IV Set"]},
        {"procedure_id": "P009", "supplies": ["Gloves", "Gauze", "Bandage"]},
        {"procedure_id": "P010", "supplies": ["Gloves", "Syringe", "IV Set"]},
    ]
    return procedures

# --- Milestone 2: Implement frequent itemset mining (e.g., using thilimarketbasket).
# Hint: Apply the `lfretail-lfmarketbasket` frequent itemset mining technique to your mock medical procedure data.
def milestone_2():  # TODO(milestone 2)
    raise NotImplementedError("TODO(milestone 2)")


# --- Milestone 3: Analyze and display the most frequent co-occurring supply itemsets.
# Hint: Sort the results from the mining algorithm by their support metric and display the top N most frequent itemsets.
def milestone_3():  # TODO(milestone 3)
    raise NotImplementedError("TODO(milestone 3)")


# --- Milestone 4: Compare the mined itemsets against simple baseline expectations.
# Hint: Consider a simple baseline where items are chosen randomly or based on their individual frequency of appearance.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")


# --- Milestone 5: Generate a report of identified supply bundles.
# Hint: Format the identified frequent itemsets and their support values into a clear, readable output, such as a CSV or a well-structured text file.
def milestone_5():  # TODO(milestone 5)
    raise NotImplementedError("TODO(milestone 5)")
