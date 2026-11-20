# Supply Co-usage Insight

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/fyqwwpjsfp/badge.svg)](https://ask.thili.ai/b/fyqwwpjsfp)

This project, 'Supply Co-usage Insight,' provides hospital administrators with a data-driven tool to analyze medical supply usage. By identifying which supplies are frequently used together across procedures, it aims to optimize stock placement and procurement efficiency within healthcare settings.

## What you are building

**Goal.** You will build a system that analyzes medical supply usage data to identify which supplies are frequently used together, helping hospital administrators optimize stock and procurement.

**Done when.** The project is complete when you have identified strong co-occurring medical supply sets, proven by outputting a list of frequent itemsets with their support, and generated a report of these identified supply bundles.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Create mock medical procedure data, where each procedure lists used supply SKUs.**  
      Hint: Use Python lists of lists or dictionaries to represent procedures and their associated supply SKUs.
- [ ] **2. Implement frequent itemset mining (e.g., using thilimarketbasket).**  
      Hint: Apply the `lfretail-lfmarketbasket` frequent itemset mining technique to your mock medical procedure data.
- [ ] **3. Analyze and display the most frequent co-occurring supply itemsets.**  
      Hint: Sort the results from the mining algorithm by their support metric and display the top N most frequent itemsets.
- [ ] **4. Compare the mined itemsets against simple baseline expectations.**  
      Hint: Consider a simple baseline where items are chosen randomly or based on their individual frequency of appearance.
- [ ] **5. Generate a report of identified supply bundles.**  
      Hint: Format the identified frequent itemsets and their support values into a clear, readable output, such as a CSV or a well-structured text file.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- Analyze how changing the minimum support threshold affects the identified bundles and their practical implications.
- Suggest specific procurement or stock placement actions based on the strongest bundles, explaining the rationale for each suggestion.
- Investigate the impact of focusing on different itemset sizes (e.g., only 2-item sets vs. larger sets) on the insights gained.
