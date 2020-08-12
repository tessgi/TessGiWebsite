Title: The TESS Extended Mission
Date: 2020-08-12 15:00
Author: Tom Barclay


On July 5, 2020, the two-year TESS Prime Mission came to a close, and the TESS Extended Mission began. Over the next 27 months, TESS will conduct additional observations of the celestial sphere intended to enhance the scientific output of the mission. The Extended Mission will include updates to the data collection modes and the methods of target selection, as well as observations of the ecliptic plane.

## Observations

During the first year of the Extended Mission, TESS will re-observe the southern ecliptic hemisphere. Because of the natural variation in the period of the TESS orbit over time, the fields observed will not overlap exactly with those observed during Year 1: as a result, many targets that fell in the gaps between sectors, cameras, and CCDs during Year 1 will be observed for the first time in Year 3. The details of the pointings during Year 3 can be found on [https://tess.mit.edu/observations](https://tess.mit.edu/observations).

The pointings during the final 15 months of the Extended Mission will cover part of the northern ecliptic hemisphere and ~60% of the ecliptic. The exact details of the ecliptic pointings will be available in the fall of 2020.

## Data Collection Modes

During the Extended Mission, data will be collected from approximately 20,000 targets per sector at two-minute cadence, just as they were during the Prime Mission. The TESS team has added a 20 second data collection mode: up to 1000 targets per sector will be observed at this cadence, of which nominally 400 are photometric calibration targets and 600 are science targets.

For the Extended Mission, the full-frame image (FFI) cadence was reduced from 30 minutes to 10 minutes to enable a broader range of science investigations to be executed using FFI data than was possible with the primary mission cadence. 

## Target Selection

During the Prime Mission, the majority of the two-minute target slots was assigned to stars around which small exoplanets might be found, and the remainder was shared between targets selected by the Guest Investigator (GI) program and Director’s Discretionary Time (DDT) targets. In the Extended Mission, the majority (~80%) of targets per sector will come from GI programs, and the remainder split between DDT targets and exoplanet targets. Exoplanet targets are chosen by the TESS project and include existing TESS Objects of Interest (TOIs) and targets from the original exoplanet Candidate Target List (CTL) that fell into gaps between CCDs or sectors during the Prime Mission: exoplanet targets from Year 1 will generally not be observed at two-minute cadence unless they were a TOI or are included in an accepted GI proposal.

The list of GI selected programs for Year 3 of the TESS Mission (Extended Mission Year 1) is available on the TESS [GI website](https://heasarc.gsfc.nasa.gov/docs/tess/approved-programs.html). Specific two-minute and 20s targets to be observed are determined shortly before the sector begins. The list of GI targets draws from both selected programs and those that were deemed good proposals but were not selected for funding. Targets for each sector are listed on the [MIT website](https://tess.mit.edu/observations/target-lists/), and broken down by GI program on the [GI website](https://heasarc.gsfc.nasa.gov/docs/tess/approved-programs.html). The call for Cycle 4 targets, covering the last 15 months of the Extended Mission, will come out in the fall of 2020, with a proposal deadline in early 2021.

Director’s Discretionary targets are allocated by the TESS PI (George Ricker) after review of the proposed observations.  Requests for DDT targets can be made by email to [tess-ddt@mit.edu](mailto:tess-ddt@mit.edu): details of the procedure and documents required for DDT requests can be found at [https://tess.mit.edu/science/ddt/](https://tess.mit.edu/science/ddt/).

Both two-minute and 20s cadence targets are solicited by the GI and DDT programs.

## Data Processing and Data Products

In the Extended Mission, the FFI and two-minute cadence data will be processed by the Science Processing Operations Center (SPOC) in the same way as in the Prime Mission (see [Jenkins et al. 2016](https://heasarc.gsfc.nasa.gov/docs/tess/docs/jenkinsSPIE2016-copyright.pdf)). The two-minute cadence data will be run through the SPOC’s Transiting Planet Search (TPS) module, and Data Validation (DV) reports will be generated for all Threshold Crossing Events (TCEs). The TESS Science Office at MIT will review all TCEs in a search for signals of transiting planets and release TESS Objects of Interest (TOIs), as was done in the Prime Mission.

The new 20s data products will be processed by SPOC into target pixel and light curve files with the same format as those created from two-minute data. These data will not be run through TPS, so no DV products or reports will be created.

One key difference in the 20s data products is that cosmic-rays are removed in ground processing at SPOC, rather than on orbit, as is done for two-minute data and FFIs. The processed target-pixel data includes a FITS extension that identifies the cosmic ray correction applied for affected pixels along with the (row, column) coordinate and cadence at which the cosmic rays were removed, allowing the observer to revert the data to its raw state and make their own custom corrections, if desired. The collateral pixel data files contain cosmic ray extensions with similar information.

The number of collateral pixels collected is lower in the Extended Mission to preserve space on the on-board solid-state recorder. For two-minute data, all leading black and the first two trailing black pixels will no longer be collected, as these were not useful for measuring CCD bias level during the Prime Mission. For 20s data, collateral pixels will be collected only in the columns and rows in which a target pixel was selected.

During the Prime Mission, data were typically released publicly via the [MAST](https://archive.stsci.edu/tess/) approximately a month after being downlinked to the ground. We anticipate maintaining this timeline during the Extended Mission. However, for the first Extended Mission sector (Sector 27), we are planning to extend the usual timeline between data downlink and public release to allow the mission team time to vet and document the new data collection modes.