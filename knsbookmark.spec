Summary:	Converts Netscape bookmarks to kfm bookmarks in KDE
Name:		knsbookmark
Version:	0.3.0
Release:	1
Group:		X11/KDE/Internet
Copyright:	GPL
Vendor:		Ewald Arnold <earnold@w-4.de>
Packager:	Troy Engel <tengel@sonic.net>
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}.patch
URL:		http://www.w-4.de/~earnold/progra-e.htm#knsbookmark
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a Netscape bookmark file into kfm bookmark tree structure (.kdelnk
files). Commandline tool.

%prep
%setup -q
%patch -p1
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install 

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
