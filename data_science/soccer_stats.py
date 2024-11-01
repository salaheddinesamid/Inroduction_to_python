# soccer_stats.py

def scoring_probability(skill_level, defense_level):
    """
    Calculate the probability of scoring based on player's skill and opponent's defense.

    Parameters:
    skill_level (float): Skill level of the player (0 to 1 scale).
    defense_level (float): Defense level of the opponent (0 to 1 scale).

    Returns:
    float: Probability of scoring (0 to 1 scale).
    """
    if not (0 <= skill_level <= 1 and 0 <= defense_level <= 1):
        raise ValueError("Skill and defense levels must be between 0 and 1.")
    return skill_level * (1 - defense_level)
help(scoring_probability)