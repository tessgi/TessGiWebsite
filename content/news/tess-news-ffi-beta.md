Title: A “Beta” Trial of Quick-Look TESS Orbit Data: Early Release of Sector 35 Orbit 1 Calibrated Full Frame Images
Date: 2021-03-04 10:00
Author: Rebekah Hounsell


Hello TESS followers! We would like to take this opportunity to inform you, the community, of a new High Level Science Product (HLSP) being released at  [MAST](https://archive.stsci.edu) called [TICA](https://archive.stsci.edu/hlsp/tica) [(Fausnaugh et al. 2020)](https://iopscience.iop.org/article/10.3847/2515-5172/abd63a).

TICA provides a calibrated version of TESS full frame images (FFIs). These FFIs are the same products used by the TESS Science Office at MIT to create the [QLP](https://www.google.com/url?q=https://archive.stsci.edu/hlsp/qlp&sa=D&source=editors&ust=1614893557574000&usg=AOvVaw10KvxqkSyHfpCT95L4I8VV)-extracted light curves, also provided as an HLSP at MAST.  TICA is able to process a full ~13.7-day orbit of FFIs within ~1 day of the data being downloaded to the ground.  In principle, this allows for “quick-look” calibrated versions of the FFIs for an orbit to be made public to the TESS community up to several weeks earlier than the full ~27-day Sector’s worth of standard mission products.

To trial rapid release of TESS data, the calibrated TICA FFIs from the first orbit of Sector 35 will be released early to the community as an HLSP on **Monday, March 8th**. These data will be made public earlier than the standard mission products, and thus **will be the first release of calibrated pixel data for this Sector**. The standard mission products for this and all following sectors will still be delivered to the community on the nominal timeline. This activity is being conducted as a “beta” trial, to test a process through which “quick-look” calibrated images could be expeditiously released to the community on an orbit-by-orbit basis, instead of waiting for a full Sector (two orbits) to be completed and processed.  This will allow our TESS community to more rapidly begin analysis, plan follow-up observations, or search for transients and moving targets.  It will also reduce the impact associated with the delay between TESS observations being completed and the data being made public, such as the decay of exoplanet orbital ephemerides or the seasonal availability of telescope time to conduct follow-up in that Sector’s region of the sky.

**What Will Be Provided As Part Of This Beta Trial?**

The TICA-calibrated FFIs from the first orbit of Sector 35 will be made available for download from the [TICA HLSP](https://archive.stsci.edu/hlsp/tica) webpage.  The files will be made available to download using [curl](https://curl.se) scripts, which will allow users to download the full set of FITS images, or select a subset of FITS images to retrieve.  These curl scripts will function in a similar way to those provided as bulk downloads for the mission-produced products.  Many users will find curl already installed on their machines, if not, the software is open source and freely available to install.

**Contents Of This Beta Trial**

* The astrometric solutions from the TICA-calibrated images typically differ from those provided by the standard TESS mission products by less than 2 arc seconds. Similarly, the TESS magnitudes of individual objects typically differ by less than 1 millimagnitude.

* Only the calibrated TICA FFis will be made available, thus serving as a quick-look version of the data.  The raw data will not be included as part of this activity, and the release does not include light curves.

* The TICA FFis will only be available for download using the bulk scripts on the HLSP page at MAST.  The TICA files will not be available through the MAST Portal, through the MAST API or astroquery.mast, and will not be available for use in TESSCut.

* These are quick-look products, thus the same level of documentation and support will not be available as for the standard mission products.

* Only Sector 35, Orbit 1 will be released as part of this beta trial.  Similar quick-look, single orbit early-releases beyond Sector 35 Orbit 1 will be re-assessed by the mission at a later date, based in part on feedback from the community.

**What Will Change With The Standard Sector 35 Release?**

Nothing will change in terms of the release of the standard Sector 35 products.  When the full Sector of data is processed, it will be released in its entirety at MAST following the normal process, including being made available through the MAST Portal, the MAST APIs, bulk scripts, and TESSCut.

**Questions or Feedback?**

If you have any problems accessing these data at MAST, please email the archive help desk at archive@stsci.edu.
If you have feedback on this early release of quick-look versions of FFI data, including if this will enable new science or greatly enhance your existing science goals, please email the [TESS Guest Investigator Office](mailto:tesshelp@bigbang.gsfc.nasa.gov).