get_ip ()
{
  echo "$CliqrTier_Centos_IP">>/tmp/private.txt
  private_ip=$(</tmp/private.txt)
}

install()
{
  python /tmp/csr1kv_acl_nat.py $private_ip
}
