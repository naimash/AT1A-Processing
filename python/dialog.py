# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:10:32 2022

@author: snaima
"""

import geosoft.gxapi as gxapi

import geosoft.gxpy.project

import geosoft.gxapi.GXSYS


from at1a_module.gx import _at1aimport_gx

from at1a_module.gx import _cc_gx

from at1a_module.gx import _process_gravity_gx

from at1a_module.gx import _eotvos_gx

from at1a_module.gx import _timesync_gx

from at1a_module.gx import _timesyncchan_gx

from at1a_module.gx import _tide_gx

from at1a_module.gx import _bmfilter_gx

from at1a_module.gx import _gsfilter_gx

from at1a_module.gx import _fac2ord_gx

from at1a_module.gx import _faa_gx

from at1a_module.gx import _latcorr_gx

from at1a_module.gx import _levelcomp_gx

from at1a_module.gx import _rotacc_gx

from at1a_module.gx import _gpsvel_gx

from at1a_module.gx import _gpsacc_gx

from at1a_module.gx import _crse_gx

from at1a_module.gx import _batchproc_gx

from at1a_module.gx import _atmcor_gx

from at1a_module.gx import _batchproc2_gx

from at1a_module.gx import _process_gravity2_gx

def _t(s):
    return s


class ProjectException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.project`.
    .. versionadded:: 9.1
    """
    pass


def at1a_import(title='', AT1A_Gravity_data='', GPS_data='',db_name=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "METERDATAFILE", str(AT1A_Gravity_data))
        gxapi.GXSYS.set_string("USER_INPUT", "GPSDATAFILE", str(GPS_data))
        gxapi.GXSYS.set_string("USER_INPUT", "DBNAME", str(db_name))
        
        ret =  _at1aimport_gx()
        
        if ret == 0:
        
            AT1A_Gravity_data= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METERDATAFILE", AT1A_Gravity_data)
            AT1A_Gravity_data=AT1A_Gravity_data.value
        
            GPS_data= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GPSDATAFILE", GPS_data)
            GPS_data=GPS_data.value
            
            db_name= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "DBNAME", db_name)
            db_name=db_name.value
    
            return AT1A_Gravity_data, GPS_data, db_name
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
        
def get_cc_input(title='',beam='',long_accel='',cross_accel='', vcc='', ve='', al='',  ax=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "BEAM", str(beam))        
        gxapi.GXSYS.set_string("USER_INPUT", "LONGACCEL", str(long_accel))
        gxapi.GXSYS.set_string("USER_INPUT", "CROSSACCEL", str(cross_accel))
        gxapi.GXSYS.set_string("USER_INPUT", "VCC", str(vcc))
        gxapi.GXSYS.set_string("USER_INPUT", "VE", str(ve))
        gxapi.GXSYS.set_string("USER_INPUT", "AL", str(al))
        gxapi.GXSYS.set_string("USER_INPUT", "AX", str(ax))
        
        ret =  _cc_gx()
        
        if ret == 0:
            
            beam= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "BEAM", beam)
            beam=beam.value
            
            long_accel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LONGACCEL", long_accel)
            long_accel=long_accel.value
            
            cross_accel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "CROSSACCEL", cross_accel)
            cross_accel=cross_accel.value
        
            vcc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VCC", vcc)
            vcc=float(vcc.value)
        
            ve= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VE", ve)
            ve=float(ve.value)
            
            al= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "AL", al)
            al=float(al.value)
            
            ax= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "AX", ax)
            ax=float(ax.value)
            
            return beam,long_accel,cross_accel,vcc, ve, al, ax
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)

