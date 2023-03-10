#Quiz Game
score = 0
print("""WELCOME TO MY QUIZ,
Press Enter to continue""")
print("""Rules:
-There is total 5 questions
-Each has 10 points and has negative points too:
-This questions are based on Computer hardware
- All are MCQ Based questions answer in A,B,C,D
------Enjoy""")
q1 = input("""

1)Which companies manufactures CPU's? :-
A) Amd and Intel
B) Samsung and Apple
C) Nokia and Vivo
D) None of above
""")
correcta = 'a'
correctb = 'b'
correctc = 'c'
correctd = 'd'
if q1 == correcta:
    print("Congrats,You are correct")
    score = score + 10
else:
    print("Better Luck next time,You are wrong ")
    if (score<=0):
        score = 0
    else:
        score = score - 10
print("Score : ",score)           
q2 = input("""

2)Which company manufactures Cpu die?
A) Amd and Intel
B) Samsung and TSMC
C) Nokia and Vivo
D) None of above""")
if q2 == correctb:
    print("Congrats,You are correct")
    score = score + 10
else:
    print("Better Luck next time,You are wrong ")
    if (score<=0):
        score = 0
    else:
        score = score - 10
print("Score : ",score)
q3 = input("""

3) What is the function of a GPU
A) Used for playing games
B) Uses its Tensor cores to earn money by cryptocurrency mining
C) Render pixels and send to the display
D) None of above
""")
if q3 == correctc:
    print("Congrats,You are correct")
    score = score + 10
    print(score,"is your score")
else:
    print("Better Luck next time,You are wrong ")
    if (score<=0):
        score = 0
    else:
        score = score - 10
print("Score : ",score)        
q4 = input('''

4) What is LGA chipset?
A) Cpu which has pins
B) Cpu which doesn't have pins
C) Motherboard has pins
D) B and C
''')
if q4 == correctd:
    print("Congrats,You are correct")
    score = score + 10
else:
    print("Better Luck next time,You are wrong ")
    if (score<=0):
        score = 0
    else:
        score = score - 10
print("Score : ",score)

    


