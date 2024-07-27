def fibbo(n):
    if n <= 1:
        return n
    last = fibbo(n - 1) 
    slast = fibbo(n - 2)
    
    return last + slast


print(fibbo(3))
