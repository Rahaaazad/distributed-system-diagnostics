from src.health_status import HealthStatus


def evaluate_heartbeat(
    age_seconds: float,
    degraded_after: float = 2.0,
    unhealthy_after: float = 5.0,
) -> HealthStatus:
    if age_seconds < 0:
        raise ValueError("Heartbeat age cannot be negative.")

    if degraded_after >= unhealthy_after:
        raise ValueError(
            "Degraded threshold must be lower than unhealthy threshold."
        )

    if age_seconds >= unhealthy_after:
        return HealthStatus.UNHEALTHY

    if age_seconds >= degraded_after:
        return HealthStatus.DEGRADED

    return HealthStatus.HEALTHY