Name:           test-package
Version:        1.0.0
Release:        1
Summary:        Test package for HAR upload
License:        MIT
BuildArch:      noarch

%description
A test RPM package for HAR upload testing.

%prep
%build
%install
mkdir -p %{buildroot}/usr/share/test-package
echo "test" > %{buildroot}/usr/share/test-package/README

%files
/usr/share/test-package/README

%changelog
* Mon Aug 18 2026 Test User <test@example.com> - 1.0.0-1
- Initial package
