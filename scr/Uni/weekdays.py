if __name__ == '__main__':
    weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    index = int(input())

    if index < 0 or index > len(weekdays):
        print("Index is out of bounds! Index must be between 0 and", len(weekdays)-1)
    else:
        print(weekdays[index])
