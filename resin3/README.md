rpm-resin
=========

This repo will build the resin package into an rpm.

The origional source can be obtained from caucho.com.

Build
-----

# Building this rpm requires both 32 and 64 bit glibc libs.
# However, I am unable to specify the arch in the spec file.
# So, you must install it manually.
yum install glibc-devel.i686 glibc-devel.x86_64 &&
rpmbuild --rebuild resin-3.1.12-1.el6.src.rpm

