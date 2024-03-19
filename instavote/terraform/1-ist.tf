resource "aws_vpc" "ist" {
  cidr_block = "10.30.0.0/16"

  tags = {
    Name = "ist"
  }
}

