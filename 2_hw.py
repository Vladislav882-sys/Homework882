def task_1() -> None:
    a: int = 11567
    b: float = 1.25625625
    c: str = "Первое задание"
    d: list = [1, 2, 3]
    e: bool = True

    print(type(a)), print(type(b)), print(type(c)), print(type(d)), print(type(e))
    
task_1()

def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3])

task_2()
#*последовательность фибоначчи

def task_3(num: int) -> int:
    return num ** 2

print(task_3(5))
