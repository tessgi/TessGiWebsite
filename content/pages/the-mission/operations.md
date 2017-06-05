Title: Operations
Save_as: operations.html

[TOC]

## Launch and orbit

TESS  is scheduled for launch via a SpaceX Falcon 9 from Cape Canaveral no earlier than March 20, 2018.  

TESS will observe from a unique High Earth Orbit (HEO) that will provide an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low-Earth orbit. The TESS orbit is elliptical, with nominal perigee and apogee of 17 and 59 Earth radii, respectively, and a 13.7-day period in 2:1 resonance with the Moon’s orbit. The orbit is above Earth’s radiation belts providing a low-radiation environment.

TESS data are returned to Earth during each orbital perigee using the Deep Space Network.

<br/>

<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_orbit_Winnpresentation.png">
*Maneuvers for achieving the TESS mission orbit (shown in light blue). (Ricker et al. 2015)*

<br/>


## Field of view

TESS is equipped with four CCD cameras that have adjacent field-of-views to produce a 4 x 1 array, or 'observing sector', yielding a combined field-of-view of 96 x 24 degrees

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_observingsectorschematic_Winnpresentation.png">
<br/>

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_cameraFOVschematic_Winnpresentation.png">
<br/>

## Observing strategy

TESS will observe the southern and northern ecliptic hemispheres for 1 year each in its 2 year prime mission, beginning in the south. Each hemisphere will be observed with 13 partially overlapping sectors, each covering ecliptic latitudes from 6 degrees to the ecliptic pole. Each  sector will be observed for two orbits (27.4 days) moving eastward until the hemisphere has been tiled by 13 sectors. The 26 observing sectors in the two year mission will cover over 90% of the sky. The sectors overlap at higher latitudes, with over 350 days of continuous coverage in the Continuous Viewing Zone (CVZ) at the ecliptic poles, which corresponds to the region accessible to NASA's upcoming James Webb Space Telescope.


<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_2yearskycoverage.png">
<br/>

## Time sampling

TESS will collect brightness measurements of about 200,000 preselected stars ('postage stamps') every 2 minutes, and Full Frame Images (FFIs) (all pixels) at 30 minute cadence. The TESS cameras have an exposure time of 2 seconds, and the images are stacked for each 2 or 30 minute cadence.



## Science data flow and archive
Data from the TESS spacecraft will be downloaded through the Deep Space Network (DSN) and delivered to the Payload Operations Center (POC) at the Massachusetts Institute ofTechnology (MIT). The POC sends uncalibrated requantized pixel data, target lists, spacecraft configuration and engineering data, and focal plane characterization models (for calibration) to the Science Processing Operations Center (SPOC) at NASA Ames. The SPOC then calibrates the science data in two steps, first by the orbit and then by the sector. The SPOC uses instrument calibration models provided by the POC to calibrate all science data. Once a full sector is calibrated the transiting planet search software is run by the SPOC to identify and flag threshold crossing events (TCE’s). Calibrated target pixels and FFIs, light curves generated from 2-min cadecence targets, and TCE's are sent to the TESS Science Office (TSO, consists of Smithsonian Astrophysical Observatory (SAO) and MIT). The processed data and meta-data from the SPOC are archived at the Mikulski Archive for Space Telescopes (MAST) located at the Space TelescopeScience Institute (STScI). MAST is the primary science data archive for TESS and will provide tools to search and retrieve data from the TESS science data archive. The TSO is responsible for detailed analysis of TCE's and the identification of TESS Objects of Interest (TOIs). The TSO delivers lists of TOIs to MAST along with dispositions and information documenting the vetting process for each TOI on a regular schedule, nominally every four months.




