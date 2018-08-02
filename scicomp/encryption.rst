==========================
Encryption for researchers
==========================

This page describes the basics of encryption to an audience of
researchers. It describes how it may be useful (nd when not needed) in a
professional researcher environment, in order to secure data. It doesn't
describe encryption for personal use (there are plenty of other guides
for that). It doesn't go into very deep details about cryptography. It
doesn't get go into deep details. Cryptography is the type of things
where there are a huge number of subtle details, and everyone has their
own opinion. This guide is designed to provide an understanding for
basic use, not cover every single subtle point.

Status: this is somewhat complete, but is not a complete guide. It will
be extended as needed.

Summary
-------

Modern cryptography is quite well developed, and available many places.
However, the human side is very difficult. Encrypting something, but not
keeping the key or password secure, has no benefits. To use your
encryption, you need to decide what your goals are (who should access,
who you want to keep safe from) and then plan accordingly. The security
of cryptography is decided more by how you manage the keys and process
than the deepest technical details.

Key management
--------------

The point of encryption is to trade a hard problem (keeping a lot of
data secure) to a more limited problem (keeping a single key or password
secure). These keys can be managed separately from the data. This
immediately takes us to the importance of key management. Let's say you
can't send data over email unless it is encrypted. If you encrypt it and
send the password in the same email as the encrypted data, you have
managed to technically satisfy the requirement while adding no real
security at all. A better strategy would be to give the password to
someone when you meet them in person, send it by another channel (e.g.
SMS, but then it is only secure as SMS+email), or even better use
asymmetric encryption (see below).

Deciding how you will manage keys is the hardest part of using
encryption. For some fun, next time you hear someone talk about using
encryption, see if they mention how they keep the keys secure. Usually,
the don't, and you have no way of knowing if they actually are doing it
securely.

Symmetric vs asymmetric encryption
----------------------------------

There are two main types of cryptography. They can both be considered
equally secure, but have different ways of managing keys.

**Symmetric encryption** uses the same password/key for encrypting and
decrypting. It is good because it is simple, because there is only one
key or password you need to know and it is easy to think "one data=one
password". However, everyone needs to know the same password, and it
can't be changed. Since the same password has to be everywhere, this can
be a bit insecure depending on the use, and you can argue it's a bit
complicated to keep that key password secure (if there are many people,
or if it needs to be automated).

**Asymmetric encryption** has different keys for encrypting and
decrypting. So, you use a "public key" to do an encryption (which
requires no password - everyone in the world can know this key and your
data is still secure). You have a separate private key (+password) which
allows only you to decrypt it. This separation of encryption and
decryption was a major mathematical breakthrough. Then, anyone who
needed to receive data securely would have their own public/private key,
and all the public keys are, well, public. When you want to send data to
someone, you just encrypt it using their public key, and there is no
need to manage sharing a password. This allows you to: encrypt so that
multiple people can read it, encrypt automatically without password, and
encrypt to someone not involved in the initial process.

With asymmetric encryption, there are some more things to consider. How
do you make sure that you have the right public key?

Encryption programs
-------------------

This lists some common programs, but this should not be taken to mean
that using these programs makes your data safe. Security depends no how
you use the program, and security will only decrease over time as new
analysis is done. It is usually best to choose well-supported open
source programs where possible. More detailed instructions will be
provided as needed.

7zip
~~~~

7zip is a file archiver (like zip). It can symmetrically encrypt files
with a passphrase.

PGP
~~~

PGP is a set of encryption standards (and also a program). It has a full
suite of encryption tools, and is quite stable and well-supported. You
ofter hear about PGP in the context of email encryption, but it can be
used for many things.

On Linux systems, it is normally found as the program gpg (Gnu Privacy
Guard). This guide uses gpg.

Full disk encryption
~~~~~~~~~~~~~~~~~~~~

Programs can encrypt the entire hard disk of your computer. This means
that any data on it is safe, should your computer be lost. There are
programs to do this for every operating system, and Aalto laptops now
come encrypted by default.

Using symmetric encryption with gpg
-----------------------------------

Encryption:

::

    gpg --symmetric input.file

Decryption:

::

    gpg input.file.gpg

This will ask you for a password. If you do not want it to, you can use
--passphrase-fd to pass it automatically. Normally, keeping a password
in a file is considered quite insecure! Make sure that the permissions
are restrictive. Anyone that can read this file once be able to read
your data forever. The file could be backed up and spread all over the
place - is that what you want? IT admins will be technically able to see
the passphrase (though they do not). Is this all within the scope of
your requirements?

::

    cat pass.txt | gpg --passphrase-fd 0 --symmetric input.file

Using asymmetric encryption with gpg
------------------------------------

When using asymmetric (public key) encryption, you have to generate two
keys: public and private (they are made at the same time). The private
key must be kept private, and has a passphrase on it too. This provides
an added level of security on top of the file permissions.

There are plenty of guides on this available. Some examples:

-  https://www.madboa.com/geek/gpg-quickstart/
-  https://gnupg.org/documentation/index.html

You can encrypt a single files to multiple keys. This means that the
owner of any of the private keys can decrypt the file. This can be
useful for backups and disaster recovery.

General warnings
----------------

-  Strong encryption is serious business. It is designed so that no one
   can read the data should the keys or passwords be lost. If you mess
   this up and lose the key/password, your data is gone forever. You
   must have backups (and those backups must also be secure), ...
-  If you keep passwords in files, or send them insecurely anyhow, then
   the technical security of your data is only as great as of that
   key/password.
-  The strength of your encryption also depends on the strength of your
   password (there is the reason it is often called a "passphrase" - a
   phrase is more secure than a standard password). Choose it carefuly.

Advanced / to do
----------------

-  How much security is enough?
-  Set cipher to AES (pre 16.04)


