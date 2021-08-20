# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api, request
import os
import boto3

app = Flask(__name__)
api = Api(app)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "")


class HelloWorld(Resource):
    def index(self):
        return {
            "hello": "world",
        }

    def resources(self):
        s3_client = boto3.client("s3")

        filename = request.args.get("filename")

        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": AWS_BUCKET_NAME, "Key": filename},
            ExpiresIn=300,
        )

        return {"temporal_url": url}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
