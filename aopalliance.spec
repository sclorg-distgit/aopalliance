%global pkg_name aopalliance
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}
Name:           %{?scl_prefix}aopalliance
Version:        1.0
Release:        10.1%{?dist}
Epoch:          0
Summary:        Java/J2EE AOP standards
License:        Public Domain
URL:            http://aopalliance.sourceforge.net/
BuildArch:      noarch
# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        %{pkg_name}-MANIFEST.MF

BuildRequires:  %{?scl_prefix_java_common}ant
Requires:       java-1.7.0-openjdk

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
intends to facilitate and standardize the use of AOP to enhance
existing middleware environments (such as J2EE), or development
environements (e.g. Eclipse).  The AOP Alliance also aims to ensure
interoperability between Java/J2EE AOP implementations to build a
larger AOP community.

%package javadoc
Summary:        API documentation for %{summary}

%description javadoc
%{summary}.

%prep

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{pkg_name}

%{?scl:EOF}

%build

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadoc

# Inject OSGi manifest required by Eclipse.
jar umf %{SOURCE2} build/%{pkg_name}.jar

%{?scl:EOF}

%install

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 build/%{pkg_name}.jar %{buildroot}%{_javadir}/
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{pkg_name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{pkg_name}

%{?scl:EOF}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{pkg_name}

%changelog
* Tue Jul 07 2015 Roland Grunberg <rgrunber@redhat.com> - 0:1.0-10.1
- SCL-ize.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-6
- Drop BR on zip, use jar instead
- Add more verbose description
- Update to current packaging guidelines

* Mon Feb 25 2013 Gerard Ryan <galileo.fedoraproject.org> 0:1.0-5
- Add OSGI manifest

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Tomas Radej <tradej@redhat.com> - 0:1.0-3
- Fixed tarball generation guide

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 6 2012 Andy Grimm <agrimm@gmail.com> 0:1.0-1
- build for Fedora
