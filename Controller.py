import view

def Start():
    while True:
        oper = view.Operation()
        if oper == 1:
            view.PrintDirrectory()
        if oper == 2:
            view.AddDirectiry()
        if oper == 3:
            view.PrintName()
        if oper == 4:
            view.SortName()
        if oper == 5:
            view.SortId()
        if oper == 6:
            break