from multiprocessing import Pool
from analytics import compute_metrics

def run_cpu_tasks(batch):
    with Pool(4) as p:
        return p.map(compute_metrics, batch)
