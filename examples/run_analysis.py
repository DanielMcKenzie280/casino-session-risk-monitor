from src.risk_monitor import analyze_session
from src.utils import load_json

session = load_json("data/sample-session.json")
result = analyze_session(session)

print(result)
