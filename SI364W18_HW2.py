## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import requests
import json

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

class AlbumEntryForm(FlaskForm):
	album_name = StringField('Enter the name of an album:', validators=[Required()])
	rating = StringField('How much do you like this album? (1 low, 3 high)', validators=[Required()])
	submit = SubmitField("Submit")


####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)


@app.route('/artistform')
def artist():
	return render_template("artistform.html")


@app.route('/artistinfo')
def artistinfo():
    baseurl = 'https://itunes.apple.com/search?'
    params = {"term": request.args['artist']}
    r = requests.get(baseurl, params = params)
    results_dict = json.loads(r.text)
    return render_template("artist_info.html", objects = results_dict['results'])


@app.route('/artistlinks')
def artistlinks():
	return render_template("artist_links.html")


@app.route('/specific/song/<artist_name>')
def song(artist_name):
    baseurl = 'https://itunes.apple.com/search?'
    params = {"term": artist_name}
    r = requests.get(baseurl, params = params)
    results_dict = json.loads(r.text)
    return render_template("specific_artist.html", results = results_dict['results'])


# @app.route('/album_entry')
# def album():
#     simpleForm = AlbumEntryForm()
#     return render_template("album_entry.html", form=simpleForm)


# @app.route('/album_result', methods = ['GET', 'POST'])
# def result():
#     form = AlbumEntryForm(request.form)
#     if request.method == 'POST' and form.validate_on_submit():
#         name = form.album_name.data
#         age = form.rating.data
#         return "The album title you just submitted was: {0}\n\n On a scale of 1 to 3, you would give it {1} stars!".format(album_name, rating)
#     flash('All fields are required!')
#     return redirect(url_for('album')))


if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
