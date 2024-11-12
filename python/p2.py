c1 = input("Metni gir: ")
b = list(c1)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = []

for char in b:
    if char in a:
        
        current_index = a.index(char)        
        yeni_index = (current_index - 3) % len(a)
        d = a[yeni_index]
        c.append(d)
        
print(c)        
        
