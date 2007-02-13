Summary:	Converts Netscape bookmarks to kfm bookmarks in KDE
Summary(pl.UTF-8):	Konwerter bookmarków Netscape do kfm
Name:		knsbookmark
Version:	0.3.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Vendor:		Ewald Arnold <earnold@w-4.de>
Source0:	ftp://ftp.kde.org/pub/kde/Attic/old/1.1.2/apps/network/%{name}-%{version}.tar.gz
# Source0-md5:	7dac3cd166c7ebad57f40f2a82996caf
#Patch0:		%{name}-0.3.2.patch
#Patch0:	%{name}-%{version}.patch
URL:		http://www.w-4.de/~earnold/progra-e.htm#knsbookmark
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Converts a Netscape bookmark file into kfm bookmark tree structure
(.kdelnk files). Commandline tool.

%description -l pl.UTF-8
Konwerter pliku z bookmarkami Netscape do drzewa bookmarków kfm (pliki
.kdelnk). Jest to narzędzie działające z linii poleceń.

%prep
%setup -q
#%patch -p1
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
	KDEDIR=%{_prefix} ; export KDEDIR
fi
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
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
%defattr(644,root,root,755)
