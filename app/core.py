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


def milestone_2(min_support=0.3):
    """
    Mine frequent supply itemsets using the Apriori algorithm.

    Returns itemsets with their counts and support values.
    """
    from itertools import combinations
    from collections import Counter

    if not 0 < min_support <= 1:
        raise ValueError("min_support must be between 0 and 1")

    procedures = milestone_1()

    transactions = [
        set(procedure["supplies"])
        for procedure in procedures
    ]

    total_transactions = len(transactions)

    if total_transactions == 0:
        return []

    # Count individual supply frequencies
    item_counts = Counter(
        item
        for transaction in transactions
        for item in transaction
    )

    # Keep only frequent individual supplies
    frequent_items = sorted(
        item for item, count in item_counts.items()
        if count / total_transactions >= min_support
    )

    results = []
    candidates = [
        (item,) for item in frequent_items
    ]

    while candidates:
        frequent_sets = []

        for candidate in candidates:
            count = sum(
                set(candidate).issubset(transaction)
                for transaction in transactions
            )

            support = count / total_transactions

            if support >= min_support:
                results.append({
                    "itemset": candidate,
                    "count": count,
                    "support": round(support, 4)
                })
                frequent_sets.append(candidate)

        if not frequent_sets:
            break

        # Generate larger candidates using Apriori pruning
        next_size = len(frequent_sets[0]) + 1
        frequent_lookup = set(frequent_sets)

        candidates = sorted({
            candidate
            for left in frequent_sets
            for right in frequent_sets
            for candidate in [
                tuple(sorted(set(left) | set(right)))
            ]
            if len(candidate) == next_size
            and all(
                subset in frequent_lookup
                for subset in combinations(
                    candidate, next_size - 1
                )
            )
        })

    return sorted(
        results,
        key=lambda result: (
            -result["support"],
            result["itemset"]
        )
    )




def milestone_3(top_n=5, min_support=0.3):
    """
    Analyze and display the top N co-occurring
    medical supply itemsets.
    """
    if not isinstance(top_n, int) or top_n < 1:
        raise ValueError("top_n must be a positive integer")

    # Get frequent itemsets from Milestone 2
    frequent_itemsets = milestone_2(
        min_support=min_support
    )

    # Only combinations of 2 or more supplies
    co_occurring = [
        item for item in frequent_itemsets
        if len(item["itemset"]) >= 2
    ]

    # Sort by support, highest first
    co_occurring.sort(
        key=lambda item: (
            -item["support"],
            item["itemset"]
        )
    )

    # Select the top N combinations
    top_itemsets = co_occurring[:top_n]

    print("\nTOP CO-OCCURRING MEDICAL SUPPLIES")
    print("-" * 65)
    print(
        f'{"Rank":<6}'
        f'{"Supply Combination":<38}'
        f'{"Support":<10}'
        f'{"Count":<8}'
    )
    print("-" * 65)

    for rank, result in enumerate(
        top_itemsets, start=1
    ):
        supplies = ", ".join(result["itemset"])

        print(
            f'{rank:<6}'
            f'{supplies:<38}'
            f'{result["support"]:<10.2f}'
            f'{result["count"]:<8}'
        )

    print("-" * 65)

    return top_itemsets



# --- Milestone 4: Compare the mined itemsets against simple baseline expectations.
# Hint: Consider a simple baseline where items are chosen randomly or based on their individual frequency of appearance.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")


# --- Milestone 5: Generate a report of identified supply bundles.
# Hint: Format the identified frequent itemsets and their support values into a clear, readable output, such as a CSV or a well-structured text file.
def milestone_5():  # TODO(milestone 5)
    raise NotImplementedError("TODO(milestone 5)")
