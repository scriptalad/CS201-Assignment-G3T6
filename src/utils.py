from contextlib import contextmanager
import time
import tracemalloc
import psutil
import os

@contextmanager
def measure_time():
    """
    Usage:
      with measure_time() as t:
          ... work ...
      elapsed = t()
    """
    start = time.perf_counter()
    yield lambda: time.perf_counter() - start

@contextmanager
def measure_memory():
    """
    Tracks Python heap (tracemalloc) and process RSS delta (psutil).
    Usage:
      with measure_memory() as m:
          ... work ...
      stats = m()  # dict with tracemalloc_current, tracemalloc_peak, rss_delta
    """
    tracemalloc.start()
    proc = psutil.Process(os.getpid())
    rss_before = proc.memory_info().rss
    try:
        yield lambda: {
            "tracemalloc_current": tracemalloc.get_traced_memory()[0],
            "tracemalloc_peak": tracemalloc.get_traced_memory()[1],
            "rss_delta": psutil.Process(os.getpid()).memory_info().rss - rss_before,
        }
    finally:
        tracemalloc.stop()
