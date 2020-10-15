"""Functions and classes for charged particles

This module contains methods used for for the equations of motion in electric and magnetic fields and the ChargedParticle class

"UNIQNAME = \"cavestru\"\n   

"""

import numpy as np

def calc_force_on_charge_by_efield(electric_field, q = 1) :
    '''Returns the force on a charge by an electric field at a given point
    Parameters
    ----------
    electric_field : n-darray
        Electric field at a point in space
    q : float 
        Charge in Coulombs, default 1C

    Returns
    -------
    force : n-darray
        Force on charge due to electric field
    '''
    force = q*electric_field
    return force

def calc_force_on_charge_by_bfield(magnetic_field, charge_velocity, q = 1) :
    '''Returns the force on a charge by an electric field at a given point
    Parameters
    ----------
    magnetic_field : n-darray
        magnetic field at a point in space
    charge_velocity : n-darray
        velocity of charge in m/s
    q : float 
        Charge in Coulombs, default 1C

    Returns
    -------
    force : n-darray
        Force on charge due to magnetic field
    '''
    force = q*np.cross(charge_velocity, magnetic_field)
    return force

def calc_acceleration_of_charge_in_ebfields(electric_field, magnetic_field, charge_velocity, q=1, m=1) :
    ''' Calculate the acceleration of a charge in the presence of both an electric and magnetic field.
    Parameters
    ----------
    electric_field : n-darray
        electric field at a point in space
    magnetic_field : n-darray
        magnetic field at a point in space
    charge_velocity : n-darray
        velocity of charge in m/s
    q : float 
        Charge in Coulombs, default 1C
    m : mass 
        Mass of charge, default to 1
    Returns
    -------
    acceleration : n-darray
        acceleration of charge due to force from magnetic and electric fields
    '''
    acceleration = (calc_force_on_charge_by_efield(electric_field,q) + \
                    calc_force_on_charge_by_bfield(magnetic_field, charge_velocity, q))/m
    return acceleration


def get_rates_of_change_euler(particle_position, particle_velocity, efield_function,
                                        bfield_function, q, m, dt) :
    '''Use Euler's method to calculate the rates of change of particle motion in an 
    electric and/or magnetic field
    '''
    
    electric_field_at_position = efield_function(particle_position)
    magnetic_field_at_position = bfield_function(particle_position)
    
    particle_acceleration = calc_acceleration_of_charge_in_ebfields(electric_field_at_position, 
                                                                    magnetic_field_at_position, 
                                                                        particle_velocity, q, m)
    return particle_velocity, particle_acceleration




class ChargedParticle : 
    """Creates an instance of a charged particle, which can be time evolved
    Parameters
    ----------
    mass : float
        mass of particle.  default 1
    charge : float
        charge of particle in Coulombs. default 1
    x0 : nd-array
        initial position of mass. default np.array([0,0,0])
    v0 : float
        initial velocity of mass. default np.array([0,0,0])
    efield_method : func
        function to calculate electric field for a charged particle at a given position
    bfield_method : func
        function to calculate magnetic field for a charged particle at a given position and velocity
    """
    def __init__(self, mass, charge, x0, v0, 
                    efield_method, bfield_method) :

        # Keep all input values as attributes
        self.mass = mass
        self.charge = charge
        self.x_now = x0
        self.v_now = v0
    
        self.efield_method = efield_method
        self.bfield_method = bfield_method

        self.x_vals = []
        self.v_vals = []
        self.a_vals = []
        
        self.timesteps = np.array([])     
        
    def _set_timesteps(self, num_timesteps, dt) :        
        """Internal method. Sets the attributes timesteps and dt.
        Parameters
        ----------
        num_timesteps : int
            number of timesteps to evolve over
        dt : float
            size of timesteps, defines the time resolution 
        """
        
        self.dt = dt
        next_timesteps = np.arange(0, dt*num_timesteps, dt)

        try :
            last_timestep = self.timesteps[-1]
            next_timesteps += last_timestep
            self.timesteps = np.concatenate([self.timesteps, next_timesteps])
            
        except IndexError : 
            self.timesteps = next_timesteps
                
    def _update_now_values(self) :
        ''' Internal method to calculate the rate of change based on class attributes.
        '''
        x_rate_of_change, v_rate_of_change = self.rate_of_change_method(self.x_now, self.v_now, 
                                                                        self.efield_method,
                                                                        self.bfield_method, 
                                                                        self.charge, self.mass, self.dt)
        self.a_now = v_rate_of_change
        self.v_now = self.v_now + v_rate_of_change * self.dt
        self.x_now = self.x_now + x_rate_of_change * self.dt

    def evolve_particle(self, num_timesteps, dt, rate_of_change_method) :
        """Evolve the charged particle, populate the acceleration, velocity and position (a_vals, v_vals, x_vals)
        Parameters
        ----------
        num_timesteps : int
            number of timesteps to evolve over
        dt : float
            size of timesteps, defines the time resolution 
        rate_of_change_method : func
            function to use to calculate change in velocity and change in position
        """
        
        self._set_timesteps(num_timesteps, dt)
        self.rate_of_change_method = rate_of_change_method
        
        for timestep in np.arange(num_timesteps) :
            # Populate
            
            self.v_vals.append(self.v_now)
            self.x_vals.append(self.x_now)

            # Update "now" values based on rate of change         
            self._update_now_values()            

            self.a_vals.append(self.a_now)
