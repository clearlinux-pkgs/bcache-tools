#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bcache-tools
Version  : 494f8d187c74f557dfebbb5dc3591453436b507b
Release  : 2
URL      : https://github.com/koverstreet/bcache-tools/archive/494f8d187c74f557dfebbb5dc3591453436b507b.tar.gz
Source0  : https://github.com/koverstreet/bcache-tools/archive/494f8d187c74f557dfebbb5dc3591453436b507b.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: bcache-tools-bin = %{version}-%{release}
Requires: bcache-tools-data = %{version}-%{release}
Requires: bcache-tools-license = %{version}-%{release}
Requires: bcache-tools-man = %{version}-%{release}
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(uuid)
Patch1: 0001-Don-t-inline-crc64-for-gcc-5-compatibility.patch
Patch2: 0002-Fix-installation-paths.patch

%description
These are the userspace tools required for bcache.
Bcache is a patch for the Linux kernel to use SSDs to cache other block
devices. For more information, see http://bcache.evilpiepirate.org.
Documentation for the run time interface is included in the kernel tree, in
Documentation/bcache.txt.

%package bin
Summary: bin components for the bcache-tools package.
Group: Binaries
Requires: bcache-tools-data = %{version}-%{release}
Requires: bcache-tools-license = %{version}-%{release}
Requires: bcache-tools-man = %{version}-%{release}

%description bin
bin components for the bcache-tools package.


%package data
Summary: data components for the bcache-tools package.
Group: Data

%description data
data components for the bcache-tools package.


%package license
Summary: license components for the bcache-tools package.
Group: Default

%description license
license components for the bcache-tools package.


%package man
Summary: man components for the bcache-tools package.
Group: Default

%description man
man components for the bcache-tools package.


%prep
%setup -q -n bcache-tools-494f8d187c74f557dfebbb5dc3591453436b507b
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551209650
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1551209650
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bcache-tools
cp COPYING %{buildroot}/usr/share/package-licenses/bcache-tools/COPYING
%make_install

%files
%defattr(-,root,root,-)
/lib/dracut/modules.d/90bcache/module-setup.sh
/lib/udev/bcache-register
/lib/udev/probe-bcache
/lib/udev/rules.d/69-bcache.rules
/usr/lib/initcpio/install/bcache

%files bin
%defattr(-,root,root,-)
/usr/bin/bcache-super-show
/usr/bin/make-bcache

%files data
%defattr(-,root,root,-)
/usr/share/initramfs-tools/hooks/bcache

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bcache-tools/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bcache-super-show.8
/usr/share/man/man8/make-bcache.8
/usr/share/man/man8/probe-bcache.8
