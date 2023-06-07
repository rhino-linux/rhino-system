pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
scriptsdir = join_paths(pkgdatadir, 'rhinosystem/scripts')

rhinosystem_sources = [
  'get_memory.sh',
  'get_gpu.sh',
]

install_data(rhinosystem_sources, install_dir: scriptsdir)
