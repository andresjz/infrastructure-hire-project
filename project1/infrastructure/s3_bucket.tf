resource "aws_s3_bucket" "ops_hire_app_bucket" {
  bucket = "ops-hire-app-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }
}
