# app.py - a minimal flask api using flask_restful
from flask import Flask, request, Response
from flask_restful import Resource, Api
import os
import boto3
import socket

app = Flask(__name__)
api = Api(app)

AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "")

class HelloWorld(Resource):
    def get(self):
        return {
            "hello": "world"
        }

class S3Resource(Resource):
    def get(self):
        s3_client = boto3.client("s3")

        filename = request.args.get('filename')

        file = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key=filename)
        return Response(
        file['Body'].read(),
        mimetype=file['ContentType'],
        headers={"Content-Disposition": "attachment;filename="+filename}
    )

class S3SignedUrl(Resource):
    def get(self):
        s3_client = boto3.client("s3")

        filename = request.args.get('filename')

        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": AWS_BUCKET_NAME, "Key": filename},
            ExpiresIn=300,
        )

        return {"signed_url": url}

class HostName(Resource):
    def get(self):
        return {
            "hostname": socket.gethostname()
        }


api.add_resource(HelloWorld, "/")
api.add_resource(S3Resource, "/resource")
api.add_resource(S3SignedUrl, "/signed-url")
api.add_resource(HostName, "/hostname")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
