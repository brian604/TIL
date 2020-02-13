import music_crawler as musicing
import flask

## 서버 시작
app = flask.Flask('음악 순위 서버')


@app.route('/')
def home():
    return flask.render_template('homework.html')


@app.route('/music', methods=['POST'])
def post_music():
    return "POST music"


@app.route('/music/naver', methods=['GET'])  # method GET은 default
def music_naver():
    try:
        c = flask.request.args['count']  # URL 늘리기 http://127.0.0.1:5000/music/naver?count=__&info=___
    except:
        c = 5
    # print(flask.request.args['info'])
    data = musicing.get_song_naver(int(c))
    return flask.jsonify(data)



# 서버 끝

app.run(port=5000, debug=True)  # 디버깅 모드. 뭔가 수정되었을때 알아서 재가동

# command+alt + l --> reformatting


# print('1')
# a= get_song_naver(3)
# print(a)

# DB에 저장
