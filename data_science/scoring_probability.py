from soccer_stats import scoring_probability
import logging
player_skill = 0.85
opponent_defense = 0.6
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(message)s")
logging.info("Calculating scoring probability")
probability = scoring_probability(player_skill, opponent_defense)

print(f"Player's probability of scoring: {probability:.2%}")