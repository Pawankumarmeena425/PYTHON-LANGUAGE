def deco_result(func):  # now result function pass as a argument in the deco_result
    def distinction(marks):
        for m in marks:
            if m>=75:
                print(m,"Distinction")
        else:
            func(marks)
    
    return distinction

@deco_result
def result (marks):
    for m in marks:
        if m>=33:
            pass
        else: 
            print("Fail")
            break
    else:
        print("pass")


marks = [23,35,67,98,67]

result(marks)