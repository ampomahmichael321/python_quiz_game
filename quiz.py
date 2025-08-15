from questions import questions
import cowsay 
import random
import csv

score = 0
attempts = 0



def main():
    playable = 5#The number of questions or games they can play
    while True:
        #Ask the user whether they want to play the game
        response = input("Welcome to the quiz game. Enter Y to start the game or N if you don't want to play: ").strip()

        #If they want to play, Start the game
        if response.upper() == "Y":
            while True:
                random.shuffle(questions)#Shuffle the questions
                question = random.choice(questions)#Select a question at random

                if not question["used"] and playable >0:#Check if the question hasnt been used and the user hasnt played 5 games
                    play_game(question)
                    playable -=1 #reduce number of questions left
                    question["used"] = True #mark the question as used

                elif question["used"]:#If question has been used, skip it
                    continue

                elif playable == 0:#If user has exhausted all five questioins, break out of the loop
                    print("\n")
                    print("End of Game")
                    name = input("What is your name? ").strip()#Ask for the user"s name
                    if not name == "":
                        display_score(name,score)
                        update_leaderboard(name,score)
                        display_leaderboard()
                        break
            break#This breaks out of the outer while loop
        elif response.upper() == "N":
            cowsay.cow("I'm sad you don't want to play this time. Guess I will see you next time")
            break
        else:
            print("The only valid inputs are 'N' and 'Y'")
        
def play_game(question):
#Print the question and options
    print("\n")
    print(question["question"])
    print(f"A. {question["A"]}")
    print(f"B. {question["B"]}")
    print(f"C. {question["C"]}")
    print(f"D. {question["D"]}")
    

#Check if an answer is correct
    while True:
        try:
            user_ans = input("Enter your Answer:").strip()#Takes away unwanted white spaces
            user_ans = user_ans.upper()
            if question[user_ans] == question["ans"]:
                print("correct Answer")
                global score
                score += 1
                break
            else:
                print("Wrong Answer")
                break
        except KeyError:
            print(f"{user_ans} is not a valid option")
            global attempts
            if attempts < 3:
                attempts +=1
                continue
            else:
                print("Maximum attempts reached")
                break
    

def display_score(name, score):
    if score <= 3:
        cowsay.cow(f"Oh poor {name}! your score is {score}/5")
    elif score > 3:
        cowsay.tux(f"You did awesome {name}! your score is {score}/5")

def update_leaderboard(name, score):
    fieldnames = ["name","score"]
    with open("leaderboard.csv", mode="a") as file: #Open the csv file in append mode so that it doesn't create a whole new file each time
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"name":name, "score":score})#Add new name and score to the csv file

def display_leaderboard():
    players = []
    with open("leaderboard.csv") as file:#open the csv file, default mode is read
        reader = csv.DictReader(file)
        for row in reader:
            player = {
                "name": row["name"],
                "score": row["score"]
            }
            players.append(player) #Add the player to the players list
        print("\t\t***LEADERBOARD***")
        for player in sorted(players, key= lambda p:  p["score"], reverse= True):#sort based on the score in descending order
            print(f"Name: {player['name']} \t\t\t\t Score: {player['score']}")




if __name__ == "__main__":
    main()

