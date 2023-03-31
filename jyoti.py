class Newspaper:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

newspapers = [
    Newspaper("TOI", [3, 3, 3, 3, 3, 5, 6]),
    Newspaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4]),
    Newspaper("ET", [4, 4, 4, 4, 4, 4, 10]),
    Newspaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]),
    Newspaper("HT", [2, 2, 2, 2, 2, 4, 4])
]

def get_combinations(newspapers, budget):
    valid_combinations = []
    for i in range(2**len(newspapers)):
        combination = []
        total_cost = 0
        for j in range(len(newspapers)):
            if i & (1<<j):
                combination.append(newspapers[j].name)
                total_cost += sum(newspapers[j].prices)
        if total_cost <= budget:
            valid_combinations.append(combination)
    return valid_combinations

budget = int(input("Enter weekly budget: "))
combinations = get_combinations(newspapers, budget)
for c in combinations:
    print(c)