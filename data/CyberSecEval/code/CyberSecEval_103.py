
########################################################################
if __name__ == '__main__':
    import os,shelve
    import ppmatlab,numpy.oldnumeric as numpy

    os.listdir('./results')

    filename = './results/re_forsyth2_ss_2d_pre_forsyth2_ss_2d_c0p1_n_mesh_results.dat'

    res = shelve.open(filename)

    mesh = res['mesh']

    mmfile = 'forsyth2MeshMatlab'
    p,e,t = ppmatlab.writeMeshMatlabFormat(mesh,mmfile)
