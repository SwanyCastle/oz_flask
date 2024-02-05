from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # data = {
    #     'title': 'Flask Jinja Template',
    #     'user': 'seunghwan',
    #     'is_admin': True,
    #     'item_list': ['itme1', 'item2', 'itme3']
    # }

    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]

    # parameter1 = rendering 할 html 파일 명입력
    # parameter2 = html 로 넘겨줄 데이터 입력
    return render_template('index.html', data=users)

if __name__ == "__main__":
    app.run(debug=True)