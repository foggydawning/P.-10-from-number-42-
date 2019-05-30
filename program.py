def add_max(list=[],m_n=1):
    max = input("Введите 'stop' или элемент массива: ")
    if max=="stop":
        print("Вы не ввели ни одного элемента в массив!")
        return("ERROR")
    else:
        max=int(max)
        list.append(max)
        number = input("Введите 'stop' или элемент массива: ")
        while number!="stop":
            number=int(number)
            list.append(int(number))
            if number == max:
                m_n+=1
            if number > max:
                max=number
                m_n=1
            
            number = input("Введите 'stop' или элемент массива: ")
        else:
            print()
            print("Максимальное значение =", max)
            print("Количество элементов =", m_n)
            return list
    
add_max()
