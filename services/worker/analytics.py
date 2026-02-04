import math

def compute_metrics(event):
    val = len(str(event))
    return math.sqrt(val * 1000)
