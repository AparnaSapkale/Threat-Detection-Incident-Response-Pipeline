from services.constants import *

def calculate_severity(event_history):

    if (
        "BRUTE_FORCE" in event_history
        and
        "SCAN" in event_history
    ):
        return HIGH

    if len(event_history) >= 3:
        return CRITICAL

    return MEDIUM


def map_attack_tactic(attack_type):

    mapping = {

        BRUTE_FORCE: CREDENTIAL_ACCESS,

        NETWORK_SCAN: RECON,

        REVERSE_SHELL: EXECUTION
    }

    return mapping.get(attack_type, "Unknown")