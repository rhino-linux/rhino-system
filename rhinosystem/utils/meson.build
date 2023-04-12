pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
utilsdir = join_paths(pkgdatadir, 'rhinosystem/utils')

rhinosystem_sources = [
  '__init__.py',
  'command.py',
  'deviceinfo.py',
  'log.py',
  'threading.py'
]

install_data(rhinosystem_sources, install_dir: utilsdir)
