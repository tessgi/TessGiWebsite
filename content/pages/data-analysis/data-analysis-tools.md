Title: Data Analysis Tools
Save_as: data-analysis-tools.html

[TOC]

Several tools exist to help the user obtain and examine TESS data, below we outline these tools.

## [lightkurve](https://docs.lightkurve.org)
Lightkurve is a Python-based package developed by the Kepler/K2 Guest
Observer (GO) Office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler/K2 GO Office to develop Lightkurve for use with TESS data. 

Lightkurve functionality:

* Reading, writing, and interacting with pipeline products (TPFs, LightCurve files, etc) 
* Extracting light curves from pixels using custom aperture photometry or custom PSF fitting. 
* Removing trends or correcting systematics using widely-used, non-controversial methods (SavGol, CBVs, SFF, ...)

The lightkurve git repository is [here](https://github.com/KeplerGO/lightkurve).

Below we list tutorials that will help first time users get to grips with using python, Lightkurve, and understanding TESS data products. Please note that these tutorials are written for Lightkurve v2.0.


###
<table class="table table-striped table-hover" style="max-width:55em;">

<tr>
    <td style="width: 15em;">
    <a href='step0-install-lightkurve.html
'>Step 0: How to get lightkurve running on your machine</a></td>
    <td></td>
    <td>In this tutorial, we show how to get the lightkurve Python package set up on your machine for you to start working with TESS.</td>
  </tr>


<tr>
    <td style="width: 15em;">
    <a href='TESS-Intro.html'>An introduction to TESS data</a></td>
    <td><a href="docs/tutorials/TESS-Intro.ipynb" download>Download</a></td>
    <td>In this tutorial, we teach the user how to search for, download, and create TESS light curves.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Target-Pixel-File-Tutorial.html'>Target Pixel File tutorial</a></td>
    <td><a href="docs/tutorials/Target-Pixel-File-Tutorial.ipynb" download>Download</a></td>
    <td>In this tutorial we learn about how to download TESS target pixel files from the archive, plot the data, access the metadata, and understand their properties and units.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Full-Frame-Image-Tutorial.html'>Full Frame Image tutorial</a></td>
    <td><a href="docs/tutorials/Full-Frame-Image-Tutorial.ipynb" download>Download</a></td>
    <td>In this tutorial, we will learn how to use Lightkurve to download TESS Full Frame Images (FFIs) from the archive, cut out specific targets, plot the data, access the metadata, and understand their properties and units.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='LightCurve-object-Tutorial.html'>LightCurve object tutorial</a></td>
    <td><a href="docs/tutorials/LightCurve-object-Tutorial.ipynb" download>Download</a></td>
    <td> In this tutorial, we will learn how to use Lightkurve to create LightCurve objects using Simple Aperture Photometry, and plot up the resulting data.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='LightCurveFile-Object-Tutorial.html'>LightCurveFile object tutorial</a></td>
    <td><a href="docs/tutorials/LightCurveFile-Object-Tutorial.ipynb" download>Download</a></td>
    <td>Here we look at LightCurveFiles. Rather than being generated a Target Pixel File, these files have been pre-generated using NASA's TESS Data Processing Pipeline.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Aperture-Photometry-Tutorial.html'>Aperture photometry tutorial</a></td>
    <td><a href="docs/tutorials/Aperture-Photometry-Tutorial.ipynb" download>Download</a></td>
    <td>Aperture photometry can be applied to TESS Target Pixel files in order to obtain light curves for an object of interest.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Making-Custom-Apertures-Tutorial.html'>Making custom apertures Tutorial</a></td>
    <td><a href="docs/tutorials/Making-Custom-Apertures-Tutorial.ipynb" download>Download</a></td>
    <td>There are some cases where you might want to produce your own aperture, this tutorial shows you how.</td> 
  </tr>
 
<tr>
    <td style="width: 15em;">
    <a href='Visual-inspection-Tutorial.html'>Visual inspection tutorial</a></td>
    <td><a href="docs/tutorials/Visual-inspection-Tutorial.ipynb" download>Download</a></td>
    <td>In this tutorial we learn how to interactively inspect our object of interest.</td>
  </tr>
  
  <tr>
    <td style="width: 15em;">
    <a href='NoiseRemovalv2.html'>Noise removal tutorial</a></td>
    <td><a href="docs/tutorials/NoiseRemovalv2.ipynb" download>Download</a></td>
    <td>In this tutorial, we introduce the user to the Corrector class. We use these correctors to remove scattered light and noise from our data.</td>
  </tr>
  
  <tr>
    <td style="width: 15em;">
    <a href='UnderstandingCrowdingv2.html'>Correcting for crowding</a></td>
    <td><a href="docs/tutorials/UnderstandingCrowdingv2.ipynb" download>Download</a></td>
    <td>In this tutorial, we examine crowding of targets and how to correct for it.</td>
  </tr>
  
  <tr>
    <td style="width: 15em;">
    <a href='TESS-CosmicRayPrimer.html'>Cosmic ray mitigation</a></td>
    <td><a href="docs/tutorials/TESS-CosmicRayPrimer.ipynb" download>Download</a></td>
    <td>In this tutorial, we examine how TESS addresses cosmic rays in different data products.</td>
  </tr>

</table>

In addition to the tutorials listed above, there are several other tutorials that can be found [here](https://docs.lightkurve.org/tutorials/index.html). These are more advanced, TESS specific tutorials.


## Tutorials

Several tutorials exist to introduce the general user to TESS data
analysis.

* [Data search tutorials from MAST can be found here](https://outerspace.stsci.edu/display/TESS/6.0+-+Data+Search+Tutorials).
* [Python notebooks from MAST can be found here](https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/TESS).
* [Python notebooks from the Kepler/K2 GO Office can be found here](http://docs.lightkurve.org/).
