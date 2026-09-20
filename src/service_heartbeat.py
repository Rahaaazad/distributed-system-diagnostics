from src.heartbeat_monitor import evaluate_heartbeat


class ServiceHeartbeat:
    def __init__(self, service_name: str, last_seen_at: float):
        if not service_name.strip():
            raise ValueError("Service name cannot be empty.")

        self.service_name = service_name
        self.last_seen_at = last_seen_at

    def age_at(self, current_time: float) -> float:
        return current_time - self.last_seen_at

    def status_at(self, current_time: float):
        age = self.age_at(current_time)
        return evaluate_heartbeat(age)