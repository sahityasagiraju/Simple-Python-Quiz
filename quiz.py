print("Welcome to our Quiz")
print("RULES OF THE QUIZ :\n You will get 2 attempts per question , if you get it right in the first try you will be awarded with 2 points and 1 point if you get in the second try .")
count=0
question1 = "Who is president of USA?"
options1 = "a.Boris Johnson\nb. Nancy Pelosi\nc. Donald Trump\nd. Barack Obama\n"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

    if response == "c":
        count+=2
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "c":
                count+=1
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

while True:
    bonus = input("Would you like to proceed to the second question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who is the defence minister of India?")
        print("a.Rajnath Singh\nb.Narasimha Roa\nc.Jaswanth Singh\nd.Pranabh Mukerjee\n")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "a":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "a":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the third question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("What is SRK's first movie")
        print("a.Kal Ho Na Ho\nb.Diwana \nc.DDLJ \nd.Happy New Year")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "b":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "b":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the fourth question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Which is the smallest country based on landmass?")
        print("a.Italy\nb.Iran\nc.Iraq\nd.Vatican city")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "d":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "d":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the fifth question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("What is the currency of Japan")
        print("a.rupee\nb.Dollar\nc.Pound\nd.Yen")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "d":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "d":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the sixth question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Which is the most populated state in India?")
        print("a.Andhra Pradesh\nb.UP \nc.Bihar \nd.Orissa")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "b":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "b":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the seventh question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who is the first woman president of India?")
        print("a.Indira Gandhi\nb.Sonia Gandhi\n.c.Priyanka Gandhi\nd.Pratibha Patil")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "d":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "d":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the eigth question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who won the first mens cricket world cup?")
        print("a.India\nb.West Inidies\nc.Austrlia\nd.England")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "b":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "b":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to proceed to the ninth question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("How many gold medals did Indian hockey team win in olympics?")
        print("a.5\nb.6\nc.8\nd.7")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "c":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "c":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
while True:
    bonus = input("Would you like to answer the final question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who is the first women chief minister of India?")
        print("a.Sucheta Kripalani\nb.Sharmila Reddy \nc.Nandhini Satpathy \nd.Mayawathi")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "a":
                count+=2
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "a":
                    count+=1
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")
print("YOUR TOTAL SCORE IS:",count,"/20")
print("THANK YOU")
