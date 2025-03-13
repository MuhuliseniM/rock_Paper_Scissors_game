from flask import Flask, render_template, request
import random

app = Flask(__name__)
application = app

# Initialize scores
user_score = 0
computer_score = 0
tie_score = 0

# Game logic
def play_game(user_choice):
    global user_score, computer_score, tie_score

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie! 🤝"
        tie_score += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win! 🎉"
        user_score += 1
    else:
        result = "You lose! 😢"
        computer_score += 1

    return user_choice, computer_choice, result

@application.route('/', methods=['GET', 'POST'])
def index():
    global user_score, computer_score, tie_score
    
    if request.method == 'POST':
        user_choice = request.form['choice']
        user_choice, computer_choice, result = play_game(user_choice)
        return render_template('index.html', 
                               user=user_choice, 
                               computer=computer_choice, 
                               result=result, 
                               user_score=user_score, 
                               computer_score=computer_score, 
                               tie_score=tie_score)

    return render_template('index.html', 
                           user_score=user_score, 
                           computer_score=computer_score, 
                           tie_score=tie_score)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
