import sys

from flask import Flask, render_template, request

from main import REPLACES, modify

app = Flask(__name__)


def int_or_default(n, default=0):
    try:
        return int(n)
    except ValueError:
        return default


@app.route('/', methods=['POST', 'GET'])
def page_index():
    if request.method == 'GET':
        return render_template(
            'index.html',
            dot_chance=REPLACES['.'].chance,
            space_chance=REPLACES[' '].chance,
            quest_mark_chance=REPLACES['?'].chance,
            excl_mark_chance=REPLACES['!'].chance,
            comma_chance=REPLACES[','].chance,
        )
    else:
        text = modify(
            request.form['text'],
            {
                '.': int_or_default(request.form['dot_chance'], REPLACES['.'].chance),
                ',': int_or_default(request.form['comma_chance'], REPLACES[','].chance),
                ' ': int_or_default(request.form['space_chance'], REPLACES[' '].chance),
                '!': int_or_default(request.form['excl_mark_chance'], REPLACES['!'].chance),
                '?': int_or_default(request.form['quest_mark_chance'], REPLACES['?'].chance)
            }
        ).replace('\n', '<br/>').replace(' ', '&nbsp;')
        return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run('0.0.0.0', 8045)