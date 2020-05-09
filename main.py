from time import sleep
from check import Core
from prometheus_client import start_http_server, Info, CollectorRegistry

def setup_prometheus():
    announce = Info('check_error_status',
                     'useless help')
    registry = CollectorRegistry()
    registry.register(announce)

if __name__ == "__main__":
    """
    Main function
    """
    setup_prometheus()

    try:
        start_http_server(9100, addr='0.0.0.0')

        while True:
            print("-----------------------Start Query------------------------")
            Core.checker()
            sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)
