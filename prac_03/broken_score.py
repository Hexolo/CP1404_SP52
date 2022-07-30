"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(get_score(score))


def get_score(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()