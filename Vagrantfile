# -*- mode: ruby -*-
# vi: set ft=ruby :

# This Vagrantfile will build an ROM of the current version of 
# resin.  Just run 'vagrant up' and wait for the rpm and srpm to
# be written to the cwd.

$buildrpm = <<BUILDRPM
echo "Running the resin 3 build script"

VERSION=`awk '/^%global VERSION/{print $NF}' /vagrant/spec/resin.spec`
RELEASE=`awk '/^%global Release/{print $NF}' /vagrant/spec/resin.spec`
BUILD_REQUIRES=`awk -F: '/^BuildRequires/ {req_line=$2 ; split(req_line,dep_array,","); for (item in dep_array) { split(dep_array[item],final_deps," "); for (dependancy in final_deps) printf "%s ", final_deps[1]}}' /vagrant/spec/resin.spec`

# We need to install both devel versions, and the spec file does not
# support adding requires by architecture.
BUILD_REQUIRES+="glibc-devel.i686 glibc-devel.x86_64 "

echo "VERSION: ${VERSION}"
echo "RELEASE: ${RELEASE}"
echo "BUILD_REQUIRES: ${BUILD_REQUIRES}"

echo "Building resin ${VERSION}"
echo "Installing dependencies via yum"
set -x
sudo yum install -y epel-release
sudo yum clean metadata
sudo yum groupinstall -y 'Development tools'
sudo yum install -y rpmdevtools ${BUILD_REQUIRES}
set +x
echo "Dependencies installed."

echo "Setting up RPM build env"
rpmdev-setuptree

echo "Copying source and config to rpm env"
cp /vagrant/spec/*spec ~/rpmbuild/SPECS/
cp /vagrant/spec/*.patch ~/rpmbuild/SOURCES/
cp /vagrant/spec/*.tar.gz ~/rpmbuild/SOURCES/

echo "Building..."
cd ~/rpmbuild/
rpmbuild -ba SPECS/resin.spec

echo "Copying output to the vagrant share."
cp ~/rpmbuild/RPMS/*/* /vagrant
cp ~/rpmbuild/SRPMS/* /vagrant

echo "Done building resin ${VERSION}-${RELEASE}"
BUILDRPM


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Bare bones Centos 6.5 box from a trustworthy community member.
  config.vm.box = "puppetlabs/centos-6.5-64-nocm"

  # This optional plugin caches RPMs for faster rebuilds.
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :machine
  end

  config.vm.provision "shell", privileged: false, inline: $buildrpm
end
