def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    p_not_a = 1 - p_a
    numerator = p_b_given_a * p_a
    denominator = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
    return numerator / denominator