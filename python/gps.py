# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:03:07 2022

@author: snaima
"""

import numpy as np



def gps_velocities(lat,lon,ht,fs):
    
    """
    Calculates velocity East, north and vertical from 
    lat, long and height postions

    Parameters:
        lat: latitude, degrees, + north
        lng: longitude, degrees, + east
        ht: height in meters
        fs: sampling frequency
        outputs:
            ve: east velocity, meters/second
            vn: north velocity, meters/second
            first and last 5 values are filled with NaN
            vu: vertical velocity
            
    """
    
    #10th order Taylor series FIR differentiator
    tay10 = np.array([1 / 1260, -5 / 504, 5 / 84, -5 / 21, 5 / 6, 0, -5 / 6, 5 / 21, -5 / 84, 5 / 504, -1 / 1260])

    deg2rad= np.pi/180;
    
    #WGS84 ellipsoid values
    e2 = 6.694379990141089e-003;
    a = 6378137;
    
    #radii of curvature constants
    sin2lat = (np.sin(np.radians(lat)))**2;
    e2term = np.sqrt(1-e2*sin2lat);
    
   #differentiate latitude and longitude using 10th order Taylor
    dlat = deg2rad * np.convolve(lat,tay10,'same');
 
    dlng = deg2rad * np.convolve(lon,tay10,'same');

    
    #convert dlat/dt to vn using radius of curvature
    vn = a * (1 - e2) * (dlat / (e2term ** 3));
    vn=fs*vn;
    # same for dlong/dt
    ve = a * dlng * (np.cos(np.radians(lat)) / e2term);
    ve=fs*ve;
    
    # set edges to NaN
    vn[0:5] = np.nan;
    vn[(-1-4):] = np.nan;

    ve[0:5] = np.nan;
    ve[(-1-4):] = np.nan;
    
    vu=np.convolve(ht,tay10,'same');
    vu=fs*vu;
    vu[0:5] = np.nan;
    vu[(-1-4):] = np.nan;
    
    return ve, vn, vu


def gps_course(ve,vn):
    
    """
    Calculates course/heading and the course velocity

    Parameters:
        ve: east velocity, meters/second
        vn: north velocity, meters/second
        outputs:
            crse: course
            vel: coure velocity
    
    """
    
    rad2deg = 180 / np.pi;
    crse = rad2deg * np.arctan2(ve,vn);
    vel=np.sqrt((ve**2)+(vn**2));
    
    return crse, vel

def gps_acceleration(ve,vn,vu,fs):
    
    """
    Calculates acceleration East, north and vertical from 
    east, north and vertcal velocities

    Parameters:
        ve: east velocity, meters/second
        vn: north velocity, meters/second
        vu: vertical velocity
        fs: sampling frequency
        outputs:
            gpsacc: verical acceleration
            acce: east acceleraion
            accn: north acceleration
            
    """
    
    #10th order Taylor series FIR differentiator
    tay10 = np.array([1 / 1260, -5 / 504, 5 / 84, -5 / 21, 5 / 6, 0, -5 / 6, 5 / 21, -5 / 84, 5 / 504, -1 / 1260])

    gpsacc=np.convolve(vu,tay10,'same');
    gpsacc=fs*gpsacc*1e5;
    gpsacc[0:5] = np.nan;
    gpsacc[(-1-4):] = np.nan;

    acce=np.convolve(ve,tay10,'same');
    acce=fs*acce*1e5;
    acce[0:5] = np.nan;
    acce[(-1-4):] = np.nan;

    accn=np.convolve(vn,tay10,'same');
    accn=fs*accn*1e5;
    accn[0:5] = np.nan;
    accn[(-1-4):] = np.nan;
    
    return gpsacc, acce, accn

def RotAccENtoCL(alpha, acce, accn):
    """rotate accelerations from E-N to C-L

    Parameters: alpha- course (degrees, + clockwise from N)
                acce- east acceleration
                accn- north acceleration

    returns: ac- cross accleration
             al- long acceleration
          
          """

    cosa = np.cos(np.radians(alpha));
    sina = np.sin(np.radians(alpha));
    ac = (acce * cosa) - (accn * sina);
    al = (acce * sina) + (accn * cosa);
    
    return -ac,al
