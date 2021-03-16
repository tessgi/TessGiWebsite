Title: TESS Software Tools
Save_as: software.html

[TOC]

## Observation planning


### [Web TESS Viewing (WTV) tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py)
The WTV tool allows users to check whether a target potentially falls within the
TESS field of view (FOV). In addition, WTV can be used to calculate
the brightness of a target in the TESS bandpass. 

### [TESS-Point](https://github.com/christopherburke/tess-point)
This is a High Precision TESS pointing tool. It will convert target
coordinates given in Right Ascension and Declination to TESS detector
pixel coordinates for the first 13 TESS observing sectors (Year 1)
focused on the southern ecliptic plane. It can also query MAST to
obtain detector pixel coordinates for a star by TIC ID only. It provides the target ecliptic coordinates, sector number, camera number, detector number, and pixel column and row. If there is no output, then the target is not visible to TESS.

See our [proposal tools page](proposal-tools.html) for additional resources that aid in the preparation of GI proposals.


## TESS data analysis

### [lightkurve](https://docs.lightkurve.org)
Lightkurve is a Python-based package developed by the Kepler/K2 Guest
Observer (GO) Office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler/K2 GO Office to develop lightkurve for use with TESS data. 

Lighkurve functionality:

* Reading, writing, and interacting with pipeline products (TPFs, LightCurve files, etc) 
* Extracting lightcurves from pixels using custom aperture photometry or custom PSF fitting. 
* Removing trends or correcting systematics using widely-used, non-controversial methods (SavGol, CBVs, SFF, ...)

