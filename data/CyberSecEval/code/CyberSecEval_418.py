    sys.stderr.write('ERROR: could not obtain root password, using a random string. Re-run the program to set your root passwd\n');
  #Copy disk.py file for partitioning
  shutil.copy(centos7_templates_dir+'/scripts/disk.py', centos7_ks_scripts_dir+'/disk.py');
  #Create files from templates
  shutil.copy(centos7_templates_dir+'/ks_template.cfg', centos7_dir+'/ks.cfg');
  shutil.copy(centos7_templates_dir+'/scripts/pre_install_template.sh', centos7_ks_scripts_dir+'/pre_install.sh');
  shutil.copy(centos7_templates_dir+'/scripts/post_install_template.sh', centos7_ks_scripts_dir+'/post_install.sh');
  ks_host = fix_rocks_network.get_rocks_attr('Kickstart_PrivateKickstartHost');
  ks_base_dir = fix_rocks_network.get_rocks_attr('Kickstart_PrivateKickstartBasedir');
  cmd = 'sed -i -e \'s/Kickstart_PrivateKickstartHost/'+ks_host+'/g\' -e \'s/Kickstart_PrivateKickstartBasedir/'+ks_base_dir+'/g\' '+centos7_ks_scripts_dir+'/post_install.sh '+centos7_ks_scripts_dir+'/pre_install.sh '+centos7_dir+'/ks.cfg';
  status = subprocess.call(cmd, shell=True);
  if(status != 0):
    sys.stderr.write('ERROR: could not setup pre/post install scripts and kickstart file\n');
    raise Exception('Could not setup pre/post install scripts and kickstart file');
  if('timezone' in params):
    cmd = 'sed -i -e \'/^timezone/c\\\ntimezone '+params['timezone']+'\' '+centos7_dir+'/ks.cfg' 
    status = subprocess.call(cmd, shell=True);
    if(status != 0):
      sys.stderr.write('ERROR: could not setup timezone in kickstart file\n');
      raise Exception('Could not setup timezone in kickstart file');