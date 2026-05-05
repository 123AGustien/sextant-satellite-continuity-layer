# Sextant Cascade Engine
# Decision Layer (Deterministic State Evaluation)

def evaluate_state(state):
    """
    Determines system decision based on input state.
    """

    if state.get("node_failure_count", 0) > 2:
        return "FAILOVER"

    if state.get("latency", 0) > 300:
        return "ESCALATE"

    if state.get("network_status") == "DEGRADED":
        return "ESCALATE"

    return "MONITOR"
