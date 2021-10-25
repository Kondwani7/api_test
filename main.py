from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)
#store on a DB

#storing and calling data in memory
'''
names = {
    "Jane":{"age":20,"gender":"female"},
    "Kondwani":{"age":21, "gender":"male"},
    "Taonga":{"age":23, "gender":"female"}
}
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
'''
#parse through requests
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="the video\'s name is missing", required=True)
video_put_args.add_argument("views", type=int, help="the video\'s views is missing", required=True)
video_put_args.add_argument("likes", type=int, help="the video\'s likes is missing", required=True)

videos = {}
#validate request
def end_if_video_id_not_found(video_id):
    if video_id not in videos:
        abort(404, message="video_id not found")

def end_if_video_id_found(video_id):
    abort(409, message="video already exists")

class Video(Resource):
    #get data
    def get(self, video_id):
        end_if_video_id_not_found(video_id)
        return videos[video_id]
    #modify data received
    def put(self, video_id):
        #parse through all the desired data arguments
    
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    #delete data
    def delete(self, video_id):
        end_if_video_id_not_found(video_id)
        del videos[video_id]
        return '', 204

#add a resource to the api
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)