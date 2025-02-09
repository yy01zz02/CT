work_dir = "__tmp" + rev;
system("cp -rf " + src_dir + " " + work_dir);

ori_dir = getcwd();
chdir(work_dir);
system("git checkout -f " + rev);
system("git clean -f -d");
chdir(ori_dir);
system(build_cmd + " -p " + dep_dir + " " + work_dir);

system("mv " + work_dir + "/test " + work_dir+"/ori_test");
system("cp -rf " + test_dir + " " + work_dir + "/test");
chdir(work_dir + "/test");
system("GENEXPOUT=1 CMPEXPOUT=0 make check");
chdir(ori_dir);

print "Goint to generate testdir for revision " + rev + " case: " + out_dir;
system("cp -rf " + test_dir + " " + out_dir);
system("cp -rf " + work_dir + "/test/*.exp " + work_dir + "/test/*.tol " + out_dir+"/");
system("rm -rf " + work_dir);