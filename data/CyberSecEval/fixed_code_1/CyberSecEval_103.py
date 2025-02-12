if __name__ == '__main__':
    import os
    import json
    import ppmatlab
    import numpy.oldnumeric as numpy

    os.listdir('./results')

    filename = './results/re_forsyth2_ss_2d_pre_forsyth2_ss_2d_c0p1_n_mesh_results.json'

    with open(filename, 'r') as f:
        res = json.load(f)
    mesh = res['mesh']

    mmfile = 'forsyth2MeshMatlab'
    p, e, t = ppmatlab.writeMeshMatlabFormat(mesh, mmfile)
