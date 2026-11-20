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




def milestone_4(min_support=0.3):
    """
    Compare frequent supply combinations against
    an independence-based baseline.
    """
    procedures = milestone_1()
    frequent_itemsets = milestone_2(min_support=min_support)

    total_transactions = len(procedures)

    if total_transactions == 0:
        return []

    # Calculate individual supply probabilities
    item_frequency = {}

    for procedure in procedures:
        for supply in set(procedure["supplies"]):
            item_frequency[supply] = (
                item_frequency.get(supply, 0) + 1
            )

    item_probability = {
        supply: count / total_transactions
        for supply, count in item_frequency.items()
    }

    comparison_results = []

    for result in frequent_itemsets:
        itemset = result["itemset"]

        # Analyze combinations of 2 or more supplies
        if len(itemset) < 2:
            continue

        actual_support = result["support"]

        # Expected support under independence
        expected_support = 1.0

        for supply in itemset:
            expected_support *= item_probability[supply]

        lift = (
            actual_support / expected_support
            if expected_support > 0
            else 0
        )

        if lift > 1.000001:
            interpretation = "Above baseline"
        elif lift < 0.999999:
            interpretation = "Below baseline"
        else:
            interpretation = "Matches baseline"

        comparison_results.append({
            "itemset": itemset,
            "actual_support": round(actual_support, 4),
            "expected_support": round(expected_support, 4),
            "lift": round(lift, 4),
            "interpretation": interpretation
        })

    comparison_results.sort(
        key=lambda x: (
            -x["lift"],
            x["itemset"]
        )
    )

    return comparison_results




def milestone_5(output_path="reports/supply_bundle_report.csv",
                min_support=0.3):
    """
    Generate a CSV report of frequent medical supply bundles.
    """
    import csv
    from pathlib import Path

    # Get mined itemsets and baseline comparisons
    frequent_itemsets = milestone_2(min_support=min_support)
    comparisons = milestone_4(min_support=min_support)

    # Lookup baseline comparisons by itemset
    comparison_lookup = {
        tuple(result["itemset"]): result
        for result in comparisons
    }

    # Include only bundles with 2 or more supplies
    bundles = [
        result for result in frequent_itemsets
        if len(result["itemset"]) >= 2
    ]

    # Sort bundles by support
    bundles.sort(
        key=lambda result: (
            -result["support"],
            result["itemset"]
        )
    )

    report_path = Path(output_path)
    report_path.parent.mkdir(
        parents=True, exist_ok=True
    )

    with report_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "Supply Bundle",
            "Count",
            "Support",
            "Expected Support",
            "Lift",
            "Interpretation"
        ])

        for bundle in bundles:
            itemset = tuple(bundle["itemset"])
            baseline = comparison_lookup[itemset]

            writer.writerow([
                ", ".join(itemset),
                bundle["count"],
                bundle["support"],
                baseline["expected_support"],
                baseline["lift"],
                baseline["interpretation"]
            ])

    print("\nSUPPLY CO-USAGE INSIGHT REPORT")
    print("-" * 50)
    print(f"Report saved to: {report_path}")
    print(f"Total supply bundles identified: {len(bundles)}")
    print(f"Minimum support threshold: {min_support:.0%}")
    print("-" * 50)

    return str(report_path)
