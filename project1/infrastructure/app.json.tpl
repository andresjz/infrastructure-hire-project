[
  {
    "cpu": ${fargate_cpu
    },
    "image": "${app_image}",
    "memory": ${fargate_memory
    },
    "name": "app",
    "networkMode": "awsvpc",
    "portMappings": [
      {
        "containerPort": ${app_port
        },
        "hostPort": ${app_port
        }
      }
    ],
    "environment": [
      {
        "name": "AWS_ACCESS_KEY_ID",
        "value": "${app_access_key_id}"
      },
      {
        "name": "AWS_SECRET_ACCESS_KEY",
        "value": "${app_access_secret_key}"
      },
      {
        "name": "AWS_DEFAULT_REGION",
        "value": "${app_default_region}"
      },
      {
        "name": "AWS_BUCKET_NAME",
        "value": "${app_bucket_name}"
      }
    ]
  }
]