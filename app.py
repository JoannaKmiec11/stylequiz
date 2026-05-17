import os
from flask import Flask, session, request, render_template, url_for, redirect
from seed_data.questions import questions
from seed_data.styles import styles


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/question/', methods=["GET", "POST"]) 
@app.route('/question/<number>', methods=["GET", "POST"])
def question(number=1):
    if request.method == "POST":
        session[number] = questions[int(number)][request.form["answer"]]
        if int(number) >= len(questions):
            return redirect(url_for('result'))
        return redirect(url_for("question", number=(int(number) +1)))
    else:
        answers = questions[int(number)]
        return render_template('question.html', number=number, answers=answers)

@app.route('/result/', methods=["GET"])
def result():
    results = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }

    # calculate the score 
    for i in range(len(questions)):
        style = session.get(str(i+1), None)
        if style:
            results[style] += 1
    
    session.clear()

    comm_styles = [max(results, key=lambda x:results[x])]

    top_style = comm_styles[0]
    for key in results.keys():
        if key == top_style:
            continue
        if results[key] == results[top_style]:
            comm_styles.append(key)

    if len(comm_styles) == 1:
        return render_template("your_style.html", style=styles[comm_styles[0]])
    if len(comm_styles) >1:
        return render_template('your_styles.html', styles=[ styles[style] for style in comm_styles ])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")