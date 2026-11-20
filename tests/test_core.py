
"""Tests for Supply Co-usage Insight milestones."""

import pytest
from app.core import milestone_1


# Milestone 1: Create mock medical procedure data
def test_milestone_1():
    procedures = milestone_1()

    # Verify that 10 procedures are generated
    assert len(procedures) == 10

    # Verify each procedure has an ID and supplies
    for procedure in procedures:
        assert "procedure_id" in procedure
        assert "supplies" in procedure

        # Each procedure must contain at least one supply
        assert len(procedure["supplies"]) > 0

        # No duplicate supplies within a procedure
        assert len(procedure["supplies"]) == len(
            set(procedure["supplies"])
        )

    # Verify procedure IDs are unique
    procedure_ids = [
        procedure["procedure_id"] for procedure in procedures
    ]
    assert len(procedure_ids) == len(set(procedure_ids))



# Milestone 2: Implement frequent itemset mining
def test_milestone_2():
    from app.core import milestone_2

    results = milestone_2(min_support=0.3)

    # Mining should return frequent itemsets
    assert len(results) > 0

    # Verify result structure
    for result in results:
        assert "itemset" in result
        assert "count" in result
        assert "support" in result

        assert result["support"] >= 0.3
        assert result["count"] >= 3

    # Check a known frequent supply combination
    gloves_syringe = next(
        result for result in results
        if set(result["itemset"]) == {
            "Gloves", "Syringe"
        }
    )

    assert gloves_syringe["count"] == 6
    assert gloves_syringe["support"] == 0.6

    # Check threshold filtering
    high_support_results = milestone_2(
        min_support=0.8
    )

    assert all(
        result["support"] >= 0.8
        for result in high_support_results
    )




# Milestone 3: Analyze frequent co-occurring supplies
def test_milestone_3():
    from app.core import milestone_3

    results = milestone_3(
        top_n=5,
        min_support=0.3
    )

    # Verify the number of results
    assert len(results) == 5

    # Every result must contain 2 or more supplies
    for result in results:
        assert len(result["itemset"]) >= 2

    # Verify descending support order
    supports = [
        result["support"] for result in results
    ]

    assert supports == sorted(
        supports, reverse=True
    )

    # Verify expected strongest pair
    assert results[0]["support"] == 0.6

    # Verify custom top N
    assert len(milestone_3(top_n=3)) == 3



# Milestone 4: Compare against baseline expectations
def test_milestone_4():
    from app.core import milestone_4

    results = milestone_4(min_support=0.3)

    # Results should not be empty
    assert len(results) > 0

    # Verify result structure
    for result in results:
        assert "itemset" in result
        assert "actual_support" in result
        assert "expected_support" in result
        assert "lift" in result
        assert "interpretation" in result

        assert len(result["itemset"]) >= 2
        assert result["lift"] > 0

    # Verify known combination
    gloves_syringe = next(
        result for result in results
        if set(result["itemset"]) == {
            "Gloves", "Syringe"
        }
    )

    assert gloves_syringe["actual_support"] == 0.6
    assert gloves_syringe["expected_support"] == 0.63
    assert gloves_syringe["lift"] == 0.9524
    assert gloves_syringe["interpretation"] == "Below baseline"

    # Verify descending lift order
    lifts = [result["lift"] for result in results]

    assert lifts == sorted(lifts, reverse=True)



# Milestone 5: Generate report
@pytest.mark.skip(reason="remove this line when you start milestone 5")
def test_milestone_5():
    raise NotImplementedError("write the test for milestone 5")
