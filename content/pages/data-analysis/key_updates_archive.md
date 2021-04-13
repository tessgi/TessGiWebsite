Title: Key update archive
Save_as: key_updates_archive.html

[TOC]


Below we outline some of the most important issues or data product modifications. For more details please see the Sector tables provided [here](data_release_notes.html), and the DRNs listed within.


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
.