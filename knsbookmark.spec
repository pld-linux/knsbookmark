%define name knsbookmark
%define	version 0.3.0
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Converts Netscape bookmarks to kfm bookmarks in KDE
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Internet
Copyright: GPL
Vendor: Ewald Arnold <earnold@w-4.de>
Packager: Troy Engel <tengel@sonic.net>
Distribution: KDE
Source: %{name}-%{version}.tar.gz
URL: http://www.w-4.de/~earnold/progra-e.htm#knsbookmark
Requires: qt kdelibs
BuildRoot: /tmp/build-%{name}-%{version}
Patch: %{name}-%{version}.patch

%description
Converts a Netscape bookmark file into kfm bookmark tree
structure (.kdelnk files). Commandline tool.

%prep
rm -rf %{builddir}

%setup
%patch -p1
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install 

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
