Title: Community tools
Save_as: community-tools.html

[TOC]

This list includes tools and software developed specifically for TESS data, as well as tools developed for Kepler and K2 that can be used or modified for TESS. The data formats are similar for Kepler/K2 and TESS: target pixel files (TPF) and full frame images (FFIs). Kepler and K2 had three data modes: long cadence (30 min) and short cadence (1 min) postage stamps (TPFs), and
quarterly FFIs (30 min). TESS has two data modes, short cadence (2 min and 20 second) postage stamps, and 30 min, 10 min, or 200 sec cadence FFIs. Note that 30 min cadenced data is only available for TESS Cycles 1 and 2, the 10 min cadence data in Cycles 3 and 4, and the 200 sec data in Cycle 5+.

Many tools are under development, and some are more robust than others. The TESS GI Office plans to update this list as new tools, software, and tutorials become available. If you have any tools you would like us to include, please contact us at [tesshelp@bigbang.gsfc.nasa.gov](mailto:tesshelp@bigbang.gsfc.nasa.gov).


### Detrending and analysis

<table class="table table-striped table-hover" style="max-width:55em;">

 <tr>
    <td style="width: 15em;"><a
    href='https://wotan.readthedocs.io/en/latest/Installation.html'>wotan</a></td>
    <td>Offers free and open source algorithms to automagically remove trends from time-series data. <a href='https://github.com/hippke/wotan/tree/master/tutorials'>Tutorials can
    be found here.</a>
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://juliet.readthedocs.io/en/latest/index.html'>Juliet</a></td>
    <td>A versatile modelling tool for transiting and non-transiting exoplanetary systems that allows users to perform quick-and-easy fits to data coming from transit photometry, radial velocity or both using bayesian inference and, in particular, using Nested Sampling in order to allow both efficient fitting and proper model comparison. <a href='https://juliet.readthedocs.io/en/latest/tutorials/transitfits.html'>Tutorials can
    be found here.</a>
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/waqasbhatti/astrobase'>astrobase</a></td>
    <td>Light curve tools: periodograms (BLS, Lomb-Scargle, analysis of
    variance), simple detrending (fit high order polynomials),
    light-curve math (phase-folding, binning). Also, a server for
    vetting. <a href='github.com/waqasbhatti/astrobase-notebooks'>A tutorial can
    be found here.</a>
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hvidy/halophot/'>halophot</a></td>
    <td>K2 Halo Photometry for very bright stars. Can be applied to TESS data.
</td>
 </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/saigrain/k2scTess'>k2scTess</a></td>
    <td>TESS systematics correction via simultaneous modeling of stellar variability and jitter-dependent systematics using Gaussian Process regression.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stephtdouglas/PySysRem'>PySysRem</a></td>
    <td>Correct systematic effects in large sets of photometric light curves.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nksaunders/skope'>skope</a></td>
    <td>scope creates a forward model of telescope detectors with pixel sensitivity variation, and synthetic stellar targets with motion relative to the CCD. It allows the for the creation of light curves and as such simulation of Kepler/K2/TESS data.
</td>
  </tr>

</table>

### Full frame image analysis

<table class="table table-striped table-hover" style="max-width:55em;">

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ryanoelkers/DIA'>DIA</a></td>
    <td>Difference Imaging Analysis to extract a light curve from FFIs.
</td>
 </tr>

  <tr>
    <td style="width: 15em;"><a
    href='http://adina.feinste.in/eleanor/index.html'>eleanor</a></td>
    <td>eleanor is an open-source python framework for downloading, analyzing, and visualizing data from the TESS Full Frame Images.
</td>
 </tr>

 
  <tr>
    <td style="width: 15em;"><a
    href='https://filtergraph.com/tess_ffi/'>Filtergraph</a></td>
    <td>This is the TESS full-frame-image (FFI) portal which hosts the
    data products from the pipeline of <a
    href='http://adsabs.harvard.edu/abs/2018AJ....156..132O'>Oelkers & Stassun (2018).</a>
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='http://web.ipac.caltech.edu/staff/fmasci/home/astro_refs/HOTPANTSsw2011.pdf'>HOTPANTS</a></td>
    <td>High Order Transform of PSF and Template Subtraction; Similar
    method, but improvement on ISIS image subtraction
    processing. <a href=' http://adsabs.harvard.edu/abs/2015ascl.soft04004B '>Documentation for HOTPANTS can be found here.</a>
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='http://www2.iap.fr/users/alard/package.html'>ISIS</a></td>
    <td>Process CCD images using image subtraction.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://docs.lightkurve.org'>Lightkurve</a></td>
    <td>Extract light curves from FFIs, and package into TPFs.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/zkbt/spyffi'>SpyFFI</a></td>
    <td>Tools for simulating TESS imaging at multiple cadences, including cartoon light curves + jitter + focus drifts, cosmic rays.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://mast.stsci.edu/tesscut/ '>TESSCut</a></td>
    <td> Create time series pixel cutouts from the TESS FFIs. Find out
    what sectors/cameras/detectors a target was observed in.
</td>
  </tr>
  
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/keatonb/TESS_PRF'>TESS_PRF</a></td>
    <td>Tools to display the TESS pixel response function (PRF) at any location on the detector.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/CheerfulUser/TESSreduce'>TESSreduce</a></td>
    <td>This builds on lightkurve, allowing the user to reduce TESS data while preserving transient signals. The user can supply a TPF or give coordinates and sector to construct a TPF with TESScut. The background subtraction accounts for the smooth background and detector straps. Alongside background subtraction TESSreduce also aligns images, performs difference imaging, and can even detect transient events!
</td>
</tr>

</table>


### Positional tools

<table class="table table-striped table-hover" style="max-width:55em;">

  <tr>
    <td style="width: 15em;"><a
    href='https://pypi.org/project/tesswcs/'>tesswcs</a></td>
    <td> Will enable you to create an astropy World Coordinate System for any pointing of the TESS telescope. You can access both the true WCS from archival data, and predict the WCS for a given RA, Dec, and spacecraft roll.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/christopherburke/tess-point'>tess-point</a></td>
    <td> Provides the target ecliptic coordinates, TESS sector number, camera number, detector number, and pixel column and row.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/'>TESS-point Web Tool</a></td>
    <td>A tool which uses tess-point for determining whether stars and galaxies are observable by TESS.
</td>
  </tr>
  
   <tr>
    <td style="width: 15em;"><a
    href='https://github.com/tessgi/toco'>toco</a></td>
    <td>A way to quickly see some info about a star based on it's TICID.
</td>
  </tr>
  

</table>

### Data handling

<table class="table table-striped table-hover" style="max-width:55em;">


  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/k2flix'>k2flix</a></td>
    <td>Create quicklook movies from the pixel data observed by Kepler/K2/TESS.
</td>
  </tr>

</table>

### Planet search, modeling, and vetting

<table class="table table-striped table-hover" style="max-width:55em;">

  
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/lkreidberg/batman'>batman</a></td>
    <td>Fast transit light curve models in Python.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/3fon3fonov/exostriker'>ExoStriker</a></td>
    <td>Performs N-body simulations, and models the RV stellar reflex motion caused by dynamically interacting planets in multi-planetary systems.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/k2ps'>k2ps</a></td>
    <td>K2 planet search.
</td>
  </tr>
  
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/mrtommyb/ktransit'>ktransit</a></td>
    <td>A simple exoplanet transit modeling tool in Python.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/matiscke/lcps'>lcps</a></td>
    <td>A tool for pre-selecting light curves with possible transit signatures.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/planetplanet'>planetplanet</a></td>
    <td>A general photodynamical code for exoplanet light curves.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/pysyzygy'>pysyzygy</a></td>
    <td>A fast and general planet transit (syzygy) code written in C and in Python.
</td>
  </tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/PyTransit'>PyTransit</a></td>
    <td>Fast and easy transit light curve modeling using Python and Fortran.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/petigura/terra'>terra</a></td>
    <td>Transit detection code.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/mindriot101/ttvfast-python'>ttvfast-python</a></td>
    <td>Python interface to the TTVFast library.
</td>
  </tr>
 
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/VESPA'>VESPA</a></td>
    <td>Calculating false positive probabilities for transit signals.
</td>
  </tr>

</table>

### Miscellaneous science tools


<table class="table table-striped table-hover" style="max-width:55em;">

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stephtdouglas/animate_spots'>animate_spots</a></td>
    <td>Make frames for animated gifs/movies showing a rotating spotted star.
</td>
</tr>
 

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ekaterinailin/AltaiPony>AltaiPony</a></td>
    <td>Python-based flare finding code for Kepler/K2/TESS light curves.
</td>
</tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/skgrunblatt/celerite-asteroseis'>celerite-asteroseis</a></td>
    <td>Transit fitting and basic time-domain asteroseismology using celerite and ktransit.
</td>
 </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://emac.gsfc.nasa.gov/'>EMAC</a></td>
    <td>The NASA Goddard Space Flight Center Exoplanet Modeling and
    Analysis Center (EMAC) serves as a repository and integration platform for modeling and analysis resources focused on the study of exoplanet characteristics and environments.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/skgrunblatt/FoFreeAST'>FoFreeAST</a></td>
    <td>Fourier-Free Asteroseismology: uses celerite to model granulation and
oscillations of stars.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/isochrones'>isochrones</a></td>
    <td>Pythonic stellar model grid access; easy MCMC fitting of stellar properties.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/danxhuber/isoclassify'>isoclassify</a></td>
    <td>Perform stellar classifications using isochrone grids.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/ldtk'>ldtk</a></td>
    <td>Python toolkit for calculating stellar limb darkening profiles.
</td>
  </tr>


  <tr>
    <td style="width: 15em;"><a
    href='https://arxiv.org/abs/1804.10295'>limb darkening</a></td>
    <td>Limb-darkening and gravity-darkening coefficients for TESS.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rpoleski/MulensModel'>MulensModel</a></td>
    <td>Microlensing Modelling package.
</td>
  </tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/natashabatalha/PandExo'>PandExo</a></td>
    <td>A community tool for transiting exoplanets with HST & JWST. 
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/pymacula'>pymacula</a></td>
    <td>Python wrapper for Macula analytic starspot code.
