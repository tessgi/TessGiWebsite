Title: Key update archive
Save_as: key_updates_archive.html

[TOC]


Below we outline some of the most important issues or data product modifications. For more details please see the Sector tables provided [here](data_release_notes.html), and the DRNs listed within.


##Cycle 3

- [**Sector 38 (April 2021):**](data_release_notes.html#sector-38)The TESS Input Catalog was updated to v8.2. This new TIC identifies some newly discovered ARTIFACT and DUPLICATE sources that were not flagged in v8.0/8.1. For a description of these anomalies please read Section 1.1 of the [DRN](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_38_drn55_v02.pdf) in addition to [supplemental material](https://outerspace.stsci.edu/display/TESS/TIC+v8+and+CTL+v8.xx+Data+Release+Notes).<p></p>

- <b>Reprocessing of Sectors 1-13 (May 2021)</b>:
- During TESS’s primary mission several updates were made to various instrument models, pipeline algorithms, and pipeline parameters. These adjustments are described below, and were applied to all data during the reprocessing of sectors 1-13. Where appropriate the DRN which describes the specific update, is provided.
	- In Sector 2, the instrument electronics model Reference Flux was updated ([DRN1](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_01_drn01_v02.pdf)). The first two overclock rows were removed from the calculation of the 1D bias correction in the CAL module ([DRN2](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_02_drn02_v02.pdf)).
	- In Sector 5, the algorithm in the CAL module that removes the 1D bias from raw pixel data was changed. The 1D bias estimate is now split into two components, a time-dependent scalar correction and a static row-dependent correction. Parameters to calibrate PDC goodness metrics were also finalized in the PDC module ([DRN7](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_05_drn07_v02.pdf)).
	- In Sector 8, the instrument PRF model was updated ([DRN10](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_08_drn10_v02.pdf)). The updated PRF model corresponds to improved performance in the spacecraft’s Attitude Control System starting in Sector 4.
	- In Sector 10, the instrument linearity model was updated ([DRN14](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_10_drn14_v02.pdf)).
	- In Sector 14, the algorithm in the TPS module for searching for transiting planets was changed. An initial run of TPS is now used to identify problematic epochs that are assigned “deemphasis weights” in a second and final run of TPS ([DRN19](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_19_drn26_v02.pdf)).
	- In Sector 20, the photometric apertures for stars with Tmag < 11 were slightly increased in the COA module. Additionally the layout and annotations of DV reports was refined through the TESS primary mission, and were finalized in Sector 20 ([DRN27](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_20_drn27_v03.pdf)).
	- In Sector 27, the algorithm in the CAL module that propagates uncertainty from the 2D bias model was changed. This uncertainty is a static term and is no longer applied to the pixel data or subsequent processing in the pipeline. Note that this change was not applied to Sectors 14–26, which were processed with version 4.0 of the science processing pipeline. Additionally, the algorithm in the PA module that estimates the sky background was changed. A scalar offset is now applied that forces the dimmest background-corrected pixels to values near zero, if those pixels were significantly 1 negative. Note that this change was not applied to Sectors 14–26, which were processed with version 4.0 of the science processing pipeline ([DRN38](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_27_drn38_v02.pdf)).
- Targets from Sectors 1–13 were reprocessed with version 8 of the TESS Input Catalog (TIC), consistent with Sectors 14–26. TIC 8 is based on Gaia DR2 rather than 2MASS, and includes significantly more stars and improved stellar parameters. The change in TIC version affects the apertures assigned to individual targets, the calculations of crowding and flux fraction reported in the CROWDSAP and FLUXFRAC keywords, and the physical properties of TCEs derived from stellar parameters.
- The timestamps for data from Sectors 1-13 have been updated. The drift error seen in sectors 1-6 has been removed ([DR42](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_reprocessing-sector_1_13_drn42_v02.pdf) and DRN46). Adjustments to timestamps for electronic effects were also applied (DR30). All data from Sector 1–36 are now reported in a consistent time system.
- New data flags were applied to Sectors 1-13 consistent with those described in [DRN30](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_reprocessing-sector_14_19_drn30_v02.pdf).These flags are primarily used to mitigate the effects of scattered light. They are applied per target rather than per CCD, and improve the contrending and planet search for the reprocessed data.
- All ”Manual Exclude” flags are now set in a consistent way for the reprocessed data, using a pointing excursion threshold of 7 arcseconds measured from the spacecraft’s fine pointing system ([DRN5](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_04_drn05_v04.pdf)).
- The planet search of the reprocessed light curves produced a different set of TCEs from the original processed data. Although there is a high degree of overlap between the original and reprocessed data, new TCEs were produced in [DR42](https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_reprocessing-sector_1_13_drn42_v02.pdf) and DR46, and not every TCE from previous data releases was recovered. To differentiate between the initial release and this reprocessed data a "pipeline instance number" is included in the filenames of the dv-timeseries, dv-reports, ad dv-result xml files. Larger pin numbers indicate later versions of the software were used to produce the data products. The DR number is also included as a keyword in the export product headers (DATAREL).
	
- [**Sector 32 (January 2021):**](data_release_notes.html#sector-32) Approximately 26 hrs lost due to a star tracker anomaly.<p></p>
- [**Sector 31 (December 2020):**](data_release_notes.html#sector-31) Approximately 4 days lost due to a star tracker anomaly.<p></p>
- [**Sector 30 (November 2020):**](data_release_notes.html#sector-30) As of Sector 30, co-trending basis vector (CBV) files only include the first eight principal components for the Single Scale co-trending mode. <p></p>
- [**Sector 27 (September 2020):**](data_release_notes.html#sector-27) This is the first data release for the extended mission. Key changes have occurred including the collection of 10-min FFI data instead of 30-min, and 20-second target pixel files.<p></p>
	- The background correction was updated for the extended mission, with the new method providing improved results for fainter and crowded stars. 
	- For targets observed in both Year 1 and Year 3, Year 3 processing was done using TIC 8.1 while TIC 7 was used for Year 1 processing; this may result in differences in results for certain targets.<p></p>

##Cycle 2
- [**Sector 26:**](cycle2_drn.html#sector-26) The TESS spacecraft configuration file was updated from version ‘0187’ to ‘0188’ between orbit 59 and 60. This update results in different naming convention between the FFIs for the two orbits.<p></p>
- [**Sector 22:**](cycle2_drn.html#sector-22) Four FFI cadences and two 2-minute cadences were lost due to computer issues. 
	<p>A ~2 second error in data product timestamps has been corrected for starting with Sector 22. Previous data products will be corrected as they are reprocessed.</p>
- [**Sector 21:**](cycle2_drn.html#sector-21) The FFI timestamps have been adjusted by ~0.5 seconds due to staggered readouts.
- [**Sector 20:**](cycle2_drn.html#sector-20) The FFI timestamps have been adjusted by ~0.5 seconds due to staggered readouts.<p></p>
The assigned timestamps of the previously released data products are too large by 2 seconds, the Sector 20 data products have been updated and have accurate timestamps.<p></p>
The photometric apertures for targets with Tmag < 11 were slightly increased. This change most noticeably affects the light curves of saturated stars, which had higher flux losses during periods of increased pointing jitter using the smaller apertures
- [**Sector 19:**](http://localhost:8000/cycle2_drn.html#sector-19) In orbit 46—no data were collected for four minutes due to an instrument reset.<p></p>
The FFI timestamps for Sector 19 do not account for the 0.5 second staggered readouts of the four cameras. The offsets for each camera can be added to the TSTART and TSTOP header values in the FFIs to correct the issue.
- [**Sector 18:**](cycle2_drn.html#sector-18) Due an eclipse of  the spacecraft by the Earth no data was taken for 6.2hrs in orbit 43.<p></p>
The FFI timestamps for Sector 18 are incorrect. The readouts of the four cameras are staggered by 0.5 sec.
- [**Sector 17:**](cycle2_drn.html#sector-17) An instrument reset occurred in orbit 42 resulting in no data being collected for six minutes between TJD 1789.18374 and 1789.18790.
- [**Sector 15:**](cycle2_drn.html#sector-15) A single upset event in the star trackers caused the spacecraft to fall out of fine pointing in orbit 38. The issue lasts for 5 minutes at TJD 1725.93651 (cadences 358907, 358908, and 358909).
- [**Sector 14:**](cycle2_drn.html#sector-14) Sector 14 is the first northern ecliptic hemisphere pointing. It uses an updated SPOC pipeline and makes use of CCD-specific anomaly flags.<p></p>
This sector uses TIC 8, which is based on Gaia DR2 astrometry and photometry, and uses Gaia DR2 parallaxes to inform stellar parameters.<p></p>


##Cycle 1
- [**Sector 13:**](cycle1_drn.html#sector-13) There is a star tracker anomaly that causes the spacecraft to fall out of fine pointing for approximately 1.25 hours from TJD 1665.2983 to 1665.350. During this time, the spacecraft exhibited increased pointing jitter.
- [**Sector 10:**](cycle1_drn.html#sector-10) A new linearity model is used in pixel calibration.
- [**Sector 8:**](cycle1_drn.html#sector-8) At TJD 1531.74, an interruption in communications between the instrument and spacecraft occurred, resulting in the instrument being turned off and a loss of ~3 days of data.
- [**Sector 7:**](cycle1_drn.html#sector-7) The spacecraft clock kernel has been updated. The estimated accuracy of the TJD values in all products associated with this data release is 50 ms.
- [**Sector 5:**](cycle1_drn.html#sector-5) The SPOC pipeline 1-D Black correction has been changed to a two-component model from the polynomial fit that had been used prior. The two components include: a time-varying correction and a static row-by- row correction. 
