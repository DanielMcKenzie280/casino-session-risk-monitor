# casino-session-risk-monitor

A lightweight Python tool for analyzing casino player session data and detecting risky behavioral patterns in iGaming environments.

This project demonstrates how session-level activity can be scored using simple rule-based logic to identify potentially problematic or suspicious behavior, such as:

- rapid deposit patterns
- unusual bet spikes
- extended session duration
- high loss chasing behavior
- bonus abuse indicators
- frequent payment behavior changes

It can be used for educational purposes, backend simulations, internal risk tooling prototypes, fraud detection experiments, or responsible gaming monitoring concepts.

## Why this project matters

In real iGaming platforms, player session monitoring is an important part of:

- fraud prevention
- bonus abuse detection
- payment risk review
- responsible gaming workflows
- manual compliance checks

This repository shows how a simple scoring model can be implemented without relying on heavy external systems.

## Features

- Rule-based risk scoring
- Clear risk flags for suspicious session behavior
- Human-readable recommendations
- JSON input support
- Simple CLI-friendly usage
- Easy to extend with custom rules

## Example input

```json
{
  "player_id": "P10293",
  "session_id": "S88912",
  "duration_minutes": 164,
  "deposits": [50, 50, 100, 200],
  "withdrawals": [20, 15],
  "avg_bet": 2.5,
  "max_bet": 40,
  "bonus_used": true,
  "rounds_played": 1380,
  "net_result": -320,
  "payment_methods_used": 2
}
