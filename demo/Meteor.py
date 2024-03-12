
Arms=0;
HENDLE=210;
pipe=100;
FC=125;
Maj=2000;
CC=6;
CS=695;

Arms5=925;
Arms6=1000;
Arms7=1100;
Arms8=1650;
Arms9=1750;
Arms10=1850;

Gear1=650;
Gear2=900;
Gear3=1125;

jointer=175;

wc=200;

HorcelPl=220;
HorcelPt=240;


def length():

    length=float(input("Enter Length OF Awning :"));
    if length<9:
        print("Length should be greate then 9ft.");
    elif length<10:
        length=10;
    return length;
length=length();

def width():
    width=int(input("Enter Width of Awning :"));
    l=length-2;
    if width>l :
        print("Width should be less then ",l);
    return width;
width=width();  

def CenterSupport():
    cs=0;
    if length>15 and width>6 :
        cs=CS+(CS*18)/100+10;
    return cs;
CS=CenterSupport();

def FCC():
    FCT=length*(FC+(FC*18)/100+10);
    if length>18:
        FCT=FCT+jointer+(jointer*18)/100;
    return FCT;
FC=FCC();

def Arms():
    if width==5 and length<=15:
        Arms=Arms5+(Arms5*18)/100+10;
        Arms=Arms*2;
    elif width==5 and length<=18:
        Arms=Arms5+(Arms5*18)/100+10;
        Arms=Arms*3;
    elif width==5 and length<=25:
        Arms=Arms5+(Arms5*18)/100+10;
        Arms=Arms*4;
    elif width==5 and length<=30:
        Arms=Arms5+(Arms5*18)/100+10;
        Arms=Arms*5;
    elif width==6 and length<=15:
        Arms=Arms6+(Arms6*18)/100+10;
        Arms=Arms*2;
    elif width==6 and length<=19:
        Arms=Arms6+(Arms6*18)/100+10;
        Arms=Arms*3;
    elif width==6 and length<=27:
        Arms=Arms6+(Arms6*18)/100+10;
        Arms=Arms*4;
    elif width==6 and length<=30:
        Arms=Arms6+(Arms6*18)/100+10;
        Arms=Arms*5;
    elif width==7 and length<=15:
        Arms=Arms7+(Arms7*18)/100+10;
        Arms=Arms*2;
    elif width==7 and length<=20:
        Arms=Arms7+(Arms7*18)/100+10;
        Arms=Arms*3;
    elif width==7 and length<=27:
        Arms=Arms7+(Arms7*18)/100+10;
        Arms=Arms*4;
    elif width==7 and length<=30:
        Arms=Arms7+(Arms7*18)/100+10;
        Arms=Arms*5;
    elif width==8 and length<=16:
        Arms=Arms8+(Arms8*18)/100+10;
        Arms=Arms*2;
    elif width==8 and length<=21:
        Arms=Arms8+(Arms8*18)/100+10;
        Arms=Arms*3;
    elif width==8 and length<=28:
        Arms=Arms8+(Arms8*18)/100+10;
        Arms=Arms*4;
    elif width==8 and length<=30:
        Arms=850+(850*18)/100+10;
        Arms=Arms*5;
    elif width==9 and length<=16:
        Arms=Arms9+(Arms9*18)/100+10;
        Arms=Arms*2;
    elif width==9 and length<=22:
        Arms=Arms9+(Arms9*18)/100+10;
        Arms=Arms*3;
    elif width==9 and length<=28:
        Arms=Arms9+(Arms9*18)/100+10;
        Arms=Arms*4;
    elif width==9 and length<=30:
        Arms=Arms9+(Arms9*18)/100+10;
        Arms=Arms*5;
    elif width==10 and length<=16:
        Arms=Arms10+(Arms10*18)/100+10;
        Arms=Arms*2;
    elif width==10 and length<=23:
        Arms=Arms10+(Arms10*18)/100+10;
        Arms=Arms*3;
    elif width==10 and length<=30:
        Arms=850+(850*18)/100+10;
        Arms=Arms*4;
    return Arms;

        



def gear():
    if width<=5 and length<=15 or length<=12 and width<=7:
        GEAR=Gear1+(Gear1*18)/100+10;
    elif width>7 and length<=15:
        GEAR=Gear2+(Gear2*18)/100+10;
    elif width>7 and length>15:
        GEAR=Gear3+(Gear3*18)/100+10;
    else:
        GEAR=Gear3+(Gear3*18)/100+10;
    return GEAR;
Gear=gear();


plain=30;
patta=40;
FT=input("TYPE OF FABRIC Plain OR Patta:");
def febric():
    
    if FT=="Plain":
        febric=plain*(length*(width+2.3));
    elif FT=="Patta":
        febric=patta*(length*(width+2.3));
    return febric;
febric=febric();

def WallClam():
    if length<=12:
        WC=wc*2;
    elif length>12:
        WC=wc*(length/5);
    return WC;
wc=WallClam();

def FCJ():
    
    if length>18:
        J=jointer;
    else:
        J=0;
    return J;
jointer=FCJ();

pipe=pipe*length;

CC=CC*(length/2);

print("C-CLam =",CC);
print("PIPE=",pipe);
print("Gear=",Gear);
print("ARMS=",Arms());
print("Febric=",febric);
print("First Chanal=",FC)
print("Wall Clam=",wc);
print("Jointer =",jointer);

Total=Gear+pipe+Arms()+febric+CC+FC+Maj+jointer+HENDLE;
AvgC=Total/(length*(width+1));
# TWC=Gear+pipe+Arms()+febric+CC+FC+Maj+HENDLE+jointer+wc;
# AvgTWC=TWC/(length*(width+1));
print("Total=",Total);
print("Average Cost =",AvgC);
# print("Total with clamp =",TWC);
# print("Average Cost with clamp =",AvgTWC);
def Horcel():
    if FT=="Plain":
        Horcel=HorcelPl*(length*(width+1));
    elif FT=="Patta":
        Horcel=HorcelPt*(length*(width+1));
    return Horcel;

Profit=Horcel()-Total;
print("Horcel Cost =",Horcel());
print("Profit =",Profit);