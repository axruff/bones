import numpy as np
from mayavi import mlab

def set_yz_side_cut_plane(plane, data_size, pos):
    nx = data_size[0]
    ny = data_size[1]
    nz = data_size[2]
    
    plane.seed.widget.origin = np.array([ pos,  0, 0])
    plane.seed.widget.normal = np.array([ 1.,  0.,  0.])
    plane.seed.widget.point1 = np.array([ pos, ny,  0])
    plane.seed.widget.point2 = np.array([ pos, 0  , nz])

def set_xy_front_cut_plane(plane, data_size, pos):
    nx = data_size[0]
    ny = data_size[1]
    nz = data_size[2]
    
    #plane.seed.widget.center = np.array([ nx / 2.0, ny / 2.0  ,  pos])
    plane.seed.widget.point1 = np.array([ nx, 0  , pos])  
    plane.seed.widget.point2 = np.array([ 0, ny, pos])
    
    plane.seed.widget.normal = np.array([ 0.,  0.,  1.])
    plane.seed.widget.origin = np.array([ 0,  0, pos])
    
    
def refresh_widget(widget):
    widget.seed.widget.enabled = False
    widget.seed.widget.enabled = True
    widget.seed.widget.enabled = False
    