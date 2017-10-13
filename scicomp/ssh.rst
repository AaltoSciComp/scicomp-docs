===
SSH
===

*Note* For triton specific instructions see
`Connecting to triton page </triton/tut/connecting>`. 

*Note* This page is a work-in-progress.

The purpose of this document is to describe how to use ssh such that
usage is reasonably convenient and secure. Key takeaways:

- Creating ssh keys
    - Do not copy private keys around. Instead create a separate
      private/public key pair for each device, and copy the public
      keys to those hosts you need to connect to.
    - Always protect the private key by a passphrase.
- Use a ssh agent (ssh-agent, GNOME keyring, macOS keyring, putty
  Pageant, etc.) in order to avoid having to type your key password
  all the time.
- Prefer ProxyJump/ProxyCommand to agent forwarding.

References
==========

- https://wiki.mozilla.org/Security/Guidelines/OpenSSH
- https://blog.0xbadc0de.be/archives/300
- http://nvlpubs.nist.gov/nistpubs/ir/2015/NIST.IR.7966.pdf
