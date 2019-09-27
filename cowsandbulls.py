import random

def play(total_guesses=10):

    num_of_guesses = 0
    random_numbers = [int(i) for i in str(random.randrange(1000, 10000))]
    win = False
    while not win and num_of_guesses < total_guesses:
        answer = str(input("Please input 4 digits number: "))
        answer_list = [int(i) for i in answer]
        answer_set = set(answer_list)
        matches = []
        if len(answer_list) == 4:
            num_of_guesses += 1
            # check of game rules
            cow = 0
            bull = 0
            for i in range(4):
                # cow check
                if random_numbers[i] == answer_list[i]:
                    cow += 1
                    matches.append(answer_list[i])
                    if cow == 4:
                        win = True
                        print("You won")
                        break

            for j in answer_set:
                if j in random_numbers and j not in matches:
                    bull += 1

            if not win:
                print("%s cows, %s bulls" %(cow, bull))
                print("Correct answer", random_numbers)
        else:
            print("Choose 4 figures")

    if num_of_guesses == total_guesses:
        print("Lost, run out of total guesses")
    print("Number of guesses ", num_of_guesses)

play()
