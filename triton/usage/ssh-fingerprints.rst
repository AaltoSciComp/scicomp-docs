Triton ssh key fingerprints
===========================

ssh key fingerprints allow you to verify the server you are connecting
to.  The usual security model is that once you connect once, you save
the key and can *always* be sure you are connecting to the same server
from then on.  To be smarter, you can actually verify the keys the
first time you connect - thus, they are provided below.

Here are the SSH key fingerprints for Triton::

  256 SHA256:04Wt813WFsYjZ7KiAyo3u6RiGBelq1R19oJd2GXIAho no comment (ECDSA)
  256 SHA256:1Mj2Gpf6iinwni/Yf9g/b/wToaUaOU87szzzCtibj6I no comment (ED25519)
  2048 SHA256:glizQJUQKoGcN2aTtp9JtXuJjJtnrKxRD8yImE06RJQ no comment (RSA)

and the same but with md5 hashes::

  256 MD5:ac:61:86:86:e1:11:29:f5:46:23:d8:25:00:8a:7b:f0 no comment (ECDSA)
  256 MD5:1d:e7:c9:f6:92:a1:c0:65:10:97:d7:72:7d:4c:82:5a no comment (ED25519)
  2048 MD5:a4:73:89:ae:8c:a5:ea:2a:04:76:cc:0b:6a:f7:e6:9a no comment (RSA)

Or this can be copied and pasted directly into your
``.ssh/authorized_keys`` file::

  triton.aalto.fi ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk8MvTSB2gYZf9Y969vhMczdGSO+rNGZQhZLUGMkMduq4q+b/LpHCn/yH1JN8NWeIDt8NELdnl+/0hmk/zk7IHxtnPvNbZuAYO1T1Hh7Kk72zQFOESHqmbYcPH5SDf12XfNYJ6cQIqHRaF4QT483+f9fvUlp7E+MKQlr3+NreKm4AHdTcHjqW75r1Mh/z0q9Qoqdgn3gDCzmN6+Y0aGyf4wICMJlKUBQP0muqSfYWX43StaPh+hoOQFYOiK1jOVEBY/HFXOuDzgCCG2b9qWhTrA3svcSKK4E6X76sXOR+8FTbC7u9xnLgm+903+zsGfsEQY2eNXfR7YChNxz4y5ASf
  triton.aalto.fi ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAZvw6Bgs+cPGFjwqMABAGC+cG2bBYR69+Hc5ChxQhwNwCW1zCg6w/pAerbr+A6IzJDx8uN03bcTZj+xzLH2kLE=
  triton.aalto.fi ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDumqy+fbEwTOtyVlPGqzS/k4i/hJ8L+kUDf6MpWO1OI
