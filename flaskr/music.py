from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,  render_template_string
)
from werkzeug.exceptions import abort
import pandas as pd


from flaskr.db import get_db

bp = Blueprint('music', __name__)


@bp.route('/')
def urls():
    return f'''
        <html>
    <body>

    <h2>ДЗ 3. Flask, SQLite</h2>
    <p>1. Вью функция должна выводить количество уникальных исполнителей (artist) из таблицы tracks.
    PATH: /names/</p>
    <a href="{url_for("music.names")}">names</a><br>
    <p>2. Вью функция должна выводить количество записей из таблицы tracks.
    PATH: /tracks/</p>
    <a href="{url_for("music.tracks")}">tracks</a><br>
    <p>3. Вью функция должна принимать название жанра трека и выводить количество записей этого    
    жанра (genre) из таблицы tracks. PATH: /tracks/genre </p>
    <a href="{url_for("music.tracks_genre")}">genre</a><br>
    <p>4. Вью функция должна выводить все названия треков (title) и соответствующую продолжительность 
    трека в секундах(length) из таблицы tracks. PATH: /tracks-sec/</p>
    # <a href="{url_for("music.tracks_sec")}">tracks_sec</a><br>
    <p>5. Вью функция должна выводить среднюю продолжительность трека и общую продолжительность всех 
    треков в секундах из таблицы tracks.
    PATH: /tracks-sec/statistics/</p>
    <a href="{url_for("music.tracks_sec_statistics")}">statistics</a><br>
    </body>
    </html>
    '''

@bp.route('/names/')
def names():
    db = get_db()
    posts = db.execute(
        "SELECT COUNT (DISTINCT artist) FROM tracks"
    ).fetchall()
    return f'Количество уникальных исполнителей (artist):&nbsp;{posts}'

@bp.route('/tracks/')
def tracks():
    db = get_db()
    max_list = db.execute(
        "SELECT id FROM tracks WHERE id = (SELECT MAX(id) FROM tracks)"
    ).fetchall()
    return f'Количество записей из таблицы tracks:&nbsp; {max_list}'


@bp.route('/tracks/genre/', methods=['GET', 'POST'])
def tracks_genre():
    if request.method == 'POST':
        pass
    else:

        db = get_db()
        list_genre = db.execute(
            "SELECT DISTINCT genre FROM tracks"
        ).fetchall()
        list_genre_new = []


        for i in list_genre:
            i=str(i)
            i = i.replace("'",'').replace('(','').replace(',','').replace(')','')
            list_genre_new.append(i)

        return render_template('list_genre.html', option=list_genre_new)
#         return render_template_string('''
# <html>
#         <form>
#             <p><input type="search" list="character">
#             <datalist id="character">
#                 <select name="genre" method="GET">
#                   {% for opt in option %}
#                     <option value="{{ opt }}"> SELECTED>{{opt}}</option>
#                   {% endfor %}
#                 </select>
#
#
#             </datalist>
#             <input type="button" value="Кнопка" onClick='location.href="/new/"'>
#         </form>
#
# </html>
#
# ''', option=list_genre)



@bp.route('/tracks/genre/result/', methods=['GET', 'POST'])
def result():

    if request.method == 'POST':
        print(request.form.get('genre_input'))
        genre_input=request.form.get('genre_input')
        db = get_db()
        quant_genre = db.execute(
            f"""SELECT COUNT(*) FROM tracks WHERE genre='{genre_input}';"""
        ).fetchall()
        print(quant_genre)

    else:
        pass
    return f'{genre_input}={quant_genre}'





@bp.route('/tracks-sec/', methods=['GET', 'POST'])
def tracks_sec():

    if request.method == 'GET':
        db = get_db()
        df = pd.read_sql("select lenght,title from tracks", db)
        records = df.to_dict("records")
        return records
    else:
        return "post"

@bp.route('/tracks-sec/statistics/', methods=['GET', 'POST'])
def tracks_sec_statistics():

    if request.method == 'GET':
        db = get_db()
        len_tracks = db.execute(
            "SELECT SUM(lenght) FROM  tracks"
        ).fetchall()
        len_tracks=[int((str(i)).replace(',', '').replace('(','').replace(')','')) for i in len_tracks]
        print(len_tracks)
        avg_tracks =db.execute(
            "SELECT AVG(lenght) FROM  tracks"
        ).fetchall()
        avg_tracks=[float((str(i)).replace(',', '').replace('(','').replace(')','')) for i in avg_tracks]
        print(avg_tracks)
        # maxx = len(max_list)
        return f'''
        <p>Средняя продолжительность трека: {avg_tracks}</p>
        <p>Общая продолжительность всех треков в секундах: {len_tracks}</p>
                '''
    else:
        return "post"
