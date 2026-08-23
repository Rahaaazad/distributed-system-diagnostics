from src.health_status import HealthStatus, is_operational


def test_healthy_status_is_operational() -> None:
    result = is_operational(HealthStatus.HEALTHY)

    assert result is True


def test_degraded_status_is_operational() -> None:
    result = is_operational(HealthStatus.DEGRADED)

    assert result is True


def test_unhealthy_status_is_not_operational() -> None:
    result = is_operational(HealthStatus.UNHEALTHY)

    assert result is False