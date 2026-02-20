import os

os.system("cls" if os.name == "nt" else "clear")

# 6. Nested Dictionary Extraction
# Given a complex JSON-like object (a dict of dicts/lists), extract the "Email" of a user buried inside.
# data = {"users": {"ID1": {"profile": {"email": "test@test.com"}}}}.
# Requirement: Use .get() safely so it returns "N/A" if any key in the chain is missing.

data = {"users": {"ID1": {"profile": {"email": "test@test.com"}}}}

# for u in data.items():
#    for p in u
