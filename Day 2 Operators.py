#!/bin/python3


# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(m_cost, tip_per, tax_per):
    total_cost = m_cost + ((tip_per / 100) * m_cost) + ((tax_per / 100) * m_cost)
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
