import pandas as pd
import numpy as np

class TinderEloAlgorithm:
    def __init__(self, k_factor=32):
        self.k_factor = k_factor

    def calculate_expected_score(self, rating_a, rating_b):
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    def update_ratings(self, rating_a, rating_b, outcome):
        expected_score_a = self.calculate_expected_score(rating_a, rating_b)
        expected_score_b = self.calculate_expected_score(rating_b, rating_a)
        
        if outcome == 1:
            actual_score_a = 1
            actual_score_b = 0
        elif outcome == -1:
            actual_score_a = 0
            actual_score_b = 1
        else:
            actual_score_a = 0.5
            actual_score_b = 0.5
        
        updated_rating_a = rating_a + self.k_factor * (actual_score_a - expected_score_a)
        updated_rating_b = rating_b + self.k_factor * (actual_score_b - expected_score_b)
        
        return updated_rating_a, updated_rating_b

# Example usage:
tinder_elo = TinderEloAlgorithm()

# Sample ratings for two users
user_a_rating = 1500
user_b_rating = 1400

# Simulating user A winning against user B
updated_a_rating, updated_b_rating = tinder_elo.update_ratings(user_a_rating, user_b_rating, 1)

print(f"Updated User A rating: {updated_a_rating}")
print(f"Updated User B rating: {updated_b_rating}")
