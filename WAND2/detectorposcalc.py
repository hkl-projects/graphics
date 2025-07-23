import numpy as np

def real2det_e6c(gamma_axis, delta_axis, s_gamma, s_delta, R, cyl_center, ray_origin):
    gamma = np.deg2rad(s_gamma)
    z_hit = R*np.tan(gamma)
    return [-s_delta, z_hit]

def real2det_e4c(tth_axis, s_tth, R, cyl_center, ray_origin):
    return [-s_tth]