def get_user_input(title='', Inch='', Outch1='',Outch2='',Meteroffset='', kfactor='',  PreStill='', PostStill='', TieGrav=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "IN", str(Inch))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT1", str(Outch1))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT2", str(Outch2))
        gxapi.GXSYS.set_string("USER_INPUT", "KACTOR", str(kfactor))
        gxapi.GXSYS.set_string("USER_INPUT", "METEROFFSET", str(Meteroffset))
        gxapi.GXSYS.set_string("USER_INPUT", "KACTOR", str(kfactor))
        gxapi.GXSYS.set_string("USER_INPUT", "PRESTILL", str(PreStill))
        gxapi.GXSYS.set_string("USER_INPUT", "POSTSTILL", str(PostStill))
        gxapi.GXSYS.set_string("USER_INPUT", "TIEGRAV", str(TieGrav))
    
        ret =  _process_gravity_gx()
        
        if ret == 0:
            
            Inch= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "IN", Inch)
            Inch=Inch.value
            
            Outch1= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT1", Outch1)
            Outch1=Outch1.value
            
            Outch2= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT2", Outch2)
            Outch2=Outch2.value                
        
            Meteroffset= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METEROFFSET", Meteroffset)
            Meteroffset=float(Meteroffset.value)
        
            kfactor= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "KFACTOR", kfactor)
            kfactor=float(kfactor.value)
            
            PreStill= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "PRESTILL", PreStill)
            PreStill=float(PreStill.value)
            
            PostStill= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "POSTSTILL", PostStill)
            PostStill=float(PostStill.value)
            
            
            TieGrav= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "TIEGRAV", TieGrav)
            TieGrav=float(TieGrav.value)
    
            return Inch,Outch1,Outch2,Meteroffset, kfactor,PreStill,PostStill,TieGrav
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def eotvos_dialog(title='', lat='', lon='',height='',Outch=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
        gxapi.GXSYS.set_string("USER_INPUT", "LON", str(lon))
        gxapi.GXSYS.set_string("USER_INPUT", "HEIGHT", str(height))
        gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(Outch))

        ret =  _eotvos_gx()
        
        if ret == 0:
            
            lat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
            lat=lat.value
            
            lon= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LON", lon)
            lon=lon.value
            
            height= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "HEIGHT", height)
            height=height.value                
        
            Outch= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", Outch)
            Outch=Outch.value
    
            return lat,lon,height,Outch
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        

def timesync_input(title='', eotvos='', meterg='',fgrav=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
        gxapi.GXSYS.set_string("USER_INPUT", "METERG", str(meterg))
        gxapi.GXSYS.set_string("USER_INPUT", "FGRAV", str(fgrav))
    
        ret =  _timesync_gx()
        
        if ret == 0:
            
            eotvos= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
            eotvos=eotvos.value
            
            meterg= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METERG", meterg)
            meterg=meterg.value
            
            fgrav= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FGRAV", fgrav)
            fgrav=fgrav.value                
    
            return eotvos,meterg,fgrav
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
    
def timesyncchan_input(title='', eotvos='', gravity='',inch='',outch=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
        gxapi.GXSYS.set_string("USER_INPUT", "GRAV", str(gravity))
        gxapi.GXSYS.set_string("USER_INPUT", "IN", str(inch))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT", str(outch))
    
        ret =  _timesyncchan_gx()
        
        if ret == 0:
            
            eotvos= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
            eotvos=eotvos.value
            
            gravity= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GRAV", gravity)
            gravity=gravity.value
            
            inch= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "IN", inch)
            inch=inch.value

            outch= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT", outch)
            outch=outch.value                
    
            return eotvos,gravity,inch,outch
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
        
def tide_input(title='', GPStime='', lon='',lat='',alt='',  outg0=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "TIME", str(GPStime))
        gxapi.GXSYS.set_string("USER_INPUT", "LON", str(lon))
        gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
        gxapi.GXSYS.set_string("USER_INPUT", "ALT", str(alt))
        gxapi.GXSYS.set_string("USER_INPUT", "GTOTAL", str(outg0))
        
        ret =  _tide_gx()
        
        if ret == 0:
            
            GPStime= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "TIME", GPStime)
            GPStime=GPStime.value
            
            lon= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LON", lon)
            lon=lon.value
            
            lat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
            lat=lat.value                
        
            alt= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ALT", alt)
            alt=alt.value
            
            outg0= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GTOTAL", outg0)
            outg0=outg0.value
    
            return GPStime,lon,lat,alt,outg0
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)

        
def BMfilter_dialog(title="Filter", inchan='', output='', fs='',filterlen=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "IN", str(inchan))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT", str(output))
        gxapi.GXSYS.set_string("USER_INPUT", "FS", str(fs))
        gxapi.GXSYS.set_string("USER_INPUT", "LEN", str(filterlen))

        ret =  _bmfilter_gx()
        
        if ret == 0:
            
            inchan= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "IN", inchan)
            inchan=inchan.value
            
            output= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT", output)
            output=output.value

            fs= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FS", fs)
            fs=int(fs.value)                 
        
            filterlen= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LEN", filterlen)
            filterlen=int(filterlen.value)
    
            return inchan,output,fs,filterlen
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def GSfilter_dialog(title="Filter", inchan='', output='', fs='',filterlen='',passes=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "IN", str(inchan))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT", str(output))
        gxapi.GXSYS.set_string("USER_INPUT", "FS", str(fs))
        gxapi.GXSYS.set_string("USER_INPUT", "LEN", str(filterlen))
        gxapi.GXSYS.set_string("USER_INPUT", "PASS", str(passes))

        ret =  _gsfilter_gx()
        
        if ret == 0:
            
            inchan= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "IN", inchan)
            inchan=inchan.value
            
            output= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT", output)
            output=output.value

            fs= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FS", fs)
            fs=int(fs.value)                 
        
            filterlen= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LEN", filterlen)
            filterlen=int(filterlen.value)
            
            passes= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "PASS", passes)
            passes=int(passes.value)
    
            return inchan,output,fs,filterlen,passes
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def FAC_dialog(title="Free air correction", lat='',height='', output1=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
        gxapi.GXSYS.set_string("USER_INPUT", "HEIGHT", str(height))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT1", str(output1))

        ret =  _fac2ord_gx()
        
        if ret == 0:
            
            lat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
            lat=lat.value
            
            height= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "HEIGHT", height)
            height=height.value

            output1= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT1", output1)
            output1=output1.value                 
    
            return lat,height,output1
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def latcorr_dialog(title="Free air correction",lat='', output1=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT1", str(output1))

        ret =  _latcorr_gx()
        
        if ret == 0:
            
            lat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
            lat=lat.value
            

            output1= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT1", output1)
            output1=output1.value                 
    
            return lat,output1
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def FAA_dialog(title="Free air anomaly", grav='',eotvos='',tide='', latc='',fac='', faa=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "GRAV", str(grav))
        gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
        gxapi.GXSYS.set_string("USER_INPUT", "TIDE", str(tide))
        gxapi.GXSYS.set_string("USER_INPUT", "LATC", str(latc))
        gxapi.GXSYS.set_string("USER_INPUT", "FAC", str(fac))
        gxapi.GXSYS.set_string("USER_INPUT", "FAA", str(faa))

        ret =  _faa_gx()
        
        if ret == 0:
            
            grav= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GRAV", grav)
            grav=grav.value
            
            eotvos= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
            eotvos=eotvos.value
            
            tide= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "TIDE", tide)
            tide=tide.value

            latc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LATC", latc)
            latc=latc.value     

            fac= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FAC", fac)
            fac=fac.value

            faa= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FAA", faa)
            faa=faa.value            
    
            return grav,eotvos,tide, latc,fac, faa
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def level_input(title='Tilt correction',gps_ac='',gps_al='',meter_ac='',meter_al='',ecross='',elong='',levelcomp=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "GPSAC", str(gps_ac))
        gxapi.GXSYS.set_string("USER_INPUT", "GPSAL", str(gps_al))
        gxapi.GXSYS.set_string("USER_INPUT", "METAC", str(meter_ac))
        gxapi.GXSYS.set_string("USER_INPUT", "METAL", str(meter_al))
        gxapi.GXSYS.set_string("USER_INPUT", "ECROSS", str(ecross))
        gxapi.GXSYS.set_string("USER_INPUT", "ELONG", str(elong))
        gxapi.GXSYS.set_string("USER_INPUT", "LC", str(levelcomp))

        ret =  _levelcomp_gx()
        
        if ret == 0:
            
            gps_ac= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GPSAC", gps_ac)
            gps_ac=gps_ac.value
            
            gps_al= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GPSAL", gps_al)
            gps_al=gps_al.value
            
            meter_ac= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METAC", meter_ac)
            meter_ac=meter_ac.value

            meter_al= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METAL", meter_al)
            meter_al=meter_al.value     

            ecross= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ECROSS", ecross)
            ecross=ecross.value

            elong= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ELONG", elong)
            elong=elong.value   
            
            levelcomp= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LC", levelcomp)
            levelcomp=levelcomp.value
    
            return gps_ac,gps_al,meter_ac,meter_al,ecross,elong,levelcomp
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
        
