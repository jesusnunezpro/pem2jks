# Convert an SSL certificate bundle in PEM format to JKS keystore

This script uses JRE's keytool to create a JKS keystore and adds all certificates in PAM enconded bundle.

This was tested with [AWS global bundle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).

## Requirements

This proof of concept was written for Windows and requires Python 3.8 or better.

**settings.py** must contain resolvable paths to keytool executable, keystore, and PEM bundle.

This script only uses packages from the standard library.

## Todo

- [ ] Testing, testing, testing
- [ ] Documentation
