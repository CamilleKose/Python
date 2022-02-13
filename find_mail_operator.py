#find_mail_operator
var = input("give me your mail: ")
result1 = var.split("@")
result2 = result1[1].split(".")
print(result2[0])