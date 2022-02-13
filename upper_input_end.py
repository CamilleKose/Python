def upper_input_end():
    var = input("Enter a sentence: ")
    print(var[0:-1] + var[-1].upper())


upper_input_end()