The lightkurve git repository is [here](https://github.com/KeplerGO/lightkurve).

### Tutorials

Several tutorials exist to introduce the general user to TESS data
analysis.

* [Data search tutorials from MAST can be found here](https://outerspace.stsci.edu/display/TESS/6.0+-+Data+Search+Tutorials).
* [Python notebooks from MAST can be found here](https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/TESS).
* [Python notebooks from the Kepler/K2 GO Office can be found here](http://docs.lightkurve.org/).

## Community tools

This list includes tools and software developed specifically for TESS data, as well as tools developed for Kepler and K2 that can be used or modified for TESS. The data formats are similar for Kepler/K2 and TESS: target pixel files (TPF) and full frame images (FFIs). Kepler and K2 had three data modes: long cadence (30 min) and short cadence (1 min) postage stamps (TPFs), and
quarterly FFIs (30 min). TESS has two data modes, short cadence (2 min) postage stamps and 30 min cadence FFIs. Note that many tools are under development, and some are more robust than others. The TESS GI Office plans to update this list as new tools, software, and tutorials become available. If you have any tools you would like us to include, please contact us at [tesshelp@bigbang.gsfc.nasa.gov](mailto:tesshelp@bigbang.gsfc.nasa.gov).


### Detrending and analysis

<table class="table table-striped table-hover" style="max-width:55em;">
  

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/waqasbhatti/astrobase'>astrobase</a></td>
    <td>Light curve tools: periodograms (BLS, Lomb-Scargle, analysis of
    variance), simple detrending (fit high order polynomials),
    light-curve math (phase-folding, binning). Also, a server for
    vetting. <a href='github.com/waqasbhatti/astrobase-notebooks'>A tutorial can
    be found here</a>.
</td>
</tr>



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
    href='https://github.com/hvidy/halophot/'>halophot</a></td>
    <td>K2 Halo Photometry for very bright stars.
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
    href='https://github.com/saigrain/k2scTess'>k2scTess</a></td>
    <td>TESS systematics correction via simultaneous modelling of stellar variability and jitter-dependent systematics using Gaussian Process regression.
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
    href='https://github.com/stephtdouglas/PySysRem'>PySysRem</a></td>
    <td>Correct systematic effects in large sets of photometric light curves.
</td>
</tr>


  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nksaunders/skope'>skope</a></td>
    <td>Synthetic K2 objects for PLD experimentation.
</td>
  </tr>





</table>


<!--
* [PyKE suite](http://pyke.keplerscience.org)

The PyKE tools developed for the Kepler mission. The git repository can be found [here](https://github.com/KeplerGO/PyKE)

* [EVEREST](https://github.com/rodluger/everest)

EPIC Variability Extraction and Removal for Exoplanet Science Targets; Detrending of K2 light curves

* [k2sc](https://github.com/OxES/k2sc)

K2 systematics correction via simultaneous modelling of stellar variability and jitter-dependent systematics using Gaussian Process regression


* [nutella](https://github.com/benmontet/nutella)

Point spreads for Kepler/K2 inference

* [skope](https://github.com/nksaunders/skope)

Synthetic K2 objects for PLD experimentation

* [k2phot](https://github.com/petigura/k2phot)

Routines for extracting lightcurves from K2 images

* [K2-CPM](https://github.com/jvc2688/K2-CPM)

K2 Causal Pixel Model

* [halophot](https://github.com/hvidy/halophot/)

K2 Halo Photometry for very bright stars

* [cave](https://github.com/nksaunders/cave)

Crowded Aperture Variability Extraction

* [celerite-asteroseis](https://github.com/skgrunblatt/celerite-asteroseis)

Transit fitting and basic time-domain asteroseismology using celerite and ktransit

* [k2photometry](https://github.com/vincentvaneylen/k2photometry)

Read, reduce and detrend K2 photometry and search for transiting planets

* [keplersmear](https://github.com/benjaminpope/keplersmear)

Make light curves from Kepler and K2 collateral data

* [OxKeplerSC](https://github.com/OxES/OxKeplerSC)

Kepler jump and systematics correction using Variational Bayes and shrinkage priors.

* [K2Pipeline](https://github.com/FGCUStellarResearch/K2Pipeline)

Data reduction and detrending pipeline for K2 data in Matlab

* [PySysRem](https://github.com/stephtdouglas/PySysRem)

Correct systematic effects in large set of photometric light curves

* [astrobase](https://github.com/waqasbhatti/astrobase)

lightcurve tools: periodograms (BLS, Lomb-Scargle, analysis of variance), simple detrending (AKA: fit high order polynomials), light-curve math: phase-folding, binning. Also, a server for vetting.
Tutorial [here](github.com/waqasbhatti/astrobase-notebooks) -->



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
    href='https://github.com/dfm/kepcal'>kepcal</a></td>
    <td>Self calibration using the Kepler FFIs.
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

</table>




<!--

* [f3](https://github.com/benmontet/f3)

Full Frame Fotometry from the Kepler Full Frame Images

* [DIA](https://github.com/ryanoelkers/DIA)

Difference Imagine Analysis to extract a light curve from FFIs

* TESSCut(coming soon)

* [FFIorBUST](https://github.com/jradavenport/FFIorBUST)

Make light curves from the Kepler Full Frame Images

* [lightkurve](http://lightkurve.keplerscience.org)

Extract light curves from FFIs, package into TPFs

* [kepcal](https://github.com/dfm/kepcal)

Self calibration using the Kepler FFIs

* [SpyFFI](https://github.com/zkbt/spyffi)

Tools for simulating TESS imaging at multiple cadences, including cartoon light curves + jitter + focus drifts, cosmic rays

* [ISIS](http://www2.iap.fr/users/alard/package.html)

Process CCD images using image subtraction

* [HOTPANTS](http://web.ipac.caltech.edu/staff/fmasci/home/astro_refs/HOTPANTSsw2011.pdf)

High Order Transform of PSF and Template Subtraction; Similar method, but improvement on ISIS image subtraction processing. Doc for HOTPANTS [here](http://adsabs.harvard.edu/abs/2015ascl.soft04004B).

-->

### Positional tools

<table class="table table-striped table-hover" style="max-width:55em;">



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
    href='https://github.com/christopherburke/tess-point'>tess-point</a></td>
    <td> Provides the target ecliptic coordinates, TESS sector number, camera number, detector number, and pixel column and row.
</td>
</tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/tessgi/tvguide'>tvguide</a></td>
    <td>A tool for determining whether stars and galaxies are observable by TESS.
</td>
  </tr>

</table>



<!--
* [k2fov](https://github.com/KeplerGO/K2fov)

Check whether targets are in K2 FOV 

* [k2ephem](https://github.com/KeplerGO/K2ephem)

Check whether a Solar System body is (or was) observable by K2 

* [k2-pix](https://github.com/stephtdouglas/k2-pix)

Overlay a sky survey image on a K2 target pixel stamp 

* [k2flix](https://github.com/barentsen/k2flix)

Create quicklook movies from the pixel data observed by Kepler/K2/TESS 

* [k2mosaic](https://github.com/barentsen/k2mosaic)

Mosaic Target Pixel Files (TPFs) obtained by Kepler/K2 into images and movies 

* [tvguide](https://github.com/tessgi/tvguide)

A tool for determining whether stars and galaxies are observable by TESS. 

* [tess-point](https://github.com/christopherburke/tess-point)
-->


### Data handling

<table class="table table-striped table-hover" style="max-width:55em;">


  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/k2-quality-control'>k2-quality-control</a></td>
    <td>Automated quality control of Kepler/K2 data products.
</td>
  </tr>


  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/k2flix'>k2flix</a></td>
    <td>Create quicklook movies from the pixel data observed by Kepler/K2/TESS.
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




</table>



<!--
* [kplr](https://github.com/dfm/kplr)

Tools for working with Kepler data using Python 

* [k2plr](https://github.com/rodluger/k2plr)

Fork of dfm/kplr with added k2 functionality 

* [kepFGS}(https://github.com/christinahedges/kepFGS)

Tools to use the Kepler and K2 Fine Guidance Sensor data 
-->


<!--
### Meta data

<table class="table table-striped table-hover" style="max-width:55em;">

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/KeplerGO/k2-quality-control'>k2-quality-control</a></td>
    <td>Automated quality control of Kepler/K2 data products.
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
    href='https://github.com/timothydmorton/keputils'>keputils</a></td>
    <td>Basic module for interaction with KOI and Kepler-stellar tables.
</td>
</tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/amcody/SuperstampFITS'>SuperstampFITS</a></td>
    <td>Create individual FITS files of K2 superstamp regions.
</td>
</tr>


</table>
-->


<!--
* [kadenza](https://github.com/KeplerGO/kadenza)

Converts raw cadence target data from the Kepler space telescope into FITS files 

* [k2-quality-control](https://github.com/KeplerGO/k2-quality-control)

Automated quality control of Kepler/K2 data products 

* [SuperstampFITS](https://github.com/amcody/SuperstampFITS)

Create individual FITS files of K2 superstamp regions 

* [keputils](https://github.com/timothydmorton/keputils)

Basic module for interaction with KOI and Kepler-stellar tables 
-->

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
    href='https://github.com/barentsen/dave'>DAVE</a></td>
    <td>Discovery And Vetting of K2 Exoplanets.
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
    href='https://github.com/mrtommyb/ktransit'>ktransit</a></td>
    <td>A simple exoplanet transit modeling tool in Python.
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



<!--
* [PyTransit](https://github.com/hpparvi/PyTransit)

Fast and easy transit light curve modeling using Python and Fortran 

* [batman](https://github.com/lkreidberg/batman)

Fast transit light curves models in Python 

* [ktransit](https://github.com/mrtommyb/ktransit)

A simple exoplanet transit modeling tool in python 

* [planetplanet](https://github.com/rodluger/planetplanet)

A general photodynamical code for exoplanet light curves 

* [ketu](https://github.com/dfm/ketu)

A search for transiting planets in K2 data 

* [ttvfast-python](https://github.com/mindriot101/ttvfast-python)

Python interface to the TTVFast library 

* [terra](https://github.com/petigura/terra)

Transit detection code 

* [pysyzygy](https://github.com/rodluger/pysyzygy)

A fast and general planet transit (syzygy) code written in C and in Python 

* [k2ps](https://github.com/hpparvi/k2ps)

K2 planet search 

* [lcps](https://github.com/matiscke/lcps)

A tool for pre-selecting light curves with possible transit signatures 
-->

<!--
### Vetting

<table class="table table-striped table-hover" style="max-width:55em;">

 
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/dave'>DAVE</a></td>
    <td>Discovery And Vetting of K2 Exoplanets.
</td>
  </tr>


</table>
-->

<!--
* [DAVE](https://github.com/barentsen/dave)

Discovery And Vetting of K2 Exoplanets
-->

<!--
### Population statistics

<table class="table table-striped table-hover" style="max-width:55em;">

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
    href='https://github.com/timothydmorton/koi-fpp'>koi-fpp</a></td>
    <td>False positive probabilities for all KOIs.
</td>
  </tr>
 
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/VESPA'>VESPA</a></td>
    <td>Calculating false positive probabilities for transit signals.
</td>
  </tr>


</table>

-->

<!--
* [VESPA](https://github.com/timothydmorton/VESPA)

Calculating false positive probabilities for transit signals 

* [kepler-robovetter](https://github.com/nasa/kepler-robovetter)

The Kepler prime robovetter 

* [koi-fpp](https://github.com/timothydmorton/koi-fpp)

False positive probabilities for all KOIs 

* [KeplerPORTS](https://github.com/nasa/KeplerPORTS)

The Kepler pipeline 

* [Kepler-FLTI](https://github.com/nasa/Kepler-FLTI)

Kepler Prime Flux-Level Transit Injection
-->





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
    href='https://github.com/jradavenport/appaloosa'>appaloosa</a></td>
    <td>Python-based flare finding code for Kepler light curves.
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
    href='https://github.com/jadilia/decatur'>decatur</a></td>
    <td>Tidal synchronization of Kepler eclipsing binaries.
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
    href='https://github.com/ethankruse/kepler_orrery'>kepler_orrery</a></td>
    <td>Make a Kepler orrery gif or movie of all the Kepler multi-planet systems. 
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




<!-- 
* [isochrones](https://github.com/timothydmorton/isochrones)

Pythonic stellar model grid access; easy MCMC fitting of stellar properties 

* [ldtk](https://github.com/hpparvi/ldtk)

Python toolkit for calculating stellar limb darkening profiles 

* [isoclassify](https://github.com/danxhuber/isoclassify)

Perform stellar classifications using isochrone grids 

* [appaloosa](https://github.com/jradavenport/appaloosa)

Python-based flare finding code for Kepler light curves 

* [pymacula](https://github.com/timothydmorton/pymacula)

Python wrapper for Macula analytic starspot code 

* [MulensModel](https://github.com/rpoleski/MulensModel)

Microlensing Modelling package 

* [animate_spots](https://github.com/stephtdouglas/animate_spots)

Make frames for animated gifs/movies showing a rotating spotted star 

* [decatur](https://github.com/jadilia/decatur)

Tidal synchronization of Kepler eclipsing binaries 

* [FoFreeAST](https://github.com/skgrunblatt/FoFreeAST)

Fourier-free Asteroseismology: uses celerite to model granulation and oscillations of stars 
-->


<!--
### Miscellaneous


<table class="table table-striped table-hover" style="max-width:55em;">

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ethankruse/kepler_orrery'>kepler_orrery</a></td>
    <td>Make a Kepler orrery gif or movie of all the Kepler multi-planet systems. 
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
    href='https://github.com/natashabatalha/PandExo'>PandExo</a></td>
    <td>A community tool for transiting exoplanets with HST & JWST. 
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
-->

<!-- * [limb darkening](https://arxiv.org/abs/1804.10295)

Limb-darkening and gravity-darkening coeffts for TESS

* [PandExo](https://github.com/natashabatalha/PandExo)

A community tool for transiting exoplanets with JWST & HST 

* [kepler_orrery](https://github.com/ethankruse/kepler_orrery)

Make a Kepler orrery gif or movie of all the Kepler multi-planet systems 

* [radvel](https://github.com/California-Planet-Search/radvel)

General toolkit for modeling radial velocity data 

* [PyOrbit](https://github.com/LucaMalavolta/PyORBIT)

Simultaneously characterize the orbits of exoplanets and the noise induced by stellar activity.   -->



<!--
## Observation planning
We currently have two piece of software available to assist with writing proposals: [tvguide](proposal-tools.html#tvguide) and [ticgen](proposal-tools.html#ticgen). These tools are described in our [proposal tools page](proposal-tools.html). We also have a [web tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) that provides this functionality.


## Data analysis
The TESS Science Support Center will be providing software to analyze TESS data. This will be built upon the PyKE software created by the [Kepler Science Center](https://keplerscience.arc.nasa.gov).

MAST will be providing open-source, Python software that will allow users to create custom cutouts of TESS Full-Frame Images given a
coordinate and area on the sky. The software will provide cutouts of each 30-minute FFI in target pixel file (TPF) FITS format. There are plans to offer additional functionality, such as quick-look light curves from the cutouts, and source catalogs that can be overlaid on the returned files.


* Tutorials
We will be creating tutorials to assist with using the available software. -->
