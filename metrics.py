from prometheus_client import Gauge, Counter
PortsGauge = Gauge('check_error_status', 'help', ['target', 'target_name'])
