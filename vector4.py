class Vector:
    def __init__(self, x ='0,0', y = 0):
        if type(x)==str:
            s=x.split(',')
            self.x = float(s[0])
            self.y = float(s[1])
        else:
            self.x = float(x)
            self.y = float(y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y
N=int(input())
s=[[0]*2 for i in range(N)]
for i in range(N):
    s[i]= list(map(float, input().split()))
a=Vector(s[0][0], s[0][1])
b=Vector(s[1][0], s[1][1])
c=Vector(s[2][0], s[2][1])
m=((a-b)*(a-b))**0.5+((c-b)*(c-b))**0.5+((a-c)*(a-c))**0.5
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and i!=k and j!=k:
                a=Vector(s[i][0], s[i][1])
                b=Vector(s[j][0], s[j][1])
                c=Vector(s[k][0], s[k][1])
                l=((a-b)*(a-b))**0.5+((c-b)*(c-b))**0.5+((a-c)*(a-c))**0.5
                if l>m:
                    m=l
print(m)