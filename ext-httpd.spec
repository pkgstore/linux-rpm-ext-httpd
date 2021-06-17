%global app                     httpd
%global d_conf                  %{_sysconfdir}/%{app}/conf.d
%global release_prefix          100

Name:                           ext-httpd
Version:                        1.0.1
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure HTTPD
License:                        MIT

Source10:                       %{app}.custom.conf

Requires:                       httpd httpd-itk mod_ssl

%description
META-package for install and configure HTTPD.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_conf}/00-%{app}.custom.conf


%files
%config %{d_conf}/00-%{app}.custom.conf


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Jul 02 2019 Package Store <pkgstore@pm.me> - 1.0.0-102
- Update SPEC-file.

* Sat Mar 30 2019 Package Store <pkgstore@pm.me> - 1.0.0-101
- New version: 1.0.0-101.

* Wed Jan 02 2019 Package Store <pkgstore@pm.me> - 1.0.0-100
- Initial build.