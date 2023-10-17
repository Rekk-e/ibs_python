import logging
import time

logging.basicConfig(level=logging.INFO)


def custom_lru_cache(max_calls: int = 3):
    """
    Allows you to cache the result of a function call
    and displays the execution time.

    max_calls  is responsible for how many times
               the called function will be executed again and the value
               in the cache will be updated, the default value for this argument is 3
    """

    def decorator(func):
        cache = {}
        counter = 0

        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.items())
            if key in cache:
                nonlocal counter
                counter += 1
                if counter <= max_calls:
                    logging.info("Return from cache")
                    return cache[args]
                else:
                    counter = 1

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logging.info(f"Execution time: {execution_time} seconds")

            cache[key] = result

            return result
        return wrapper
    return decorator



