import time

REQUEST_LOG = {}
LIMIT = 30
WINDOW = 60

def check_rate_limit(ip):
    now = time.time()
    REQUEST_LOG.setdefault(ip, [])

    REQUEST_LOG[ip] = [t for t in REQUEST_LOG[ip] if now - t < WINDOW]

    if len(REQUEST_LOG[ip]) >= LIMIT:
        return False

    REQUEST_LOG[ip].append(now)
    return True