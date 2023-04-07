totalNumberOfCranes = int(input("Введите общее количество журавликов сделанных Петей, Катей и Сережей: "))
if totalNumberOfCranes % 3 == 0 and totalNumberOfCranes % 2 == 0:
     kate = (totalNumberOfCranes // 3) *2 
     pit = serj = (totalNumberOfCranes - kate) // 2
     print(f"Катя сделала {kate}, Петя сделал {pit}, Сережа сделал {serj}")
else:
     print('Введено не верное значение общего количества журавлей')