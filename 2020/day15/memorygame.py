def play_turns(turns, starting_numbers):
    numbers = []
    last_number = 0
    for i in range(turns):
        print('-' * 20, i)
        if i < len(starting_numbers):
            speak = starting_numbers[i]
            print(speak)
            numbers.append((speak, [i+1]))
        else:
            spoken, when = numbers[i-1]
            if len(when) == 1:
                speak = 0
                numbers.append((speak, [when, [i+1]]))
        last_number = speak
        print(last_number)
    return last_number
