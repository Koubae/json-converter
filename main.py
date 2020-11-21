from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
import jinja2
import converter
from converter.dict_sample import MyClass, inst_class
import os
from decimal import Decimal
from fractions import Fraction
from datetime import datetime, date


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)
app.config['ENV'] = 'production'

user_mode_display = None
user_theme_display = None


def first_call(app):

    with app.app_context():  
        session['is_data'] = False
        session['user_mode'] = 'JSON'
        session['theme'] = 'light'
        user_mode_display = session['user_mode']
        user_theme_display = session['theme']
    return 
    

APP_CACHE = []
APP_MODE = {'JSON', 'python'}


def serve_index():
    """ Index page helper checks whether the user's did add something to convertor and for possible error to display (i.e. incorrect data input) """

    if session['is_data'] and len(APP_CACHE):  
        return APP_CACHE.pop()

    elif len(APP_CACHE) and APP_CACHE[0] == 'err':
        msg = APP_CACHE.pop()
        token = APP_CACHE.pop()
        msg_token = [token, msg] 
        return msg_token
    return 

@app.route('/', methods=['GET', 'POST'])
def index():

    # Creates Default session's attr.
    if 'is_data' not in session:    
        first_call(app)

    user_mode_display = session['user_mode']
    user_theme_display = session.get('theme')
    
    session_result = serve_index()
    if session_result:
        return render_template('index.html', session_result=session_result, mode=user_mode_display, theme=user_theme_display)
    return render_template('index.html', mode=user_mode_display, theme=user_theme_display)

    


@app.route('/send-data', methods=['GET', 'POST'])
def get_data():

    error = None

    if request.method == 'POST':
    # 1 Check and gather any error when getting User's form request if failed, returns back to home page + err
        try:
            data = request.form['input']
            user_mode = request.form['user_mode']
            user_theme = request.form.get('theme', None)
        except Exception as err:
            print('==='*15 + '\n' + 'ERROR' + '\n' + '==='*15)
            print(err)
            error = err
            flash(err, 'error')
            print('==='*15 + '\n' + '!!!!!' + '\n' + '==='*15)
        finally:
            if error:
                    APP_CACHE.append('err')
                    APP_CACHE.append(error)
                    session['user_mode'] = user_mode
                    return redirect(url_for('index'))



    
        # If User toggled theme 'on' and request has Token, set user_theme to new theme
        if user_theme and user_theme != session.get('theme', None):
                session['theme'] = user_theme
        # If the on Token is not in the request, means that User has set theme back to light, Set session to light
        elif not user_theme and session.get('theme') == 'on':
            session['theme'] = 'light'

        # 2 Convert From JSON to Python Dict
        if user_mode in APP_MODE and user_mode == 'JSON':
            
            try:                     
                converted_data = converter.Decoder(data)
                assert isinstance(converted_data, dict)
            except (converter.JSONDecodeError, AssertionError) as err:
                print('==='*15 + '\n' + 'ERROR' + '\n' + '==='*15)
                print(err)
                error = err
                flash(f'{err}--Error while deserializing the JSON Object', 'error')
                print('==='*15 + '\n' + '!!!!!' + '\n' + '==='*15)
                
            else:
                
                session['user_mode'] = user_mode
                session['user_data'] = str(converted_data) # Convert to String to avoid werkzeug error
                session['is_data'] = True    
                APP_CACHE.append(converted_data) # The actual Dict Result will be stored here, then POPs out in /home
                
            finally:
                if error:
                    APP_CACHE.append('err')
                    APP_CACHE.append(error)
                session['user_mode'] = user_mode
                return redirect(url_for('index'))

        # TODO [1]
        # 3 Convert From Any data to String         
        elif user_mode in APP_MODE and user_mode == 'python':
        
            try:
                converted_json = converter.Encoder(data.strip())                
                assert isinstance(converted_json, str)                
            except ValueError as err:
                print('==='*15 + '\n' + 'ERROR' + '\n' + '==='*15)
                print(err)
                error = err
                flash('Error while serializing to JSON', 'error')
                print('==='*15 + '\n' + '!!!!!' + '\n' + '==='*15)
            else:
                session['user_data'] = str(converted_json)
                session['user_mode'] = user_mode
                session['is_data'] = True          
                APP_CACHE.append(converted_json) # The actual JSON Result will be stored here, then POPs out in /home
            finally:
                if error:
                    APP_CACHE.append('err')
                    APP_CACHE.append(error)
                session['user_mode'] = user_mode
                return redirect(url_for('index'))
        else:
            session['user_mode'] = user_mode
            user_mode_display = session['user_mode']
            return render_template('index.html', mode=user_mode_display)

 
if __name__ == '__main__':
    print(app.config)
    app.run(port=8000)



# [1] -- Be able to convert real Dict data to Python. 
# The issue encountered is that once the data (i.e a Python Dict) is passed Through the Website 
# To the Flask App, it becomes a String.
# As solutioin I see 3 different possible option:
# 1) Process the data in Broser side (JavaScript.)
# 2) Process the Sring in the Flask App using Python (maybe Serpy?)
# 3) Send the Data from Browser to Python but so that is easily deserialize to a Dict (using AJAX).
# 4) User can add a choosen Schema and is stored in the browser or Cached?