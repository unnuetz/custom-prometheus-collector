import random
random.uniform(0, 1)
import metrics
class Core:
    def checker():
        #
        #here i want to clear/delete all existing metrics i added in the last cycle
        #
        print("collection data ...")
        print(random.random())
        metrics.PortsGauge.labels(target=random.random(), target_name="test-target").set(random.random())
