def evaluate_rules(session: dict) -> tuple[list, int]:
    """
    Apply rule-based checks to a player session.
    Returns:
        (flags, score)
    """
    flags = []
    score = 0

    deposits = session.get("deposits", [])
    withdrawals = session.get("withdrawals", [])
    duration_minutes = session.get("duration_minutes", 0)
    avg_bet = session.get("avg_bet", 0)
    max_bet = session.get("max_bet", 0)
    bonus_used = session.get("bonus_used", False)
    rounds_played = session.get("rounds_played", 0)
    net_result = session.get("net_result", 0)
    payment_methods_used = session.get("payment_methods_used", 1)

    # Rapid deposit pattern
    if len(deposits) >= 4:
        flags.append("rapid_deposit_pattern")
        score += 18

    # Unusual bet spike
    if avg_bet > 0 and max_bet >= avg_bet * 10:
        flags.append("unusual_bet_spike")
        score += 20

    # Extended session duration
    if duration_minutes >= 180:
        flags.append("extended_session_duration")
        score += 15
    elif duration_minutes >= 120:
        flags.append("extended_session_duration")
        score += 10

    # High loss chasing behavior
    if net_result <= -300 and len(deposits) >= 3:
        flags.append("high_loss_chasing_behavior")
        score += 20

    # Bonus abuse suspicion
    if bonus_used and len(deposits) >= 3 and rounds_played < 150:
        flags.append("bonus_abuse_suspected")
        score += 15

    # Multiple small withdrawals
    if len(withdrawals) >= 3 and all(w <= 25 for w in withdrawals):
        flags.append("multiple_small_withdrawals")
        score += 10

    # Payment method switching
    if payment_methods_used >= 3:
        flags.append("payment_method_switching")
        score += 12
    elif payment_methods_used == 2:
        score += 5

    return flags, min(score, 100)
