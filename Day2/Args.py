def args(*hi,**hello):
    for i in hi:
        print(i, end=" ")
    
    for i in hello:
        print("\n")
        print(hello[i])

args("hi","hi",me="hello")
