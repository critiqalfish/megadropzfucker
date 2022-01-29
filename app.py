import flask
import waitress
import megadropzfucker
import sqlite3
import time

app = flask.Flask(__name__)

db = sqlite3.connect('database.db', check_same_thread=False)
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS links (
                ilink text,
                olink text
            )""")
cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS xlink ON links (olink)")
db.commit()

avg_time = [0]

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        if flask.request.form.get('submit') == 'SUBMIT':
            ilink = flask.request.form['submit_link']
            with db:
                cursor.execute("SELECT olink FROM links WHERE ilink=?", (ilink,))
                dlinks = cursor.fetchall()
            if dlinks == []:
                try:
                    tb = int(time.time())
                    olinks = megadropzfucker.link(ilink)
                    timed = int(time.time()) - tb
                    if len(avg_time) <= 10:
                        avg_time.append(timed)
                    else:
                        avg_time.pop(0)
                        avg_time.append(timed)
                    for link in olinks:
                        cursor.execute("INSERT OR IGNORE INTO links VALUES (?, ?)", (ilink, link))
                    db.commit()
                    print('PULLED FROM NET AND ADDED TO DB: ', olinks)
                except megadropzfucker.Error as e:
                    print('[ERROR]: ', e)
                    return flask.render_template('error.html', error=e)
            else:
                olinks = []
                for link in dlinks:
                    olinks.append(link[0])
                print('PULLED FROM DB: ', olinks)
            return flask.render_template('result.html', links=olinks)
        elif flask.request.form.get('credits') == 'CREDITS':
            return flask.render_template('credits.html')
        elif flask.request.form.get('back') == 'BACK':
            return flask.render_template('index.html', avgt=sum(avg_time) / len(avg_time))
    elif flask.request.method == 'GET':
        return flask.render_template('index.html', avgt=sum(avg_time) / len(avg_time))

if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
    #waitress.serve(app, host='0.0.0.0', port=7997)