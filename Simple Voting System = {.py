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

winner = max(candidates, key=candidates.get)
print(f"\nWinner: {winner}")
