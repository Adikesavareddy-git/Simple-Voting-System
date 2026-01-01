candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

print("Welcome to Simple Voting System\n")
print("Candidates:")
for name in candidates:
    print("-", name)

votes = int(input("\nEnter number of voters: "))

for i in range(votes):
    vote = input(f"Voter {i+1}, enter your vote: ").title()

    if vote in candidates:
        candidates[vote] += 1
    else:
        print("Invalid vote. Vote ignored.")

print("\nVoting Results:")
for name, count in candidates.items():
    print(f"{name}: {count} votes")

max_votes = max(candidates.values())
winners = [name for name, count in candidates.items() if count == max_votes]

if len(winners) == 1:
    print(f"\nWinner: {winners[0]}")
else:
    print("\nResult: Tie between", ", ".join(winners))
