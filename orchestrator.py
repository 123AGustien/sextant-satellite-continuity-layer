# Sextant Resilience Simulation Framework
# Orchestrator (Root Execution Controller)

from cascade_engine import evaluate_state
from response_engine import execute_response
from satellite_model import apply_constraint


def run_system(state):
    """
    Executes full deterministic pipeline:
    Cascade → Response → Satellite
    """

    # STEP 1: Decision Layer
    decision = evaluate_state(state)

    # STEP 2: Execution Layer
    response = execute_response(decision)

    # STEP 3: Communication Constraint Layer
    final_state = apply_constraint(response)

    return {
        "input_state": state,
        "cascade_decision": decision,
        "response_state": response,
        "final_state": final_state
    }


if __name__ == "__main__":

    # Deterministic test input
    test_state = {
        "latency": 320,
        "node_failure_count": 1,
        "network_status": "DEGRADED"
    }

    result = run_system(test_state)

    print("\n=== SEXTANT SIMULATION OUTPUT ===")
    for key, value in result.items():
        print(f"{key}: {value}")
