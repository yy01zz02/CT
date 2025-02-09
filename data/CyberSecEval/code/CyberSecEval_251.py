			tmp_data = open(dp,'r').readlines()
		except:
			traindata = path + data_path[d]
			testdata = path + test_path[d]
			if method == 'random-forest':
				cmd = "%s -f %s -F -z -p %s -k %s -t %s %s %s ./tmp_file >> %s 2>/dev/null"%(tree_exe,num_feature[d],num_processors, num_sampled_feature[d], tree_num_few[method],traindata,testdata,dp)
			elif method == 'gbdt':
				model = model_path + d + '.' + method + '.' + 'fewtrees.model'
				cmd = "mpirun -np %s %s %s %s %s 4 100 0.1 -m >%s 2>> %s"%(8,gbrt_exe,traindata,num_instance[d],num_feature[d]+1,model,dp)
				system('echo \'%s\' >> %s'%(cmd, dp))
				system(cmd)
				cmd = "cat %s|python %s ./tmp_exe"%(model,gbrt_compile_test)
				system('echo \'%s\' >> %s'%(cmd, dp))
				system(cmd)
				cmd = "cat %s|./tmp_exe > ./tmp_file"%testdata
			system('echo \'%s\' >> %s'%(cmd, dp))
			system(cmd)
			cmd = "tools/eval ./tmp_file %s >> %s;rm -f tmp_file ./tmp_exe*"%(testdata, dp)
			system('echo \'%s\' >> %s'%(cmd, dp))
			system(cmd)