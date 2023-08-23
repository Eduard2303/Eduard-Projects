def skrivUt(tekst1,tekst2,tall1):
    print(tekst1) 
    print(tekst2," ", tall1)

antallOppgaver = 4 
t1="Melding til alle programmerere: "
t2="Antall oppgaver igjen: "
t3="Hvor mange nye oppgaver får vi: "
t4="Vi har fått flere oppgaver. Antall oppgaver er nå: "

1 skrivUt(t1,t2,antallOppgaver)

2 antallNyeOppgaver = int(input(t3)) 	
antallOppgaver = antallOppgaver + antallNyeOppgaver
3 skrivUt(t1,t2,antallOppgaver) 

if antallOppgaver > 10:
4    print("Det er mer enn 10 oppgaver igjen.") 
elif antallOppgaver == 10:
    print("Det er 10 oppgaver igjen.") 	
else:
    print("Det er mindre enn 10 oppgaver igjen")
