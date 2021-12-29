#!/usr/bin/env python
# coding: utf-8

# # Problema 1

# In[9]:


def func(n):
    if n==4:
        return n
    else:
        return 2*func(n+1)


# In[7]:


func(2)


#  # Problema 2

# In[10]:


def f(x,y):
    if x==0:
        return y
    return f(x-1,x+y) 


# In[11]:


f(4,3)


# # Problema 3

# In[12]:


def g(n):
    if n==0 or n==1:
        return n
    if n%3!=0:
        return 0
    return g(n/3)


# In[21]:


g(27)


# In[14]:


g(7)


# In[15]:


g(9)


# In[16]:


g(3)


# In[17]:


g(8)


# # Problema 6

# In[469]:


import itertools

def valida(cadena):
    pila=[]
    llaves={'{':'}'}
    for c in cadena:
        if c in llaves:
            pila.append(c)
        elif len(pila)==0 or c!=llaves[pila.pop()]:
            return False
    return len(pila)==0

def ParentesisBalanceados(n):
    base=""
    for i in range(n):
        base+="{" 
    for i in range(n):
        base+="}"      
    permutaciones=list(set(itertools.permutations(base)))
    h=[]
    for i in range(len(permutaciones)):
        if permutaciones[i][0]=="{" and permutaciones[i][-1]=="}":
            h.append(permutaciones[i])
    l=[]
    for e in set(h):
        if valida(e)==True:
            l.append(e)
    for i in range(len(l)):
        parentesis=""
        for j in range(2*n):
            parentesis=parentesis+l[i][j]
        print(parentesis)


# In[494]:


ParentesisBalanceados(6)


# # Problema 7

# In[464]:


import itertools 

def NSubstring(c,n): 
    potencia=[]
    for i in range(len(c)):
        potencia=potencia+list(itertools.combinations(c,i+1))
    flat=[]
    for e in potencia:
        crc=""
        for i in range(len(e)):
            crc=crc+e[i]
        flat.append(crc)
    lista=list(flat)
    lista.sort()
    cadena=""
    for e in lista:
        cadena = cadena + e
    contador=[]
    for e in lista:
        j=0
        for i in range(len(e)):
            contador.append(e[j])
            j+=1
    print("La cadena ordenada es: " + cadena)
    print("La letra en la posición_ " +  str(n)  + " es: " + contador[n-1])


# In[467]:


NSubstring('hnabd',15)


# # Problema 8 

# In[487]:


def SuperDigit(cifra, veces):
    numero=""
    for j in range(veces):
        numero = numero + str(cifra)
    if len(numero)==1:
        print(n)
    else:
        while len(numero)!=1:
            sum=0
            for i in range(len(numero)):
                sum=sum + int(numero[i])
            numero=str(sum)
        return int(numero)            


# In[493]:


SuperDigit(148,3)


# In[1]:


def max_num(a, b):

c=1s

return max(a,b)+c


# In[ ]:




