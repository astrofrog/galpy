# Tests of the quasiisothermaldf module
import numpy
#fiducial setup uses these
from galpy.potential import MWPotential, vcirc, omegac, epifreq, verticalfreq
from galpy.actionAngle import actionAngleAdiabatic, actionAngleStaeckel
from galpy.df import quasiisothermaldf
aAA= actionAngleAdiabatic(pot=MWPotential,c=True)
aAS= actionAngleStaeckel(pot=MWPotential,c=True,delta=0.5)

def test_meanvR_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvR_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvR_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvR_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvT_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,gl=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,mc=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,gl=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,mc=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvz_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvz_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_sigmar_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.,gl=True))-2.*numpy.log(0.2)-0.2) < 0.2, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.2,gl=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,-0.25,gl=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmar_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.,mc=True))-2.*numpy.log(0.2)-0.2) < 0.2, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.2,mc=True))-2.*numpy.log(0.2)-0.2) < 0.4, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,-0.25,mc=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmat_staeckel_gl():
    #colder, st closer to epicycle expectation
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    gamma= 2.*omegac(MWPotential,0.9)/epifreq(MWPotential,0.9)
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.,gl=True)/qdf.sigmaR2(0.9,0.,gl=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.2,gl=True)/qdf.sigmaR2(0.9,0.2,gl=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmat_staeckel_mc():
    numpy.random.seed(2)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    gamma= 2.*omegac(MWPotential,0.9)/epifreq(MWPotential,0.9)
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.,mc=True)/qdf.sigmaR2(0.9,0.,mc=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.2,mc=True)/qdf.sigmaR2(0.9,0.2,mc=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmaz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #from Bovy & Rix 2013, we know that this has to be smaller
    assert numpy.log(qdf.sigmaz2(0.9,0.,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.2,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,0.2,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,-0.25,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,-0.25,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmaz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #from Bovy & Rix 2013, we know that this has to be smaller
    assert numpy.log(qdf.sigmaz2(0.9,0.,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.2,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,0.2,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,-0.25,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,-0.25,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmarz_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,gl=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for adiabatic approx."
    return None

def test_sigmarz_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,mc=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for adiabatic approx."
    return None

def test_sigmarz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,gl=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for staeckel approx."
    return None

def test_sigmarz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,mc=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for staeckel approx."
    return None

def test_tilt_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #should be zero everywhere
    assert numpy.fabs(qdf.tilt(0.9,0.,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,0.2,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    return None

def test_tilt_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #should be zero everywhere
    assert numpy.fabs(qdf.tilt(0.9,0.,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,0.2,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    return None

def test_tilt_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #should be zero in the mid-plane and roughly toward the GC elsewhere
    assert numpy.fabs(qdf.tilt(0.9,0.,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero in the mid-plane for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,0.1,gl=True)-numpy.arctan(0.1/0.9)/numpy.pi*180.) < 2., "qdf's tilt deviates more than expected from expected for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.15,gl=True)-numpy.arctan(-0.15/0.9)/numpy.pi*180.) < 2.5, "qdf's tilt deviates more than expected from expected for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,gl=True)-numpy.arctan(-0.25/0.9)/numpy.pi*180.) < 4., "qdf's tilt deviates more than expected from expected for staeckel approx."
    return None

def test_tilt_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #should be zero in the mid-plane and roughly toward the GC elsewhere
    assert numpy.fabs(qdf.tilt(0.9,0.,mc=True)) < 1., "qdf's tilt deviates more than expected from zero in the mid-plane for staeckel approx." #this is tough
    assert numpy.fabs(qdf.tilt(0.9,0.1,mc=True)-numpy.arctan(0.1/0.9)/numpy.pi*180.) < 3., "qdf's tilt deviates more than expected from expected for staeckel approx."
    return None

def test_estimate_hr():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=0.)-0.25)/0.25) < 0.1, 'estimated scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=None)-0.5)/0.5) < 0.15, 'estimated scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=None,fixed_quad=False)-1.0)/1.0) < 0.3, 'estimated scale length deviates more from input scale length than expected'
    return None

def test_estimate_hz():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from scipy import integrate
    from galpy.potential import evaluateDensities
    expec_hz= 0.1**2./2.\
        /integrate.quad(lambda x: evaluateDensities(0.9,x,MWPotential),
                        0.,0.125)[0]/2./numpy.pi
    assert numpy.fabs((qdf.estimate_hz(0.9,z=0.125)-expec_hz)/expec_hz) < 0.1, 'estimated scale height not as expected'
    assert qdf.estimate_hz(0.9,z=0.) > 1., 'estimated scale height at z=0 not very large'
    #Another one
    qdf= quasiisothermaldf(1./4.,0.3,0.2,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    expec_hz= 0.2**2./2.\
        /integrate.quad(lambda x: evaluateDensities(0.9,x,MWPotential),
                        0.,0.125)[0]/2./numpy.pi
    assert numpy.fabs((qdf.estimate_hz(0.9,z=0.125)-expec_hz)/expec_hz) < 0.15, 'estimated scale height not as expected'
    return None

def test_estimate_hsr():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsr(0.9,z=0.)-1.0)/1.0) < 0.25, 'estimated radial-dispersion scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,2.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsr(0.9,z=0.05)-2.0)/2.0) < 0.25, 'estimated radial-dispersion scale length deviates more from input scale length than expected'
    return None

def test_estimate_hsz():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsz(0.9,z=0.)-1.0)/1.0) < 0.25, 'estimated vertical-dispersion scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,1.,2.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsz(0.9,z=0.05)-2.0)/2.0) < 0.25, 'estimated vertical-dispersion scale length deviates more from input scale length than expected'
    return None

def test_meanjr():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs(numpy.log(qdf.meanjr(0.9,0.,mc=True))\
                          -2.*numpy.log(0.2)-0.2
                      +numpy.log(epifreq(MWPotential,0.9))) < 0.4, 'meanjr is not what is expected'
    assert numpy.fabs(numpy.log(qdf.meanjr(0.5,0.,mc=True))\
                          -2.*numpy.log(0.2)-1.
                      +numpy.log(epifreq(MWPotential,0.5))) < 0.4, 'meanjr is not what is expected'
    return None

def test_meanlz():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    assert numpy.fabs(numpy.log(qdf.meanlz(0.9,0.,mc=True))\
                          -numpy.log(0.9*dfc.meanvT(0.9))) < 0.1, 'meanlz is not what is expected'
    assert numpy.fabs(numpy.log(qdf.meanlz(0.5,0.,mc=True))\
                          -numpy.log(0.5*dfc.meanvT(0.5))) < 0.2, 'meanlz is not what is expected'
    return None

def test_meanjz():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    ldiff= numpy.log(qdf.meanjz(0.9,0.,mc=True))-2.*numpy.log(0.1)-0.2\
        +numpy.log(verticalfreq(MWPotential,0.9))
    #expect this to be smaller than the rough estimate, but not by more than an order of magnitude
    assert ldiff > -1. and ldiff < 0., 'meanjz is not what is expected'
    ldiff= numpy.log(qdf.meanjz(0.5,0.,mc=True))-2.*numpy.log(0.1)-1.0\
        +numpy.log(verticalfreq(MWPotential,0.5))
    assert ldiff > -1. and ldiff < 0., 'meanjz is not what is expected'
    return None

def test_sampleV():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    numpy.random.seed(1)
    samples= qdf.sampleV(0.8,0.1,n=1000)
    #test vR
    assert numpy.fabs(numpy.mean(samples[:,0])) < 0.02, 'sampleV vR mean is not zero'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,0]))-0.5*numpy.log(qdf.sigmaR2(0.8,0.1))) < 0.05, 'sampleV vR stddev is not equal to sigmaR'
    #test vT
    assert numpy.fabs(numpy.mean(samples[:,1]-qdf.meanvT(0.8,0.1))) < 0.015, 'sampleV vT mean is not equal to meanvT'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,1]))-0.5*numpy.log(qdf.sigmaT2(0.8,0.1))) < 0.05, 'sampleV vT stddev is not equal to sigmaT'
    #test vz
    assert numpy.fabs(numpy.mean(samples[:,2])) < 0.01, 'sampleV vz mean is not zero'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,2]))-0.5*numpy.log(qdf.sigmaz2(0.8,0.1))) < 0.05, 'sampleV vz stddev is not equal to sigmaz'
    return None

def test_pvR_adiabatic():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    pvR= numpy.array([qdf.pvR(vr,R,z) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for adiabatic actions'
    return None

def test_pvR_staeckel():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    pvR= numpy.array([qdf.pvR(vr,R,z) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    return None

def test_pvR_staeckel_diffngl():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    #ngl=10
    pvR= numpy.array([qdf.pvR(vr,R,z,ngl=10) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    #ngl=40
    pvR= numpy.array([qdf.pvR(vr,R,z,ngl=40) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvR= numpy.array([qdf.pvR(vr,R,z,ngl=11) for vr in vRs])
    except ValueError: pass
    else: raise AssertionError('pvR w/ ngl=odd did not raise ValueError')
    return None

def test_pvT_adiabatic():
    # Test pvT by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vTs= numpy.linspace(0.,1.5,101)
    pvT= numpy.array([qdf.pvT(vt,R,z) for vt in vTs])
    mvT= numpy.sum(vTs*pvT)/numpy.sum(pvT)
    svT= numpy.sqrt(numpy.sum(vTs**2.*pvT)/numpy.sum(pvT)-mvT**2.)
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvT not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvT not equal to that from sigmaT2 for adiabatic actions'
    return None

def test_pvT_staeckel():
    # Test pvT by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vTs= numpy.linspace(0.,1.5,101)
    pvT= numpy.array([qdf.pvT(vt,R,z) for vt in vTs])
    mvT= numpy.sum(vTs*pvT)/numpy.sum(pvT)
    svT= numpy.sqrt(numpy.sum(vTs**2.*pvT)/numpy.sum(pvT)-mvT**2.)
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvT not equal to that from sigmaT2 for staeckel actions'
    return None

def test_pvT_staeckel_diffngl():
    # Test pvT by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vTs= numpy.linspace(0.,1.5,101)
    #ngl=10
    pvT= numpy.array([qdf.pvT(vt,R,z,ngl=10) for vt in vTs])
    mvT= numpy.sum(vTs*pvT)/numpy.sum(pvT)
    svT= numpy.sqrt(numpy.sum(vTs**2.*pvT)/numpy.sum(pvT)-mvT**2.)
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvT not equal to that from sigmaT2 for staeckel actions'
    #ngl=40
    pvT= numpy.array([qdf.pvT(vt,R,z,ngl=40) for vt in vTs])
    mvT= numpy.sum(vTs*pvT)/numpy.sum(pvT)
    svT= numpy.sqrt(numpy.sum(vTs**2.*pvT)/numpy.sum(pvT)-mvT**2.)
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvT not equal to that from sigmaT2 for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvT= numpy.array([qdf.pvT(vt,R,z,ngl=11) for vt in vTs])
    except ValueError: pass
    else: raise AssertionError('pvT w/ ngl=odd did not raise ValueError')
    return None

def test_pvz_adiabatic():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    pvz= numpy.array([qdf.pvz(vz,R,z) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for adiabatic actions'
    return None

def test_pvz_staeckel():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    pvz= numpy.array([qdf.pvz(vz,R,z) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #same w/ explicit sigmaR input
    pvz= numpy.array([qdf.pvz(vz,R,z,_sigmaR1=0.95*numpy.sqrt(qdf.sigmaR2(R,z))) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    return None

def test_pvz_staeckel_diffngl():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    #ngl=10
    pvz= numpy.array([qdf.pvz(vz,R,z,ngl=10) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #ngl=40
    pvz= numpy.array([qdf.pvz(vz,R,z,ngl=40) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvz= numpy.array([qdf.pvz(vz,R,z,ngl=11) for vz in vzs])
    except ValueError: pass
    else: raise AssertionError('pvz w/ ngl=odd did not raise ValueError')
    return None

def test_pvz_staeckel_arrayin():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    pvz= qdf.pvz(0.05,R*numpy.ones(2),z*numpy.ones(2))
    assert numpy.all(numpy.log(pvz)-numpy.log(qdf.pvz(0.05,R,z))) < 10.**-10., 'pvz calculated with R and z array input does not equal to calculated with scalar input'
    return None

def test_pvRvT_adiabatic():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vTs= numpy.linspace(0.,1.5,51)
    pvRvT= numpy.array([[qdf.pvRvT(vr,vt,R,z) for vt in vTs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vTs),1)).T
    tvT= numpy.tile(vTs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvT)/numpy.sum(pvRvT)
    mvT= numpy.sum(tvT*pvRvT)/numpy.sum(pvRvT)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvT)/numpy.sum(pvRvT)-mvR**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvRvT)/numpy.sum(pvRvT)-mvT**2.)
    svRvT= (numpy.sum(tvR*tvT*pvRvT)/numpy.sum(pvRvT)-mvR*mvT)/svR/svT
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvT not equal to zero for adiabatic actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvRvT not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvRvT not equal to that from sigmaR2 for adiabatic actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvRvT not equal to that from sigmaT2 for adiabatic actions'
    assert numpy.fabs(svRvT) < 0.01, 'correlation between vR and vT calculated from pvRvT not equal to zero for adiabatic actions'
    return None

def test_pvRvT_staeckel():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vTs= numpy.linspace(0.,1.5,51)
    pvRvT= numpy.array([[qdf.pvRvT(vr,vt,R,z) for vt in vTs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vTs),1)).T
    tvT= numpy.tile(vTs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvT)/numpy.sum(pvRvT)
    mvT= numpy.sum(tvT*pvRvT)/numpy.sum(pvRvT)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvT)/numpy.sum(pvRvT)-mvR**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvRvT)/numpy.sum(pvRvT)-mvT**2.)
    svRvT= (numpy.sum(tvR*tvT*pvRvT)/numpy.sum(pvRvT)-mvR*mvT)/svR/svT
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvRvT not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvRvT not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svRvT) < 0.01, 'correlation between vR and vT calculated from pvRvT not equal to zero for staeckel actions'
    return None

def test_pvRvT_staeckel_diffngl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vTs= numpy.linspace(0.,1.5,51)
    #ngl=10
    pvRvT= numpy.array([[qdf.pvRvT(vr,vt,R,z,ngl=10) for vt in vTs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vTs),1)).T
    tvT= numpy.tile(vTs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvT)/numpy.sum(pvRvT)
    mvT= numpy.sum(tvT*pvRvT)/numpy.sum(pvRvT)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvT)/numpy.sum(pvRvT)-mvR**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvRvT)/numpy.sum(pvRvT)-mvT**2.)
    svRvT= (numpy.sum(tvR*tvT*pvRvT)/numpy.sum(pvRvT)-mvR*mvT)/svR/svT
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvRvT not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvRvT not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svRvT) < 0.01, 'correlation between vR and vT calculated from pvRvT not equal to zero for staeckel actions'
    #ngl=24
    pvRvT= numpy.array([[qdf.pvRvT(vr,vt,R,z,ngl=40) for vt in vTs] for vr in vRs])
    mvR= numpy.sum(tvR*pvRvT)/numpy.sum(pvRvT)
    mvT= numpy.sum(tvT*pvRvT)/numpy.sum(pvRvT)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvT)/numpy.sum(pvRvT)-mvR**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvRvT)/numpy.sum(pvRvT)-mvT**2.)
    svRvT= (numpy.sum(tvR*tvT*pvRvT)/numpy.sum(pvRvT)-mvR*mvT)/svR/svT
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvRvT not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvRvT not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvRvT not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svRvT) < 0.01, 'correlation between vR and vT calculated from pvRvT not equal to zero for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvRvT= numpy.array([[qdf.pvRvT(vr,vt,R,z,ngl=11) for vt in vTs] for vr in vRs])
    except ValueError: pass
    else: raise AssertionError('pvz w/ ngl=odd did not raise ValueError')
    return None

def test_pvTvz_adiabatic():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vTs= numpy.linspace(0.,1.5,51)
    vzs= numpy.linspace(-1.,1.,21)
    pvTvz= numpy.array([[qdf.pvTvz(vt,vz,R,z) for vt in vTs] for vz in vzs])
    tvT= numpy.tile(vTs,(len(vzs),1))
    tvz= numpy.tile(vzs,(len(vTs),1)).T
    mvz= numpy.sum(tvz*pvTvz)/numpy.sum(pvTvz)
    mvT= numpy.sum(tvT*pvTvz)/numpy.sum(pvTvz)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvTvz)/numpy.sum(pvTvz)-mvz**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvTvz)/numpy.sum(pvTvz)-mvT**2.)
    svTvz= (numpy.sum(tvz*tvT*pvTvz)/numpy.sum(pvTvz)-mvz*mvT)/svz/svT
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvTvz not equal to zero for adiabatic actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvTvz not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvTvz not equal to that from sigmaz2 for adiabatic actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvTvz not equal to that from sigmaT2 for adiabatic actions'
    assert numpy.fabs(svTvz) < 0.01, 'correlation between vz and vT calculated from pvTvz not equal to zero for adiabatic actions'
    return None

def test_pvTvz_staeckel():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,21)
    vTs= numpy.linspace(0.,1.5,51)
    pvTvz= numpy.array([[qdf.pvTvz(vt,vz,R,z) for vt in vTs] for vz in vzs])
    tvz= numpy.tile(vzs,(len(vTs),1)).T
    tvT= numpy.tile(vTs,(len(vzs),1))
    mvz= numpy.sum(tvz*pvTvz)/numpy.sum(pvTvz)
    mvT= numpy.sum(tvT*pvTvz)/numpy.sum(pvTvz)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvTvz)/numpy.sum(pvTvz)-mvz**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvTvz)/numpy.sum(pvTvz)-mvT**2.)
    svTvz= (numpy.sum(tvz*tvT*pvTvz)/numpy.sum(pvTvz)-mvz*mvT)/svz/svT
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvTvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvTvz not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svTvz) < 0.01, 'correlation between vz and vT calculated from pvTvz not equal to zero for staeckel actions'
    return None

def test_pvTvz_staeckel_diffngl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,21)
    vTs= numpy.linspace(0.,1.5,51)
    #ngl=10
    pvTvz= numpy.array([[qdf.pvTvz(vt,vz,R,z,ngl=10) for vt in vTs] for vz in vzs])
    tvz= numpy.tile(vzs,(len(vTs),1)).T
    tvT= numpy.tile(vTs,(len(vzs),1))
    mvz= numpy.sum(tvz*pvTvz)/numpy.sum(pvTvz)
    mvT= numpy.sum(tvT*pvTvz)/numpy.sum(pvTvz)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvTvz)/numpy.sum(pvTvz)-mvz**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvTvz)/numpy.sum(pvTvz)-mvT**2.)
    svTvz= (numpy.sum(tvz*tvT*pvTvz)/numpy.sum(pvTvz)-mvz*mvT)/svz/svT
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvTvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvTvz not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svTvz) < 0.01, 'correlation between vz and vT calculated from pvTvz not equal to zero for staeckel actions'
    #ngl=24
    pvTvz= numpy.array([[qdf.pvTvz(vt,vz,R,z,ngl=40) for vt in vTs] for vz in vzs])
    mvz= numpy.sum(tvz*pvTvz)/numpy.sum(pvTvz)
    mvT= numpy.sum(tvT*pvTvz)/numpy.sum(pvTvz)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvTvz)/numpy.sum(pvTvz)-mvz**2.)
    svT= numpy.sqrt(numpy.sum(tvT**2.*pvTvz)/numpy.sum(pvTvz)-mvT**2.)
    svTvz= (numpy.sum(tvz*tvT*pvTvz)/numpy.sum(pvTvz)-mvz*mvT)/svz/svT
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvT-qdf.meanvT(R,z)) < 0.01, 'mean vT calculated from pvTvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvTvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(numpy.log(svT)-0.5*numpy.log(qdf.sigmaT2(R,z))) < 0.01, 'sigma vT calculated from pvTvz not equal to that from sigmaT2 for staeckel actions'
    assert numpy.fabs(svTvz) < 0.01, 'correlation between vz and vT calculated from pvTvz not equal to zero for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvTvz= numpy.array([[qdf.pvTvz(vt,vz,R,z,ngl=11) for vt in vTs] for vz in vzs])
    except ValueError: pass
    else: raise AssertionError('pvz w/ ngl=odd did not raise ValueError')
    return None

def test_pvRvz_adiabatic():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vzs= numpy.linspace(-1.,1.,21)
    pvRvz= numpy.array([[qdf.pvRvz(vr,vz,R,z) for vz in vzs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vzs),1)).T
    tvz= numpy.tile(vzs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvz)/numpy.sum(pvRvz)
    mvz= numpy.sum(tvz*pvRvz)/numpy.sum(pvRvz)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvz)/numpy.sum(pvRvz)-mvR**2.)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvRvz)/numpy.sum(pvRvz)-mvz**2.)
    svRvz= (numpy.sum(tvR*tvz*pvRvz)/numpy.sum(pvRvz)-mvR*mvz)/svR/svz
    sR2= qdf.sigmaR2(R,z) #direct calculation
    sz2= qdf.sigmaz2(R,z)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvz not equal to zero for adiabatic actions'
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvRvz not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(sR2)) < 0.01, 'sigma vR calculated from pvRvz not equal to that from sigmaR2 for adiabatic actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(sz2)) < 0.01, 'sigma vz calculated from pvRvz not equal to that from sigmaz2 for adiabatic actions'
    assert numpy.fabs(svRvz-qdf.sigmaRz(R,z)/numpy.sqrt(sR2*sz2)) < 0.01, 'correlation between vR and vz calculated from pvRvz not equal to zero for adiabatic actions'
    return None

def test_pvRvz_staeckel():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vzs= numpy.linspace(-1.,1.,21)
    pvRvz= numpy.array([[qdf.pvRvz(vr,vz,R,z) for vz in vzs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vzs),1)).T
    tvz= numpy.tile(vzs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvz)/numpy.sum(pvRvz)
    mvz= numpy.sum(tvz*pvRvz)/numpy.sum(pvRvz)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvz)/numpy.sum(pvRvz)-mvR**2.)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvRvz)/numpy.sum(pvRvz)-mvz**2.)
    svRvz= (numpy.sum(tvR*tvz*pvRvz)/numpy.sum(pvRvz)-mvR*mvz)/svR/svz
    sR2= qdf.sigmaR2(R,z) #direct calculation
    sz2= qdf.sigmaz2(R,z)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(sR2)) < 0.01, 'sigma vR calculated from pvRvz not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(sz2)) < 0.01, 'sigma vz calculated from pvRvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(svRvz-qdf.sigmaRz(R,z)/numpy.sqrt(sR2*sz2)) < 0.01, 'correlation between vR and vz calculated from pvRvz not equal to zero for adiabatic actions'
    return None

def test_pvRvz_staeckel_diffngl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,21)
    vzs= numpy.linspace(-1.,1.,21)
    #ngl=10
    pvRvz= numpy.array([[qdf.pvRvz(vr,vz,R,z,ngl=10) for vz in vzs] for vr in vRs])
    tvR= numpy.tile(vRs,(len(vzs),1)).T
    tvz= numpy.tile(vzs,(len(vRs),1))
    mvR= numpy.sum(tvR*pvRvz)/numpy.sum(pvRvz)
    mvz= numpy.sum(tvz*pvRvz)/numpy.sum(pvRvz)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvz)/numpy.sum(pvRvz)-mvR**2.)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvRvz)/numpy.sum(pvRvz)-mvz**2.)
    svRvz= (numpy.sum(tvR*tvz*pvRvz)/numpy.sum(pvRvz)-mvR*mvz)/svR/svz
    sR2= qdf.sigmaR2(R,z) #direct calculation
    sz2= qdf.sigmaz2(R,z)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(sR2)) < 0.01, 'sigma vR calculated from pvRvz not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(sz2)) < 0.01, 'sigma vz calculated from pvRvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(svRvz-qdf.sigmaRz(R,z)/numpy.sqrt(sR2*sz2)) < 0.01, 'correlation between vR and vz calculated from pvRvz not equal to zero for adiabatic actions'
    #ngl=24
    pvRvz= numpy.array([[qdf.pvRvz(vr,vz,R,z,ngl=40) for vz in vzs] for vr in vRs])
    mvR= numpy.sum(tvR*pvRvz)/numpy.sum(pvRvz)
    mvz= numpy.sum(tvz*pvRvz)/numpy.sum(pvRvz)
    svR= numpy.sqrt(numpy.sum(tvR**2.*pvRvz)/numpy.sum(pvRvz)-mvR**2.)
    svz= numpy.sqrt(numpy.sum(tvz**2.*pvRvz)/numpy.sum(pvRvz)-mvz**2.)
    svRvz= (numpy.sum(tvR*tvz*pvRvz)/numpy.sum(pvRvz)-mvR*mvz)/svR/svz
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvRvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(sR2)) < 0.01, 'sigma vR calculated from pvRvz not equal to that from sigmaR2 for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(sz2)) < 0.01, 'sigma vz calculated from pvRvz not equal to that from sigmaz2 for staeckel actions'
    assert numpy.fabs(svRvz-qdf.sigmaRz(R,z)/numpy.sqrt(sR2*sz2)) < 0.01, 'correlation between vR and vz calculated from pvRvz not equal to zero for adiabatic actions'
    #ngl=11, shouldn't work
    try:
        pvRvz= numpy.array([[qdf.pvRvz(vr,vz,R,z,ngl=11) for vz in vzs] for vr in vRs])
    except ValueError: pass
    else: raise AssertionError('pvz w/ ngl=odd did not raise ValueError')
    return None

