#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-sqlite3
Version  : 1.3.10
Release  : 4
URL      : https://rubygems.org/downloads/sqlite3-1.3.10.gem
Source0  : https://rubygems.org/downloads/sqlite3-1.3.10.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rubygem-sqlite3-lib
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : sqlite-autoconf-dev

%description
= SQLite3/Ruby Interface
* https://github.com/sparklemotion/sqlite3-ruby
* http://groups.google.com/group/sqlite3-ruby

%package lib
Summary: lib components for the rubygem-sqlite3 package.
Group: Libraries

%description lib
lib components for the rubygem-sqlite3 package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n sqlite3-1.3.10
gem spec %{SOURCE0} -l --ruby > rubygem-sqlite3.gemspec

%build
gem build rubygem-sqlite3.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
sqlite3-1.3.10.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/sqlite3-1.3.10.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/sqlite3-1.3.10/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/sqlite3-1.3.10/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/sqlite3-1.3.10/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/API_CHANGES.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ChangeLog.cvs
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/.RUBYARCHDIR.-.sqlite3.time
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/backup.c
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/backup.h
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/backup.o
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/database.c
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/database.h
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/database.o
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/exception.c
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/exception.h
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/exception.o
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/sqlite3.c
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/sqlite3.o
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/sqlite3_ruby.h
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/statement.c
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/statement.h
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/statement.o
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/faq/faq.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/faq/faq.yml
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/database.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/pragmas.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/resultset.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/statement.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/translator.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/value.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/tasks/faq.rake
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/tasks/gem.rake
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/tasks/native.rake
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/tasks/vendor_sqlite3.rake
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_backup.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_collation.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_database.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_database_readonly.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_deprecated.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_integration.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_integration_open_close.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_integration_pending.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_integration_resultset.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_integration_statement.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_result_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_sqlite3.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_statement.rb
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/test/test_statement_execute.rb
/usr/lib64/ruby/gems/2.3.0/specifications/sqlite3-1.3.10.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/sqlite3-1.3.10/sqlite3/sqlite3_native.so
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/ext/sqlite3/sqlite3_native.so
/usr/lib64/ruby/gems/2.3.0/gems/sqlite3-1.3.10/lib/sqlite3/sqlite3_native.so
