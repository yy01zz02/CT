
                else:
                    # scaling required
                    command = "'%s' -r %d -y -i %s.%s -vf scale=%d:%d -c:v h264 -r %d -b:v %dk '%s.%s'" % (ffmpeg, framerate, saveText,
                                                                                                           imageFormat, newWidth, newHeight,
                                                                                                           25, bitrate, outputPrefix,
                                                                                                           outputSuffix)

                # run command
                self.log.emit("debug", 'Command: "%s"' % command)
                process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, stderr = process.communicate()
                status = process.poll()

            else:
                command = "'%s' -r %d -y -i %s.%s -r %d -b:v %dk '%s.%s'" % (ffmpeg, framerate, saveText,
                                                                             imageFormat, 25, bitrate,
                                                                             outputPrefix, outputSuffix)
