# Sextant Satellite Model
# Communication Constraint Simulation Layer

def apply_constraint(response_state):
    """
    Simulates communication degradation constraints.
    """

    if response_state == "RECOVERY_MODE":
        return "SATELLITE_MODE_ACTIVE"

    if response_state == "DEGRADED_OPERATION":
        return "HIGH_LATENCY_LINK"

    return "TERRESTRIAL_STABLE"