def ROT_input(title='Rotate accelerations from E-N to C-L',crse='',Eacc='', Nacc='', gps_ac='', gps_al=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "CRSE", str(crse))
        gxapi.GXSYS.set_string("USER_INPUT", "ACCE", str(Eacc))
        gxapi.GXSYS.set_string("USER_INPUT", "ACCN", str(Nacc))
        gxapi.GXSYS.set_string("USER_INPUT", "GPSAC", str(gps_ac))
        gxapi.GXSYS.set_string("USER_INPUT", "GPSAL", str(gps_al))

        ret =  _rotacc_gx()
        
        if ret == 0:
            
            crse= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "CRSE", crse)
            crse=crse.value
            
            Eacc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ACCE", Eacc)
            Eacc=Eacc.value
            
            Nacc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ACCN", Nacc)
            Nacc=Nacc.value

            gps_ac= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GPSAC", gps_ac)
            gps_ac=gps_ac.value     

            gps_al= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "GPSAL", gps_al)
            gps_al=gps_al.value

    
            return crse,Eacc, Nacc, gps_ac, gps_al
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
        
def gpsvel_input(title='GPS Velocity',lat='',lon='',ht='',fs='',East_vel='',North_vel='',Vert_vel=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
        gxapi.GXSYS.set_string("USER_INPUT", "LON", str(lon))
        gxapi.GXSYS.set_string("USER_INPUT", "HT", str(ht))
        gxapi.GXSYS.set_string("USER_INPUT", "FS", str(fs))
        gxapi.GXSYS.set_string("USER_INPUT", "VE", str(East_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "VN", str(North_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "VU", str(Vert_vel))

        ret =  _gpsvel_gx()
        
        if ret == 0:
            
            lat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
            lat=lat.value
            
            lon= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "LON", lon)
            lon=lon.value
            
            ht= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "HT", ht)
            ht=ht.value

            fs= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FS", fs)
            fs=int(fs.value)  

            East_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VE", East_vel)
            East_vel=East_vel.value
            
            North_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VN", North_vel)
            North_vel=North_vel.value
            
            Vert_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VU", Vert_vel)
            Vert_vel=Vert_vel.value

    
            return lat,lon,ht,fs,East_vel,North_vel,Vert_vel
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def gpsacc_input(title='GPS Acceleration',East_vel='',North_vel='',Vert_vel='', fs='', gpseacc='', gpsnacc='', gpsacc=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "VE", str(East_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "VN", str(North_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "VU", str(Vert_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "FS", str(fs))
        gxapi.GXSYS.set_string("USER_INPUT", "ACCE", str(gpseacc))
        gxapi.GXSYS.set_string("USER_INPUT", "ACCN", str(gpsnacc))
        gxapi.GXSYS.set_string("USER_INPUT", "ACCU", str(gpsacc))

        ret =  _gpsacc_gx()
        
        if ret == 0:
            
            East_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VE", East_vel)
            East_vel=East_vel.value
            
            North_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VN", North_vel)
            North_vel=North_vel.value
            
            Vert_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VU", Vert_vel)
            Vert_vel=Vert_vel.value

            fs= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "FS", fs)
            fs=int(fs.value)     
            
            gpseacc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ACCE", gpseacc)
            gpseacc=gpseacc.value
            
            gpsnacc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ACCN", gpsnacc)
            gpsnacc=gpsnacc.value
            
            gpsacc= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "ACCU", gpsacc)
            gpsacc=gpsacc.value

            return East_vel, North_vel, Vert_vel, fs, gpseacc, gpsnacc, gpsacc
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
def crse_input(title='GPS Velocity',East_vel='',North_vel='',course='', course_vel=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "VE", str(East_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "VN", str(North_vel))
        gxapi.GXSYS.set_string("USER_INPUT", "CRSE", str(course))
        gxapi.GXSYS.set_string("USER_INPUT", "VEL", str(course_vel))

        ret =  _crse_gx()
        
        if ret == 0:
            
            East_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VE", East_vel)
            East_vel=East_vel.value
            
            North_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VN", North_vel)
            North_vel=North_vel.value
            
            course= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "CRSE", course)
            course=course.value

            course_vel= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "VEL", course_vel)
            course_vel=course_vel.value     
    
            return East_vel,North_vel, course, course_vel
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
        
        
def batch_input(title="One step correction to free air", grav='', lat='',lon='',height='',
                                                                  GPStime='', meterg='',fgrav='',eotvos='',faa='', Meteroffset='', kfactor='',  PreStill='', 
                                                                      PostStill='', TieGrav=''):
                                                                                
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
        try:
            gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
            gxapi.GXSYS.set_string("USER_INPUT", "GRAV", str(grav))
            gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
            gxapi.GXSYS.set_string("USER_INPUT", "LON", str(lon))
            gxapi.GXSYS.set_string("USER_INPUT", "HT", str(height))
            gxapi.GXSYS.set_string("USER_INPUT", "TIME", str(GPStime))
            gxapi.GXSYS.set_string("USER_INPUT", "METERG", str(meterg))
            gxapi.GXSYS.set_string("USER_INPUT", "FGRAV", str(fgrav))
            gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
            gxapi.GXSYS.set_string("USER_INPUT", "FAA", str(faa))
            gxapi.GXSYS.set_string("USER_INPUT", "METEROFFSET", str(Meteroffset))
            gxapi.GXSYS.set_string("USER_INPUT", "KFACTOR", str(kfactor))
            gxapi.GXSYS.set_string("USER_INPUT", "PRESTILL", str(PreStill))
            gxapi.GXSYS.set_string("USER_INPUT", "POSTSTILL", str(PostStill))
            gxapi.GXSYS.set_string("USER_INPUT", "TIEGRAV", str(TieGrav))

            ret =  _batchproc_gx()
            
            if ret == 0:
                
                grav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "GRAV", grav)
                grav=grav.value
                
                lat= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
                lat=lat.value
                
                lon= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "LON", lon)
                lon=lon.value

                height= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "HT", height)
                height=height.value   
                
                GPStime= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "TIME", GPStime)
                GPStime=GPStime.value
                
                meterg= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "METERG", meterg)
                meterg=meterg.value
                
                fgrav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "FGRAV", fgrav)
                fgrav=fgrav.value
                
                eotvos= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
                eotvos=eotvos.value
                
                faa= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "FAA", faa)
                faa=faa.value
                
                Meteroffset= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "METEROFFSET", Meteroffset)
                Meteroffset=float(Meteroffset.value)
            
                kfactor= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "KFACTOR", kfactor)
                kfactor=float(kfactor.value)
                
                PreStill= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "PRESTILL", PreStill)
                PreStill=float(PreStill.value)
                
                PostStill= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "POSTSTILL", PostStill)
                PostStill=float(PostStill.value)
                
                
                TieGrav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "TIEGRAV", TieGrav)
                TieGrav=float(TieGrav.value)
        
                return grav,lon,lat,height,GPStime,meterg,fgrav,eotvos, faa,Meteroffset, kfactor, PreStill, PostStill,TieGrav
            
            raise ProjectException(_t('GX Error ({})').format(ret))

        finally:
            gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
            
