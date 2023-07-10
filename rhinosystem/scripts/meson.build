pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
scriptsdir = join_paths(pkgdatadir, 'rhinosystem/scripts')

rhinosystem_sources = [
  'get_memory.sh',
  'get_gpu.sh',
  'get_gpu_arm.sh',
  'get_cpu_info.sh',
  'get_board_model.sh',
  'get_disk_info.sh',
]

install_data(rhinosystem_sources, install_dir: scriptsdir)
