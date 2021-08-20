output "public_subnet_arn" {
  description = "Public subnet ARN"
  value       = aws_subnet.public_subnets.*.arn
}

output "private_subnet_arn" {
  description = "Private subnet ARN"
  value       = aws_subnet.private_subnets.*.arn
}

output "alb_hostname" {
  description = "The public dns to access to the application"
  value = aws_alb.main_alb.dns_name
}

output "bucket_id" {
  value       = aws_s3_bucket.ops_hire_app_bucket.id
  description = "Bucket Name (aka ID)"
}

# Don't print these values
output "access_key_id" {
  value       = aws_iam_access_key.iam_s3_access.id
  description = "The access key ID"
}

output "secret_access_key" {
  sensitive   = true
  value       = aws_iam_access_key.iam_s3_access.secret
  description = "The secret access key. This will be written to the state file in plain-text"
}