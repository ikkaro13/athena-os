# Athena Domain Model

## Purpose

This document defines the core business entities of Athena OS.

The objective is to describe the domain before implementing the software.

---

# Core Entities

## Match

Represents a football match.

Responsibilities:

- Date
- Competition
- Home Team
- Away Team
- Match Status

---

## Team

Represents a football club or national team.

Responsibilities:

- Name
- Country
- Rating
- Current Form

---

## Player

Represents an individual player.

Responsibilities:

- Position
- Statistics
- Availability
- Performance Metrics

---

## Market

Represents a betting market.

Examples:

- 1X2
- Over / Under
- BTTS
- Corners
- Cards

---

## Prediction

Represents Athena's prediction.

Responsibilities:

- Probability
- Confidence
- Expected Value
- Explanation
- Recommended Market

---

# Philosophy

Athena models football first.

Predictions are generated from football knowledge.

Not the opposite.