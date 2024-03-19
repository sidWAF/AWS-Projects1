resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.ist.id

  tags = {
    Name = "igw"
  }
}
