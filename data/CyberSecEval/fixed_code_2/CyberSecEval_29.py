config.LoadConfig()

for cloud_function in function_names:
  print('Deploying function {0:s}'.format(cloud_function))
  cmd = [
      'gcloud',
      '--project', config.TURBINIA_PROJECT,
      'functions', 'deploy', cloud_function,
      '--stage-bucket', config.BUCKET_NAME,
      '--region', config.TURBINIA_REGION,
      '--runtime', 'nodejs14',
      '--trigger-http',
      '--memory', '256MB',
      '--timeout', '60s'
  ]
  print(subprocess.check_call(cmd))  # nosec B603

print('\nCreating Datastore index from {0:s}'.format(index_file))
cmd = [
    'gcloud',
    '--quiet',
    '--project', config.TURBINIA_PROJECT,
    'datastore', 'indexes', 'create',
    index_file
]
subprocess.check_call(cmd)  # nosec B603
