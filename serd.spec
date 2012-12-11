Name:           serd
Version:        0.18.0
Release:        %mkrel 1
Summary:        Lightweight RDF syntax library

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:         http://download.drobilla.net/%{name}-%{version}.tar.bz2
URL:            http://drobilla.net/software/
License:        MIT
Group:          System/Libraries

BuildRequires:  waf, pkgconfig

%description
Lightweight C library for RDF syntax which supports reading
and writing Turtle and NTriples. Serd is not intended to be a swiss-army
knife of RDF syntax, but rather is suited to resource limited or
performance critical applications, or situations where a simple
reader/writer with minimal dependencies is ideal
(e.g. in LV2 hosts or plugins).

%files -n %{name}
%defattr(-,root,root,-)
%doc %{_mandir}/man1/serdi.*
%{_bindir}/serdi

#-----------------------------------
%package -n %{lib_name}

Summary:        Lightweight RDF syntax library
Group:          System/Libraries

%description -n %{lib_name}
Lightweight C library for RDF syntax which supports reading
and writing Turtle and NTriples. Serd is not intended to be a swiss-army
knife of RDF syntax, but rather is suited to resource limited or
performance critical applications, or situations where a simple
reader/writer with minimal dependencies is ideal
(e.g. in LV2 hosts or plugins).

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Headers for the Lightweight RDF syntax library
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against serd.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
./waf

%install
rm -rf %{buildroot}

./waf install --destdir=%{buildroot}

%clean
rm -rf %{buildroot}



%changelog
* Sat Aug 25 2012 Frank Kober <emuse@mandriva.org> 0.18.0-1mdv2012.0
+ Revision: 815732
- new version 0.18.0

* Mon Apr 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.14.0-1
+ Revision: 792788
- version update 0.14.0

* Sun Oct 23 2011 Frank Kober <emuse@mandriva.org> 0.5.0-1
+ Revision: 705724
- new version 0.5.0

* Sat Jun 25 2011 Frank Kober <emuse@mandriva.org> 0.4.2-1
+ Revision: 687116
- imported package serd

