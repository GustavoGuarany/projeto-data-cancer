terraform {
  backend "s3" {
    # Edit the bucket name and region
    bucket         = "data-platform-stack2-terraform-backend"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"

    dynamodb_table = "terraform-locks"
    encrypt = true

  }
}