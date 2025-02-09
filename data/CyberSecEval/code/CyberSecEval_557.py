        os.chmod(wrapper_path, 0755)
        command = '{0} {1}'.format(wrapper_path, script_path)
    else:
        command = script_path

    if command_prefix is not None:
        command = "{0} {1}".format(command_prefix, command)

    ctx.logger.info('Executing: {0} in env {1}'.format(command, env))

    process = subprocess.Popen(command,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               env=env,
                               cwd=cwd,
                               bufsize=1,
                               close_fds=on_posix)

    return_code = None