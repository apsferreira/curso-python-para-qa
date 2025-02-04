import random

tests_cases = []
for i in range(5):
    test_case = input(f"Digite o nome do {i + 1} teste case: ")
    tests_cases.append(test_case)

print("\nResultados da execução:")
for test_case in tests_cases:
    result = random.choice(["Pass", "Fail"])
    print(f"{test_case}: {result}")
