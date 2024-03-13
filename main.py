import time
import threading
import asyncio
from multiprocessing import Process


def calc_average(num: iter) -> float:
    """Average function used for sequential programming, threading and multiprocessing"""
    sum_num = 0
    for t in num:
        sum_num += t
    avg = sum_num / len(num)
    time.sleep(1)
    return avg


def main_sequential(list_1: iter, list_2: iter, list_3: iter) -> None:
    """Main wrapper for sequential example"""
    s = time.perf_counter()

    # TODO: complete this part

    elapsed = time.perf_counter() - s
    print(f"Sequential programming Elapsed Time: {elapsed} seconds")


async def calc_average_async(num: iter) -> float:
    """Average function used for asynchronous programming only (needs await asyncio.sleep())"""
    sum_num = 0
    for t in num:
        sum_num += t
    avg = sum_num / len(num)
    await asyncio.sleep(1)
    return avg


async def main_async(list_1: iter, list_2: iter, list_3: iter) -> None:
    """Main wrapper for asynchronous example"""
    s = time.perf_counter()

    # TODO: complete this part

    elapsed = time.perf_counter() - s
    print(f"Asynchronous programming Elapsed Time: {elapsed} seconds")


async def main_threading(list_1: iter, list_2: iter, list_3: iter) -> None:
    """Main wrapper for threading example"""
    s = time.perf_counter()

    # TODO: complete this part

    elapsed = time.perf_counter() - s
    print(f"Threading programming Elapsed Time: {elapsed} seconds")


async def main_multiprocessing(list_1: iter, list_2: iter, list_3: iter) -> None:
    """Main wrapper for threading example"""
    s = time.perf_counter()

    # TODO: complete this part

    elapsed = time.perf_counter() - s
    print(f"Multiprocessing Elapsed Time: {elapsed} seconds")


if __name__ == "__main__":  # Need to use this if-statement so multiprocessing don't cause an infinite loop
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [2, 4, 6, 8, 10]
    l3 = [1, 3, 5, 7, 9, 11]
    main_sequential(l1, l2, l3)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async(l1, l2, l3))
    main_threading(l1, l2, l3)
    main_multiprocessing(l1, l2, l3)
