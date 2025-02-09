		try:
			OfeliaDebianVMConfigurator.logger.debug("Regenerating SSH keys...\n Deleting old keys...")
			subprocess.check_call("rm -f "+path+"/etc/ssh/ssh_host_*", shell=True, stdout=None)
			#subprocess.check_call("chroot "+path+" dpkg-reconfigure openssh-server ", shell=True, stdout=None)
			
			OfeliaDebianVMConfigurator.logger.debug("Creating SSH1 key; this may take some time...")
			subprocess.check_call("ssh-keygen -q -f "+path+"/etc/ssh/ssh_host_key -N '' -t rsa1", shell=True, stdout=None)
			OfeliaDebianVMConfigurator.logger.debug("Creating SSH2 RSA key; this may take some time...")
			subprocess.check_call("ssh-keygen -q -f "+path+"/etc/ssh/ssh_host_rsa_key -N '' -t rsa", shell=True, stdout=None)
			OfeliaDebianVMConfigurator.logger.debug("Creating SSH2 DSA key; this may take some time...")
			subprocess.check_call("ssh-keygen -q -f "+path+"/etc/ssh/ssh_host_dsa_key -N '' -t dsa", shell=True, stdout=None)
		except Exception as e:
			OfeliaDebianVMConfigurator.logger.error("Fatal error; could not regenerate SSH keys. Aborting to prevent VM to be unreachable..."+str(e))
			raise e


	#Public methods
	@staticmethod
	def createVmConfigurationFile(vm):
