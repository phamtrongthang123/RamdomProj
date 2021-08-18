class Kernel:
    def __init__(self): self.globals, self.locals = {},{}
    def __call__(self,code):
        try: c = compile(code, 'kernel', 'eval')
        except SyntaxError: c = compile(code, 'kernel', 'exec')
        return eval(c, self.globals, self.locals)


k = Kernel()
k('def return_15(): return 15')
k('a = 2')
k('a +=2')
k('a += return_15()')
print(k('a'))