from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=10)

def io_task(data):
    return data

def process_io_tasks(batch):
    futures = [executor.submit(io_task, item) for item in batch]
    return [f.result() for f in futures]
