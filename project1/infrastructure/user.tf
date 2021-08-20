resource "aws_iam_user" "app_user" {
  name          = "ops-hire-app-user"
  force_destroy = true
}

resource "aws_iam_access_key" "iam_s3_access" {
  user    = aws_iam_user.app_user.name
}

resource "aws_iam_user_policy" "app_policy" {
  name = "ops-hire-app-user"
  user = aws_iam_user.app_user.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:Get*",
        "s3:List*",
        "s3:HeadBucket"
      ],
      "Effect": "Allow",
      "Resource": "${aws_s3_bucket.ops_hire_app_bucket.arn}/*"
    }
  ]
}
EOF
}


output "access_key_id" {
  value       = aws_iam_access_key.iam_s3_access.id
  description = "The access key ID"
}

output "secret_access_key" {
  sensitive   = true
  value       = aws_iam_access_key.iam_s3_access.secret
  description = "The secret access key. This will be written to the state file in plain-text"
}