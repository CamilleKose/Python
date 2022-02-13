var = input("give me your mail please: ")
result1 = var.split("@")
result2 = result1[1].split(".")
print(result2[0])