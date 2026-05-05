# Sextant Resilience Simulation Framework
# Orchestrator - Execution Pipeline Controller

from cascade_engine import evaluate_state
from response_engine import execute_response
from satellite_model import apply_constraint


def run_system(state):
    """
    Executes full deterministic pipeline:
    Cascade → Response → Satellite
    """

    # Step 1: Cascade (Decision Layer)
    decision = evaluate_state(state)

    # Step 2: Response (Execution Layer)
    response = execute_response(decision)

    # Step 3: Satellite (Communication Constraint Layer)
    final_output = apply_constraint(response)

    return {
        "input_state": state,
        "cascade_decision": decision,
        "response_state": response,
        "final_state": final_output
    }


if __name__ == "__main__":

    # Example deterministic input
    test_state = {
        "latency": 320,
        "node_failure_count": 1,
        "network_status": "DEGRADED"
    }

    result = run_system(test_state)

    print("\n=== SEXTANT SIMULATION OUTPUT ===")
    for k, v in result.items():
        print(f"{k}: {v}")
