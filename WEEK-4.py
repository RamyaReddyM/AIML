from sympy import symbols, Or, Not, Implies, satisfiable

#define the propositional variables
Rain=symbols('Rain')
Harry_Visited_Hagrid=symbols('Harry_Visited_Hagrid')
Harry_Visited_Dumbledore=symbols('Harry_Visited_Dumbledore')

#define the logical sentences
#Sentence 1: If it did not rain, Harry visited Hagrid
sentence_1 = Implies(Not(Rain), Harry_Visited_Hagrid)

#Sentence 2: Harry visited Hagrid or Dumbledore today, but not both
sentence_2 = Or(Harry_Visited_Hagrid, Harry_Visited_Dumbledore) & Not(Harry_Visited_Hagrid & Harry_Visited_Dumbledore)

#Sentence 3: Harry visited Dubmledore today
sentence_3 = Harry_Visited_Dumbledore

#combine all sentences into a single logical expression
knowledge_base = sentence_1 & sentence_2 & sentence_3

#Check for satisfiability to infer the truth value of Rain
solution = satisfiable(knowledge_base, all_models=True)

#Determine if it rained today based on the solution
for model in solution:
    if model[Rain]:
        print("It rained today.")
    else:
        print("It did not rain today.")





#C:\Users\student\AppData\Local\Programs\Python\Python39
#open cmd and command: python.exe -m pip install sympy
