i = int(input("Ile przedniotów: "))
j = 0
subject = []
grade = []
while(j < i):
    subject.append(input("Przedniot: "))
    grade.append(input("Ocena: "))
    j += 1
j = 0
print("\nLista:")
while(j < i):
    print(subject[j], ":", grade[j])
    j +=  1

