Triton ssh key fingerprints
===========================

ssh key fingerprints allow you to verify the server you are connecting
to.  The usual security model is that once you connect once, you save
the key and can *always* be sure you are connecting to the same server
from then on.  To be smarter, you can actually verify the keys the
first time you connect - thus, they are provided below.

You can verify SSH key fingerprints with a command like::

  ssh-keygen -l -E sha256 -f <(ssh-keyscan triton.aalto.fi 2>/dev/null)


Here are the SSH key fingerprints for Triton::

  256 SHA256:04Wt813WFsYjZ7KiAyo3u6RiGBelq1R19oJd2GXIAho no comment (ECDSA)
  256 SHA256:1Mj2Gpf6iinwni/Yf9g/b/wToaUaOU87szzzCtibj6I no comment (ED25519)
  2048 SHA256:glizQJUQKoGcN2aTtp9JtXuJjJtnrKxRD8yImE06RJQ no comment (RSA)

  # triton v3:
  3072 SHA256:3u8iICwjmvJ/+9YGxqqK+3r7FmrDflcgpoGl5ygtAWw login4.triton.aalto.fi (RSA)
  256 SHA256:OqCehC2lbHdl8mYGI/G9vlxTwew3H3KrvxKDkwIQy9Y login4.triton.aalto.fi (ECDSA)
  256 SHA256:ibL4dBsdrwRjbJCBWL1J5p/Sg4PGHWxTG6HF65yPcps login4.triton.aalto.fi (ED25519)


and the same but with md5 hashes::

  256 MD5:ac:61:86:86:e1:11:29:f5:46:23:d8:25:00:8a:7b:f0 no comment (ECDSA)
  256 MD5:1d:e7:c9:f6:92:a1:c0:65:10:97:d7:72:7d:4c:82:5a no comment (ED25519)
  2048 MD5:a4:73:89:ae:8c:a5:ea:2a:04:76:cc:0b:6a:f7:e6:9a no comment (RSA)

  # triton v3:
  3072 MD5:2e:54:9f:f8:05:0e:b6:75:3a:b6:d4:88:e9:ac:1c:18 login4.triton.aalto.fi (RSA)
  256 MD5:24:fc:03:f8:bc:20:ae:02:97:b4:3d:a1:97:44:f6:1f login4.triton.aalto.fi (ECDSA)
  256 MD5:d0:63:0e:2c:2b:8d:59:d9:37:88:53:3d:54:b3:4e:69 login4.triton.aalto.fi (ED25519)


Or this can be copied and pasted directly into your
``.ssh/known_hosts`` file::

  triton.aalto.fi ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk8MvTSB2gYZf9Y969vhMczdGSO+rNGZQhZLUGMkMduq4q+b/LpHCn/yH1JN8NWeIDt8NELdnl+/0hmk/zk7IHxtnPvNbZuAYO1T1Hh7Kk72zQFOESHqmbYcPH5SDf12XfNYJ6cQIqHRaF4QT483+f9fvUlp7E+MKQlr3+NreKm4AHdTcHjqW75r1Mh/z0q9Qoqdgn3gDCzmN6+Y0aGyf4wICMJlKUBQP0muqSfYWX43StaPh+hoOQFYOiK1jOVEBY/HFXOuDzgCCG2b9qWhTrA3svcSKK4E6X76sXOR+8FTbC7u9xnLgm+903+zsGfsEQY2eNXfR7YChNxz4y5ASf
  triton.aalto.fi ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAZvw6Bgs+cPGFjwqMABAGC+cG2bBYR69+Hc5ChxQhwNwCW1zCg6w/pAerbr+A6IzJDx8uN03bcTZj+xzLH2kLE=
  triton.aalto.fi ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDumqy+fbEwTOtyVlPGqzS/k4i/hJ8L+kUDf6MpWO1OI

  # triton v3
  login4.triton.aalto.fi ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCdoiR+g/NcJJ2MufNgZapo9x90KtK7SHTzlEscsCELwM8mVrcyB1bw4dVxl2V52p8NOyCCgNnsCMPsVHZ9xXGrmiULQQ7Caw/7zKG7LAgo3mh0HZ/5Vl9w+McMaEzP5ag4l7C3mOU38U+ZWXS2d+YBl3dFLikRSJFZdljLOmXPe0j3vRvBcPWz7i6ftgMd9CKkBsBxJW8GPWzBIIU3wkhGpGhJlIpivu19JZ7wCCELD68qnJCweWxgnB0xvpep1mdYgkaZXRUnLDyStQuWzN9UpfUhY/lpmWs+xWHoCk4B1FSSoLobZv0LQXG55eKzsPQg+avURg4nZksm9j2VvCH+581HuExSSIs60zNHIHTfZARI0sFi5Ygsf5a+cUE//SmjBdTcp+zLzH6cE/Kt1DKcz77o36F1Jd86hhLBJjkPyd6Z7+dMbrxXqDU9JYjnrTcrblTjdbnCllcIpvfDbtAQbo7L3mcLhKGgvrWlznthrctI2wWcfwFaV9xukspe048=
  login4.triton.aalto.fi ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLF3oitopSKxSNvugA8CWEFwjsrMCEejPgXODoHTbPWo03wW2I2b87Or/g30uppTragZvt6V+7D886FOxaHdEgU=
  login4.triton.aalto.fi ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEiAKYEcl1Dfo/FKfQVXvtEDhP7sywCld6H27v4tl6uX


There is also a page for `ssh host keys for the Aalto shell
servers kosh, lyta, brute, force
<https://www.aalto.fi/en/services/linux-shell-servers-at-aalto>`__