def test_pvRvz_staeckel_arrayin():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    pvRvz= qdf.pvRvz(0.1,0.05,R*numpy.ones(2),z*numpy.ones(2))
    assert numpy.all(numpy.log(pvRvz)-numpy.log(qdf.pvRvz(0.1,0.05,R,z))) < 10.**-10., 'pvRvz calculated with R and z array input does not equal to calculated with scalar input'
    return None

def test_setup_diffsetups():
    #Test the different ways to setup a qdf object
    #Test errors
    try:
        qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                               aA=aAS,cutcounter=True)
    except IOError: pass
    else: raise AssertionError("qdf setup w/o pot set did not raise exception")
    try:
        qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                               pot=MWPotential,cutcounter=True)
    except IOError: pass
    else: raise AssertionError("qdf setup w/o aA set did not raise exception")
    from galpy.potential import LogarithmicHaloPotential
    try:
        qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                               pot=LogarithmicHaloPotential(),
                               aA=aAS,cutcounter=True)
    except IOError: pass
    else: raise AssertionError("qdf setup w/ aA potential different from pot= did not raise exception")
    #precompute
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True,
                           _precomputerg=True)
    qdfnpc= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                              pot=MWPotential,aA=aAS,cutcounter=True,
                              _precomputerg=False)
    assert numpy.fabs(qdf.rg(1.1)-qdfnpc.rg(1.1)) < 10.**-5., 'rg calculated from qdf instance w/ precomputerg set is not the same as that computed from an instance w/o it set'