</td>
  </tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/LucaMalavolta/PyORBIT'>PyOrbit</a></td>
    <td>General toolkit for modeling radial velocity data. 
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/California-Planet-Search/radvel'>radvel</a></td>
    <td>Simultaneously characterize the orbits of exoplanets and the noise induced by stellar activity.
</td>
</tr>


</table>


### Kepler/K2 tools

Although not directly applicable to TESS data, below we list some of the tools developed for Kepler/K2. 
These tools may be modified to work with TESS. 

<table class="table table-striped table-hover" style="max-width:55em;">
<tr>
    <td style="width: 15em;"><a
    href='https://github.com/nksaunders/cave'>cave</a></td>
    <td>Crowded Aperture Variability Extraction.
</td>
 </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/everest'>EVEREST</a></td>
    <td>EPIC Variability Extraction and Removal for Exoplanet Science Targets; Detrending of K2 light curves.
</td>
  </tr>
  
   <tr>
    <td style="width: 15em;"><a
    href='https://github.com/jvc2688/K2-CPM'>K2-CPM</a></td>
    <td>K2 Causal Pixel Model.
</td>
 </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/petigura/k2phot'>k2phot</a></td>
    <td>Routines for extracting lightcurves from K2 images.
</td>
 </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/vincentvaneylen/k2photometry'>k2photometry</a></td>
    <td>Read, reduce and detrend K2 photometry and search for transiting planets.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/FGCUStellarResearch/K2Pipeline'>K2Pipeline</a></td>
    <td>Data reduction and detrending pipeline for K2 data in Matlab.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/OxES/k2sc'>k2sc</a></td>
    <td>K2 systematics correction via simultaneous modelling of stellar variability and jitter-dependent systematics using Gaussian Process regression.
</td>
  </tr>

<tr>
    <td style="width: 15em;"><a
    href='https://github.com/benjaminpope/keplersmear'>keplersmear</a></td>
    <td>Make light curves from Kepler and K2 collateral data.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/benmontet/nutella'>nutella</a></td>
    <td>Point spreads for Kepler/K2 inference.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/OxES/OxKeplerSC'>OxKeplerSC</a></td>
    <td>Kepler jump and systematics correction using Variational Bayes and shrinkage priors.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/benmontet/f3'>f3</a></td>
    <td>Full Frame Fotometry from the Kepler Full Frame Images.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/jradavenport/FFIorBUST'>FFIorBUST</a></td>
    <td>Make light curves from the Kepler Full Frame Images.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/dfm/kepcal'>kepcal</a></td>
    <td>Self calibration using the Kepler FFIs.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stephtdouglas/k2-pix'>k2-pix</a></td>
    <td>Overlay a sky survey image on a K2 target pixel stamp.
</td>
  </tr>


  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/K2ephem'>k2ephem</a></td>
    <td>Check whether a Solar System body is (or was) observable by K2.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/K2fov'>k2fov</a></td>
    <td>Check whether targets are in K2 FOV.
</td>
  </tr>
  
    <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/k2-quality-control'>k2-quality-control</a></td>
    <td>Automated quality control of Kepler/K2 data products.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/k2mosaic'>k2mosaic</a></td>
    <td>Mosaic Target Pixel Files (TPFs) obtained by Kepler/K2 into images and movies.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/kadenza'>kadenza</a></td>
    <td>Converts raw cadence target data from the Kepler space telescope into FITS files.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/christinahedges/kepFGS'>kepFGS</a></td>
    <td>Tools to use the Kepler and K2 Fine Guidance Sensor data.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/keputils'>keputils</a></td>
    <td>Basic module for interaction with KOI and Kepler-stellar tables.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/dfm/kplr'>kplr</a></td>
    <td>Tools for working with Kepler data using Python.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/k2plr'>k2plr</a></td>
    <td>Fork of dfm/kplr with added K2 functionality.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/amcody/SuperstampFITS'>SuperstampFITS</a></td>
    <td>Create individual FITS files of K2 superstamp regions.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/dave'>DAVE</a></td>
    <td>Discovery And Vetting of K2 Exoplanets.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nasa/Kepler-FLTI'>Kepler-FLTI</a></td>
    <td>Kepler Prime Flux-Level Transit Injection.
</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nasa/kepler-robovetter'>kepler-robovetter</a></td>
    <td>The Kepler prime robovetter.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nasa/KeplerPORTS'>KeplerPORTS</a></td>
    <td>The Kepler pipeline.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/dfm/ketu'>ketu</a></td>
    <td>A search for transiting planets in K2 data.
</td>
  </tr>
  
   <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/koi-fpp'>koi-fpp</a></td>
    <td>False positive probabilities for all KOIs.
</td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/jadilia/decatur'>decatur</a></td>
    <td>Tidal synchronization of Kepler eclipsing binaries.
</td>
</tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ethankruse/kepler_orrery'>kepler_orrery</a></td>
    <td>Make a Kepler orrery gif or movie of all the Kepler multi-planet systems. 
</td>
  </tr>

</table>





