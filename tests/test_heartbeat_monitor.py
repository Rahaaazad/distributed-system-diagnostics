import pytest

from src.health_status import HealthStatus
from src.heartbeat_monitor import evaluate_heartbeat


def test_recent_heartbeat_is_healthy() -> None:
    assert evaluate_heartbeat(1.0) is HealthStatus.HEALTHY


def test_degraded_boundary_is_degraded() -> None:
    assert evaluate_heartbeat(2.0) is HealthStatus.DEGRADED


def test_unhealthy_boundary_is_unhealthy() -> None:
    assert evaluate_heartbeat(5.0) is HealthStatus.UNHEALTHY


def test_negative_age_is_rejected() -> None:
    with pytest.raises(ValueError):
        evaluate_heartbeat(-1.0)


def test_invalid_thresholds_are_rejected() -> None:
    with pytest.raises(ValueError):
        evaluate_heartbeat(
            age_seconds=1.0,
            degraded_after=5.0,
            unhealthy_after=2.0,
        )