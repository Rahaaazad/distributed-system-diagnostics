from src.service_heartbeat import ServiceHeartbeat


def test_heartbeat_age_is_calculated():
    heartbeat = ServiceHeartbeat("camera", 100.0)

    result = heartbeat.age_at(103.0)

    assert result == 3.0

def test_heartbeat_status_is_degraded():
    heartbeat = ServiceHeartbeat("camera", 100.0)

    result = heartbeat.status_at(103.0)

    assert result.value == "degraded"