variable "environment" {
    default = "prod"
    type = string
    description = "setup the environment"
  
}

variable "project_name" {
    default = "data-cancer"
    description = "data-cancer"
  
}

variable "bucket_names" {
    type = list(string)
    default = ["landing","processing","curated"]
  
}