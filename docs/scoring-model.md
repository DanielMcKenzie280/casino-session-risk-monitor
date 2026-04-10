# Scoring Model

This project uses a simple rule-based risk scoring approach.

## Core idea

Each suspicious behavioral pattern adds a certain number of points to the total risk score.

The more abnormal the session looks, the higher the final score.

## Rule examples

### rapid_deposit_pattern
Triggered when the player makes 4 or more deposits in a single session.

Score impact: **+18**

### unusual_bet_spike
Triggered when the maximum bet is at least 10x higher than the average bet.

Score impact: **+20**

### extended_session_duration
Triggered when the session lasts at least 120 minutes.

Score impact:
- 120-179 min → **+10**
- 180+ min → **+15**

### high_loss_chasing_behavior
Triggered when the player has a significant negative session result and continues depositing.

Score impact: **+20**

### bonus_abuse_suspected
Triggered when a bonus is used, multiple deposits exist, and the number of rounds is relatively low.

Score impact: **+15**

### multiple_small_withdrawals
Triggered when the player makes at least 3 withdrawals and all of them are small.

Score impact: **+10**

### payment_method_switching
Triggered when multiple payment methods are used in one session.

Score impact:
- 2 methods → **+5**
- 3+ methods → **+12**

## Risk level mapping

- 0-24 → low
- 25-49 → medium
- 50-74 → high
- 75+ → critical

## Notes

This model is intentionally simple and educational.
It should not be used as a production fraud or compliance engine without:
- historical player context
- jurisdiction-specific controls
- transaction timestamps
- behavioral baselines
- manual review workflows
