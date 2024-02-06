from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

# GET
# (1) 전체 게시글 불러오는 API
@app.route('/api/v1/feeds/', methods=['GET'])
def show_all_feeds():
    data = {
        'result': 'success', 'data': {'feeds1': 'data1', 'feeds2': 'data2'}
    }
    return data

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {
       'result':'success', 'data': {'feeds1': 'data1'}
    }
    return data


# POST
# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds/', methods=['POST'])
def create_one_feed():
    # name = request.form.get('name')
    name = request.form['name']

    # age = request.form.get('age')
    age = request.form['age']
    print(name, age)

    return jsonify({'result':'success', 'data': {'name': name, 'age': age}})

datas = [{"items": [{"name": "item1", "price": 10}]}]
@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {'datas': datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    req = request.get_json()
    new_data = {'items': req.get('items', [])}
    datas.append(new_data)

    return new_data, 201
