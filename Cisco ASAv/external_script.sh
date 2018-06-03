get_ip ()
{
  echo "$CliqrTier_Centos_IP">>/tmp/private.txt
  private_ip=$(</tmp/private.txt)
  echp "CliqrTier_CentOS_PUBLIC_IP">>/tmp/public.txt
  public_ip=$(</tmp/public.txt)
}

install()
{
  python /tmp/asav_single_acl_aws.py $private_ip
}
