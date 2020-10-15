"""Module with electric and magnetic field functions

This module contains methods used for the electric and magnetic fields


"UNIQNAME = \"cavestru\"\n   

"""

import numpy as np

def constant_electric_field(charge_position) :
    '''Example constant electric field along x-axis [1,0,0]
    Parameters
    ----------
    charge_position : n-darray
        position of charged particle

    Returns
    -------
    electric field : n-darray
        electric field at charge_position
    
    '''
    return np.array([1,0,0])
    
    
def constant_magnetic_field(charge_position) :
    '''Example constant magnetic field along y axis, [0,1,0], magnitude 1 T
        Parameters
    ----------
    charge_position : n-darray
        position of charged particle

    Returns
    -------
    magnetic field : n-darray
        magnetic field at charge_position
    '''
    return np.array([0,1,0])

def linearly_increasing_bfield(charge_position) :
    '''Magnetic field that happens to linearly increase with z, with proportionality 0.1 T/m.  
    Parameters
    ----------
    charge_position : n-darray
        position of charged particle

    Returns
    -------
    magnetic field : n-darray
        magnetic field at charge_position
    '''
    z = charge_position[2]
    bfield = np.array([0,0,0.1]) * z
    return bfield

