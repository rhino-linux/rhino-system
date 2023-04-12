pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
viewsdir = join_paths(pkgdatadir, 'rhinosystem/views')

rhinosystem_sources = [
  '__init__.py',
  'sysinfo.py',
  'upgrade.py'
]

install_data(rhinosystem_sources, install_dir: viewsdir)
subdir('upgradepages')