from pythonping import ping
from SitePingMetrics import SitePingMetrics

PING_TIMEOUT=4
PING_COUNT=9
UNACCEPTABLE_PING_MS=30.0
PING_ITERATIONS=10
SLEEP_LENGTH=10.0
PING_THRESHOLD=3


class SitePinger():
    def __init__(self, site_addr):
        self.site_addr = site_addr
        self.ping_timeout = PING_TIMEOUT
        self.ping_count = PING_COUNT
        self.ping_threshold_ms = UNACCEPTABLE_PING_MS
        self.sleep_length_sec = SLEEP_LENGTH
        
    def get_site(self):
        return self.site_addr
    
    def capture_ping_metrics(self):
        return ping(self.site_addr, timeout=self.ping_timeout, count=self.ping_count)
    
    def num_long_pings(self, responses):
        num_long_png = 0
        for response in responses:
            if response.time_elapsed_ms > self.ping_threshold_ms:
                num_long_png += 1
        return num_long_png  
    
    def analyize_ping_metrics(self, responses):
        metrics = SitePingMetrics()
        max_ping = responses.rtt_max_ms
        num_long_responses = self.num_long_pings(responses)
        print("The max ping for {} was {} ms and the number of pings over {} was {}".format(self.site_addr, max_ping, self.ping_threshold_ms, num_long_responses))
        return metrics
        
    def run_ping(self):
        responses = self.capture_ping_metrics()
        metrics = self.analyize_ping_metrics(responses)
        