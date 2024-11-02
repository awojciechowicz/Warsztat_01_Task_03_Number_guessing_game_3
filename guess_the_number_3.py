from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    Imagine number between 0 and 1000! <br>
    <form method="GET" action="/guessing">
        <input type="submit" value="Go!">
    """
    return html

@app.route('/guessing', methods=['GET', 'POST'])
def guessing():
    if request.method == "GET":
        guess = 500
        html = f"""
        I'm guessing: {guess}
        <form method="POST" action="/guessing">
            <input type="submit" name="user_answer" value="Too low">
            <input type="submit" name="user_answer" value="Too high">
            <input type="submit" name="user_answer" value="You won">
            <input type="hidden" name="max" value="1000">
            <input type="hidden" name="min" value="0">
            <input type="hidden" name="guess" value="{guess}">
        </form>
        """
    else:
        min = int(request.form.get('min'))
        max = int(request.form.get("max"))
        user_answer = request.form.get('user_answer')
        guess = int(request.form.get('guess'))
        if user_answer == "Too low":
            min = guess
        elif user_answer == "Too high":
            max = guess
        else:
            html = f"""
            I guess! Your number is {guess}! <br>
            """
            return html

        guess = int((max - min) / 2) + min
        html = f"""
        I'm guessing: {guess}
        <form method="POST" action="/guessing">
            <input type="submit" name="user_answer" value="Too low">
            <input type="submit" name="user_answer" value="Too high">
            <input type="submit" name="user_answer" value="You won">
            <input type="hidden" name="max" value={max}>
            <input type="hidden" name="min" value={min}>
            <input type="hidden" name="guess" value="{guess}">
        </form>
        """

    return html

if __name__ == '__main__':
    app.run(debug=True)
