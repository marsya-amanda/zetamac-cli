import random, time

def generate_problem() -> tuple[str, float]:
    random.seed()
    ops = ('+', '-', '*', '/')
    range = [1, 99]
    x = random.randint(range[0], range[1])
    y = random.randint(range[0], range[1])
    op = random.choice(ops)

    if op == '+':
        question = f"{x} + {y} = "
        answer = x + y
    elif op == '-':
        question = f"{x} - {y} = "
        answer = x - y
    elif op == '*':
        question = f"{x} * {y} = "
        answer = x * y
    elif op == '/':
        z = x * y
        question = f"{x} / {z} = "
        answer = y

    return question, answer

if __name__ == "__main__":
    print("Press q to quit. Starting now...")
    inp = ""
    score = 0

    time_limit = 2 * 60 + time.time()
    while inp != "q" and time.time() < time_limit:
        question, answer = generate_problem()
        print(question)
        inp = input("")
        if inp == "q":
            quit()
        if int(inp) == answer: score += 1

    print("Score: ", score)