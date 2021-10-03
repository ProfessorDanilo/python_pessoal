from vpython import *


#QUARTA PARTE
scene2 = canvas(width=500, height=400, center=vector(-0.6,1,0))



#PRIMEIRA PARTE
#equação do mhs:
#v=Acos(wt+q)
#A é a amplitude
#w é a velocidade de fase
#q é a fase inicial
#setamos então as grandezas:
A=1
w=2*pi
q=0
t=0
v=-w*A*sin(w*t+q)
dt=0.01 #aqui escolhemos o delta t para calcular o delta s

massa=box(pos=vector(A,0.25,0),size=vector(0.5,0.5,0.5), color=vector(0,0,1))


#TERCEIRA PARTE:
chao=box(pos=vector(-A/2,-0.05,0),size=vector(4*A,0.1,1.5), color=vector(1,0.75,0.45))
parede=box(pos=vector(-2.5*A-0.05,0.4,0),size=vector(0.1,1,1.5), color=vector(1,0.75,0.45))



#QUINTA PARTE
mola=helix(pos=vector(-2.5*A,0.25,0),axis=vector(4*A,0.25,0), radius=0.1, thickness=0.05 )



#SEXTA PARTE
text(text='+A', align='center', color=color.green, height=0.5, pos=vector(A,1,0) )
curve(vector(+A,0.9,0), vector(+A,0.5,0), color=color.green)
curve(vector(+A,0,0), vector(+A,-0.5,0), color=color.green)
text(text='-A', align='center', color=color.green, height=0.5, pos=vector(-A,1,0) )
curve(vector(-A,0.9,0), vector(-A,0.5,0), color=color.green)
curve(vector(-A,0,0), vector(-A,-0.5,0), color=color.green)
text(text='0', align='center', color=color.green, height=0.5, pos=vector(0,-1,0) )
curve(vector(0,0,0), vector(0,-0.5,0), color=color.green)
curve(vector(0,0.75,0), vector(0,0.5,0), color=color.green)



#SEGUNA PARTE
while(True):
    rate(20)
    t=t+dt
    v=-w*A*sin(w*t+q)
    ds=dt*v
    massa.pos=massa.pos+vector(ds,0,0)

    #QUINTA PARTE
    mola.axis=massa.pos+vector(2.25*A,-0.25,0)




    
    
    