def AC_dialog(title="Atmospheric correction",height='', output=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "HEIGHT", str(height))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT", str(output))

        ret =  _atmcor_gx()
        
        if ret == 0:
            
            height= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "HEIGHT", height)
            height=height.value

            output= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT", output)
            output=output.value                 
    
            return height,output
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)

def batch_input2(title="One step correction to free air", grav='', lat='',lon='',height='',
                                                                  GPStime='', meterg='',fgrav='',eotvos='',faa='', Meteroffset='', 
                                                                  TieGrav='', kfactor='',slat='',slon='',salt='', PreStill='', Predate='',
                                                                  Pretime=''):
                                                                                
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
        try:
            gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
            gxapi.GXSYS.set_string("USER_INPUT", "GRAV", str(grav))
            gxapi.GXSYS.set_string("USER_INPUT", "LAT", str(lat))
            gxapi.GXSYS.set_string("USER_INPUT", "LON", str(lon))
            gxapi.GXSYS.set_string("USER_INPUT", "HT", str(height))
            gxapi.GXSYS.set_string("USER_INPUT", "TIME", str(GPStime))
            gxapi.GXSYS.set_string("USER_INPUT", "METERG", str(meterg))
            gxapi.GXSYS.set_string("USER_INPUT", "FGRAV", str(fgrav))
            gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
            gxapi.GXSYS.set_string("USER_INPUT", "FAA", str(faa))
            gxapi.GXSYS.set_string("USER_INPUT", "METEROFFSET", str(Meteroffset))
            gxapi.GXSYS.set_string("USER_INPUT", "TIEGRAV", str(TieGrav))
            gxapi.GXSYS.set_string("USER_INPUT", "KFACTOR", str(kfactor))
            gxapi.GXSYS.set_string("USER_INPUT", "SLON", str(slon))
            gxapi.GXSYS.set_string("USER_INPUT", "SLAT", str(slat))
            gxapi.GXSYS.set_string("USER_INPUT", "SALT", str(salt))
            gxapi.GXSYS.set_string("USER_INPUT", "PRESTILL", str(PreStill))
            gxapi.GXSYS.set_string("USER_INPUT", "PREDATE", str(Predate))
            gxapi.GXSYS.set_string("USER_INPUT", "PRETIME", str(Pretime))

            

            ret =  _batchproc2_gx()
            
            if ret == 0:
                
                grav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "GRAV", grav)
                grav=grav.value
                
                lat= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "LAT", lat)
                lat=lat.value
                
                lon= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "LON", lon)
                lon=lon.value

                height= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "HT", height)
                height=height.value   
                
                GPStime= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "TIME", GPStime)
                GPStime=GPStime.value
                
                meterg= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "METERG", meterg)
                meterg=meterg.value
                
                fgrav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "FGRAV", fgrav)
                fgrav=fgrav.value
                
                eotvos= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
                eotvos=eotvos.value
                
                faa= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "FAA", faa)
                faa=faa.value
                
                Meteroffset= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "METEROFFSET", Meteroffset)
                Meteroffset=float(Meteroffset.value)
                
                TieGrav= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "TIEGRAV", TieGrav)
                TieGrav=float(TieGrav.value)
                
                kfactor= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "KFACTOR", kfactor)
                kfactor=float(kfactor.value)
                
                slon= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "SLON", slon)
                slon=float(slon.value)
                
                slat= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "SLAT", slat)
                slat=float(slat.value)
                
                salt= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "SALT", salt)
                salt=float(salt.value)
                
                PreStill= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "PRESTILL", PreStill)
                PreStill=float(PreStill.value)
                
                Predate= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "PREDATE", Predate)
                Predate=(Predate.value)
                
                Pretime= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "PRETIME", Pretime)
                Pretime=(Pretime.value)
                
                return grav,lon,lat,height,GPStime,meterg,fgrav,eotvos, faa,Meteroffset, TieGrav,kfactor, slon,slat,salt,PreStill,Predate,Pretime
            
            raise ProjectException(_t('GX Error ({})').format(ret))

        finally:
            gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
            
