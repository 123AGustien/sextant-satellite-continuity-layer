# Sextant Resilience Simulation Framework
# Deterministic System Test Suite

from orchestrator import run_system


def test_case_1():
    return run_system({
        "latency": 100,
        "node_failure_count": 0,
        "network_status": "STABLE"
    })


def test_case_2():
    return run_system({
        "latency": 350,
        "node_failure_count": 1,
        "network_status": "DEGRADED"
    })


def test_case_3():
    return run_system({
        "latency": 500,
        "node_failure_count": 3,
        "network_status": "CRITICAL"
    })


def run_all_tests():
    print("\n=== SEXTANT DETERMINISTIC TEST SUITE ===\n")

    tests = [
        ("CASE 1 - NORMAL SYSTEM", test_case_1),
        ("CASE 2 - DEGRADED LATENCY", test_case_2),
        ("CASE 3 - FAILURE STATE", test_case_3),
    ]

    for name, test in tests:
        print(f"\n--- {name} ---")
        result = test()

        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    run_all_tests()
