import time

class SiteScheduler:
    def __init__(self, site_pingers, sleep_duration=1):
        self.site_pingers = site_pingers
        self.sleep_duration = sleep_duration
        
    def run(self, iterations=10):
        for _ in range(iterations):
            for pinger in self.site_pingers:
                pinger.run_ping()
            time.sleep(self.sleep_duration)
        