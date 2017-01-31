###formation energy###
import numpy as np
import math
import matplotlib.pyplot as plt

####define some useful parameters:
#U1, the valence band maximum, 0 eV
#U2, the band gap energy, for 3C-SiC is 2.4 eV
#E1, the total energy of system with charged defect
#E2, the total energy of pristine system
#e, the Fermi level, for 3C-SiC is about 8 eV
#c, the chemical potential for atoms
#q, the charge state
    
Tot_defect_q=[-814.80491972,-813.01410858,-811.2992635,-809.5074766,-808.2079037,-804.67988922]
Tot_perfect=-844.75659091
u=[0,3.787]
e=1.600064
c=[-11.232,-19.476,-17.385,-11.232,-15.123]
def formation_energy(Tot_defect,Tot_perfect,u,e,c):
    E1=Tot_defect
    E2=Tot_perfect
    E_VBM=e
    Fermi=u
    chem=c
    q=input('the charge state of this defect:')         #0 is 0 charge state, 1 is +1, 2 is +2
    i=input('the Fermi level is:')                      #0 is VBM, 1 is CBM
    j=input('the chemcial condition is:')               #0 is O-rich, 1 is O-poor
    m=input('the extra electron or hole level close to CBM:')
    Ef=E1[q]-E2+c[j]-q*(Fermi[i]+e)+m*(Eexp-u[1])
    return Ef
Formation_energy=formation_energy(Tot_defect_q,Tot_perfect,u,e,c)
print Formation_energy
