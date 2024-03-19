resource "aws_eks_addon" "csi_driver" {
  cluster_name             = aws_eks_cluster.ist.name
  addon_name               = "aws-ebs-csi-driver"
  addon_version            = "v1.16.0-eksbuild.1"
  service_account_role_arn = aws_iam_role.eks_ebs_csi_driver.arn
}

resource "null_resource" "update_kubeconfig" {
  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --region us-east-1 --name ${aws_eks_cluster.ist.name}"
  }

  depends_on = [aws_eks_cluster.ist]
}