def test_call_diffinoutputs():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #when specifying rg etc., first get these from a previous output
    val, trg, tkappa, tnu, tOmega= qdf((0.03,0.9,0.02),_return_freqs=True)
    #First check that just supplying these again works
    assert numpy.fabs(val-qdf((0.03,0.9,0.02),rg=trg,kappa=tkappa,nu=tnu,
                              Omega=tOmega)) < 10.**-8., 'qdf calls w/ rg, and frequencies specified and w/ not specified do not agrees'
    #Also calculate the frequencies
    assert numpy.fabs(val-qdf((0.03,0.9,0.02),rg=trg,
                              kappa=epifreq(MWPotential,trg),
                              nu=verticalfreq(MWPotential,trg),
                              Omega=omegac(MWPotential,trg))) < 10.**-8., 'qdf calls w/ rg, and frequencies specified and w/ not specified do not agrees'
    #Also test _return_actions
    val, jr,lz,jz= qdf(0.9,0.1,0.95,0.1,0.08,_return_actions=True)
    assert numpy.fabs(val-qdf((jr,lz,jz))) < 10.**-8., 'qdf call w/ R,vR,... and actions specified do not agree'
    acs= aAS(0.9,0.1,0.95,0.1,0.08)
    assert numpy.fabs(acs[0]-jr) < 10.**-8., 'direct calculation of jr and that returned from qdf.__call__ does not agree'
    assert numpy.fabs(acs[1]-lz) < 10.**-8., 'direct calculation of lz and that returned from qdf.__call__ does not agree'
    assert numpy.fabs(acs[2]-jz) < 10.**-8., 'direct calculation of jz and that returned from qdf.__call__ does not agree'
    #Test unbound orbits
    #Find unbound orbit, new qdf s.t. we can get UnboundError (only with 
    taAS= actionAngleStaeckel(pot=MWPotential,c=False,delta=0.5)
    qdfnc= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                             pot=MWPotential,
                             aA=taAS,
                             cutcounter=True)
    from galpy.actionAngle import UnboundError
    try: acs= taAS(0.9,10.,-20.,0.1,10.)
    except UnboundError: pass
    else: 
        print acs
        raise AssertionError('Test orbit in qdf that is supposed to be unbound is not')
    assert qdfnc(0.9,10.,-20.,0.1,10.) < 10.**-10., 'unbound orbit does not return qdf equal to zero'
    #Test negative lz
    assert qdf((0.03,-0.1,0.02)) < 10.**-8., 'qdf w/ cutcounter=True and negative lz does not return 0'
    assert qdf((0.03,-0.1,0.02),log=True) <= numpy.finfo(numpy.dtype(numpy.float64)).min+1., 'qdf w/ cutcounter=True and negative lz does not return 0'
    #Test func
    val= qdf((0.03,0.9,0.02))
    fval= qdf((0.03,0.9,0.02),func=lambda x,y,z: numpy.sin(x)*numpy.cos(y)\
                  *numpy.exp(z))
    assert numpy.fabs(val*numpy.sin(0.03)*numpy.cos(0.9)*numpy.exp(0.02)-
                      fval) < 10.**-8, 'qdf __call__ w/ func does not work as expected'  
    lfval= qdf((0.03,0.9,0.02),func=lambda x,y,z: numpy.sin(x)*numpy.cos(y)\
                   *numpy.exp(z),log=True)
    assert numpy.fabs(numpy.log(val)+numpy.log(numpy.sin(0.03)\
                                                   *numpy.cos(0.9)\
                                                   *numpy.exp(0.02))-
                      lfval) < 10.**-8, 'qdf __call__ w/ func does not work as expected'
    return None