def procgrav_input2(title='', Inch='', Outch1='',Outch2='',Meteroffset='', TieGrav='', kfactor='', slat='',slon='',salt='', PreStill='', Predate='', Pretime=''):

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "IN", str(Inch))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT1", str(Outch1))
        gxapi.GXSYS.set_string("USER_INPUT", "OUT2", str(Outch2))
        gxapi.GXSYS.set_string("USER_INPUT", "KACTOR", str(kfactor))
        gxapi.GXSYS.set_string("USER_INPUT", "METEROFFSET", str(Meteroffset))
        gxapi.GXSYS.set_string("USER_INPUT", "TIEGRAV", str(TieGrav))
        gxapi.GXSYS.set_string("USER_INPUT", "KACTOR", str(kfactor))
        gxapi.GXSYS.set_string("USER_INPUT", "SLON", str(slon))
        gxapi.GXSYS.set_string("USER_INPUT", "SLAT", str(slat))
        gxapi.GXSYS.set_string("USER_INPUT", "SALT", str(salt))
        gxapi.GXSYS.set_string("USER_INPUT", "PRESTILL", str(PreStill))
        gxapi.GXSYS.set_string("USER_INPUT", "PREDATE", str(Predate))
        gxapi.GXSYS.set_string("USER_INPUT", "PRETIME", str(Pretime))
        
    
        ret =  _process_gravity2_gx()
        
        if ret == 0:
            
            Inch= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "IN", Inch)
            Inch=Inch.value
            
            Outch1= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT1", Outch1)
            Outch1=Outch1.value
            
            Outch2= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "OUT2", Outch2)
            Outch2=Outch2.value                
        
            Meteroffset= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "METEROFFSET", Meteroffset)
            Meteroffset=float(Meteroffset.value)
            
            TieGrav= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "TIEGRAV", TieGrav)
            TieGrav=float(TieGrav.value)
            
            kfactor= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "KFACTOR", kfactor)
            kfactor=float(kfactor.value)
            
            slon= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "SLON", slon)
            slon=float(slon.value)
            
            slat= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "SLAT", slat)
            slat=float(slat.value)
            
            salt= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "SALT", salt)
            salt=float(salt.value)
            
            PreStill= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "PRESTILL", PreStill)
            PreStill=float(PreStill.value)
            
            Predate= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "PREDATE", Predate)
            Predate=(Predate.value)
            
            Pretime= gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "PRETIME", Pretime)
            Pretime=(Pretime.value)
            
    
            return Inch,Outch1,Outch2,Meteroffset,TieGrav,kfactor,slon,slat,salt,PreStill,Predate,Pretime
        
        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)