from SitePinger import SitePinger
from SiteScheduler import SiteScheduler

google_site = SitePinger("www.google.com")
amazon_site = SitePinger("www.amazon.com")
sites = [google_site, amazon_site]
scheduler = SiteScheduler(sites)
scheduler.run()