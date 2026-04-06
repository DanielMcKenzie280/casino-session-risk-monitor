def calculate_risk_level(score: int) -> str:
    """
    Convert numeric score into a human-readable risk level.
    """
    if score >= 75:
        return "critical"
    if score >= 50:
        return "high"
    if score >= 25:
        return "medium"
    return "low"


def build_recommendation(risk_level: str) -> str:
    """
    Return a basic recommendation for the given risk level.
    """
    recommendations = {
        "low": "no action needed",
        "medium": "monitor session activity",
        "high": "manual review suggested",
        "critical": "immediate review recommended",
    }
    return recommendations.get(risk_level, "monitor session activity")
