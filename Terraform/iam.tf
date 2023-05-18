 data "aws_partition" "current" {}

 resource "aws_iam_role" "glue_job" {
   name               = "${var.project_name}-glue-job-role"
   path               = "/"
   description        = "Provides write permissions to CloudWatch Logs and S3 Full Access"
   assume_role_policy = file("permissions/role_glueJobs.json")
 }

 resource "aws_iam_policy" "glue_job_policy" {
   name        = "${var.project_name}-glue-job-policy"
   path        = "/"
   description = "Provides write permissions to CloudWatch Logs and S3 Full Access"
   policy      = file("permissions/policy_glueJobs.json")
 }

 resource "aws_iam_role_policy_attachment" "glue_job1" {
   role       = aws_iam_role.glue_job.name
   policy_arn = aws_iam_policy.glue_job_policy.arn
 }



