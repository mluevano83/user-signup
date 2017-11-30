from flask import Flask, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/", methods=['POST'])
def validate_form():
    un_input = request.form['username']
    pw_input = request.form['password']
    vfy_input = request.form['verify']
    em_input = request.form['email']
    un_error = ""
    pw_error = ""
    vfy_error = ""
    em_error = ""

    if not un_input:
        un_error = "Please enter a username, chum"
    else:
        if len(un_input) < 3 or len(un_input) > 20:
            un_input = ""
            un_error = "Username must be between 3 and 20 characters, my dude"
        else:
            for char in un_input:
                if char == " ":
                    un_input = ""
                    un_error = "Usernames cannot contain spaces, friendo"

    if not pw_input:
        pw_error = "Super-Please enter a password"
    elif len(pw_input) < 3 or len(pw_input) > 20:
        pw_input = ""
        pw_error = "Password must be between 3 and 20 characters, please"
    else:
        for char in pw_input:
            if char == " ":
                pw_input = ""
                pw_error = "Password cannot contain spaces, tho"

    if not vfy_input:
        vfy_error = "Please re-enter your password for verification reasons"
    elif vfy_input != pw_input:
        vfy_error = "Passwords do not match, yo"

    if em_input:
        a_count = em_input.count('@')
        p_count = em_input.count('.')
        char_count = len(em_input)
        if char_count < 3:
            em_error = "email must be at least 3 characters"
        if char_count > 20:
            em_error = "email must be less than 20 characters"
        if a_count != 1:
            em_error = "email must contain exaclty one @ symbol"
        if p_count != 1:
            em_error = "email must contain exactly one period"
        for char in em_input:
            if char == " ":
                em_input = ""
                em_error = "email cannot contain spaces, either"

    else:
        if not em_input:
            em_error = ""

    if not un_error and not pw_error and not vfy_error and not em_error:
        return render_template('welcome.html', un_input=un_input)
    else:
        return render_template('forms.html', un_error=un_error, pw_error=pw_error, vfy_error=vfy_error, em_error=em_error, un_input=un_input, em_input=em_input)

"""
    if len(em_input) < 3 or len(em_input) > 20
        em_input = ""
        em_error = "Email must be min 3 characters and max 20"

    if not em_input and not un_error and not pw_error and not vfy_error and not em_error:
        return render_template('welcome.html', un_input=un_input)
    else:
        return render_template('forms.html', un_error=un_error, pw_error=pw_error, vfy_error=vfy_error, em_error=em_error, un_input=un_input, em_input=em_input)

  
    else:
        for char in em_input:
            if char == " ":
                em_input = ""
                em_error = "Email cannot contain spaces, tho"
        else:
            if len(em_input) > 3 and len(em_input) < 20:
                if em_input.count('.') != 1:
                    em_input = ""
                    em_error = 'Email must contain exactly one period (".") character'
            else:
                if em_input.count('@') != 1:
                    em_input = ""
                    em_error = 'Email must contain exactly one "@" symbol'
        if not un_error and not pw_error and not vfy_error and not em_error:
            return render_template('welcome.html', un_input=un_input)
        else:
            return render_template('forms.html', un_error=un_error, pw_error=pw_error, vfy_error=vfy_error, em_error=em_error, un_input=un_input, em_input=em_input)
"""
app.run()
