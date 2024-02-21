name = "EleutherAI/pythia-14m"
steps = [0] + [2**x for x in range(10)] + [x for x in range(1000, 143001, 1000)]

with open("todo.txt", "w") as file:
    for step in steps:
        file.write(
            f"{name} step{str(step)}\n"
        )
