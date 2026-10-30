MIN_MONTHS = 3 # paid fewer months than this = at risk of lapsing

# A list of dictionaries: each dict is one placeholder
policies = [
    {"name": "Ade", "premium": 1500, "months_paid": 6},
    {"name": "Bola", "premium": 2000, "months_paid": 2},
    {"name": "Chidi", "premium": 1200, "months_paid": 12},
]

def total_paid(policy):
    """Return how much one policyholder has paid in total."""

    return policy["premium"] * policy["months_paid"]

def at_risk(policy): 
    """Return True if the policyholder is at risk of losing coverage if user paid for less than 3 months, False otherwise."""
    return policy["months_paid"] < MIN_MONTHS

for p in policies:
    print(f"{p['name']} has paid {total_paid(p)} naira")          

for p in policies:
    if at_risk(p):
        print(f"{p['name']} is at risk of lapsing.")
