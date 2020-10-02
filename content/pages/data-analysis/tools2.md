Title: Data Analysis Tools
Save_as: tools2.html

[TOC]

Several tools exist to help the user obtain and examine TESS data, below we outline these tools.

## [lightkurve](https://docs.lightkurve.org)
Lightkurve is a Python-based package developed by the Kepler/K2 Guest
Observer (GO) Office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler/K2 GO Office to develop lightkurve for use with TESS data. 

Lighkurve functionality:

* Reading, writing, and interacting with pipeline products (TPFs, LightCurve files, etc) 
* Extracting lightcurves from pixels using custom aperture photometry or custom PSF fitting. 
* Removing trends or correcting systematics using widely-used, non-controversial methods (SavGol, CBVs, SFF, ...)

The lightkurve git repository is [here](https://github.com/KeplerGO/lightkurve).

In addition to the tutorials found [here](https://docs.lightkurve.org/tutorials/index.html) you can find TESS specific tutorials listed below.


###
<table class="table table-striped table-hover" style="max-width:55em;">

<tr>
    <td style="width: 15em;">
    <a href='Target-Pixel-Files.html'>Target Pixel File</a></td>
    <td><a href="tutorials/Target-Pixel-Files.ipynb" download>Download</a></td>
    <td>In this tutorial we learn about how to download TESS target pixel files from the archive, plot the data, access the metadata, and understand their properties and units.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Full-Frame-Images.html'>Full Frame Images</a></td>
    <td><a href="tutorials/Full-Frame-Images.ipynb" download>Download</a></td>
    <td>In this tutorial, we will learn how to use Lightkurve to download TESS Full Frame Images (FFIs) from the archive, cut out specific targets, plot the data, access the metadata, and understand their properties and units.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='LightCurve-objects.html'>LightCurve Ojects</a></td>
    <td><a href="tutorials/LightCurve-objects.ipynb" download>Download</a></td>
    <td> In this tutorial, we will learn how to use Lightkurve to create LightCurve objects using Simple Aperture Photometry, and plot up the resulting data.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='LightCurveFile-Objects.html'>LightCurveFile Objects</a></td>
    <td><a href="tutorials/LightCurveFile-Objects.ipynb" download>Download</a></td>
    <td>Here we look at LightCurveFiles. Rather than being generated a Target Pixel File, these files have been pre-generated using NASA's TESS Data Processing Pipeline.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Aperture-Photometry.html'>Aperture Photometry</a></td>
    <td><a href="tutorials/Aperture-Photometry.ipynb" download>Download</a></td>
    <td>Aperture Photometry can be applied to TESS Target Pixel files in order to obtain light curves for an object of interest.</td>
  </tr>

<tr>
    <td style="width: 15em;">
    <a href='Making-Custom-Apertures.html'>Making Custom Apertures</a></td>
    <td><a href="tutorials/Making-Custom-Apertures.ipynb" download>Download</a></td>
    <td>There are some cases where you might want to produce your own aperture, this tutorial shows you how.</td> 
  </tr>
 
<tr>
    <td style="width: 15em;">
    <a href='Visual-inspection.html'>Visual Inspection</a></td>
    <td><a href="tutorials/Visual-inspection.ipynb" download>Download</a></td>
    <td>In this tutorial we learn how to interactively inspect our object of interest.</td>
  </tr>

</table>

## Tutorials

Several tutorials exist to introduce the general user to TESS data
analysis.

* [Data search tutorials from MAST can be found here](https://outerspace.stsci.edu/display/TESS/6.0+-+Data+Search+Tutorials).
* [Python notebooks from MAST can be found here](https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/TESS).
* [Python notebooks from the Kepler/K2 GO Office can be found here](http://docs.lightkurve.org/).
