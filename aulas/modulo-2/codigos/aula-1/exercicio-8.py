linguagens = {"Python", "Java", "C++", "Javascript"}

linguagens.add("Rust")
# linguagens.remove("Java")

# if "Python" in linguagens:
#     print("Python está na lista de linguagens")

outros = {"C", "Python", "Go"}

print(linguagens | outros)
print(linguagens & outros)
print(linguagens - outros)
print(outros - linguagens)