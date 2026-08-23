from enum import Enum


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


def is_operational(status: HealthStatus) -> bool:
    return status in (
        HealthStatus.HEALTHY,
        HealthStatus.DEGRADED,
    )


if __name__ == "__main__":
    current_status = HealthStatus.HEALTHY

    print(f"Status: {current_status.value}")
    print(f"Operational: {is_operational(current_status)}")