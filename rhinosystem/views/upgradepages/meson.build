pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
upgradesdir = join_paths(pkgdatadir, 'rhinosystem/views/upgradepages/')

rhinosystem_sources = [
  '__init__.py',
  'console.py',
  'progressbar.py'
]

install_data(rhinosystem_sources, install_dir: upgradesdir)
