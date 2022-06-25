import asyncio


test_list = [(3, 2, 'first'), (2, 2, 'second'), (3, 2, 'third'), (1, 2, 'fourth')]


test_line = [5, 3]


async def process(init) -> int:
    print(f'{init[2]}: start')

    await asyncio.sleep(init[0])

    new_number = init[1] + 3

    print(f'{init[2]}: finish ({new_number})')

    return (init[0], new_number, init[2])


async def red(res: tuple, new: int) -> tuple:
    return await process(res)


async def line_process(seconds: int, number: int, title: str) -> None:
    result = (seconds, number, title)
    for _ in test_line:
        result = await red(result, _)

    # res = await process(seconds, number, title)
    # await process(*res)


def main(loop):
    tasks = []

    tasks.append(loop.create_task(line_process(*test_list[0])))
    tasks.append(loop.create_task(line_process(*test_list[1])))
    tasks.append(loop.create_task(line_process(*test_list[2])))

    return asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(loop))
