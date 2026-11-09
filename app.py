import argparse
import json
from pathlib import Path

DATA_FILE = Path('budget.json')

# load the file
def load() -> dict:
    if not DATA_FILE.exists():
        raise SystemExit("File not created yet. Run python app.py init <budget>")
    return json.loads(DATA_FILE.read_text())

# save the file
def save(data: dict):
    DATA_FILE.write_text(json.dumps(data, indent=2))

# -- SETUP

parser = argparse.ArgumentParser(description="Expense tracker")
sub = parser.add_subparsers(dest='command', required=True)

# initialize
init_p = sub.add_parser('init', help='Set up a new monthly budget') # command
init_p.add_argument('budget', type=float)
init_p.add_argument('--rent', type=float, default=0) # optional

# adding
add_p = sub.add_parser('add', help='Add money to your budget.') # command
add_p.add_argument('amount', type=float)

# spending
spend_p = sub.add_parser('spend', help='Subtracts the money you spent from your budget.') # command
spend_p.add_argument('amount', type=float)

# output
sub.add_parser('show', help="Shows you current budget's balance.") # command

args = parser.parse_args()

# -- LOGIC

if args.command == 'init':
    data = {"budget": args.budget - args.rent}
    save(data)
    print(f"Budget has been set to {data["budget"]:.2f}.")
    if args.rent > 0:
        print(f"Rent has already been subtracted.")
else:
    data = load()
    if args.command == 'add':
        data["budget"] += args.amount
    elif args.command == 'spend':
        data["budget"] -= args.amount

    save(data)
    print(f"Your current balance is {data['budget']}")





