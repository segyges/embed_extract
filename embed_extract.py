from transformers import AutoModelForCausalLM
import torch
import os

with open("todo.txt", "r") as file:
    todos = file.read().splitlines()

with open("done.txt", "r") as file:
    dones = set(file.read().splitlines())

for todo in todos:
    if todo in dones:
        continue
    name, step = todo.split(" ")
    model = AutoModelForCausalLM.from_pretrained(name, revision=step)
    embedding = model.gpt_neox.embed_in
    folder = "embeds/" + name.split("/")[1]
    if not os.path.exists(folder):
        os.makedirs(folder)
    torch.save(embedding, f"./{folder}/{step}.pth")
    with open("done.txt", "a") as file:
        file.write(todo + "\n")
