Title: Sector 71
Save_as: sector_71.html

[TOC]

TIC ID's that had issues in Sector 71.

##Targets not processed in 2-min pipeline and so missing a light curve:
96868656, 97399295, 245873777, 306349516, 328228602, 336959864, 336960775, 
365228825,
377021610,
380961590,
381002396,
381082274,
408586952,
408626777,
408673267,
408746940,
408835304,
423088367,
620026605,
620035300,
620037161,
620038190,
620055870,
620055974,
620057377,
620057970,
620060715,
620067407,
630507667,
630508026,
630542709,
10002285112


##Targets not processed in 20-sec pipeline and so missing a light curve:
97399295, 337135425, 377021610, 381002396, 408586952, 10002285112

For targets that were not processed with the photometric pipeline, the target pixel files
with original and calibrated pixel data are provided, but no light curves are produced. Note
that the target pixel files do not include a background correction for stars without light
curves. The most common reason for a target to not be processed with the photometric
pipeline is that the target exceeds a brightness threshold (Tmag ≲ 1.8) that results in
large pixel stamps. A target located too close to a very bright star, having a comparably
bright companion, impacted by saturated star bleed trails, or having an error in identifying
a clean background region are less common causes for a target to not be processed with
the photometric pipeline. Visual examination of the target along with custom aperture
selection may be needed for photometric analysis of the impacted targets.

##Targets with aperture warnings in 2-min data: 
91329512, 91329517, 94964412, 155463741, 184842719, 245873777, 423082848, 440755032, 514810889, 800823400

##Targets with aperture warnings in 20-sec data: 
155463741

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.