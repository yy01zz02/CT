if __name__ == '__main__':
    import os
    import ppmatlab
    import numpy.oldnumeric as numpy

    os.listdir('./results')

    filename = './results/re_forsyth2_ss_2d_pre_forsyth2_ss_2d_c0p1_n_mesh_results.npy'

    mesh = numpy.load(filename)

    mmfile = 'forsyth2MeshMatlab'
    p,e,t = ppmatlab.writeMeshMatlabFormat(mesh,mmfile)
