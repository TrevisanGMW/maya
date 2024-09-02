//Maya ASCII 2023 scene
//Name: skel_biped_poses.ma
//Last modified: Mon, Jun 24, 2024 11:15:36 AM
//Codeset: 1252
requires maya "2023";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202405151550-05a853e76d";
fileInfo "osv" "Windows 11 Pro v2009 (Build: 22631)";
fileInfo "UUID" "03F1E29B-439D-5E3C-AEE1-149C63B34690";
createNode joint -n "C_root_JNT";
	rename -uid "1EDE203B-490D-198A-CB8A-1EAC29E1D707";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.77114505347442108;
createNode joint -n "C_hips_JNT" -p "C_root_JNT";
	rename -uid "DFD9CA35-4767-035C-4CC8-EF9D835B6EE9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 0 103.34534728425831 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 90 0 90 ;
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 103.31450653076175 0 1;
	setAttr ".radi" 1.9278626336860527;
createNode joint -n "L_upperLeg_JNT" -p "C_hips_JNT";
	rename -uid "91C79500-457F-BA02-DDEF-53B1817B598F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -2.8754497942558004 0 10.250824075415816 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018159649943283555 -0.99949309688237409 -0.026149118501747934 0
		 1.0210002789859567e-06 -0.026153412665838469 0.99965794100026428 0 -0.99983509996043596 -0.018153464969845691 -0.00047391633610310364 0
		 10.250824075415816 100.43905673650595 0 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_lowerLeg_JNT" -p "L_upperLeg_JNT";
	rename -uid "6C175ABE-47E9-FE83-6F3D-E4998FCAF202";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 44.485311800062036 5.2252795127396e-15 -1.5987211554602254e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.0000000000000027 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.01815610703232675 -0.99845241517638095 -0.052565486831973138 0
		 0.00059749713167521587 -0.052563308536415609 0.99861741502583623 0 -0.99983498577245644 -0.018162412399161762 -0.00035777260157829707 0
		 11.058661765322755 55.976294679683946 -1.1632516898470273 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_foot_JNT" -p "L_lowerLeg_JNT";
	rename -uid "4E7918DF-4918-2241-5B57-7BA75A419E24";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 46.810241652265823 6.6613381477509392e-15 -6.2172489379008766e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.000000000000008 ;
	setAttr ".bps" -type "matrix" 0.018156107394490421 -0.99845244703692981 -0.052564881529844044 0
		 0.00059748612652948973 -0.052562703334299556 0.99861744688770526 0 -0.99983498577245644 -0.018162412399161762 -0.00035777260157829707 0
		 11.90855352297042 9.238495846989089 -3.6238548310206884 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_ball_JNT" -p "L_foot_JNT";
	rename -uid "64B53FD8-4833-87CC-4DEE-78818D5ECA42";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 5.635757490447892 13.547156637101248 0.11035332316931168 ;
	setAttr ".r" -type "double3" 1.3487539696081226e-13 1.2602637324256179e-15 -8.9453100416161387e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.0408881951410527 0.00061370209481448877 91.943344199823215 ;
	setAttr ".bps" -type "matrix" -7.8444957398895514e-06 -0.018673504796261044 0.99982563487694598 0
		 4.9545244643067754e-10 0.99982563490770859 0.018673504796839453 0 -0.99999999996923183 1.4697959488385592e-07 -7.8431186818287953e-06 0
		 11.908636066059918 2.8973805318404233 9.6082897362973601 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_toe_JNT" -p "L_ball_JNT";
	rename -uid "DE2D9442-4A41-246A-A845-A8A70E320D8A";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0 0 ;
	setAttr ".t" -type "double3" 10.215816652113086 2.6645352591003757e-15 1.2434497875801753e-14 ;
	setAttr ".r" -type "double3" 1.3487539696081226e-13 1.2602637324256179e-15 -8.9453100416161387e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -7.8444957398895514e-06 -0.018673504796261044 0.99982563487694598 0
		 4.9545244643067754e-10 0.99982563490770859 0.018673504796839453 0 -0.99999999996923183 1.4697959488385592e-07 -7.8431186818287953e-06 0
		 11.90855592812971 2.7066154305894687 19.822325106282783 1;
	setAttr ".radi" 0.77114505347442108;
	setAttr ".oclr" -type "float3" 1 0 0 ;
	setAttr ".nts" -type "string" "This is an end joint. This means that this joint shouldn't be an influence when skinning.";
createNode joint -n "L_lowerLegTwist01_JNT" -p "L_lowerLeg_JNT";
	rename -uid "48D3FBF8-47AE-75BD-AE2A-44A21F6741ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 15.603299191204819 2.0382410327979272e-05 8.8817841970012523e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.7460266350512111e-05 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018156107032326896 -0.99845241517638084 -0.052565486831973512 0
		 0.00059749713167554677 -0.052563308536415963 0.99861741502583612 0 -0.99983498577245633 -0.018162412399161609 -0.00035777260157798449 0
		 11.341956950180256 40.397142109962324 -1.9834467505323612 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_lowerLegTwist02_JNT" -p "L_lowerLeg_JNT";
	rename -uid "88D72EF2-42B4-BB74-1CAA-F783A8CAAA7C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 31.206599191201501 1.0180894986611122e-05 -1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.746026635051201e-05 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018156107032326896 -0.99845241517638084 -0.05256548683197354 0
		 0.0005974971316755472 -0.052563308536415991 0.99861741502583612 0 -0.99983498577245633 -0.018162412399161609 -0.00035777260157798449 0
		 11.625252135037762 24.817989540240706 -2.8036418112176928 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_lowerLegTwist03_JNT" -p "L_lowerLeg_JNT";
	rename -uid "2CBDD1BF-4665-7C22-97CC-48B5E4ED1B57";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 46.809999191198145 -2.0685742896375814e-08 -8.8817841970012523e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.7460266353692747e-05 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018156107032326896 -0.99845241517638084 -0.052565486831973568 0
		 0.00059749713167554775 -0.052563308536416019 0.99861741502583612 0 -0.99983498577245633 -0.018162412399161609 -0.00035777260157798449 0
		 11.908549135505972 9.2387371252775665 -3.6238421284517077 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperLegTwist01_JNT" -p "L_upperLeg_JNT";
	rename -uid "DC278C63-4508-632D-0396-F3916C8A6586";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -2.1191937094044988e-12 0 ;
	setAttr ".r" -type "double3" -6.361109362927032e-15 -1.2722218725854067e-14 -9.5416640443905503e-15 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.9418761294741617e-05 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018159649943283451 -0.9994930968823742 -0.026149118501747993 0
		 1.0210002791511805e-06 -0.02615341266583851 0.99965794100026406 0 -0.99983509996043562 -0.018153464969845517 -0.00047391633610293607 0
		 10.25082407541581 100.43905673650596 -6.8894889682711741e-17 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperLegTwist02_JNT" -p "L_upperLeg_JNT";
	rename -uid "6D7EE55B-460F-B727-30CF-9E8A814EDE1C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 14.828329999996512 1.0201698699106963e-05 -8.8817841970012523e-15 ;
	setAttr ".r" -type "double3" 1.7655625192200634e-31 -6.3611093629270335e-15 -3.1805546814635168e-15 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 1.7502849951421205e-05 3.4623519499325072e-05 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018159649943283451 -0.9994930968823742 -0.026149118501747993 0
		 1.0210002791511805e-06 -0.02615341266583851 0.99965794100026406 0 -0.99983509996043562 -0.018153464969845517 -0.00047391633610293607 0
		 10.520101357459296 85.61824326321215 -0.38774775835302461 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperLegTwist03_JNT" -p "L_upperLeg_JNT";
	rename -uid "457E3ED3-4B8F-5552-7418-06A5A6E2A3D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 29.656659999992996 2.0403399517851725e-05 -1.5987211554602254e-14 ;
	setAttr ".r" -type "double3" 6.361109362927032e-15 6.361109362927032e-15 -1.9083328088781101e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.2317440787257207e-28 1.7564992455200907e-05 3.4746447605166279e-05 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018159649943283451 -0.9994930968823742 -0.026149118501747993 0
		 1.0210002791511805e-06 -0.02615341266583851 0.99965794100026406 0 -0.99983509996043562 -0.018153464969845517 -0.00047391633610293607 0
		 10.789378639502786 70.79742978991834 -0.77549551670604855 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperLeg_JNT" -p "C_hips_JNT";
	rename -uid "B699E55E-4056-1D42-E6CF-5599C926B1EA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -2.8754497942558004 0 -10.250824075415816 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.01816282075241217 0.99949302218403979 0.026149771466117969 0
		 -2.2257782703155576e-06 0.02615412620142275 -0.99965792233027706 0 -0.99983504236317011 0.018156549453420483 0.0004772573559825172 0
		 -10.250824075415816 100.43905673650595 0 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_lowerLeg_JNT" -p "R_upperLeg_JNT";
	rename -uid "C6121F66-48DF-40D4-41B9-6AABA9D6E293";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -44.485311800061893 -6.8156775771823734e-15 -2.3092638912203256e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.0000000000000027 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018153094006779346 0.9984525025960147 0.052564866952521938 0
		 0.00059431213359552012 0.052562745323406386 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654669 0.00036078401999857339 0
		 -11.058802819755487 55.976298002662752 -1.1632807371706126 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_foot_JNT" -p "R_lowerLeg_JNT";
	rename -uid "58178B56-452F-0871-0CB2-6E90AEBDC3C7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -46.810241652265958 -1.4654943925052066e-14 1.4210854715202004e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 2.9999999999999947 ;
	setAttr ".bps" -type "matrix" 0.018153094006779346 0.9984525025960147 0.05256486695252182 0
		 0.00059431213359551795 0.052562745323406268 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654669 0.00036078401999857339 0
		 -11.908553536949141 9.2384950778336119 -3.6238548616373576 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_ball_JNT" -p "R_foot_JNT";
	rename -uid "4439559B-450D-4B6F-6954-88998C1AC02F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -5.6357574857569315 -13.547156637855489 -0.11035347015034169 ;
	setAttr ".r" -type "double3" 3.1030286611028435e-13 1.2722218725854054e-14 4.5720473546038399e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.0407094222516615 0.0011268561608820545 91.943344489884666 ;
	setAttr ".bps" -type "matrix" -1.9598161124935359e-06 0.018673377209547828 -0.999825637288697 0
		 1.2390526452077388e-10 -0.99982563729061713 -0.018673377209584043 0 -0.99999999999807998 -3.6720269186441001e-08 1.9594720799182334e-06 0
		 -11.908575945448527 2.8973792331999935 9.6082894521791289 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_toe_JNT" -p "R_ball_JNT";
	rename -uid "AFD5C08B-40DF-5B5B-1394-44B30430BA9A";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0 0 ;
	setAttr ".t" -type "double3" -10.215816652113055 1.7763568394002505e-14 -4.4408920985006262e-14 ;
	setAttr ".r" -type "double3" 3.1030286611028435e-13 1.2722218725854054e-14 4.5720473546038399e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1.9598161124935359e-06 0.018673377209547828 -0.999825637288697 0
		 1.2390526452077388e-10 -0.99982563729061713 -0.018673377209584043 0 -0.99999999999807998 -3.6720269186441001e-08 1.9594720799182334e-06 0
		 -11.908555924326409 2.7066154353514911 19.822324846802545 1;
	setAttr ".radi" 0.77114505347442108;
	setAttr ".oclr" -type "float3" 1 0 0 ;
	setAttr ".nts" -type "string" "This is an end joint. This means that this joint shouldn't be an influence when skinning.";
createNode joint -n "R_lowerLegTwist01_JNT" -p "R_lowerLeg_JNT";
	rename -uid "A8FAC63A-4510-591A-2B3C-9CA157A57B1D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -15.603299999999997 2.6645352591003757e-15 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018153094006779374 0.99845250259601448 0.052564866952522382 0
		 0.0005943121335959848 0.052562745323406823 -0.99861744657158591 0 -0.99983504238002663 0.0181592363226558 0.0003607840199981158 0
		 -11.342050991471472 40.397144068906357 -1.9834661256909196 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_lowerLegTwist02_JNT" -p "R_lowerLeg_JNT";
	rename -uid "E509BB9B-46AC-0B22-638C-1E980A0A36B7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -31.2066 1.3322676295501878e-15 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018153094006779374 0.99845250259601448 0.052564866952522382 0
		 0.0005943121335959848 0.052562745323406823 -0.99861744657158591 0 -0.99983504238002663 0.0181592363226558 0.0003607840199981158 0
		 -11.625299163187453 24.817990135149969 -2.8036515142112122 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_lowerLegTwist03_JNT" -p "R_lowerLeg_JNT";
	rename -uid "8A12DC4B-4E7B-71C8-9E58-BA917363B5A9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -46.81000000000008 4.4408920985006262e-16 -1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".bps" -type "matrix" 0.018153094006779374 0.99845250259601448 0.052564866952522382 0
		 0.0005943121335959848 0.052562745323406823 -0.99861744657158591 0 -0.99983504238002663 0.0181592363226558 0.0003607840199981158 0
		 -11.908549150212835 9.2387363561433133 -3.6238421592182002 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperLegTwist01_JNT" -p "R_upperLeg_JNT";
	rename -uid "CF381662-4BE8-A4A2-34E5-B88510C53754";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 0 4.4408920985006163e-16 -1.7763568394002505e-15 ;
	setAttr ".r" -type "double3" 0 0 -1.272221872585407e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018162820752412431 0.99949302218403968 0.026149771466118247 0
		 -2.225778270309982e-06 0.026154126201423013 -0.99965792233027706 0 -0.99983504236317022 0.018156549453420517 0.00047725735598252268 0
		 -10.250824075415816 100.43905673650593 7.5429159086893461e-16 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperLegTwist02_JNT" -p "R_upperLeg_JNT";
	rename -uid "477CA852-4E92-671F-1172-66BD9D663060";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -14.82832999999998 3.9264310552899931e-16 -1.7763568394002505e-15 ;
	setAttr ".r" -type "double3" 0 0 -1.272221872585407e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018162820752412431 0.99949302218403968 0.026149771466118247 0
		 -2.225778270309982e-06 0.026154126201423013 -0.99965792233027706 0 -0.99983504236317022 0.018156549453420517 0.00047725735598252268 0
		 -10.520148375263437 85.618244370863678 -0.38775744072418472 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperLegTwist03_JNT" -p "R_upperLeg_JNT";
	rename -uid "87C735FE-47DE-4655-17CF-7E9AD6C73359";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -29.656659999999988 3.41197001207937e-16 -1.7763568394002505e-15 ;
	setAttr ".r" -type "double3" 0 0 -1.272221872585407e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".bps" -type "matrix" 0.018162820752412431 0.99949302218403968 0.026149771466118247 0
		 -2.225778270309982e-06 0.026154126201423013 -0.99965792233027706 0 -0.99983504236317022 0.018156549453420517 0.00047725735598252268 0
		 -10.789472675111057 70.79743200522141 -0.77551488144837011 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "C_spine01_JNT" -p "C_hips_JNT";
	rename -uid "6029A2CA-4039-C7C7-762F-B59566F6E457";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 8.9815018984766226 0 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 112.29600842923837 0 1;
	setAttr ".radi" 1.9278626336860527;
createNode joint -n "C_spine02_JNT" -p "C_spine01_JNT";
	rename -uid "F75617AC-4D9D-B3B1-D3A2-2BB8AA885922";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 12.051947200161649 1.1664122257998452e-16 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 124.34795562940002 1.1664122257998452e-16 1;
	setAttr ".radi" 1.9278626336860527;
createNode joint -n "C_spine03_JNT" -p "C_spine02_JNT";
	rename -uid "71BBA91B-494F-EC1A-398E-75A117FF7400";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 10.950878550191902 -5.2793890417247838e-15 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 135.29883417959192 -5.1627478191447992e-15 1;
	setAttr ".radi" 1.9278626336860527;
createNode joint -n "L_clavicle_JNT" -p "C_spine03_JNT";
	rename -uid "11E32F42-40AE-8977-73AF-FE81A348C2FD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 17.12096460700613 8.897747231229418e-15 3.0000000000000004 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999943 -68.170229709586209 -90 ;
	setAttr ".bps" -type "matrix" 0.92827745102459658 -0.0057398191852651159 -0.37184409151551379 0
		 -0.37185021696614146 9.4368957093138266e-16 -0.92829274269609208 0 0.0053282324940698844 0.99998352710218197 -0.0021343530093863852 0
		 3.0000000000000004 152.41979878659805 3.7349994120846188e-15 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_upperArm_JNT" -p "L_clavicle_JNT";
	rename -uid "D130D401-4627-B729-33C7-1A9E364198D1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 15.384392355224897 1.1990408665951691e-14 3.979039320256561e-13 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -21.829770290413791 ;
	setAttr ".bps" -type "matrix" 0.80417589873551287 -0.59438396874882871 -0.0029701157083974567 0
		 -0.003693340543622354 5.5077470362263625e-16 -0.99999317959455514 0 0.59437991480917229 0.80418138357859992 -0.0021952624102588364 0
		 17.280984521070454 152.33149515620448 -5.7205953988468305 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_lowerArm_JNT" -p "L_upperArm_JNT";
	rename -uid "AC422C25-47E8-7C8D-F366-BA96579A08DA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 30.350649617122833 -1.0418332863082469e-12 -5.6843418860808015e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -0.2 ;
	setAttr ".bps" -type "matrix" 0.73539834240599866 -0.54103722910382024 0.40800489544877977 0
		 0.32544794906083802 -0.24612154125310989 -0.91296649411864372 0 0.59436765594924812 0.80417840287765374 -0.0049179168905496493 0
		 41.688245454126559 134.29155558267351 -5.8107403400336626 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_hand_JNT" -p "L_lowerArm_JNT";
	rename -uid "3DB74D05-434A-885F-1AFB-43B8F2B7DF95";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 29.260659756082042 5.595524044110789e-14 -6.5369931689929217e-13 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 0.20000000000000318 ;
	setAttr ".bps" -type "matrix" 0.62008096390219802 -0.68156193053703096 0.38855235560829671 0
		 0.38275973751099335 -0.16950411611781901 -0.90816481871939525 0 0.68483179069508493 0.71185791381549746 0.15576818992211244 0
		 63.206486136455169 118.46044930649308 6.1277520845088613 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "L_thumb01_JNT" -p "L_hand_JNT";
	rename -uid "BCEF5641-496F-6AEF-D677-2E90D171C325";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.0330070101521898 -3.1783308274265085 -1.7525546123307834 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 170 25.000000000000011 -25.000000000000011 ;
	setAttr ".bps" -type "matrix" -0.27106708400438051 -0.63456770130799978 0.7237723871674322 0
		 -0.46475174607187836 0.74475299881354451 0.47890373279122878 0 -0.8429284966665338 -0.20655944232814422 -0.49679447087561618 0
		 62.670453860149948 115.68443748077262 9.91969008289756 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_thumb02_JNT" -p "L_thumb01_JNT";
	rename -uid "134D2169-4D09-B178-EF2B-929AC0D0CAA8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.4411660968214735 1.3855583347321954e-13 -1.9895196601282805e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.15610830560490241 -0.65932648686930651 0.73547180818420543 0
		 -0.69715136444100245 0.45393243919056198 0.55491018706503759 0 -0.69972149601053069 -0.59936126364913256 -0.38878773599189043 0
		 61.737667000709962 113.50078462089374 12.410311083433813 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_thumb03_JNT" -p "L_thumb02_JNT";
	rename -uid "EB75BEA2-4BCE-E4EC-A00C-6180B4D04BB3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.6975205785490779 7.0166095156309893e-14 1.1368683772161603e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.081680974274693702 -0.74100759328523047 0.6665102888441915 0
		 -0.70698918777222874 0.42828393933551828 0.56279583836451219 0 -0.70249164181127544 -0.51718528014714493 -0.48890170707864983 0
		 62.158772367561454 111.72223785458118 14.394261420953395 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_pinky_meta_JNT" -p "L_hand_JNT";
	rename -uid "C133885F-4B14-F82D-A465-F5A0D47CEFF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.5569999999997179 3.7279999999999527 -0.27699999999990155 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.61390804362397966 -0.73015603857474876 0.29998178829156935 0
		 0.78924277487836259 0.56073174706275819 -0.25035125351843035 0 0.014586167285497664 0.39045110727052207 0.92050810781608106 0
		 67.26942498437559 114.52547560202179 4.4695989362214386 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_pinky01_JNT" -p "L_pinky_meta_JNT";
	rename -uid "EAEF9C5C-4A4B-CE2B-7049-1787E6BC46DA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.3084338330970269 -0.31243273655044845 0.3668743761459865 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.50020916339506971 -0.79997810355277466 0.33139979887095644 0
		 0.86578174881405545 0.45561273760434856 -0.20697583615762233 0 0.014586167285497664 0.39045110727052207 0.92050810781608106 0
		 69.059265137376883 112.07785821275083 5.8779975989461706 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_pinky02_JNT" -p "L_pinky01_JNT";
	rename -uid "6339B086-4740-F767-98B6-41AE4A992148";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.7376223054287436 -2.8421709430404007e-14 1.8474111129762605e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.25990565222729112 -0.89044218578225343 0.37357966448888635 0
		 0.96552384520747392 0.23379616466175321 -0.1144685883778971 0 0.014586167285497664 0.39045110727052207 0.92050810781608106 0
		 70.428648900467024 109.88782031261023 6.7852450803500837 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_pinky03_JNT" -p "L_pinky02_JNT";
	rename -uid "0A969D2D-4419-9917-3A16-AF89966D2D67";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.2943363456668777 1.7053025658242404e-13 4.7961634663806763e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.075398416111184308 -0.91841447020119227 0.38836830428471841 0
		 0.99704680059255202 0.063740048292153795 -0.042835542156831677 0 0.014586167285497664 0.39045110727052207 0.92050810781608106 0
		 71.024959884816525 107.84484644205502 7.6423624825890029 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_ring_meta_JNT" -p "L_hand_JNT";
	rename -uid "4392E4C0-438E-4D2A-5744-92A9B989776F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.659999999999684 1.8899999999999348 0.76000000000001933 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90 0 0 ;
	setAttr ".bps" -type "matrix" 0.57582335505632243 -0.72287525888694248 0.381940864350512 0
		 0.79967423130927595 0.5951994665784679 -0.07911206459590292 0 -0.17014284455009987 0.35098284156614135 0.92079447075585619 0
		 67.339951493063026 115.50501994522764 6.3403583786045612 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_ring01_JNT" -p "L_ring_meta_JNT";
	rename -uid "337A7B6D-412A-3C0E-55B5-0CB7BFEBE107";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.6385194145720305 -0.13607294733967024 -0.00038684019187407159 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.4890802159544308 -0.78113055816224797 0.38811801487060887 0
		 0.8554834626165303 0.51637786167814337 -0.03875498881873609 0 -0.17014284455009987 0.35098284156614135 0.92079447075585619 0
		 69.326347738324245 112.79369796151163 7.7404664402522751 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_ring02_JNT" -p "L_ring01_JNT";
	rename -uid "CFFA0BBD-4412-286C-4615-0C9D74F7311D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8599716183124855 1.4210854715202004e-13 -3.5527136788005009e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.28399152673820749 -0.8736446591955277 0.39508710710428407 0
		 0.943677362049687 0.32763139637235117 0.046159554439444278 0 -0.16976998879615496 0.35972583667319963 0.91748322782158798 0
		 71.214183490986642 109.77855617680883 9.2385909622085745 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_ring03_JNT" -p "L_ring02_JNT";
	rename -uid "55EA5FCC-4992-BF8D-035B-F089BD077B0B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.7281147574064448 0 9.9475983006414026e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.033357313033973157 -0.92836675893085474 0.37016543677033603 0
		 0.98491900203585658 0.093447757287088873 0.14560932692209799 0 -0.16976998879615496 0.35972583667319963 0.91748322782158798 0
		 71.98894496605952 107.39515328932823 10.316433929560867 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_middle_meta_JNT" -p "L_hand_JNT";
	rename -uid "B2AD1207-4F6F-93FC-058D-BC90E0F090C8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.7489999999996542 -0.37000000000008271 1.4700000000001125 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 0.47420450304376427 -0.77912609826477974 0.40999099050554427 0
		 0.84129395719823341 0.53827446075763796 0.049850601579232073 0 -0.25952758403444082 0.32128356306972022 0.91072625153032172 0
		 67.016332263469025 116.33285935464521 8.5379874434042584 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_middle01_JNT" -p "L_middle_meta_JNT";
	rename -uid "C298428C-4964-E8C5-7A0B-70A93ECF5C20";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.1497049935343995 0.03980994166707319 0.0027520440324897422 ;
	setAttr ".r" -type "double3" -5.5173828725626983e-33 -3.1805546814635168e-15 1.987846675914698e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.47420450304376427 -0.77912609826477974 0.40999099050554427 0
		 0.84129395719823341 0.53827446075763796 0.049850601579232073 0 -0.25952758403444082 0.32128356306972022 0.91072625153032172 0
		 69.016918689727973 113.12202875547885 10.243820012295915 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_middle02_JNT" -p "L_middle01_JNT";
	rename -uid "A453725D-440F-394C-D03C-2C98AD4E3072";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.3953968914290016 -5.6843418860808015e-14 -7.9936057773011271e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.27211618524137399 -0.88209736066926447 0.3845218173654123 0
		 0.9272633184408301 0.34716735534821369 0.14020544088810191 0 -0.25716827176730428 0.31840080665859583 0.91240638221977211 0
		 71.101235688308094 109.69746032513459 12.045893137477869 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_middle03_JNT" -p "L_middle02_JNT";
	rename -uid "0C58A10D-4BF3-E270-2858-9F8A6642EFBB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.6033506852285058 4.2632564145606011e-13 9.7699626167013776e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.024421448323835322 -0.94908781025167199 0.31406356250519119 0
		 0.96642993937575139 0.10278841186725152 0.23547338419445563 0 -0.2557670133929465 0.29776982858828099 0.91973711681249304 0
		 71.809649545618385 107.40105155679817 13.046938274201493 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_index_meta_JNT" -p "L_hand_JNT";
	rename -uid "BFC74590-4EF6-D539-60DC-C3B2DDC7A7BD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.8119999999996139 -2.537000000000063 1.2339999999998383 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.49259522800281419 -0.7376655950049944 0.461735217732829 0
		 0.76654808758932225 0.61897608083283573 0.17109249185740225 0 -0.41201210026164059 0.26966290308967267 0.8703608147976567 0
		 66.064336710404291 116.48923790498806 10.493698111150813 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_index01_JNT" -p "L_index_meta_JNT";
	rename -uid "03761A6B-49CE-DB5C-798E-8AAC609764B2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8841418335244953 0.058187307654094411 0.007985052246887836 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.46201126569155671 -0.7614800761046181 0.45463577077677336 0
		 0.78536082128667306 0.58943194042480829 0.18915170629673819 0 -0.41201210026164059 0.26966290308967267 0.8703608147976567 0
		 68.018959873741835 113.66220993229359 12.304048474399261 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_index02_JNT" -p "L_index01_JNT";
	rename -uid "33F2EE19-4D1A-BF90-8BB4-12A9FCAAEA71";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8337976624461731 8.5265128291212022e-14 -4.8849813083506888e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.15090576000109612 -0.921818116681555 0.35704175015838502 0
		 0.89859528200212768 0.27844798159606188 0.33910653297834836 0 -0.41201210026164059 0.26966290308967267 0.8703608147976567 0
		 69.790217584174002 110.74284939652445 14.047030029667685 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_index03_JNT" -p "L_index02_JNT";
	rename -uid "A159BD15-437D-EC68-DB70-52A918C9263A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.3509375903510659 8.5265128291212022e-14 3.6859404417555197e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.058559525480017943 -0.94539234078712098 0.32063079071823897 0
		 0.90929467787596063 0.18307168180332473 0.37372175225447496 0 -0.41201210026164059 0.26966290308967267 0.8703608147976567 0
		 70.144987607961141 108.57571253455119 14.886412901439828 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "L_weapon_parent_JNT" -p "L_hand_JNT";
	rename -uid "A9B2CDCB-41FF-F8E2-9016-65BD437777B6";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".t" -type "double3" 8.9999999999998579 -3.730349362740526e-14 -5.9999999999999147 ;
	setAttr ".r" -type "double3" 1.5902773407317584e-15 6.3611093629270335e-15 -1.5902773407317584e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "L_weapon_child_JNT" -p "L_weapon_parent_JNT";
	rename -uid "5CD40935-4A51-DAAD-6E8F-53921844F23E";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".t" -type "double3" -2.1316282072803006e-13 -8.8817841970012523e-16 3.979039320256561e-13 ;
	setAttr ".r" -type "double3" 1.5902773407317584e-15 6.3611093629270335e-15 -1.5902773407317584e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "L_lowerArmTwist03_JNT" -p "L_lowerArm_JNT";
	rename -uid "FA84D5F0-4CD9-4476-586E-58899469B3ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 29.261000000000102 -8.8817841970012523e-16 -4.8316906031686813e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599877 -0.54103722910382124 0.40800489544878082 0
		 0.32544794906083807 -0.24612154125311098 -0.91296649411864372 0 0.59436765594924801 0.80417840287765341 -0.0049179168905501757 0
		 63.20673635126834 118.46026522186656 6.1278909056931159 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_lowerArmTwist02_JNT" -p "L_lowerArm_JNT";
	rename -uid "ED46245E-4CC7-D994-169F-799C2D46D2AD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 19.507000000000112 -1.3322676295501878e-14 -4.5474735088646412e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599877 -0.54103722910382124 0.40800489544878082 0
		 0.32544794906083807 -0.24612154125311098 -0.91296649411864372 0 0.59436765594924801 0.80417840287765341 -0.0049179168905501757 0
		 56.033660919440251 123.73754235454525 2.1482111554857166 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_lowerArmTwist01_JNT" -p "L_lowerArm_JNT";
	rename -uid "4DD280E2-4517-41DC-FCF8-02A59ECDCFBE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 9.7540000000001044 -1.7763568394002505e-14 -4.8316906031686813e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599877 -0.54103722910382124 0.40800489544878082 0
		 0.32544794906083807 -0.24612154125311098 -0.91296649411864372 0 0.59436765594924801 0.80417840287765341 -0.0049179168905501757 0
		 48.861320885954527 129.0142784499948 -1.8310605898262451 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperArmTwist01_JNT" -p "L_upperArm_JNT";
	rename -uid "FB1A4C3C-42F3-7119-94B2-25BA13DAE171";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 0 0 4.2632564145606011e-13 ;
	setAttr ".r" -type "double3" -2.0673605429512861e-14 9.5416640443905503e-15 -3.1805546814635183e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 -0.59438396874882904 -0.0029701157083969532 0
		 -0.0036933405436224667 -4.5519019260015543e-16 -0.99999317959455603 0 0.59437991480917218 0.80418138357859925 -0.0021952624102596252 0
		 17.28098452107028 152.33149515620448 -5.7205953988468243 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperArmTwist02_JNT" -p "L_upperArm_JNT";
	rename -uid "9308D770-4ED5-7FE8-B794-FA9424FDE47E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 10.11699999999999 5.3290705182007514e-15 4.5474735088646412e-13 ;
	setAttr ".r" -type "double3" -2.0673605429512861e-14 9.5416640443905503e-15 -3.1805546814635183e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 -0.59438396874882904 -0.0029701157083969532 0
		 -0.0036933405436224667 -4.5519019260015543e-16 -0.99999317959455603 0 0.59437991480917218 0.80418138357859925 -0.0021952624102596252 0
		 25.416832088577472 146.31811254437258 -5.7506440594686774 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "L_upperArmTwist03_JNT" -p "L_upperArm_JNT";
	rename -uid "CA31B4D3-4E19-ED64-F737-B6BFC62C05A7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 20.233999999999988 6.2172489379008766e-15 6.8212102632969618e-13 ;
	setAttr ".r" -type "double3" -2.0673605429512861e-14 9.5416640443905503e-15 -3.1805546814635183e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 -0.59438396874882904 -0.0029701157083969532 0
		 -0.0036933405436224667 -4.5519019260015543e-16 -0.99999317959455603 0 0.59437991480917218 0.80418138357859925 -0.0021952624102596252 0
		 33.552679656084678 140.30472993254068 -5.7806927200905296 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_clavicle_JNT" -p "C_spine03_JNT";
	rename -uid "8A3FF25F-4A58-83CC-50A1-F69C28C7501C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 17.120964607006044 3.5339843292742149e-14 -3.0000000000000102 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000099 -68.170229709586224 90.000000000000099 ;
	setAttr ".bps" -type "matrix" 0.9282774510245968 0.0057398191852641167 0.37184409151551384 0
		 -0.37185021696614157 -1.0824674490095274e-15 0.9282927426960923 0 0.0053282324940688852 -0.99998352710218219 0.002134353009385886 0
		 -3.0000000000000102 152.41979878659797 3.0177095473597349e-14 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_upperArm_JNT" -p "R_clavicle_JNT";
	rename -uid "9D5989B3-4254-6AC5-A830-6E9CA9D70D47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -15.384392355224843 -4.3298697960381105e-14 -5.9685589803848416e-13 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -21.829770290413787 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 0.59438396874882837 0.0029701157083976953 0
		 -0.0036933405436221892 -1.1579279202145187e-15 0.99999317959455536 0 0.59437991480917174 -0.80418138357860036 0.002195262410258211 0
		 -17.280984521070415 152.33149515620417 -5.7205953988468075 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_lowerArm_JNT" -p "R_upperArm_JNT";
	rename -uid "B323E46D-446B-5E94-1D45-C2B697147BAA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -30.350649617122567 9.9564800848384039e-13 5.4001247917767614e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -0.2 ;
	setAttr ".bps" -type "matrix" 0.73539834240599922 0.54103722910381968 -0.40800489544877994 0
		 0.32544794906083857 0.24612154125310939 0.91296649411864383 0 0.59436765594924712 -0.80417840287765441 0.0049179168905492659 0
		 -41.688245454126488 134.29155558267354 -5.8107403400337008 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_hand_JNT" -p "R_lowerArm_JNT";
	rename -uid "09E88A56-4499-9B0F-6C2C-D88D26363067";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -29.260659756081857 -7.9047879353311146e-14 5.1159076974727213e-13 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 0.20000000000000251 ;
	setAttr ".bps" -type "matrix" 0.62008096390219869 0.68156193053703062 -0.38855235560829687 0
		 0.38275973751099379 0.16950411611781863 0.90816481871939536 0 0.68483179069508404 -0.71185791381549812 -0.15576818992211275 0
		 -63.206486136454899 118.46044930649309 6.1277520845087592 1;
	setAttr ".radi" 2.5704835115814038;
createNode joint -n "R_thumb01_JNT" -p "R_hand_JNT";
	rename -uid "0D46C2A3-4C4E-D1A3-EC39-8FB633070A0D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -3.0330070101527724 3.1783308274263433 1.7525546123302718 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -170 -25 155 ;
	setAttr ".bps" -type "matrix" 0.27106708400437807 -0.63456770130799922 0.72377238716743353 0
		 0.46475174607187875 0.7447529988135444 0.47890373279122905 0 -0.84292849666653435 0.20655944232814605 0.49679447087561446 0
		 -62.670453860150438 115.68443748077271 9.9196900828975725 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_thumb02_JNT" -p "R_thumb01_JNT";
	rename -uid "FA476CA6-4495-4EAB-2D03-F29083996A62";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.441166096821457 1.8207657603852567e-13 1.4210854715202004e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.15610830560490457 -0.65932648686930595 0.73547180818420554 0
		 0.69715136444100312 0.4539324391905607 0.55491018706503825 0 -0.69972149601052958 0.59936126364913411 0.38878773599188987 0
		 -61.737667000710402 113.50078462089384 12.410311083433825 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_thumb03_JNT" -p "R_thumb02_JNT";
	rename -uid "71DEBBDF-4ABA-F00D-A41B-AA9460826714";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.697520578549164 1.5987211554602254e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.081680974274698337 -0.74100759328522903 0.66651028884419239 0
		 0.70698918777222852 0.42828393933551695 0.56279583836451386 0 -0.7024916418112751 0.51718528014714793 0.488901707078647 0
		 -62.158772367561873 111.72223785458127 14.394261420953422 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_pinky_meta_JNT" -p "R_hand_JNT";
	rename -uid "512279C2-4106-A292-5618-9CA56CC131FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -4.5570000000000874 -3.7280000000000477 0.27699999999958891 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90 0 180 ;
	setAttr ".bps" -type "matrix" -0.6139080436239811 -0.73015603857474809 0.2999817882915688 0
		 -0.78924277487836125 0.5607317470627603 -0.25035125351842896 0 0.014586167285495999 -0.39045110727052079 -0.92050810781608194 0
		 -67.269424984375789 114.52547560202187 4.4695989362214066 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_pinky01_JNT" -p "R_pinky_meta_JNT";
	rename -uid "87848FBD-429E-DF4A-2EC6-1D85BD1CE800";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.3084338330971264 -0.31243273655078951 -0.366874376146054 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.50020916339507215 -0.7999781035527741 0.3313997988709555 0
		 -0.86578174881405401 0.4556127376043515 -0.20697583615762138 0 0.014586167285495999 -0.39045110727052079 -0.92050810781608194 0
		 -69.059265137376983 112.0778582127506 5.877997598946342 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_pinky02_JNT" -p "R_pinky01_JNT";
	rename -uid "87D17E16-4AD4-F0DB-33EC-57BA75C3B35F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.7376223054285873 -2.5579538487363607e-13 -1.3500311979441904e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.25990565222729223 -0.89044218578225409 0.37357966448888535 0
		 -0.9655238452074737 0.23379616466175468 -0.11446858837789577 0 0.014586167285495999 -0.39045110727052079 -0.92050810781608194 0
		 -70.428648900466854 109.88782031260996 6.7852450803502533 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_pinky03_JNT" -p "R_pinky02_JNT";
	rename -uid "1BE71C39-4E64-44D6-FDB2-02ACBFC28AB7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.294336345667034 1.4210854715202004e-13 -2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.075398416111187583 -0.91841447020119293 0.38836830428471708 0
		 -0.99704680059255191 0.063740048292157125 -0.042835542156831399 0 0.014586167285495999 -0.39045110727052079 -0.92050810781608194 0
		 -71.024959884816397 107.84484644205456 7.6423624825891867 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_ring_meta_JNT" -p "R_hand_JNT";
	rename -uid "10A334B1-4AB9-3911-19E7-50B869D0794E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -4.6600000000000392 -1.890000000000029 -0.76000000000055934 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999986 -7.0622500768802538e-31 180 ;
	setAttr ".bps" -type "matrix" -0.57582335505632321 -0.72287525888694226 0.38194086435051161 0
		 -0.7996742313092754 0.59519946657846812 -0.079112064595904225 0 -0.17014284455009882 -0.35098284156614179 -0.9207944707558563 0
		 -67.339951493063353 115.5050199452279 6.3403583786045443 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_ring01_JNT" -p "R_ring_meta_JNT";
	rename -uid "1B7D3441-4323-3AD4-5C81-74B20D1F6405";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.6385194145724284 -0.13607294734006814 0.00038684019199397568 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.48908021595443318 -0.78113055816224686 0.38811801487060854 0
		 -0.85548346261652897 0.51637786167814514 -0.038754988818738137 0 -0.17014284455009882 -0.35098284156614179 -0.9207944707558563 0
		 -69.326347738324529 112.79369796151134 7.74046644025234 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_ring02_JNT" -p "R_ring01_JNT";
	rename -uid "E37BF57D-401C-7A8F-5D91-0A8F6EB9A361";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8599716183125707 5.6843418860808015e-14 -5.8619775700208265e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.28399152673820899 -0.87364465919552747 0.39508710710428413 0
		 -0.94367736204968633 0.32763139637235222 0.046159554439443348 0 -0.16976998879615454 -0.35972583667319979 -0.91748322782158809 0
		 -71.214183490986855 109.77855617680846 9.2385909622087752 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_ring03_JNT" -p "R_ring02_JNT";
	rename -uid "66365829-44FD-3B1A-F7F1-3C9067B1A336";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.7281147574063027 0 -7.2830630415410269e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.033357313033976516 -0.92836675893085463 0.37016543677033659 0
		 -0.98491900203585625 0.093447757287091565 0.14560932692209647 0 -0.16976998879615454 -0.35972583667319979 -0.91748322782158809 0
		 -71.988944966059748 107.39515328932798 10.316433929560992 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_middle_meta_JNT" -p "R_hand_JNT";
	rename -uid "35A410B6-4D66-94AC-A147-EFA16241D256";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -4.7490000000001231 0.36999999999994149 -1.470000000000482 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999972 180 0 ;
	setAttr ".bps" -type "matrix" -0.47420450304376538 -0.77912609826477952 0.40999099050554449 0
		 -0.84129395719823274 0.53827446075763907 0.049850601579232226 0 -0.25952758403444171 -0.32128356306971984 -0.91072625153032205 0
		 -67.016332263469351 116.33285935464531 8.5379874434042229 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_middle01_JNT" -p "R_middle_meta_JNT";
	rename -uid "6EFA7DAD-4C2F-949F-42C6-86859C19F92D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.1497049935342716 0.039809941666675286 -0.0027520440325305984 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.47420450304376538 -0.77912609826477952 0.40999099050554449 0
		 -0.84129395719823274 0.53827446075763907 0.049850601579232226 0 -0.25952758403444171 -0.32128356306971984 -0.91072625153032205 0
		 -69.0169186897282 113.12202875547884 10.243820012295938 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_middle02_JNT" -p "R_middle01_JNT";
	rename -uid "5071F35F-4DEA-638D-583D-2BAE95B777AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 4.3953968914293142 -2.5579538487363607e-13 -2.6645352591003757e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.27211618524137526 -0.8820973606692647 0.38452181736541219 0
		 -0.92726331844082988 0.34716735534821452 0.14020544088810141 0 -0.25716827176730439 -0.31840080665859538 -0.91240638221977266 0
		 -71.101235688308648 109.69746032513444 12.045893137478052 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_middle03_JNT" -p "R_middle02_JNT";
	rename -uid "56BEC238-4EAD-C06C-1870-4D8F1FAB1495";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.6033506852284916 1.9895196601282805e-13 1.4921397450962104e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.024421448323836588 -0.94908781025167266 0.31406356250519041 0
		 -0.96642993937575161 0.10278841186725204 0.23547338419445527 0 -0.25576701339294661 -0.29776982858827977 -0.91973711681249393 0
		 -71.809649545618484 107.40105155679777 13.046938274201471 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_index_meta_JNT" -p "R_hand_JNT";
	rename -uid "1A020656-4942-13D6-57EF-E39C2EBFC968";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -4.8120000000000971 2.5369999999999644 -1.2340000000006057 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999986 -7.0622500768802538e-31 180 ;
	setAttr ".bps" -type "matrix" -0.49259522800281508 -0.73766559500499429 0.46173521773282883 0
		 -0.76654808758932091 0.61897608083283695 0.17109249185740411 0 -0.4120121002616422 -0.269662903089671 -0.87036081479765692 0
		 -66.064336710404874 116.48923790498841 10.493698111150882 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_index01_JNT" -p "R_index_meta_JNT";
	rename -uid "E3BEBC2D-4851-6FB5-5FC5-58BA54528657";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8841418335245237 0.05818730765307123 -0.0079850522469033791 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.46201126569155787 -0.76148007610461788 0.45463577077677314 0
		 -0.78536082128667162 0.58943194042480973 0.18915170629673991 0 -0.4120121002616422 -0.269662903089671 -0.87036081479765692 0
		 -68.018959873741679 113.66220993229329 12.304048474399208 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_index02_JNT" -p "R_index01_JNT";
	rename -uid "6AE08922-4E42-EEE2-8A8C-638B5B78B131";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 3.8337976624460026 1.1368683772161603e-13 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.15090576000109779 -0.92181811668155533 0.35704175015838419 0
		 -0.89859528200212679 0.27844798159606327 0.33910653297834992 0 -0.4120121002616422 -0.269662903089671 -0.87036081479765692 0
		 -69.790217584173703 110.74284939652425 14.047030029667532 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_index03_JNT" -p "R_index02_JNT";
	rename -uid "01715162-4DB8-6F5B-CA84-3A8718B800EB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 2.3509375903513501 2.8421709430404007e-14 -1.2345680033831741e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.058559525480020927 -0.9453923407871212 0.32063079071823852 0
		 -0.90929467787595986 0.18307168180332742 0.3737217522544759 0 -0.4120121002616422 -0.269662903089671 -0.87036081479765692 0
		 -70.144987607960815 108.57571253455077 14.886412901439815 1;
	setAttr ".radi" 1.2852417557907019;
createNode joint -n "R_weapon_parent_JNT" -p "R_hand_JNT";
	rename -uid "6B3C8FE6-4DCC-B607-407F-43BD609418E6";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".t" -type "double3" -9.0000000000000711 -1.865174681370263e-14 5.99999999999946 ;
	setAttr ".r" -type "double3" -8.8278125961003172e-32 1.5902773407317584e-15 -6.3611093629270335e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "R_weapon_child_JNT" -p "R_weapon_parent_JNT";
	rename -uid "EEEE98F8-4C57-4B50-E7D7-DB981D26251A";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".t" -type "double3" 9.9475983006414026e-14 -4.8849813083506888e-14 -2.8421709430404007e-14 ;
	setAttr ".r" -type "double3" -8.8278125961003172e-32 1.5902773407317584e-15 -6.3611093629270335e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "R_lowerArmTwist01_JNT" -p "R_lowerArm_JNT";
	rename -uid "DCDD3F75-4CBC-B339-E689-C298FC9D4810";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -9.7540000000000688 -9.7699626167013776e-15 5.1159076974727213e-13 ;
	setAttr ".r" -type "double3" 4.7708320221952744e-15 -4.7708320221952744e-15 6.361109362927032e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599944 0.54103722910381957 -0.40800489544877988 -1.6581664431844987e-19
		 0.32544794906083879 0.24612154125310887 0.91296649411864395 -7.499119254655101e-20
		 0.59436765594924734 -0.80417840287765474 0.0049179168905490586 -1.2130786653420387e-18
		 -48.861320885954719 129.01427844999486 -1.8310605898263139 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_lowerArmTwist02_JNT" -p "R_lowerArm_JNT";
	rename -uid "9C1B4120-4B8B-915C-2B4D-12849D115C79";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -19.506999999999955 1.7763568394002505e-15 7.1054273576010019e-13 ;
	setAttr ".r" -type "double3" 4.7708320221952744e-15 -4.7708320221952744e-15 6.361109362927032e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599944 0.54103722910381957 -0.40800489544877988 -1.6581664431844987e-19
		 0.32544794906083879 0.24612154125310887 0.91296649411864395 -7.499119254655101e-20
		 0.59436765594924734 -0.80417840287765474 0.0049179168905490586 -1.2130786653420387e-18
		 -56.033660919440436 123.7375423545453 2.1482111554856349 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_lowerArmTwist03_JNT" -p "R_lowerArm_JNT";
	rename -uid "8278C977-4F70-19A3-6A9B-6C8BA78F6211";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -29.261000000000102 -5.3290705182007514e-15 5.6843418860808015e-13 ;
	setAttr ".r" -type "double3" 4.7708320221952744e-15 -4.7708320221952744e-15 6.361109362927032e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.73539834240599944 0.54103722910381957 -0.40800489544877988 -1.6581664431844987e-19
		 0.32544794906083879 0.24612154125310887 0.91296649411864395 -7.499119254655101e-20
		 0.59436765594924734 -0.80417840287765474 0.0049179168905490586 -1.2130786653420387e-18
		 -63.20673635126856 118.46026522186666 6.1278909056930333 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperArmTwist01_JNT" -p "R_upperArm_JNT";
	rename -uid "66CE93B9-4312-CA5B-A84E-C8B2D9EA443E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -7.1054273576010019e-14 6.2172489379008766e-15 4.5474735088646412e-13 ;
	setAttr ".r" -type "double3" 7.9513867036587888e-15 -2.2069531490250784e-31 3.180554681463516e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 0.59438396874883037 0.0029701157083975695 0
		 -0.0036933405436219676 -1.2593065568130972e-15 0.99999317959455547 0 0.59437991480917163 -0.80418138357859892 0.0021952624102579929 0
		 -17.280984521070419 152.33149515620394 -5.7205953988468137 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperArmTwist02_JNT" -p "R_upperArm_JNT";
	rename -uid "6CCA5733-4B85-E378-6B50-BEB7AFE7A5E0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -10.117000000000075 7.9936057773011271e-15 6.8212102632969618e-13 ;
	setAttr ".r" -type "double3" 7.9513867036587888e-15 -2.2069531490250784e-31 3.180554681463516e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 0.59438396874883037 0.0029701157083975695 0
		 -0.0036933405436219676 -1.2593065568130972e-15 0.99999317959455547 0 0.59437991480917163 -0.80418138357859892 0.0021952624102579929 0
		 -25.41683208857761 146.31811254437204 -5.750644059468673 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "R_upperArmTwist03_JNT" -p "R_upperArm_JNT";
	rename -uid "8A1E9F3F-4714-C73D-A316-3BABA1D003DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" -20.234000000000041 2.6645352591003757e-15 6.2527760746888816e-13 ;
	setAttr ".r" -type "double3" 7.9513867036587888e-15 -2.2069531490250784e-31 3.180554681463516e-15 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.80417589873551343 0.59438396874883037 0.0029701157083975695 0
		 -0.0036933405436219676 -1.2593065568130972e-15 0.99999317959455547 0 0.59437991480917163 -0.80418138357859892 0.0021952624102579929 0
		 -33.552679656084806 140.30472993254011 -5.7806927200905296 1;
	setAttr ".radi" 2.5704835115814038;
	setAttr ".liw" yes;
createNode joint -n "C_neck01_JNT" -p "C_spine03_JNT";
	rename -uid "31D1185D-4340-5FEC-2B5C-F0AC6BC47E1C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 22.142144871168256 -4.0901220894534793 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 157.44097905076018 -4.0901220894534847 1;
	setAttr ".radi" 1.5422901069488422;
createNode joint -n "C_neck02_JNT" -p "C_neck01_JNT";
	rename -uid "E7C6AF56-4479-F22D-ECFB-E4B1DAF741CC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".t" -type "double3" 6.2159582718826414 1.7383894777904931 0 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 163.65693732264282 -2.3517326116629915 1;
	setAttr ".radi" 0.77114505347442108;
createNode joint -n "C_head_JNT" -p "C_neck02_JNT";
	rename -uid "34429CA1-47B4-5039-0BBA-4EB3ADF49658";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 6.2159582718826414 1.7383894777905093 0 ;
	setAttr ".r" -type "double3" 0 0 -1.272221872585407e-14 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 0.916648537625536 ;
	setAttr ".bps" -type "matrix" 0 0.99987202616752791 0.015997852594718635 0 0 -0.015997852594718635 0.99987202616752791 0
		 1 0 0 0 0 169.87289559452546 -0.61334313387248218 1;
	setAttr ".radi" 4.4983461452674565;
createNode joint -n "L_eye_JNT" -p "C_head_JNT";
	rename -uid "3DAB8D50-49E6-3C32-4020-F8862D1DFC41";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0 ;
	setAttr ".t" -type "double3" 6.5130752316649989 7.976991863642068 3.1145353317260742 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.916648537625534 -90 0 ;
	setAttr ".radi" 3.8557252673721054;
createNode joint -n "R_eye_JNT" -p "C_head_JNT";
	rename -uid "676D23D1-4813-BF92-3F98-38810613BB3E";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0 ;
	setAttr ".t" -type "double3" 6.5130752316649989 7.976991863642068 -3.1145353317260742 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.916648537625534 -90 0 ;
	setAttr ".radi" 3.8557252673721054;
createNode joint -n "C_jaw_JNT" -p "C_head_JNT";
	rename -uid "DAFF9223-4C9D-6293-4B5D-EDBF66CD1A70";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".t" -type "double3" 2.7098497602138707 2.992274539640849 -3.7617570592466878e-30 ;
	setAttr ".r" -type "double3" 0 0 -6.3611093629270351e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 137.0855091496114 ;
	setAttr ".bps" -type "matrix" 0 -0.74317002357032014 0.66910261998178577 0 0 -0.66910261998178577 -0.74317002357032014 0
		 1 0 0 0 -3.7617570592466878e-30 172.53452859787069 2.4219002499454545 1;
	setAttr ".radi" 1.5422901069488422;
createNode joint -n "C_placement_JNT" -p "C_root_JNT";
	rename -uid "101E287B-4D85-FCD5-CB08-ADA6FA311534";
createNode transform -s -n "persp";
	rename -uid "48DEF73A-422B-985F-14CB-C08C745DC11C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -235.78638885367602 163.65400105464678 382.61506722880682 ;
	setAttr ".r" -type "double3" -9.3383527296053668 -30.600000000000076 4.6189139452943012e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "3D4DC2A0-4271-F22D-916E-14B372F98968";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 504.63810916061709;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "C61B49BC-4DF5-9719-99A8-1CB546A8A863";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "5023AEE6-4CE7-45F4-4FF0-42BFB4EA3274";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "3BF788E2-4149-8854-5D25-E18B36359490";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "42ED6A6D-4B5B-DC99-E8D9-AA86A523B550";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "6B5703D3-4C76-52B2-5DF0-65880D1AF08C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "30C46703-4C9A-AEA9-F2D8-31AAD1787446";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "73DEF6BD-4632-BAB5-AA09-0595F741D84B";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "EF7FFFA2-48B8-8337-7814-CB82DE60BC8A";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "4840131D-4917-EB9C-548A-9FAAA8153026";
createNode displayLayerManager -n "layerManager";
	rename -uid "274DD61D-4A9C-9945-D605-A9A3EB17E203";
createNode displayLayer -n "defaultLayer";
	rename -uid "13939BDB-4E12-9F36-CC71-BDA279BFCF38";
	setAttr ".ufem" -type "stringArray" 0  ;
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "620B8DC9-433D-F34E-73BE-2AA04DD96B8C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "3AE63B64-4B13-4063-1B87-09A314C487E5";
	setAttr ".g" yes;
createNode dagPose -n "apose";
	rename -uid "C699CDD8-44F7-A2FF-FC07-1485927274E9";
	setAttr -s 96 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 103.31450653076175 0 1;
	setAttr ".wm[2]" -type "matrix" 0.01815964994328333 -0.99949309688237409 -0.026149118501748211 0
		 1.0210002792630517e-06 -0.026153412665838739 0.99965794100026428 0 -0.99983509996043596 -0.018153464969845472 -0.0004739163361028257 0
		 10.250824075415816 100.43905673650595 0 1;
	setAttr ".wm[3]" -type "matrix" 0.018156107032326514 -0.99845241517638095 -0.052565486831973589 0
		 0.000597497131675157 -0.05256330853641606 0.99861741502583623 0 -0.99983498577245644 -0.018162412399161523 -0.00035777260157835149 0
		 11.058661765322769 55.976294679683924 -1.1632516898470349 1;
	setAttr ".wm[4]" -type "matrix" 0.018156107394490185 -0.99845244703692981 -0.052564881529844502 0
		 0.00059748612652943097 -0.052562703334300014 0.99861744688770526 0 -0.99983498577245644 -0.018162412399161523 -0.00035777260157835149 0
		 11.908553522970438 9.238495846989089 -3.6238548310207088 1;
	setAttr ".wm[5]" -type "matrix" -7.8444957399404005e-06 -0.018673504796261502 0.99982563487694598 0
		 4.9545268582251722e-10 0.99982563490770859 0.018673504796839911 0 -0.99999999996923183 1.4697959512324776e-07 -7.8431186818749823e-06 0
		 11.908636066059969 2.8973805318404198 9.6082897362973192 1;
	setAttr ".wm[6]" -type "matrix" -7.8444957399404005e-06 -0.018673504796261502 0.99982563487694598 0
		 4.9545268582251722e-10 0.99982563490770859 0.018673504796839911 0 -0.99999999996923183 1.4697959512324776e-07 -7.8431186818749823e-06 0
		 11.908555928129749 2.7066154305894607 19.822325106282761 1;
	setAttr ".wm[7]" -type "matrix" 0.01815610664167603 -0.99845238081001431 -0.052566139733007895 0
		 0.00059750900222834227 -0.052563961329572639 0.99861738065804539 0 -0.99983498577245644 -0.018162412399161523 -0.00035777260157835149 0
		 11.34195694767412 40.397141846138879 -1.9834263537877421 1;
	setAttr ".wm[8]" -type "matrix" 0.01815610664167603 -0.99845238081001431 -0.052566139733007895 0
		 0.00059750900222834227 -0.052563961329572639 0.99861738065804539 0 -0.99983498577245644 -0.018162412399161523 -0.00035777260157835149 0
		 11.625252126436195 24.817989812645965 -2.8036316018837808 1;
	setAttr ".wm[9]" -type "matrix" 0.01815610664167603 -0.99845238081001431 -0.052566139733007951 0
		 0.00059750900222834324 -0.052563961329572695 0.99861738065804539 0 -0.99983498577245644 -0.018162412399161523 -0.00035777260157835149 0
		 11.90854912080893 9.2387379339150044 -3.6238421065937985 1;
	setAttr ".wm[10]" -type "matrix" 0.018159649943981466 -0.99949311487534986 -0.026148430749902574 0
		 1.0085066730601604e-06 -0.026152725027403741 0.99965795899028576 0 -0.99983509996043596 -0.018153464969845472 -0.0004739163361028257 0
		 10.250824075415816 100.43905673650598 -2.1192120227719314e-12 1;
	setAttr ".wm[11]" -type "matrix" 0.018159955375882234 -0.99949310714094275 -0.026148514269259585 0
		 1.0100265042439113e-06 -0.026152808677738792 0.99965795680184799 0 -0.99983509441293661 -0.018153770297359626 -0.00047392432401270081 0
		 10.520101357469663 85.61824299640638 -0.3877375601438206 1;
	setAttr ".wm[12]" -type "matrix" 0.01815995646029684 -0.99949310717736428 -0.026148512123979235 0
		 1.0099875427115036e-06 -0.02615280653332613 0.99965795685794967 0 -0.99983509439324048 -0.01815377138140117 -0.00047392435237249427 0
		 10.789378639523509 70.797429256306785 -0.77547512028552157 1;
	setAttr ".wm[13]" -type "matrix" 0.018162820752412122 0.99949302218403979 0.026149771466117962 0
		 -2.2257782708713467e-06 0.026154126201422757 -0.99965792233027706 0 -0.99983504236317011 0.01815654945342042 0.0004772573559830715 0
		 -10.250824075415816 100.43905673650595 0 1;
	setAttr ".wm[14]" -type "matrix" 0.018153094006779093 0.9984525025960147 0.052564866952521987 0
		 0.00059431213359502257 0.052562745323406448 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654388 0.00036078401999905781 0
		 -11.058802819755481 55.976298002662759 -1.1632807371706122 1;
	setAttr ".wm[15]" -type "matrix" 0.018153094006779093 0.9984525025960147 0.052564866952522285 0
		 0.000594312133595028 0.052562745323406747 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654388 0.00036078401999905781 0
		 -11.908553536949126 9.2384950778336048 -3.6238548616373603 1;
	setAttr ".wm[16]" -type "matrix" -1.9598161129747048e-06 0.018673377209548307 -0.999825637288697 0
		 1.2390553513763614e-10 -0.99982563729061713 -0.018673377209584514 0 -0.99999999999807998 -3.6720269467466204e-08 1.9594720803941439e-06 0
		 -11.90857594544852 2.8973792331999908 9.6082894521791236 1;
	setAttr ".wm[17]" -type "matrix" -1.9598161129747048e-06 0.018673377209548307 -0.999825637288697 0
		 1.2390553513763614e-10 -0.99982563729061713 -0.018673377209584514 0 -0.99999999999807998 -3.6720269467466204e-08 1.9594720803941439e-06 0
		 -11.908555924326393 2.7066154353514809 19.822324846802545 1;
	setAttr ".wm[18]" -type "matrix" 0.018153094006779093 0.9984525025960147 0.052564866952521987 0
		 0.00059431213359502257 0.052562745323406448 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654388 0.00036078401999905781 0
		 -11.34205099147146 40.397144068906364 -1.9834661256909012 1;
	setAttr ".wm[19]" -type "matrix" 0.018153094006779093 0.9984525025960147 0.052564866952521987 0
		 0.00059431213359502257 0.052562745323406448 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654388 0.00036078401999905781 0
		 -11.625299163187435 24.817990135149966 -2.803651514211186 1;
	setAttr ".wm[20]" -type "matrix" 0.018153094006779093 0.9984525025960147 0.052564866952521987 0
		 0.00059431213359502257 0.052562745323406448 -0.99861744657158613 0 -0.99983504238002663 0.018159236322654388 0.00036078401999905781 0
		 -11.90854915021281 9.2387363561432281 -3.6238421592181709 1;
	setAttr ".wm[21]" -type "matrix" 0.018162820752412122 0.99949302218403979 0.026149771466117962 0
		 -2.2257782708713467e-06 0.026154126201422757 -0.99965792233027706 0 -0.99983504236317011 0.01815654945342042 0.0004772573559830715 0
		 -10.250824075415814 100.43905673650595 -4.4478507621646165e-16 1;
	setAttr ".wm[22]" -type "matrix" 0.018162820752412122 0.99949302218403979 0.026149771466117962 0
		 -2.2257782708713467e-06 0.026154126201422757 -0.99965792233027706 0 -0.99983504236317011 0.01815654945342042 0.0004772573559830715 0
		 -10.520148375263428 85.618244370863707 -0.38775744072418084 1;
	setAttr ".wm[23]" -type "matrix" 0.018162820752412122 0.99949302218403979 0.026149771466117962 0
		 -2.2257782708713467e-06 0.026154126201422757 -0.99965792233027706 0 -0.99983504236317011 0.01815654945342042 0.0004772573559830715 0
		 -10.789472675111044 70.797432005221438 -0.775514881448362 1;
	setAttr ".wm[24]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 112.29600842923837 0 1;
	setAttr ".wm[25]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 124.34795562940002 1.1664122257998452e-16 1;
	setAttr ".wm[26]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 135.29883417959192 -5.1627478191447992e-15 1;
	setAttr ".wm[27]" -type "matrix" 0.92827745102459669 -0.0057398191852651159 -0.3718440915155139 0
		 -0.37185021696614157 9.1593399531575415e-16 -0.9282927426960923 0 0.0053282324940697734 0.99998352710218208 -0.0021343530093864138 0
		 3.0000000000000004 152.41979878659805 3.7349994120846188e-15 1;
	setAttr ".wm[28]" -type "matrix" 0.80417589873551309 -0.59438396874882871 -0.0029701157083972737 0
		 -0.0036933405436223002 2.8883145875013838e-16 -0.99999317959455536 0 0.59437991480917207 0.80418138357860003 -0.0021952624102589981 0
		 17.280984521070454 152.33149515620428 -5.7205953988468279 1;
	setAttr ".wm[29]" -type "matrix" 0.73539834240599866 -0.54103722910382024 0.40800489544878005 0
		 0.32544794906083807 -0.24612154125311031 -0.91296649411864383 0 0.59436765594924801 0.80417840287765374 -0.0049179168905499285 0
		 41.688245454126829 134.29155558267365 -5.8107403400336644 1;
	setAttr ".wm[30]" -type "matrix" 0.62008096390219836 -0.68156193053703085 0.38855235560829676 0
		 0.38275973751099335 -0.16950411611781904 -0.90816481871939558 0 0.68483179069508449 0.71185791381549768 0.1557681899221123 0
		 63.206486136455105 118.46044930649282 6.1277520845088667 1;
	setAttr ".wm[31]" -type "matrix" -0.2710670840043804 -0.63456770130799978 0.72377238716743231 0
		 -0.46475174607187908 0.74475299881354462 0.47890373279122928 0 -0.84292849666653369 -0.20655944232814472 -0.49679447087561657 0
		 62.670453860150111 115.68443748077257 9.919690082897624 1;
	setAttr ".wm[32]" -type "matrix" 0.15610830560490269 -0.65932648686930628 0.73547180818420554 0
		 -0.69715136444100279 0.45393243919056231 0.55491018706503814 0 -0.6997214960105308 -0.599361263649133 -0.38878773599189048 0
		 61.737667000710083 113.5007846208937 12.410311083433903 1;
	setAttr ".wm[33]" -type "matrix" 0.081680974274693757 -0.74100759328523036 0.66651028884419128 0
		 -0.70698918777222886 0.42828393933551873 0.56279583836451297 0 -0.70249164181127588 -0.51718528014714493 -0.48890170707864994 0
		 62.15877236756161 111.72223785458124 14.394261420953493 1;
	setAttr ".wm[34]" -type "matrix" 0.61390804362397977 -0.73015603857474876 0.29998178829156941 0
		 0.78924277487836225 0.56073174706275819 -0.25035125351843102 0 0.014586167285497886 0.39045110727052246 0.92050810781608128 0
		 67.269424984375746 114.52547560202171 4.4695989362214918 1;
	setAttr ".wm[35]" -type "matrix" 0.50020916339506982 -0.79997810355277477 0.33139979887095661 0
		 0.86578174881405523 0.45561273760434845 -0.20697583615762294 0 0.014586167285497886 0.39045110727052246 0.92050810781608128 0
		 69.059265137377039 112.07785821275077 5.877997598946215 1;
	setAttr ".wm[36]" -type "matrix" 0.25990565222729117 -0.89044218578225354 0.37357966448888669 0
		 0.96552384520747381 0.23379616466175299 -0.1144685883778976 0 0.014586167285497886 0.39045110727052246 0.92050810781608128 0
		 70.428648900467209 109.88782031261016 6.785245080350121 1;
	setAttr ".wm[37]" -type "matrix" 0.075398416111184058 -0.91841447020119238 0.38836830428471886 0
		 0.99704680059255202 0.063740048292153323 -0.042835542156831996 0 0.014586167285497886 0.39045110727052246 0.92050810781608128 0
		 71.02495988481671 107.84484644205493 7.6423624825890357 1;
	setAttr ".wm[38]" -type "matrix" 0.57582335505632298 -0.72287525888694215 0.38194086435051217 0
		 0.79967423130927529 0.59519946657846834 -0.07911206459590317 0 -0.17014284455010012 0.35098284156614151 0.92079447075585652 0
		 67.339951493063182 115.5050199452276 6.3403583786046163 1;
	setAttr ".wm[39]" -type "matrix" 0.48908021595443124 -0.78113055816224786 0.3881180148706091 0
		 0.85548346261652974 0.5163778616781437 -0.038754988818736229 0 -0.17014284455010012 0.35098284156614151 0.92079447075585652 0
		 69.326347738324415 112.79369796151157 7.740466440252324 1;
	setAttr ".wm[40]" -type "matrix" 0.28399152673820832 -0.87364465919552758 0.39508710710428435 0
		 0.94367736204968633 0.32763139637235178 0.046159554439444105 0 -0.16976998879615526 0.35972583667319979 0.91748322782158831 0
		 71.214183490986784 109.77855617680876 9.2385909622086206 1;
	setAttr ".wm[41]" -type "matrix" 0.033357313033974212 -0.92836675893085485 0.37016543677033631 0
		 0.98491900203585603 0.093447757287089511 0.14560932692209788 0 -0.16976998879615526 0.35972583667319979 0.91748322782158831 0
		 71.988944966059663 107.39515328932815 10.316433929560931 1;
	setAttr ".wm[42]" -type "matrix" 0.47420450304376477 -0.77912609826477963 0.40999099050554438 0
		 0.84129395719823297 0.5382744607576383 0.049850601579231726 0 -0.25952758403444087 0.32128356306972028 0.91072625153032205 0
		 67.016332263469181 116.33285935464517 8.5379874434043082 1;
	setAttr ".wm[43]" -type "matrix" 0.47420450304376477 -0.77912609826477963 0.40999099050554438 0
		 0.84129395719823297 0.5382744607576383 0.049850601579231726 0 -0.25952758403444087 0.32128356306972028 0.91072625153032205 0
		 69.016918689728399 113.12202875547895 10.243820012295973 1;
	setAttr ".wm[44]" -type "matrix" 0.27211618524137476 -0.88209736066926447 0.38452181736541258 0
		 0.92726331844082976 0.34716735534821419 0.14020544088810161 0 -0.25716827176730439 0.31840080665859588 0.91240638221977244 0
		 71.101235688308549 109.6974603251347 12.045893137477931 1;
	setAttr ".wm[45]" -type "matrix" 0.024421448323835811 -0.94908781025167221 0.31406356250519146 0
		 0.96642993937575128 0.10278841186725168 0.23547338419445554 0 -0.25576701339294661 0.2977698285882811 0.91973711681249337 0
		 71.809649545618839 107.40105155679827 13.046938274201556 1;
	setAttr ".wm[46]" -type "matrix" 0.49259522800281463 -0.73766559500499418 0.46173521773282905 0
		 0.76654808758932225 0.61897608083283606 0.17109249185740144 0 -0.41201210026163998 0.26966290308967311 0.87036081479765759 0
		 66.064336710404447 116.48923790498802 10.493698111150866 1;
	setAttr ".wm[47]" -type "matrix" 0.46201126569155732 -0.76148007610461776 0.45463577077677347 0
		 0.78536082128667306 0.58943194042480873 0.1891517062967373 0 -0.41201210026163998 0.26966290308967311 0.87036081479765759 0
		 68.018959873741991 113.66220993229355 12.304048474399305 1;
	setAttr ".wm[48]" -type "matrix" 0.15090576000109673 -0.92181811668155478 0.35704175015838546 0
		 0.8985952820021279 0.27844798159606232 0.33910653297834759 0 -0.41201210026163998 0.26966290308967311 0.87036081479765759 0
		 69.790217584174144 110.74284939652438 14.047030029667726 1;
	setAttr ".wm[49]" -type "matrix" 0.058559525480018138 -0.94539234078712087 0.32063079071823936 0
		 0.90929467787596086 0.18307168180332484 0.37372175225447429 0 -0.41201210026163998 0.26966290308967311 0.87036081479765759 0
		 70.144987607961284 108.57571253455112 14.886412901439869 1;
	setAttr ".wm[50]" -type "matrix" 0.62008096390219836 -0.68156193053703085 0.38855235560829676 0
		 0.38275973751099335 -0.16950411611781904 -0.90816481871939558 0 0.68483179069508449 0.71185791381549768 0.1557681899221123 0
		 64.678224067404344 108.05524444876671 8.6901141454508561 1;
	setAttr ".wm[51]" -type "matrix" 0.62008096390219836 -0.68156193053703085 0.38855235560829676 0
		 0.38275973751099335 -0.16950411611781904 -0.90816481871939558 0 0.68483179069508449 0.71185791381549768 0.1557681899221123 0
		 64.678224067404486 108.05524444876714 8.6901141454508366 1;
	setAttr ".wm[52]" -type "matrix" 0.73539834240599866 -0.54103722910382024 0.40800489544878005 0
		 0.32544794906083807 -0.24612154125311031 -0.91296649411864383 0 0.59436765594924801 0.80417840287765374 -0.0049179168905499285 0
		 63.206736351268546 118.46026522186632 6.1278909056931319 1;
	setAttr ".wm[53]" -type "matrix" 0.73539834240599866 -0.54103722910382024 0.40800489544878005 0
		 0.32544794906083807 -0.24612154125311031 -0.91296649411864383 0 0.59436765594924801 0.80417840287765374 -0.0049179168905499285 0
		 56.03366091944045 123.73754235454501 2.1482111554857486 1;
	setAttr ".wm[54]" -type "matrix" 0.73539834240599866 -0.54103722910382024 0.40800489544878005 0
		 0.32544794906083807 -0.24612154125311031 -0.91296649411864383 0 0.59436765594924801 0.80417840287765374 -0.0049179168905499285 0
		 48.861320885954726 129.01427844999455 -1.8310605898262025 1;
	setAttr ".wm[55]" -type "matrix" 0.80417589873551309 -0.59438396874882871 -0.0029701157083972737 0
		 -0.0036933405436223002 2.8883145875013838e-16 -0.99999317959455536 0 0.59437991480917207 0.80418138357860003 -0.0021952624102589981 0
		 17.280984521070707 152.33149515620462 -5.7205953988468288 1;
	setAttr ".wm[56]" -type "matrix" 0.80417589873551309 -0.59438396874882871 -0.0029701157083972737 0
		 -0.0036933405436223002 2.8883145875013838e-16 -0.99999317959455536 0 0.59437991480917207 0.80418138357860003 -0.0021952624102589981 0
		 25.416832088577902 146.31811254437275 -5.7506440594686898 1;
	setAttr ".wm[57]" -type "matrix" 0.80417589873551309 -0.59438396874882871 -0.0029701157083972737 0
		 -0.0036933405436223002 2.8883145875013838e-16 -0.99999317959455536 0 0.59437991480917207 0.80418138357860003 -0.0021952624102589981 0
		 33.552679656085218 140.30472993254105 -5.7806927200905456 1;
	setAttr ".wm[58]" -type "matrix" 0.9282774510245968 0.0057398191852634506 0.37184409151551379 0
		 -0.3718502169661414 1.3877787807814457e-16 0.9282927426960923 0 0.005328232494067775 -0.99998352710218197 0.0021343530093867746 0
		 -3.0000000000000102 152.41979878659797 3.0177095473597349e-14 1;
	setAttr ".wm[59]" -type "matrix" 0.80417589873551409 0.59438396874882726 0.0029701157083973934 0
		 -0.0036933405436221909 -3.7990444123892075e-16 0.99999317959455536 0 0.59437991480917063 -0.80418138357860103 0.0021952624102589005 0
		 -17.280984521070408 152.33149515620443 -5.7205953988468083 1;
	setAttr ".wm[60]" -type "matrix" 0.73539834240599977 0.54103722910381835 -0.40800489544878021 0
		 0.32544794906083935 0.24612154125310903 0.91296649411864372 0 0.5943676559492459 -0.80417840287765519 0.0049179168905491791 0
		 -41.688245454126317 134.2915555826736 -5.8107403400336928 1;
	setAttr ".wm[61]" -type "matrix" 0.62008096390219936 0.68156193053702951 -0.38855235560829715 0
		 0.38275973751099468 0.16950411611781796 0.90816481871939514 0 0.68483179069508282 -0.71185791381549901 -0.15576818992211328 0
		 -63.206486136454579 118.46044930649303 6.1277520845087459 1;
	setAttr ".wm[62]" -type "matrix" 0.27106708400437712 -0.63456770130799978 0.72377238716743331 0
		 0.46475174607188008 0.74475299881354329 0.478903732791229 0 -0.84292849666653358 0.20655944232814755 0.49679447087561468 0
		 -62.67045386015036 115.68443748077271 9.919690082897656 1;
	setAttr ".wm[63]" -type "matrix" -0.15610830560490491 -0.65932648686930573 0.73547180818420532 0
		 0.69715136444100345 0.45393243919055964 0.55491018706503803 0 -0.69972149601052869 0.59936126364913478 0.3887877359918902 0
		 -61.737667000710282 113.50078462089387 12.410311083433918 1;
	setAttr ".wm[64]" -type "matrix" -0.081680974274699086 -0.74100759328522869 0.66651028884419228 0
		 0.70698918777222886 0.4282839393355159 0.56279583836451363 0 -0.70249164181127421 0.51718528014714882 0.488901707078647 0
		 -62.158772367561944 111.72223785458139 14.394261420953583 1;
	setAttr ".wm[65]" -type "matrix" -0.61390804362398177 -0.73015603857474709 0.29998178829156907 0
		 -0.78924277487836081 0.56073174706276141 -0.25035125351842846 0 0.014586167285494556 -0.39045110727052068 -0.92050810781608206 0
		 -67.269424984375704 114.5254756020219 4.4695989362214803 1;
	setAttr ".wm[66]" -type "matrix" -0.50020916339507315 -0.79997810355277299 0.33139979887095561 0
		 -0.86578174881405345 0.455612737604353 -0.20697583615762094 0 0.014586167285494556 -0.39045110727052068 -0.92050810781608206 0
		 -69.059265137376798 112.07785821275073 5.8779975989463793 1;
	setAttr ".wm[67]" -type "matrix" -0.25990565222729328 -0.89044218578225343 0.37357966448888535 0
		 -0.96552384520747336 0.23379616466175643 -0.11446858837789532 0 0.014586167285494556 -0.39045110727052068 -0.92050810781608206 0
		 -70.428648900466698 109.88782031261013 6.785245080350232 1;
	setAttr ".wm[68]" -type "matrix" -0.075398416111189165 -0.9184144702011926 0.38836830428471703 0
		 -0.9970468005925518 0.063740048292159457 -0.04283554215683115 0 0.014586167285494556 -0.39045110727052068 -0.92050810781608206 0
		 -71.024959884816212 107.84484644205475 7.6423624825891814 1;
	setAttr ".wm[69]" -type "matrix" -0.57582335505632398 -0.72287525888694115 0.38194086435051178 0
		 -0.79967423130927462 0.59519946657846901 -0.079112064595904141 0 -0.17014284455009965 -0.35098284156614157 -0.9207944707558563 0
		 -67.339951493063296 115.50501994522794 6.3403583786046358 1;
	setAttr ".wm[70]" -type "matrix" -0.48908021595443452 -0.78113055816224553 0.38811801487060865 0
		 -0.85548346261652797 0.51637786167814648 -0.038754988818738255 0 -0.17014284455009965 -0.35098284156614157 -0.9207944707558563 0
		 -69.326347738324458 112.79369796151136 7.7404664402524155 1;
	setAttr ".wm[71]" -type "matrix" -0.28399152673821043 -0.87364465919552647 0.39508710710428441 0
		 -0.94367736204968578 0.32763139637235394 0.046159554439443362 0 -0.16976998879615557 -0.35972583667319968 -0.91748322782158798 0
		 -71.214183490986798 109.77855617680848 9.238590962208832 1;
	setAttr ".wm[72]" -type "matrix" -0.033357313033978458 -0.92836675893085396 0.37016543677033686 0
		 -0.98491900203585603 0.093447757287093869 0.14560932692209638 0 -0.16976998879615557 -0.35972583667319968 -0.91748322782158798 0
		 -71.988944966059648 107.39515328932799 10.316433929561061 1;
	setAttr ".wm[73]" -type "matrix" -0.47420450304376621 -0.7791260982647783 0.40999099050554444 0
		 -0.84129395719823163 0.53827446075764018 0.049850601579232712 0 -0.25952758403444254 -0.32128356306971934 -0.91072625153032194 0
		 -67.016332263469252 116.33285935464531 8.537987443404301 1;
	setAttr ".wm[74]" -type "matrix" -0.47420450304376621 -0.7791260982647783 0.40999099050554444 0
		 -0.84129395719823163 0.53827446075764018 0.049850601579232712 0 -0.25952758403444254 -0.32128356306971934 -0.91072625153032194 0
		 -69.016918689728072 113.12202875547901 10.243820012295931 1;
	setAttr ".wm[75]" -type "matrix" -0.27211618524137693 -0.88209736066926359 0.38452181736541197 0
		 -0.92726331844082877 0.34716735534821658 0.14020544088810197 0 -0.25716827176730545 -0.31840080665859471 -0.91240638221977255 0
		 -71.101235688308208 109.69746032513441 12.045893137478037 1;
	setAttr ".wm[76]" -type "matrix" -0.0244214483238385 -0.94908781025167221 0.31406356250519013 0
		 -0.96642993937575106 0.10278841186725435 0.23547338419445571 0 -0.25576701339294761 -0.29776982858827922 -0.9197371168124937 0
		 -71.809649545618328 107.40105155679787 13.04693827420148 1;
	setAttr ".wm[77]" -type "matrix" -0.49259522800281563 -0.73766559500499329 0.46173521773282883 0
		 -0.76654808758932003 0.61897608083283773 0.17109249185740427 0 -0.41201210026164259 -0.26966290308967045 -0.87036081479765681 0
		 -66.064336710404788 116.48923790498844 10.493698111150964 1;
	setAttr ".wm[78]" -type "matrix" -0.46201126569155815 -0.7614800761046171 0.45463577077677303 0
		 -0.78536082128667084 0.58943194042481017 0.18915170629674022 0 -0.41201210026164259 -0.26966290308967045 -0.87036081479765681 0
		 -68.018959873741565 113.66220993229332 12.304048474399252 1;
	setAttr ".wm[79]" -type "matrix" -0.15090576000109862 -0.92181811668155456 0.35704175015838407 0
		 -0.89859528200212602 0.27844798159606432 0.33910653297835003 0 -0.41201210026164259 -0.26966290308967045 -0.87036081479765681 0
		 -69.790217584173661 110.74284939652431 14.04703002966761 1;
	setAttr ".wm[80]" -type "matrix" -0.058559525480022037 -0.94539234078712053 0.32063079071823847 0
		 -0.90929467787595908 0.18307168180332875 0.37372175225447596 0 -0.41201210026164259 -0.26966290308967045 -0.87036081479765681 0
		 -70.144987607960758 108.57571253455079 14.886412901439908 1;
	setAttr ".wm[81]" -type "matrix" 0.62008096390219936 0.68156193053702951 -0.38855235560829715 0
		 0.38275973751099468 0.16950411611781796 0.90816481871939514 0 0.68483179069508282 -0.71185791381549901 -0.15576818992211328 0
		 -64.678224067404301 108.0552444487671 8.6901141454508348 1;
	setAttr ".wm[82]" -type "matrix" 0.62008096390219936 0.68156193053702951 -0.38855235560829715 0
		 0.38275973751099468 0.16950411611781796 0.90816481871939514 0 0.68483179069508282 -0.71185791381549901 -0.15576818992211328 0
		 -64.678224067404273 108.05524444876718 8.6901141454507567 1;
	setAttr ".wm[83]" -type "matrix" 0.73539834240599977 0.54103722910381835 -0.40800489544878021 0
		 0.32544794906083935 0.24612154125310903 0.91296649411864372 0 0.5943676559492459 -0.80417840287765519 0.0049179168905491791 0
		 -48.861320885954186 129.01427844999449 -1.8310605898262686 1;
	setAttr ".wm[84]" -type "matrix" 0.73539834240599977 0.54103722910381835 -0.40800489544878021 0
		 0.32544794906083935 0.24612154125310903 0.91296649411864372 0 0.5943676559492459 -0.80417840287765519 0.0049179168905491791 0
		 -56.033660919439697 123.73754235454486 2.14821115548565 1;
	setAttr ".wm[85]" -type "matrix" 0.73539834240599977 0.54103722910381835 -0.40800489544878021 0
		 0.32544794906083935 0.24612154125310903 0.91296649411864372 0 0.5943676559492459 -0.80417840287765519 0.0049179168905491791 0
		 -63.206736351268013 118.46026522186625 6.1278909056931052 1;
	setAttr ".wm[86]" -type "matrix" 0.80417589873551409 0.59438396874882726 0.0029701157083973934 0
		 -0.0036933405436221909 -3.7990444123892075e-16 0.99999317959455536 0 0.59437991480917063 -0.80418138357860103 0.0021952624102589005 0
		 -17.280984521070195 152.33149515620403 -5.7205953988468012 1;
	setAttr ".wm[87]" -type "matrix" 0.80417589873551409 0.59438396874882726 0.0029701157083973934 0
		 -0.0036933405436221909 -3.7990444123892075e-16 0.99999317959455536 0 0.59437991480917063 -0.80418138357860103 0.0021952624102589005 0
		 -25.416832088577259 146.31811254437196 -5.7506440594686552 1;
	setAttr ".wm[88]" -type "matrix" 0.80417589873551409 0.59438396874882726 0.0029701157083973934 0
		 -0.0036933405436221909 -3.7990444123892075e-16 0.99999317959455536 0 0.59437991480917063 -0.80418138357860103 0.0021952624102589005 0
		 -33.552679656084464 140.30472993254014 -5.7806927200905172 1;
	setAttr ".wm[89]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 157.44097905076018 -4.0901220894534847 1;
	setAttr ".wm[90]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 163.65693732264282 -2.3517326116629915 1;
	setAttr ".wm[91]" -type "matrix" 0 0.99987202616752791 0.015997852594718635 0 0 -0.015997852594718635 0.99987202616752791 0
		 1 0 0 0 0 169.87289559452546 -0.61334313387248218 1;
	setAttr ".wm[92]" -type "matrix" 1 0 0 0 0 1.0000000000000002 -6.9388939039072284e-18 0
		 0 -1.0408340855860843e-16 1.0000000000000002 0 3.1145353317260742 176.25752258300807 7.4668231010436861 1;
	setAttr ".wm[93]" -type "matrix" 1 0 0 0 0 1.0000000000000002 -6.9388939039072284e-18 0
		 0 -1.0408340855860843e-16 1.0000000000000002 0 -3.1145353317260742 176.25752258300807 7.4668231010436861 1;
	setAttr ".wm[94]" -type "matrix" 0 -0.74317002357032025 0.66910261998178566 0 0 -0.66910261998178566 -0.74317002357032025 0
		 1 0 0 0 -3.7617570592466878e-30 172.534528597872 2.4219002499454554 1;
	setAttr ".wm[95]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 96 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 -0 1 0 103.31450653076175
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.50000000000000011 0.50000000000000011 0.50000000000000011 0.50000000000000011 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 -1.0213496411025387e-06 0.018160674896577446
		 -0.026156395077294513 1 -2.8754497942558004 0 10.250824075415816 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 6.123233995736766e-17 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 -0.00011645353092069408 2.8305036716493161e-06
		 0.025922248156131797 0 44.485311800062036 5.2252795127396e-15 -1.5987211554602254e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.026176948307873173 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 2.7784141011513779e-16 -7.27544911078977e-18
		 -0.052359271419670318 1 46.810241652265823 6.6613381477509392e-15 -6.2172489379008766e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.026176948307873218 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 2.3540197569005272e-15 2.1995751574299856e-17
		 -1.5612511283791261e-16 0 5.635757490447892 13.547156637101248 0.11035332316931168 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.0063168970971849096 -0.0065271641577584463 0.71896663489025947 0.69498523067306794 1
		 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 2.3540197569005272e-15 2.1995751574299856e-17
		 -1.5612511283791261e-16 0 10.215816652113086 2.6645352591003757e-15 1.2434497875801753e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 -0 0 0 15.603299191204819 2.0382410327979272e-05
		 8.8817841970012523e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249324523244e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 -0 0 0 31.206599191201501 1.0180894986611122e-05
		 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249324523159e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 -0 0 0 46.809999191198145 -2.0685742896375814e-08
		 -8.8817841970012523e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249327298875e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 -1.1102230246251563e-16 -2.2204460492503131e-16
		 -1.6653345369377348e-16 1 2.8421709430404007e-14 -2.1191937094044988e-12 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 3.439935858254653e-07 0.99999999999994083 1
		 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 3.0814879110195774e-33 -1.1102230246251565e-16
		 -5.5511151231257827e-17 1 14.828329999996512 1.0201698699106963e-05 -8.8817841970012523e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.6150320942980196e-14 1.5274118006740725e-07 3.0214720694583242e-07 0.99999999999994271 1
		 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 1.1102230246251563e-16 1.1102230246251563e-16
		 -3.3306690738754696e-16 1 29.656659999992996 2.0403399517851725e-05 -1.5987211554602254e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.6478608921569813e-14 1.5328347571560156e-07 3.0321995704091692e-07 0.99999999999994227 1
		 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 2.2265399203327291e-06 0.018163761283801053
		 -0.026157108857039962 1 -2.8754497942558004 0 -10.250824075415816 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 6.123233995736766e-17 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 -0.00011645353485117617 -3.439694404715506e-06
		 0.025923525026627411 0 -44.485311800061893 -6.8156775771823734e-15 -2.3092638912203256e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.026176948307873173 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 2.2372824009837757e-16 -6.1388710185087694e-17
		 -0.052359877559830091 1 -46.810241652265958 -1.4654943925052066e-14 1.4210854715202004e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.026176948307873104 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 5.4158066919995917e-15 2.2204460492503109e-16
		 7.979727989493373e-17 0 -5.6357574857569315 -13.547156637855489 -0.11035347015034169 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.0063190324569505915 -0.0065229302991719864 0.7189666750727598 0.69498520944257569 1
		 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 5.4158066919995917e-15 2.2204460492503109e-16
		 7.979727989493373e-17 0 -10.215816652113055 1.7763568394002505e-14 -4.4408920985006262e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 1 1 1 0 -0 0 0 -15.603299999999997
		 2.6645352591003757e-15 1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 0 -0 0 0 -31.206600000000002
		 1.3322676295501878e-15 1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 0 -0 0 0 -46.81000000000008 4.4408920985006262e-16
		 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 -2.2204460492503136e-16 1 0
		 4.4408920985006163e-16 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 1 1 1 0 0 -2.2204460492503136e-16 1 -14.82832999999998
		 3.9264310552899931e-16 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 0 0 -2.2204460492503136e-16 1 -29.656659999999988
		 3.41197001207937e-16 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 1 1 1 0 0 -0 1 8.9815018984766226 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 0 0 -0 1 12.051947200161649 1.1664122257998452e-16
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 -0 1 10.950878550191902 -5.2793890417247838e-15
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 2.9151200009363622e-16 0.0057398507026245899
		 -2.6919069943811314e-17 3 17.12096460700613 8.897747231229418e-15 3.0000000000000004 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.69431490382536298 0.13389105394303547 -0.69431490382536309 0.13389105394303613 1
		 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 1 1 1 -0.00047547496416186713 0.63116819782179634
		 0.0042341740933757544 3 15.384392355224897 1.1990408665951691e-14 3.979039320256561e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.18935054436666893 0.98190955354759946 1
		 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 1 1 1 -0.002482440411283416 -0.0011182590647257652
		 -0.41975123914685364 0 30.350649617122833 -1.0418332863082469e-12 -5.6843418860808015e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.0017453283658983088 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 1 1 1 0.0969353503919725 0.18272065590621708
		 -0.0062316162141394542 5 29.260659756082042 5.595524044110789e-14 -6.5369931689929217e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.0017453283658983366 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 1 1 1 0.0054701176280619324 -0.2118646596680635
		 0.34449856776361604 0 3.0330070101521898 -3.1783308274265085 -1.7525546123307834 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.95360976239370576 -0.19208823158104982 -0.22892184008178468 0.036404992639125833 1
		 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0.23615432433658948 0.36910017659168032
		 -0.22861602156432842 0 3.4411660968214735 1.3855583347321954e-13 -1.9895196601282805e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 0.019350598041365397 -0.12819714213518832
		 -0.023654333190160706 0 2.6975205785490779 7.0166095156309893e-14 1.1368683772161603e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 1 1 1 -0.4511840193820052 0.086418352979909491
		 -0.052837656255377688 0 4.5569999999997179 3.7279999999999527 -0.27699999999990155 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654746 1
		 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 1 1 1 -1.5229670056866989e-16 -1.0462663283431505e-17
		 -0.13718287920675395 0 3.3084338330970269 -0.31243273655044845 0.3668743761459865 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[36]" -type "matrix" "xform" 1 1 1 5.8650446582968372e-17 -2.0297413736553794e-17
		 -0.26094864309672822 0 2.7376223054287436 -2.8421709430404007e-14 1.8474111129762605e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[37]" -type "matrix" "xform" 1 1 1 -5.526744918478568e-17 -5.1958610091793049e-18
		 -0.18747504961705852 0 2.2943363456668777 1.7053025658242404e-13 4.7961634663806763e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[38]" -type "matrix" "xform" 1 1 1 -0.28071556545567994 -0.0039329379183902762
		 -0.060785993592368207 0 4.659999999999684 1.8899999999999348 0.76000000000001933 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654757 1
		 1 1 yes;
	setAttr ".xm[39]" -type "matrix" "xform" 1 1 1 -5.8340304309596353e-17 5.2529845945927213e-17
		 -0.10471975511966061 0 3.6385194145720305 -0.13607294733967024 -0.00038684019187407159 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[40]" -type "matrix" "xform" 1 1 1 -0.0030636142463254285 -0.0088407276601590347
		 -0.22540489895161719 0 3.8599716183124855 1.4210854715202004e-13 -3.5527136788005009e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[41]" -type "matrix" "xform" 1 1 1 1.4119756941316233e-16 -9.6393886446416606e-18
		 -0.25846504529092412 0 2.7281147574064448 0 9.9475983006414026e-14 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[42]" -type "matrix" "xform" 1 1 1 -0.18690868893923257 -0.058801801996214417
		 -0.16707685935614761 0 4.7489999999996542 -0.37000000000008271 1.4700000000001125 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654746 0 0 0.70710678118654768 1
		 1 1 yes;
	setAttr ".xm[43]" -type "matrix" "xform" 1 1 1 -9.6296497219361793e-35 -5.5511151231257827e-17
		 3.4694469519536142e-18 0 4.1497049935343995 0.03980994166707319 0.0027520440324897422 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[44]" -type "matrix" "xform" 1 1 1 -0.0014224791846640524 0.0038309351522519525
		 -0.22870229334323841 0 4.3953968914290016 -5.6843418860808015e-14 -7.9936057773011271e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[45]" -type "matrix" "xform" 1 1 1 -0.00096001621030565587 0.021918902252160404
		 -0.26600278558969559 0 2.6033506852285058 4.2632564145606011e-13 9.7699626167013776e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[46]" -type "matrix" "xform" 1 1 1 -0.033297389784642688 -0.10594679818669513
		 -0.11676291195887625 0 4.8119999999996139 -2.537000000000063 1.2339999999998383 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654746 1
		 1 1 yes;
	setAttr ".xm[47]" -type "matrix" "xform" 1 1 1 2.5972821614176223e-17 9.0734990660654995e-17
		 -0.039409534510032276 0 3.8841418335244953 0.058187307654094411 0.007985052246887836 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[48]" -type "matrix" "xform" 1 1 1 6.8893691030784833e-17 -2.2013058408556529e-16
		 -0.36537387320022008 0 3.8337976624461731 8.5265128291212022e-14 -4.8849813083506888e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[49]" -type "matrix" "xform" 1 1 1 -2.8002616841718396e-16 4.1279906590251431e-17
		 -0.10207042227713464 0 2.3509375903510659 8.5265128291212022e-14 3.6859404417555197e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[50]" -type "matrix" "xform" 1 1 1 2.7755575615628914e-17 1.1102230246251565e-16
		 -2.7755575615628914e-17 0 8.9999999999998579 -3.730349362740526e-14 -5.9999999999999147 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[51]" -type "matrix" "xform" 1 1 1 2.7755575615628914e-17 1.1102230246251565e-16
		 -2.7755575615628914e-17 0 -2.1316282072803006e-13 -8.8817841970012523e-16 3.979039320256561e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[52]" -type "matrix" "xform" 1 1 1 0 -0 0 0 29.261000000000102 -8.8817841970012523e-16
		 -4.8316906031686813e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[53]" -type "matrix" "xform" 1 1 1 0 -0 0 0 19.507000000000112 -1.3322676295501878e-14
		 -4.5474735088646412e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[54]" -type "matrix" "xform" 1 1 1 0 -0 0 0 9.7540000000001044 -1.7763568394002505e-14
		 -4.8316906031686813e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[55]" -type "matrix" "xform" 1 1 1 -3.6082248300317588e-16 1.6653345369377348e-16
		 -5.5511151231257852e-17 3 0 0 4.2632564145606011e-13 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[56]" -type "matrix" "xform" 1 1 1 -3.6082248300317588e-16 1.6653345369377348e-16
		 -5.5511151231257852e-17 3 10.11699999999999 5.3290705182007514e-15 4.5474735088646412e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[57]" -type "matrix" "xform" 1 1 1 -3.6082248300317588e-16 1.6653345369377348e-16
		 -5.5511151231257852e-17 3 20.233999999999988 6.2172489379008766e-15 6.8212102632969618e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[58]" -type "matrix" "xform" 1 1 1 1.0131539941979221e-15 0.0057398507026235369
		 -2.4848005604269803e-17 3 17.120964607006044 3.5339843292742149e-14 -3.0000000000000102 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.13389105394303574 -0.69431490382536332 0.13389105394303574 0.69431490382536276 1
		 1 1 yes;
	setAttr ".xm[59]" -type "matrix" "xform" 1 1 1 -0.00047547496416148907 0.63116819782179667
		 0.00423417409337598 3 -15.384392355224843 -4.3298697960381105e-14 -5.9685589803848416e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.1893505443666689 0.98190955354759946 1
		 1 1 yes;
	setAttr ".xm[60]" -type "matrix" "xform" 1 1 1 -0.0024824404112824519 -0.0011182590647263262
		 -0.41975123914685397 0 -30.350649617122567 9.9564800848384039e-13 5.4001247917767614e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.0017453283658983088 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[61]" -type "matrix" "xform" 1 1 1 0.096935350391972555 0.1827206559062175
		 -0.0062316162141399433 5 -29.260659756081857 -7.9047879353311146e-14 5.1159076974727213e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.0017453283658983307 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[62]" -type "matrix" "xform" 1 1 1 -0.0054701176280610771 0.21186465966806051
		 0.34449856776361626 0 -3.0330070101527724 3.1783308274263433 1.7525546123302718 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.19208823158104976 -0.95360976239370576 0.036404992639125867 0.22892184008178459 1
		 1 1 yes;
	setAttr ".xm[63]" -type "matrix" "xform" 1 1 1 -0.23615432433659067 -0.3691001765916791
		 -0.22861602156432884 0 3.441166096821457 1.8207657603852567e-13 1.4210854715202004e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[64]" -type "matrix" "xform" 1 1 1 -0.019350598041364759 0.12819714213518502
		 -0.023654333190161338 0 2.697520578549164 1.5987211554602254e-14 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[65]" -type "matrix" "xform" 1 1 1 0.45118401938200298 -0.086418352979910448
		 -0.052837656255376883 0 -4.5570000000000874 -3.7280000000000477 0.27699999999958891 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.329780281177467e-17 -0.70710678118654757 0.70710678118654757 4.329780281177467e-17 1
		 1 1 yes;
	setAttr ".xm[66]" -type "matrix" "xform" 1 1 1 5.3478315973437868e-17 3.1494914024642298e-17
		 -0.13718287920675257 0 3.3084338330971264 -0.31243273655078951 -0.366874376146054 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[67]" -type "matrix" "xform" 1 1 1 1.4444495287888721e-17 -1.1007864552199249e-16
		 -0.26094864309672983 0 2.7376223054285873 -2.5579538487363607e-13 -1.3500311979441904e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[68]" -type "matrix" "xform" 1 1 1 -2.5484289329880764e-16 3.3845497566438994e-16
		 -0.18747504961705561 0 2.294336345667034 1.4210854715202004e-13 -2.1316282072803006e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[69]" -type "matrix" "xform" 1 1 1 0.28071556545568177 0.0039329379183894488
		 -0.060785993592368512 0 -4.6600000000000392 -1.890000000000029 -0.76000000000055934 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.3297802811774658e-17 -0.70710678118654746 0.70710678118654768 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[70]" -type "matrix" "xform" 1 1 1 -3.7715091646245317e-16 -2.2821813600194819e-16
		 -0.10471975511965802 0 3.6385194145724284 -0.13607294734006814 0.00038684019199397568 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[71]" -type "matrix" "xform" 1 1 1 0.0030636142463246552 0.0088407276601591457
		 -0.22540489895161878 0 3.8599716183125707 5.6843418860808015e-14 -5.8619775700208265e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[72]" -type "matrix" "xform" 1 1 1 -3.8176079514447684e-16 -7.760138470653078e-17
		 -0.25846504529092207 0 2.7281147574063027 0 -7.2830630415410269e-14 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[73]" -type "matrix" "xform" 1 1 1 0.18690868893923335 0.058801801996214417
		 -0.16707685935614747 0 -4.7490000000001231 0.36999999999994149 -1.470000000000482 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4.3297802811774652e-17 0.70710678118654768 -0.70710678118654735 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[74]" -type "matrix" "xform" 1 1 1 0 -0 0 0 4.1497049935342716 0.039809941666675286
		 -0.0027520440325305984 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[75]" -type "matrix" "xform" 1 1 1 0.0014224791846645791 -0.0038309351522524092
		 -0.22870229334323805 0 4.3953968914293142 -2.5579538487363607e-13 -2.6645352591003757e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[76]" -type "matrix" "xform" 1 1 1 0.00096001621030567365 -0.021918902252161167
		 -0.26600278558969548 0 2.6033506852284916 1.9895196601282805e-13 1.4921397450962104e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[77]" -type "matrix" "xform" 1 1 1 0.033297389784640676 0.10594679818669453
		 -0.11676291195887653 0 -4.8120000000000971 2.5369999999999644 -1.2340000000006057 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.3297802811774658e-17 -0.70710678118654746 0.70710678118654768 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[78]" -type "matrix" "xform" 1 1 1 2.1324326606699471e-17 3.2661158315545211e-16
		 -0.039409534510032533 0 3.8841418335245237 0.05818730765307123 -0.0079850522469033791 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[79]" -type "matrix" "xform" 1 1 1 1.7806848254494649e-16 -1.9996089043599227e-16
		 -0.36537387320021963 0 3.8337976624460026 1.1368683772161603e-13 -7.1054273576010019e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[80]" -type "matrix" "xform" 1 1 1 -2.420414788824893e-16 -1.5827011826429303e-16
		 -0.10207042227713263 0 2.3509375903513501 2.8421709430404007e-14 -1.2345680033831741e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[81]" -type "matrix" "xform" 1 1 1 -1.5407439555097887e-33 2.7755575615628914e-17
		 -1.1102230246251565e-16 0 -9.0000000000000711 -1.865174681370263e-14 5.99999999999946 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[82]" -type "matrix" "xform" 1 1 1 -1.5407439555097887e-33 2.7755575615628914e-17
		 -1.1102230246251565e-16 0 9.9475983006414026e-14 -4.8849813083506888e-14 -2.8421709430404007e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[83]" -type "matrix" "xform" 1 1 1 8.3266726846886728e-17 -8.3266726846886728e-17
		 1.1102230246251563e-16 0 -9.7540000000000688 -9.7699626167013776e-15 5.1159076974727213e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[84]" -type "matrix" "xform" 1 1 1 8.3266726846886728e-17 -8.3266726846886728e-17
		 1.1102230246251563e-16 0 -19.506999999999955 1.7763568394002505e-15 7.1054273576010019e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[85]" -type "matrix" "xform" 1 1 1 8.3266726846886728e-17 -8.3266726846886728e-17
		 1.1102230246251563e-16 0 -29.261000000000102 -5.3290705182007514e-15 5.6843418860808015e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[86]" -type "matrix" "xform" 1 1 1 1.3877787807814452e-16 -3.8518598887744703e-33
		 5.5511151231257815e-17 3 -7.1054273576010019e-14 6.2172489379008766e-15 4.5474735088646412e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[87]" -type "matrix" "xform" 1 1 1 1.3877787807814452e-16 -3.8518598887744703e-33
		 5.5511151231257815e-17 3 -10.117000000000075 7.9936057773011271e-15 6.8212102632969618e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[88]" -type "matrix" "xform" 1 1 1 1.3877787807814452e-16 -3.8518598887744703e-33
		 5.5511151231257815e-17 3 -20.234000000000041 2.6645352591003757e-15 6.2527760746888816e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[89]" -type "matrix" "xform" 1 1 1 0 0 -0 1 22.142144871168256 -4.0901220894534793
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[90]" -type "matrix" "xform" 1 1 1 0 0 -0 1 6.2159582718826414 1.7383894777904931
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[91]" -type "matrix" "xform" 1 1 1 0 0 -2.2204460492503136e-16 1 6.2159582718826414
		 1.7383894777905093 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.0079991822229547836 0.99996800603007496 1
		 1 1 yes;
	setAttr ".xm[92]" -type "matrix" "xform" 1 1 1 0 -0 0 0 6.5130752316649989 7.976991863642068
		 3.1145353317260742 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.50398359412651483 -0.49598441190356013 -0.50398359412651483 0.49598441190356013 1
		 1 1 yes;
	setAttr ".xm[93]" -type "matrix" "xform" 1 1 1 0 -0 0 0 6.5130752316649989 7.976991863642068
		 -3.1145353317260742 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.50398359412651483 -0.49598441190356013 -0.50398359412651483 0.49598441190356013 1
		 1 1 yes;
	setAttr ".xm[94]" -type "matrix" "xform" 1 1 1 0 0 -1.1102230246251568e-16 0 2.7098497602138707
		 2.992274539640849 -3.7617570592466878e-30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0.93069079510034292 0.36580683962371668 1 1 1 yes;
	setAttr ".xm[95]" -type "matrix" "xform" 1 1 1 0 -0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 96 ".m";
	setAttr -s 96 ".p";
createNode dagPose -n "tpose";
	rename -uid "7C27CFCF-4806-CE9D-DA6D-FA84FD8A8D08";
	setAttr -s 96 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 103.34534728425831 0 1;
	setAttr ".wm[2]" -type "matrix" -1.2246467991473532e-16 -1 0 0 0 0 1 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415816 100.46989749000251 0 1;
	setAttr ".wm[3]" -type "matrix" -1.2229684632711994e-16 -0.99862953475457383 -0.052335956242943876 0
		 -6.4093061293237156e-18 -0.052335956242943876 0.99862953475457383 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415826 55.984585689940474 5.2252795127396e-15 1;
	setAttr ".wm[4]" -type "matrix" -1.2246467991473532e-16 -0.99999999999999989 9.0205620750793969e-17 0
		 1.0785207688568521e-32 9.0205620750793969e-17 0.99999999999999989 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415883 9.2384958469890819 -2.4498587588346008 1;
	setAttr ".wm[5]" -type "matrix" 1.0711122180698589e-05 0.033911251914732293 0.99942484803953491 0
		 0.018165926872210109 0.99925992234225092 -0.033905850548720501 0 -0.99983498587824249 0.018155841873463755 -0.00060532612730963473 0
		 10.140470752246571 3.6027383565411917 11.097297878266644 1;
	setAttr ".wm[6]" -type "matrix" 1.0711122180698589e-05 0.033911251914732293 0.99942484803953491 0
		 0.018165926872210109 0.99925992234225092 -0.033905850548720501 0 -0.99983498587824249 0.018155841873463755 -0.00060532612730963473 0
		 10.140580175106896 3.9491694885457185 21.307238883404516 1;
	setAttr ".wm[7]" -type "matrix" -1.2229684213665751e-16 -0.99862950053685129 -0.052336609151902171 0
		 -6.4093860876103065e-18 -0.052336609151902171 0.99862950053685129 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415816 40.402669211258257 -0.81659322923950872 1;
	setAttr ".wm[8]" -type "matrix" -1.2229684213665751e-16 -0.99862950053685129 -0.052336609151902171 0
		 -6.4093860876103065e-18 -0.052336609151902171 0.99862950053685129 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415824 24.820753525531583 -1.6332170428193802 1;
	setAttr ".wm[9]" -type "matrix" -1.2229684213665751e-16 -0.99862950053685129 -0.052336609151902226 0
		 -6.4093860876103134e-18 -0.052336609151902226 0.99862950053685129 0 -1 1.2246467991473532e-16 0 0
		 10.25082407541583 9.2387379768549067 -2.4498460900601731 1;
	setAttr ".wm[10]" -type "matrix" -1.2246467991470633e-16 -0.9999999999997633 6.8798717165088983e-07 0
		 8.4254128761670289e-23 6.8798717165088983e-07 0.9999999999997633 0 -1 1.2246467991473532e-16 0 0
		 10.250824075415816 100.46989749000248 -2.1191937094044988e-12 1;
	setAttr ".wm[11]" -type "matrix" 3.0548236001236016e-07 -0.99999999999977074 6.0429441389161614e-07 0
		 7.4004721971502811e-23 6.0429441389164431e-07 0.99999999999981737 0 -0.99999999999995337 -3.0548236001230436e-07 1.8460128377191018e-13 0
		 10.250824075415823 85.641567490005997 1.0201698699106963e-05 1;
	setAttr ".wm[12]" -type "matrix" 3.0656695130874894e-07 -0.99999999999976907 6.064399140817845e-07 0
		 7.4267457343774346e-23 6.0643991408181309e-07 0.99999999999981615 0 -0.99999999999995304 -3.0656695130869261e-07 1.8591443568626853e-13 0
		 10.250824075415828 70.813237490009513 2.0403399517851725e-05 1;
	setAttr ".wm[13]" -type "matrix" 0 1 0 0 -1.2246467991473532e-16 -0 -1 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415816 100.46989749000251 0 1;
	setAttr ".wm[14]" -type "matrix" 6.4093061293237156e-18 0.99862953475457383 0.052335956242943876 0
		 -1.2229684632711994e-16 0.052335956242943876 -0.99862953475457383 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415792 55.984585689940616 6.8156775771823703e-15 1;
	setAttr ".wm[15]" -type "matrix" 1.6948183510607676e-32 0.99999999999999989 1.3877787807814457e-16 0
		 -1.2246467991473532e-16 1.3877787807814457e-16 -0.99999999999999989 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415807 9.238495846989089 -2.4498587588345986 1;
	setAttr ".wm[16]" -type "matrix" 1.966735020238448e-05 -0.033911256969734259 -0.9994248477318981 0
		 0.018162807208990574 -0.99925997329879857 0.033906020072742425 0 -0.99983504241824028 -0.018153027670799966 0.00059627082671773028 0
		 -10.140470605265463 3.6027383612321566 11.097297879020889 1;
	setAttr ".wm[17]" -type "matrix" 1.966735020238448e-05 -0.033911256969734259 -0.9994248477318981 0
		 0.018162807208990574 -0.99925997329879857 0.033906020072742425 0 -0.99983504241824028 -0.018153027670799966 0.00059627082671773028 0
		 -10.140671523309118 3.9491695448776358 21.307238881015969 1;
	setAttr ".wm[18]" -type "matrix" 6.4093061293237156e-18 0.99862953475457383 0.052335956242943876 0
		 -1.2229684632711994e-16 0.052335956242943876 -0.99862953475457383 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415794 40.402669470304573 -0.8166136260455219 1;
	setAttr ".wm[19]" -type "matrix" 6.4093061293237156e-18 0.99862953475457383 0.052335956242943876 0
		 -1.2229684632711994e-16 0.052335956242943876 -0.99862953475457383 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415794 24.820753250668531 -1.6332272520910469 1;
	setAttr ".wm[20]" -type "matrix" 6.4093061293237156e-18 0.99862953475457383 0.052335956242943876 0
		 -1.2229684632711994e-16 0.052335956242943876 -0.99862953475457383 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415791 9.2387371680789343 -2.4498461117322008 1;
	setAttr ".wm[21]" -type "matrix" 0 1 0 0 -1.2246467991473532e-16 0 -1 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415814 100.46989749000251 -4.4408920985006183e-16 1;
	setAttr ".wm[22]" -type "matrix" 0 1 0 0 -1.2246467991473532e-16 0 -1 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415814 85.641567490002529 -3.9264310552899951e-16 1;
	setAttr ".wm[23]" -type "matrix" 0 1 0 0 -1.2246467991473532e-16 0 -1 0 -1 0 1.2246467991473532e-16 0
		 -10.250824075415814 70.813237490002521 -3.411970012079372e-16 1;
	setAttr ".wm[24]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 112.32684918273493 0 1;
	setAttr ".wm[25]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 124.37879638289658 1.1664122257998452e-16 1;
	setAttr ".wm[26]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 135.32967493308848 -5.1627478191447992e-15 1;
	setAttr ".wm[27]" -type "matrix" 0.9282927426960923 0 -0.37185021696614157 0 -0.37185021696614157 1.1102230246251567e-15 -0.92829274269609252 0
		 3.3306690738754696e-16 1 1.0547118733938989e-15 0 3.0000000000000004 152.45063954009461 3.7349994120846188e-15 1;
	setAttr ".wm[28]" -type "matrix" 1 -4.1283667258767058e-16 1.6653345369377348e-16 0
		 1.1102230246251565e-16 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 17.28121977414451 152.45063954009501 -5.7206896351826355 1;
	setAttr ".wm[29]" -type "matrix" 0.99999390765779039 -4.1643166459981815e-16 0.0034906514152238995 0
		 0.0034906514152238432 1.0291646287773671e-15 -0.99999390765779061 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 47.631869391267344 152.45063954009495 -5.7206896351815884 1;
	setAttr ".wm[30]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 5.5511151231257827e-17 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 76.892350881396879 152.4506395400943 -5.6185508717936914 1;
	setAttr ".wm[31]" -type "matrix" 0.82139380484326951 -0.42261826174070033 0.38302222155948895 0
		 -0.34968662994703908 0.15737869562426182 0.92355357559802098 0 -0.45059014436778316 -0.89253893528903006 -0.018514070102097973 0
		 79.925357891549069 150.69808492776352 -2.4402200443671833 1;
	setAttr ".wm[32]" -type "matrix" 0.82139380484326951 -0.42261826174070033 0.38302222155948895 0
		 -0.34968662994703908 0.15737869562426182 0.92355357559802098 0 -0.45059014436778316 -0.89253893528903006 -0.018514070102097973 0
		 82.751910404914966 149.243785293564 -1.1221769612072954 1;
	setAttr ".wm[33]" -type "matrix" 0.82139380484326951 -0.42261826174070033 0.38302222155948895 0
		 -0.34968662994703908 0.15737869562426182 0.92355357559802098 0 -0.45059014436778316 -0.89253893528903006 -0.018514070102097973 0
		 84.967637096572332 148.10376383564773 -0.088966636508926777 1;
	setAttr ".wm[34]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 81.449350881396597 152.1736395400944 -9.3465508717936459 1;
	setAttr ".wm[35]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 84.757784714493624 151.86120680354395 -8.9796764956476594 1;
	setAttr ".wm[36]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 87.495407019922368 151.86120680354392 -8.9796764956474746 1;
	setAttr ".wm[37]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 89.789743365589246 151.86120680354409 -8.9796764956474266 1;
	setAttr ".wm[38]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.0547118733938989e-15 0 -5.5511151231257827e-17 -1.0306119765336379e-15 1.0000000000000002 0
		 81.552350881396563 153.21063954009432 -7.5085508717936253 1;
	setAttr ".wm[39]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.0547118733938989e-15 0 -5.5511151231257827e-17 -1.0306119765336379e-15 1.0000000000000002 0
		 85.190870295968594 153.07456659275465 -7.5089377119854994 1;
	setAttr ".wm[40]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.0547118733938989e-15 0 -5.5511151231257827e-17 -1.0306119765336379e-15 1.0000000000000002 0
		 89.050841914281079 153.07456659275479 -7.5089377119855349 1;
	setAttr ".wm[41]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.0547118733938989e-15 0 -5.5511151231257827e-17 -1.0306119765336379e-15 1.0000000000000002 0
		 91.778956671687524 153.07456659275479 -7.5089377119854355 1;
	setAttr ".wm[42]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754706e-16 1.0000000000000002 8.326672684688678e-16 0 -5.5511151231257765e-17 -8.0856737160860682e-16 1.0000000000000004 0
		 81.641350881396534 153.92063954009441 -5.2485508717936069 1;
	setAttr ".wm[43]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754706e-16 1.0000000000000002 8.326672684688678e-16 0 -5.5511151231257765e-17 -8.0856737160860682e-16 1.0000000000000004 0
		 85.791055874930933 153.96044948176149 -5.2457988277611163 1;
	setAttr ".wm[44]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754706e-16 1.0000000000000002 8.326672684688678e-16 0 -5.5511151231257765e-17 -8.0856737160860682e-16 1.0000000000000004 0
		 90.186452766359935 153.96044948176143 -5.2457988277611234 1;
	setAttr ".wm[45]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754706e-16 1.0000000000000002 8.326672684688678e-16 0 -5.5511151231257765e-17 -8.0856737160860682e-16 1.0000000000000004 0
		 92.78980345158844 153.96044948176186 -5.2457988277611136 1;
	setAttr ".wm[46]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 81.704350881396493 153.68463954009414 -3.0815508717936262 1;
	setAttr ".wm[47]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 85.588492714920989 153.74282684774823 -3.0735658195467379 1;
	setAttr ".wm[48]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 89.422290377367162 153.74282684774832 -3.0735658195467424 1;
	setAttr ".wm[49]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 3.3306690738754696e-16 1 1.2767564783189302e-15 0 -5.5511151231257901e-17 -1.2526565814586692e-15 1.0000000000000002 0
		 91.773227967718228 153.7428268477484 -3.073565819546705 1;
	setAttr ".wm[50]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 5.5511151231257827e-17 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 85.892350881396737 146.45063954009439 -5.6185508717936594 1;
	setAttr ".wm[51]" -type "matrix" 1 -4.1283667258767053e-16 1.1145598333150986e-16 0
		 5.5511151231257827e-17 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 85.892350881396524 146.45063954009478 -5.6185508717936585 1;
	setAttr ".wm[52]" -type "matrix" 0.99999390765779039 -4.1643166459981815e-16 0.0034906514152238995 0
		 0.0034906514152238432 1.0291646287773671e-15 -0.99999390765779061 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 76.892691123242059 152.45063954009447 -5.6185496841207208 1;
	setAttr ".wm[53]" -type "matrix" 0.99999390765779039 -4.1643166459981815e-16 0.0034906514152238995 0
		 0.0034906514152238432 1.0291646287773671e-15 -0.99999390765779061 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 67.138750547947978 152.4506395400945 -5.6525974980248019 1;
	setAttr ".wm[54]" -type "matrix" 0.99999390765779039 -4.1643166459981815e-16 0.0034906514152238995 0
		 0.0034906514152238432 1.0291646287773671e-15 -0.99999390765779061 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 57.385809966561538 152.45063954009447 -5.6866418212774761 1;
	setAttr ".wm[55]" -type "matrix" 1 -4.1283667258767058e-16 1.6653345369377348e-16 0
		 1.1102230246251565e-16 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 17.28121977414451 152.45063954009544 -5.7206896351826355 1;
	setAttr ".wm[56]" -type "matrix" 1 -4.1283667258767058e-16 1.6653345369377348e-16 0
		 1.1102230246251565e-16 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 27.398219774144501 152.45063954009547 -5.7206896351826391 1;
	setAttr ".wm[57]" -type "matrix" 1 -4.1283667258767058e-16 1.6653345369377348e-16 0
		 1.1102230246251565e-16 1.0306119765336379e-15 -1.0000000000000002 0 3.3306690738754696e-16 1 1.0547118733938989e-15 0
		 37.515219774144498 152.45063954009569 -5.7206896351826382 1;
	setAttr ".wm[58]" -type "matrix" 0.92829274269609219 -6.6613381477509392e-16 0.37185021696614134 0
		 -0.37185021696614134 1.3877787807814454e-16 0.92829274269609241 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -3.0000000000000102 152.45063954009453 3.0177095473597349e-14 1;
	setAttr ".wm[59]" -type "matrix" 0.99999999999999978 -6.6997176999364148e-16 -2.2204460492503131e-16 0
		 1.6653345369377348e-16 -1.1887550648589755e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -17.281219774144457 152.45063954009512 -5.7206896351826142 1;
	setAttr ".wm[60]" -type "matrix" 0.99999390765779017 -6.6955273534139751e-16 -0.0034906514152239542 0
		 0.0034906514152238978 -1.2121342016271994e-16 0.99999390765779039 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -47.631869391267017 152.45063954009461 -5.7206896351816114 1;
	setAttr ".wm[61]" -type "matrix" 0.99999999999999978 -6.6997176999364158e-16 -1.7824283715661693e-16 0
		 1.227316859253591e-16 -1.1887550648589751e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -76.892350881396354 152.45063954009413 -5.6185508717937367 1;
	setAttr ".wm[62]" -type "matrix" -0.82139380484326996 -0.42261826174069889 0.38302222155948923 0
		 0.3496866299470392 0.15737869562426227 0.92355357559802032 0 -0.45059014436778205 0.89253893528903039 0.018514070102097116 0
		 -79.925357891549126 150.69808492776386 -2.4402200443673934 1;
	setAttr ".wm[63]" -type "matrix" -0.82139380484326996 -0.42261826174069889 0.38302222155948923 0
		 0.3496866299470392 0.15737869562426227 0.92355357559802032 0 -0.45059014436778205 0.89253893528903039 0.018514070102097116 0
		 -82.751910404914966 149.24378529356431 -1.1221769612074717 1;
	setAttr ".wm[64]" -type "matrix" -0.82139380484326996 -0.42261826174069889 0.38302222155948923 0
		 0.3496866299470392 0.15737869562426227 0.92355357559802032 0 -0.45059014436778205 0.89253893528903039 0.018514070102097116 0
		 -84.967637096572474 148.1037638356481 -0.088966636509117514 1;
	setAttr ".wm[65]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509392e-16 0.99999999999999978 1.3877787807814454e-16 0 -2.451963658400944e-16 1.1887550648589758e-16 -1 0
		 -81.449350881396441 152.17363954009454 -9.3465508717937844 1;
	setAttr ".wm[66]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509392e-16 0.99999999999999978 1.3877787807814454e-16 0 -2.451963658400944e-16 1.1887550648589758e-16 -1 0
		 -84.757784714493567 151.86120680354375 -8.9796764956477286 1;
	setAttr ".wm[67]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509392e-16 0.99999999999999978 1.3877787807814454e-16 0 -2.451963658400944e-16 1.1887550648589758e-16 -1 0
		 -87.495407019922155 151.8612068035435 -8.9796764956475936 1;
	setAttr ".wm[68]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509392e-16 0.99999999999999978 1.3877787807814454e-16 0 -2.451963658400944e-16 1.1887550648589758e-16 -1 0
		 -89.789743365589189 151.86120680354364 -8.9796764956475723 1;
	setAttr ".wm[69]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -81.552350881396393 153.21063954009469 -7.5085508717937648 1;
	setAttr ".wm[70]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -85.190870295968821 153.07456659275462 -7.5089377119857579 1;
	setAttr ".wm[71]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -89.050841914281392 153.07456659275468 -7.5089377119856984 1;
	setAttr ".wm[72]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -91.778956671687695 153.07456659275468 -7.5089377119856247 1;
	setAttr ".wm[73]" -type "matrix" -0.99999999999999978 7.9243644990837683e-16 1.7824283715661695e-16 0
		 7.8859849468982927e-16 0.99999999999999978 5.8286708792820718e-16 0 -1.2273168592535876e-16 5.6296471633596002e-16 -1 0
		 -81.641350881396477 153.92063954009461 -5.2485508717937943 1;
	setAttr ".wm[74]" -type "matrix" -0.99999999999999978 7.9243644990837683e-16 1.7824283715661695e-16 0
		 7.8859849468982927e-16 0.99999999999999978 5.8286708792820718e-16 0 -1.2273168592535876e-16 5.6296471633596002e-16 -1 0
		 -85.791055874930748 153.96044948176129 -5.2457988277612628 1;
	setAttr ".wm[75]" -type "matrix" -0.99999999999999978 7.9243644990837683e-16 1.7824283715661695e-16 0
		 7.8859849468982927e-16 0.99999999999999978 5.8286708792820718e-16 0 -1.2273168592535876e-16 5.6296471633596002e-16 -1 0
		 -90.186452766360063 153.96044948176103 -5.2457988277612353 1;
	setAttr ".wm[76]" -type "matrix" -0.99999999999999978 7.9243644990837683e-16 1.7824283715661695e-16 0
		 7.8859849468982927e-16 0.99999999999999978 5.8286708792820718e-16 0 -1.2273168592535876e-16 5.6296471633596002e-16 -1 0
		 -92.789803451588554 153.96044948176123 -5.2457988277613836 1;
	setAttr ".wm[77]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -81.704350881396451 153.68463954009474 -3.0815508717937714 1;
	setAttr ".wm[78]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -85.588492714920974 153.74282684774781 -3.0735658195468667 1;
	setAttr ".wm[79]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -89.422290377366977 153.74282684774792 -3.0735658195468583 1;
	setAttr ".wm[80]" -type "matrix" -0.99999999999999978 6.6997176999364158e-16 3.0070751707135227e-16 0
		 6.6613381477509402e-16 1 -3.0531133177191805e-16 0 -2.451963658400946e-16 -1.0316909843913365e-16 -1.0000000000000002 0
		 -91.773227967718327 153.74282684774795 -3.0735658195467339 1;
	setAttr ".wm[81]" -type "matrix" 0.99999999999999978 -6.6997176999364158e-16 -1.7824283715661693e-16 0
		 1.227316859253591e-16 -1.1887550648589751e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -85.892350881396425 146.45063954009467 -5.6185508717937545 1;
	setAttr ".wm[82]" -type "matrix" 0.99999999999999978 -6.6997176999364158e-16 -1.7824283715661693e-16 0
		 1.227316859253591e-16 -1.1887550648589751e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -85.892350881396325 146.4506395400947 -5.6185508717938033 1;
	setAttr ".wm[83]" -type "matrix" 0.99999390765779017 -6.6955273534139751e-16 -0.0034906514152239542 0
		 0.0034906514152238978 -1.2121342016271994e-16 0.99999390765779039 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -57.385809966561169 152.4506395400941 -5.6866418212775267 1;
	setAttr ".wm[84]" -type "matrix" 0.99999390765779017 -6.6955273534139751e-16 -0.0034906514152239542 0
		 0.0034906514152238978 -1.2121342016271994e-16 0.99999390765779039 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -67.138750547947481 152.4506395400939 -5.6525974980248366 1;
	setAttr ".wm[85]" -type "matrix" 0.99999390765779017 -6.6955273534139751e-16 -0.0034906514152239542 0
		 0.0034906514152238978 -1.2121342016271994e-16 0.99999390765779039 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -76.892691123241718 152.45063954009407 -5.6185496841207483 1;
	setAttr ".wm[86]" -type "matrix" 0.99999999999999978 -6.6997176999364148e-16 -2.2204460492503131e-16 0
		 1.6653345369377348e-16 -1.1887550648589755e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -17.281219774144528 152.45063954009467 -5.720689635182608 1;
	setAttr ".wm[87]" -type "matrix" 0.99999999999999978 -6.6997176999364148e-16 -2.2204460492503131e-16 0
		 1.6653345369377348e-16 -1.1887550648589755e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -27.398219774144529 152.45063954009444 -5.7206896351826035 1;
	setAttr ".wm[88]" -type "matrix" 0.99999999999999978 -6.6997176999364148e-16 -2.2204460492503131e-16 0
		 1.6653345369377348e-16 -1.1887550648589755e-16 1 0 -6.6613381477509392e-16 -0.99999999999999978 -1.3877787807814454e-16 0
		 -37.515219774144498 152.4506395400945 -5.7206896351826071 1;
	setAttr ".wm[89]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 157.47181980425674 -4.0901220894534847 1;
	setAttr ".wm[90]" -type "matrix" 0 1 0 0 0 0 1 0 1 0 0 0 0 163.68777807613938 -2.3517326116629915 1;
	setAttr ".wm[91]" -type "matrix" 0 0.99987202616752791 0.015997852594718635 0 0 -0.015997852594718635 0.99987202616752791 0
		 1 0 0 0 0 169.90373634802202 -0.61334313387248218 1;
	setAttr ".wm[92]" -type "matrix" 1 0 0 0 0 1.0000000000000002 -6.9388939039072284e-18 0
		 0 -1.0408340855860843e-16 1.0000000000000002 0 3.1145353317260742 176.28836333650463 7.4668231010436861 1;
	setAttr ".wm[93]" -type "matrix" 1 0 0 0 0 1.0000000000000002 -6.9388939039072284e-18 0
		 0 -1.0408340855860843e-16 1.0000000000000002 0 -3.1145353317260742 176.28836333650463 7.4668231010436861 1;
	setAttr ".wm[94]" -type "matrix" 0 -0.74317002357032025 0.66910261998178566 0 0 -0.66910261998178566 -0.74317002357032025 0
		 1 0 0 0 -3.7617570592466878e-30 172.56536935136856 2.4219002499454554 1;
	setAttr ".wm[95]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 96 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 -0 1 0 103.34534728425831
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.50000000000000011 0.50000000000000011 0.50000000000000011 0.50000000000000011 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 -0 1 -2.8754497942558004 0
		 10.250824075415816 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 6.123233995736766e-17 1
		 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 44.485311800062036 5.2252795127396e-15
		 -1.5987211554602254e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.026176948307873166 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 -0 1 46.810241652265823 6.6613381477509392e-15
		 -6.2172489379008766e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.026176948307873212 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 1.9637069748057456e-15 1.8323016715004797e-17
		 2.3245294578089215e-16 0 5.635757490447892 13.547156637101248 0.11035332316931168 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.0063168970971849096 -0.0065271641577584463 0.71896663489025947 0.69498523067306794 1
		 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 1.9637069748057456e-15 1.8323016715004797e-17
		 2.3245294578089215e-16 0 10.215816652113086 2.6645352591003757e-15 1.2434497875801753e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 15.603299191204819 2.0382410327979272e-05
		 8.8817841970012523e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249324523244e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 31.206599191201501 1.0180894986611122e-05
		 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249324523159e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 -5.5511151231257827e-17 -3.3306690738754701e-16
		 -5.5511151231257827e-17 0 46.809999191198145 -2.0685742896375814e-08 -8.8817841970012523e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -3.2690249327298875e-07 0.9999999999999466 1
		 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 -0 1 2.8421709430404007e-14
		 -2.1191937094044988e-12 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 3.439935858254653e-07 0.99999999999994083 1
		 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 -0 1 14.828329999996512 1.0201698699106963e-05
		 -8.8817841970012523e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.615032094298019e-14 1.5274118006740722e-07 3.0214720694583242e-07 0.99999999999994271 1
		 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 -0 1 29.656659999992996 2.0403399517851725e-05
		 -1.5987211554602254e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.6478608921569813e-14 1.5328347571560156e-07 3.0321995704091692e-07 0.99999999999994227 1
		 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 -0 1 -2.8754497942558004
		 0 -10.250824075415816 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 6.123233995736766e-17 1
		 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 -44.485311800061893 -6.8156775771823734e-15
		 -2.3092638912203256e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.026176948307873166 0.99965732497555726 1
		 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 -0 1 -46.810241652265958
		 -1.4654943925052066e-14 1.4210854715202004e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0.026176948307873097 0.99965732497555726 1 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 -6.203371150093063e-15 -2.4750607197806469e-31
		 -7.9797279894933126e-17 0 -5.6357574857569315 -13.547156637855489 -0.11035347015034169 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.0063190324569505915 -0.0065229302991719864 0.7189666750727598 0.69498520944257569 1
		 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 -6.203371150093063e-15 -2.4750607197806469e-31
		 -7.9797279894933126e-17 0 -10.215816652113055 1.7763568394002505e-14 -4.4408920985006262e-14 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 1 1 1 1.1102230246251565e-16 -1.1102230246251565e-16
		 -1.1102230246251565e-16 0 -15.603299999999997 2.6645352591003757e-15 1.7763568394002505e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 1.1102230246251565e-16 -1.1102230246251565e-16
		 -1.1102230246251565e-16 0 -31.206600000000002 1.3322676295501878e-15 1.7763568394002505e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 1.1102230246251565e-16 -1.1102230246251565e-16
		 -1.1102230246251565e-16 0 -46.81000000000008 4.4408920985006262e-16 -1.7763568394002505e-15 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 -0 1 0 4.4408920985006163e-16
		 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 1 1 1 0 0 -0 1 -14.82832999999998 3.9264310552899931e-16
		 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 0 0 -0 1 -29.656659999999988
		 3.41197001207937e-16 -1.7763568394002505e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 1 1 1 0 0 -0 1 8.9815018984766226 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 0 0 -0 1 12.051947200161649 1.1664122257998452e-16
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 -0 1 10.950878550191902 -5.2793890417247838e-15
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 17.12096460700613 8.897747231229418e-15
		 3.0000000000000004 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.69431490382536287 0.13389105394303541 -0.69431490382536298 0.13389105394303619 1
		 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 15.384392355224897
		 1.1990408665951691e-14 3.979039320256561e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 -0.18935054436666893 0.98190955354759946 1 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 1 1 1 0 0 0 0 30.350649617122833 -1.0418332863082469e-12
		 -5.6843418860808015e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.0017453283658983088 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 1 1 1 -0 0 -0 5 29.260659756082042
		 5.595524044110789e-14 -6.5369931689929217e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0.0017453283658983366 0.99999847691328769 1 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.0330070101521898 -3.1783308274265085
		 -1.7525546123307834 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.95360976239370576 -0.19208823158104979 -0.22892184008178465 0.036404992639125847 1
		 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.4411660968214735 1.3855583347321954e-13
		 -1.9895196601282805e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.6975205785490779 7.0166095156309893e-14
		 1.1368683772161603e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.5569999999997179 3.7279999999999527
		 -0.27699999999990155 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654746 1
		 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.3084338330970269 -0.31243273655044845
		 0.3668743761459865 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[36]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.7376223054287436 -2.8421709430404007e-14
		 1.8474111129762605e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[37]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.2943363456668777 1.7053025658242404e-13
		 4.7961634663806763e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[38]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.659999999999684 1.8899999999999348
		 0.76000000000001933 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654757 1
		 1 1 yes;
	setAttr ".xm[39]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.6385194145720305 -0.13607294733967024
		 -0.00038684019187407159 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[40]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8599716183124855 1.4210854715202004e-13
		 -3.5527136788005009e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[41]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.7281147574064448 0
		 9.9475983006414026e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[42]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.7489999999996542 -0.37000000000008271
		 1.4700000000001125 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654746 0 0 0.70710678118654768 1
		 1 1 yes;
	setAttr ".xm[43]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.1497049935343995 0.03980994166707319
		 0.0027520440324897422 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[44]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.3953968914290016 -5.6843418860808015e-14
		 -7.9936057773011271e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[45]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.6033506852285058 4.2632564145606011e-13
		 9.7699626167013776e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[46]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.8119999999996139 -2.537000000000063
		 1.2339999999998383 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654757 0 0 0.70710678118654746 1
		 1 1 yes;
	setAttr ".xm[47]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8841418335244953 0.058187307654094411
		 0.007985052246887836 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[48]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8337976624461731 8.5265128291212022e-14
		 -4.8849813083506888e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[49]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.3509375903510659 8.5265128291212022e-14
		 3.6859404417555197e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[50]" -type "matrix" "xform" 1 1 1 -1.3877787807814457e-17 -1.1102230246251565e-16
		 7.7037197775489451e-34 0 8.9999999999998579 -3.730349362740526e-14 -5.9999999999999147 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[51]" -type "matrix" "xform" 1 1 1 -1.3877787807814457e-17 -1.1102230246251565e-16
		 7.7037197775489451e-34 0 -2.1316282072803006e-13 -8.8817841970012523e-16 3.979039320256561e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[52]" -type "matrix" "xform" 1 1 1 -1.6653345369377348e-16 1.1102230246251565e-16
		 5.5511151231257815e-17 0 29.261000000000102 -8.8817841970012523e-16 -4.8316906031686813e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[53]" -type "matrix" "xform" 1 1 1 -1.6653345369377348e-16 1.1102230246251565e-16
		 5.5511151231257815e-17 0 19.507000000000112 -1.3322676295501878e-14 -4.5474735088646412e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[54]" -type "matrix" "xform" 1 1 1 -1.6653345369377348e-16 1.1102230246251565e-16
		 5.5511151231257815e-17 0 9.7540000000001044 -1.7763568394002505e-14 -4.8316906031686813e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[55]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 0 0 4.2632564145606011e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[56]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 10.11699999999999 5.3290705182007514e-15
		 4.5474735088646412e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[57]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 20.233999999999988
		 6.2172489379008766e-15 6.8212102632969618e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[58]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 17.120964607006044
		 3.5339843292742149e-14 -3.0000000000000102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		-0.13389105394303574 -0.69431490382536332 0.13389105394303574 0.69431490382536276 1
		 1 1 yes;
	setAttr ".xm[59]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 -15.384392355224843
		 -4.3298697960381105e-14 -5.9685589803848416e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 -0.18935054436666887 0.98190955354759946 1 1 1 yes;
	setAttr ".xm[60]" -type "matrix" "xform" 1 1 1 0 0 0 0 -30.350649617122567 9.9564800848384039e-13
		 5.4001247917767614e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -0.0017453283658983088 0.99999847691328769 1
		 1 1 yes;
	setAttr ".xm[61]" -type "matrix" "xform" 1 1 1 -0 0 -0 5 -29.260659756081857
		 -7.9047879353311146e-14 5.1159076974727213e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0.0017453283658983307 0.99999847691328769 1 1 1 yes;
	setAttr ".xm[62]" -type "matrix" "xform" 1 1 1 0 0 0 0 -3.0330070101527724 3.1783308274263433
		 1.7525546123302718 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.19208823158104976 -0.95360976239370576 0.036404992639125867 0.22892184008178459 1
		 1 1 yes;
	setAttr ".xm[63]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.441166096821457 1.8207657603852567e-13
		 1.4210854715202004e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[64]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.697520578549164 1.5987211554602254e-14
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[65]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.5570000000000874 -3.7280000000000477
		 0.27699999999958891 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.329780281177467e-17 -0.70710678118654757 0.70710678118654757 4.329780281177467e-17 1
		 1 1 yes;
	setAttr ".xm[66]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.3084338330971264 -0.31243273655078951
		 -0.366874376146054 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[67]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.7376223054285873 -2.5579538487363607e-13
		 -1.3500311979441904e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[68]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.294336345667034 1.4210854715202004e-13
		 -2.1316282072803006e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[69]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.6600000000000392 -1.890000000000029
		 -0.76000000000055934 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.3297802811774658e-17 -0.70710678118654746 0.70710678118654768 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[70]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.6385194145724284 -0.13607294734006814
		 0.00038684019199397568 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[71]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8599716183125707 5.6843418860808015e-14
		 -5.8619775700208265e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[72]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.7281147574063027 0
		 -7.2830630415410269e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[73]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.7490000000001231 0.36999999999994149
		 -1.470000000000482 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4.3297802811774652e-17 0.70710678118654768 -0.70710678118654735 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[74]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.1497049935342716 0.039809941666675286
		 -0.0027520440325305984 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[75]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.3953968914293142 -2.5579538487363607e-13
		 -2.6645352591003757e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[76]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.6033506852284916 1.9895196601282805e-13
		 1.4921397450962104e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[77]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.8120000000000971 2.5369999999999644
		 -1.2340000000006057 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -4.3297802811774658e-17 -0.70710678118654746 0.70710678118654768 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[78]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8841418335245237 0.05818730765307123
		 -0.0079850522469033791 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[79]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8337976624460026 1.1368683772161603e-13
		 -7.1054273576010019e-15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[80]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.3509375903513501 2.8421709430404007e-14
		 -1.2345680033831741e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[81]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.0000000000000711 -1.865174681370263e-14
		 5.99999999999946 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[82]" -type "matrix" "xform" 1 1 1 0 0 0 0 9.9475983006414026e-14
		 -4.8849813083506888e-14 -2.8421709430404007e-14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[83]" -type "matrix" "xform" 1 1 1 -1.2490009027033014e-16 4.1633363423443364e-17
		 -5.5511151231257827e-17 0 -9.7540000000000688 -9.7699626167013776e-15 5.1159076974727213e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[84]" -type "matrix" "xform" 1 1 1 -1.2490009027033014e-16 4.1633363423443364e-17
		 -5.5511151231257827e-17 0 -19.506999999999955 1.7763568394002505e-15 7.1054273576010019e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[85]" -type "matrix" "xform" 1 1 1 -1.2490009027033014e-16 4.1633363423443364e-17
		 -5.5511151231257827e-17 0 -29.261000000000102 -5.3290705182007514e-15 5.6843418860808015e-13 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[86]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 -7.1054273576010019e-14
		 6.2172489379008766e-15 4.5474735088646412e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[87]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 -10.117000000000075
		 7.9936057773011271e-15 6.8212102632969618e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[88]" -type "matrix" "xform" 1 1 1 -0 -0 0 3 -20.234000000000041
		 2.6645352591003757e-15 6.2527760746888816e-13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[89]" -type "matrix" "xform" 1 1 1 0 0 -0 1 22.142144871168256 -4.0901220894534793
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[90]" -type "matrix" "xform" 1 1 1 0 0 -0 1 6.2159582718826414 1.7383894777904931
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[91]" -type "matrix" "xform" 1 1 1 0 0 -0 1 6.2159582718826414 1.7383894777905093
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0.0079991822229547836 0.99996800603007496 1
		 1 1 yes;
	setAttr ".xm[92]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.5130752316649989 7.976991863642068
		 3.1145353317260742 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.50398359412651483 -0.49598441190356013 -0.50398359412651483 0.49598441190356013 1
		 1 1 yes;
	setAttr ".xm[93]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.5130752316649989 7.976991863642068
		 -3.1145353317260742 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -0.50398359412651483 -0.49598441190356013 -0.50398359412651483 0.49598441190356013 1
		 1 1 yes;
	setAttr ".xm[94]" -type "matrix" "xform" 1 1 1 0 0 -1.1102230246251568e-16 0 2.7098497602138707
		 2.992274539640849 -3.7617570592466878e-30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0.93069079510034292 0.36580683962371668 1 1 1 yes;
	setAttr ".xm[95]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 96 ".m";
	setAttr -s 96 ".p";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "02F83088-461A-38A3-3310-279CF5457779";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -camera \"|top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n"
		+ "            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n"
		+ "            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -bluePencil 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n"
		+ "            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n"
		+ "            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n"
		+ "            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n"
		+ "            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -bluePencil 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 1\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -bluePencil 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"ModelPanel\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"ModelPanel\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 0\n            -holdOuts 1\n            -selectionHiliteDisplay 0\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 0\n            -nurbsCurves 0\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 0\n            -lights 0\n            -cameras 0\n            -controlVertices 0\n            -hulls 0\n            -grid 0\n            -imagePlane 0\n            -joints 0\n            -ikHandles 0\n            -deformers 0\n            -dynamics 0\n"
		+ "            -particleInstancers 0\n            -fluids 0\n            -hairSystems 0\n            -follicles 0\n            -nCloths 0\n            -nParticles 0\n            -nRigids 0\n            -dynamicConstraints 0\n            -locators 0\n            -manipulators 0\n            -pluginShapes 0\n            -dimensions 0\n            -handles 0\n            -pivots 0\n            -textures 0\n            -strokes 0\n            -motionTrails 0\n            -clipGhosts 0\n            -bluePencil 0\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1319\n            -height 723\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n"
		+ "            -pluginObjects \"gpuCacheDisplayFilter\" 0 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner2\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner2\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n"
		+ "            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -showUfeItems 1\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n"
		+ "            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n"
		+ "            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n"
		+ "            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -showUfeItems 1\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n"
		+ "                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -showUfeItems 1\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n"
		+ "                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -showUfeItems 1\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n"
		+ "                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n"
		+ "                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -image \"C:/work/Batman/characters/Bane/sourceimages/Bane_tpage_2048.tga\" \n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n"
		+ "                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n"
		+ "                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"|persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n"
		+ "                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n"
		+ "                -clipGhosts 1\n                -bluePencil 1\n                -greasePencils 0\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n"
		+ "            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n"
		+ "            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n"
		+ "            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -bluePencil 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1135\n            -height 724\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n"
		+ "            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n"
		+ "            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -showUfeItems 1\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n"
		+ "            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n"
		+ "\t\t\t\t-removeAllPanels\n\t\t\t\t-ap true\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -bluePencil 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1135\\n    -height 724\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -bluePencil 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1135\\n    -height 724\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "BEDDB1E3-49E1-0CF3-6798-4D9B64D02CB4";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 100 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".fzn";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".rm";
	setAttr -av -k on ".lm";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -av -k on ".hom";
	setAttr -av -k on ".hodm";
	setAttr -av -k on ".xry";
	setAttr -av -k on ".jxr";
	setAttr -av -k on ".sslt";
	setAttr -av -k on ".cbr";
	setAttr -av -k on ".bbr";
	setAttr -av -k on ".mhl";
	setAttr -k on ".cons";
	setAttr -k on ".vac";
	setAttr -av -k on ".hwi";
	setAttr -k on ".csvd";
	setAttr -av -k on ".ta";
	setAttr -av -k on ".tq";
	setAttr -k on ".ts";
	setAttr -av -k on ".etmr";
	setAttr -av -k on ".tmr";
	setAttr -av -k on ".aoon";
	setAttr -av -k on ".aoam";
	setAttr -av -k on ".aora";
	setAttr -k on ".aofr";
	setAttr -av -k on ".aosm";
	setAttr -av -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av -k on ".mbe";
	setAttr -av -k on ".mbt";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".mbsc";
	setAttr -k on ".mbc";
	setAttr -k on ".mbfa";
	setAttr -k on ".mbftb";
	setAttr -k on ".mbftg";
	setAttr -k on ".mbftr";
	setAttr -av -k on ".mbfta";
	setAttr -k on ".mbfe";
	setAttr -k on ".mbme";
	setAttr -av -k on ".mbcsx";
	setAttr -av -k on ".mbcsy";
	setAttr -av -k on ".mbasx";
	setAttr -av -k on ".mbasy";
	setAttr -av -k on ".blen";
	setAttr -av -k on ".blth";
	setAttr -av -k on ".blfr";
	setAttr -av -k on ".blfa";
	setAttr -av -k on ".blat";
	setAttr -av -k on ".msaa";
	setAttr -av -k on ".aasc";
	setAttr -av -k on ".aasq";
	setAttr -k on ".laa";
	setAttr -k on ".fprt" yes;
	setAttr -k on ".rtfm";
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -k on ".hio";
	setAttr -cb on ".ai_override";
	setAttr -cb on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -k on ".hio";
	setAttr -cb on ".ai_override";
	setAttr -cb on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".macc";
	setAttr -av -k on ".macd";
	setAttr -av -k on ".macq";
	setAttr -av -k on ".mcfr" 30;
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -av -k on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf" 51;
	setAttr -av -cb on ".imfkey" -type "string" "exr";
	setAttr -av -k on ".gama";
	setAttr -av -k on ".exrc";
	setAttr -av -k on ".expt";
	setAttr -av -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -av -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -av -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -cb on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -av -cb on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -av -k on ".pram";
	setAttr -av -k on ".poam";
	setAttr -av -k on ".prlm";
	setAttr -av -k on ".polm";
	setAttr -av -cb on ".prm";
	setAttr -av -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -k on ".ope";
	setAttr -av -k on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -av -k on ".hwcc";
	setAttr -av -k on ".hwdp";
	setAttr -av -k on ".hwql";
	setAttr -av -k on ".hwfr" 30;
	setAttr -av -k on ".soll";
	setAttr -av -k on ".sosl";
	setAttr -av -k on ".bswa";
	setAttr -av -k on ".shml";
	setAttr -av -k on ".hwel";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "C_root_JNT.s" "C_hips_JNT.is";
connectAttr "C_hips_JNT.s" "L_upperLeg_JNT.is";
connectAttr "L_upperLeg_JNT.s" "L_lowerLeg_JNT.is";
connectAttr "L_lowerLeg_JNT.s" "L_foot_JNT.is";
connectAttr "L_foot_JNT.s" "L_ball_JNT.is";
connectAttr "L_ball_JNT.s" "L_toe_JNT.is";
connectAttr "L_lowerLeg_JNT.s" "L_lowerLegTwist01_JNT.is";
connectAttr "L_lowerLeg_JNT.s" "L_lowerLegTwist02_JNT.is";
connectAttr "L_lowerLeg_JNT.s" "L_lowerLegTwist03_JNT.is";
connectAttr "L_upperLeg_JNT.s" "L_upperLegTwist01_JNT.is";
connectAttr "L_upperLeg_JNT.s" "L_upperLegTwist02_JNT.is";
connectAttr "L_upperLeg_JNT.s" "L_upperLegTwist03_JNT.is";
connectAttr "C_hips_JNT.s" "R_upperLeg_JNT.is";
connectAttr "R_upperLeg_JNT.s" "R_lowerLeg_JNT.is";
connectAttr "R_lowerLeg_JNT.s" "R_foot_JNT.is";
connectAttr "R_foot_JNT.s" "R_ball_JNT.is";
connectAttr "R_ball_JNT.s" "R_toe_JNT.is";
connectAttr "R_lowerLeg_JNT.s" "R_lowerLegTwist01_JNT.is";
connectAttr "R_lowerLeg_JNT.s" "R_lowerLegTwist02_JNT.is";
connectAttr "R_lowerLeg_JNT.s" "R_lowerLegTwist03_JNT.is";
connectAttr "R_upperLeg_JNT.s" "R_upperLegTwist01_JNT.is";
connectAttr "R_upperLeg_JNT.s" "R_upperLegTwist02_JNT.is";
connectAttr "R_upperLeg_JNT.s" "R_upperLegTwist03_JNT.is";
connectAttr "C_hips_JNT.s" "C_spine01_JNT.is";
connectAttr "C_spine01_JNT.s" "C_spine02_JNT.is";
connectAttr "C_spine02_JNT.s" "C_spine03_JNT.is";
connectAttr "C_spine03_JNT.s" "L_clavicle_JNT.is";
connectAttr "L_clavicle_JNT.s" "L_upperArm_JNT.is";
connectAttr "L_upperArm_JNT.s" "L_lowerArm_JNT.is";
connectAttr "L_lowerArm_JNT.s" "L_hand_JNT.is";
connectAttr "L_hand_JNT.s" "L_thumb01_JNT.is";
connectAttr "L_thumb01_JNT.s" "L_thumb02_JNT.is";
connectAttr "L_thumb02_JNT.s" "L_thumb03_JNT.is";
connectAttr "L_hand_JNT.s" "L_pinky_meta_JNT.is";
connectAttr "L_pinky_meta_JNT.s" "L_pinky01_JNT.is";
connectAttr "L_pinky01_JNT.s" "L_pinky02_JNT.is";
connectAttr "L_pinky02_JNT.s" "L_pinky03_JNT.is";
connectAttr "L_hand_JNT.s" "L_ring_meta_JNT.is";
connectAttr "L_ring_meta_JNT.s" "L_ring01_JNT.is";
connectAttr "L_ring01_JNT.s" "L_ring02_JNT.is";
connectAttr "L_ring02_JNT.s" "L_ring03_JNT.is";
connectAttr "L_hand_JNT.s" "L_middle_meta_JNT.is";
connectAttr "L_middle_meta_JNT.s" "L_middle01_JNT.is";
connectAttr "L_middle01_JNT.s" "L_middle02_JNT.is";
connectAttr "L_middle02_JNT.s" "L_middle03_JNT.is";
connectAttr "L_hand_JNT.s" "L_index_meta_JNT.is";
connectAttr "L_index_meta_JNT.s" "L_index01_JNT.is";
connectAttr "L_index01_JNT.s" "L_index02_JNT.is";
connectAttr "L_index02_JNT.s" "L_index03_JNT.is";
connectAttr "L_hand_JNT.s" "L_weapon_parent_JNT.is";
connectAttr "L_weapon_parent_JNT.s" "L_weapon_child_JNT.is";
connectAttr "L_lowerArm_JNT.s" "L_lowerArmTwist03_JNT.is";
connectAttr "L_lowerArm_JNT.s" "L_lowerArmTwist02_JNT.is";
connectAttr "L_lowerArm_JNT.s" "L_lowerArmTwist01_JNT.is";
connectAttr "L_upperArm_JNT.s" "L_upperArmTwist01_JNT.is";
connectAttr "L_upperArm_JNT.s" "L_upperArmTwist02_JNT.is";
connectAttr "L_upperArm_JNT.s" "L_upperArmTwist03_JNT.is";
connectAttr "C_spine03_JNT.s" "R_clavicle_JNT.is";
connectAttr "R_clavicle_JNT.s" "R_upperArm_JNT.is";
connectAttr "R_upperArm_JNT.s" "R_lowerArm_JNT.is";
connectAttr "R_lowerArm_JNT.s" "R_hand_JNT.is";
connectAttr "R_hand_JNT.s" "R_thumb01_JNT.is";
connectAttr "R_thumb01_JNT.s" "R_thumb02_JNT.is";
connectAttr "R_thumb02_JNT.s" "R_thumb03_JNT.is";
connectAttr "R_hand_JNT.s" "R_pinky_meta_JNT.is";
connectAttr "R_pinky_meta_JNT.s" "R_pinky01_JNT.is";
connectAttr "R_pinky01_JNT.s" "R_pinky02_JNT.is";
connectAttr "R_pinky02_JNT.s" "R_pinky03_JNT.is";
connectAttr "R_hand_JNT.s" "R_ring_meta_JNT.is";
connectAttr "R_ring_meta_JNT.s" "R_ring01_JNT.is";
connectAttr "R_ring01_JNT.s" "R_ring02_JNT.is";
connectAttr "R_ring02_JNT.s" "R_ring03_JNT.is";
connectAttr "R_hand_JNT.s" "R_middle_meta_JNT.is";
connectAttr "R_middle_meta_JNT.s" "R_middle01_JNT.is";
connectAttr "R_middle01_JNT.s" "R_middle02_JNT.is";
connectAttr "R_middle02_JNT.s" "R_middle03_JNT.is";
connectAttr "R_hand_JNT.s" "R_index_meta_JNT.is";
connectAttr "R_index_meta_JNT.s" "R_index01_JNT.is";
connectAttr "R_index01_JNT.s" "R_index02_JNT.is";
connectAttr "R_index02_JNT.s" "R_index03_JNT.is";
connectAttr "R_hand_JNT.s" "R_weapon_parent_JNT.is";
connectAttr "R_weapon_parent_JNT.s" "R_weapon_child_JNT.is";
connectAttr "R_lowerArm_JNT.s" "R_lowerArmTwist01_JNT.is";
connectAttr "R_lowerArm_JNT.s" "R_lowerArmTwist02_JNT.is";
connectAttr "R_lowerArm_JNT.s" "R_lowerArmTwist03_JNT.is";
connectAttr "R_upperArm_JNT.s" "R_upperArmTwist01_JNT.is";
connectAttr "R_upperArm_JNT.s" "R_upperArmTwist02_JNT.is";
connectAttr "R_upperArm_JNT.s" "R_upperArmTwist03_JNT.is";
connectAttr "C_spine03_JNT.s" "C_neck01_JNT.is";
connectAttr "C_neck01_JNT.s" "C_neck02_JNT.is";
connectAttr "C_neck02_JNT.s" "C_head_JNT.is";
connectAttr "C_head_JNT.s" "L_eye_JNT.is";
connectAttr "C_head_JNT.s" "R_eye_JNT.is";
connectAttr "C_head_JNT.s" "C_jaw_JNT.is";
connectAttr "C_root_JNT.s" "C_placement_JNT.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":defaultArnoldDisplayDriver.msg" ":defaultArnoldRenderOptions.drivers"
		 -na;
connectAttr ":defaultArnoldFilter.msg" ":defaultArnoldRenderOptions.filt";
connectAttr ":defaultArnoldDriver.msg" ":defaultArnoldRenderOptions.drvr";
connectAttr "C_root_JNT.msg" "apose.m[0]";
connectAttr "C_hips_JNT.msg" "apose.m[1]";
connectAttr "L_upperLeg_JNT.msg" "apose.m[2]";
connectAttr "L_lowerLeg_JNT.msg" "apose.m[3]";
connectAttr "L_foot_JNT.msg" "apose.m[4]";
connectAttr "L_ball_JNT.msg" "apose.m[5]";
connectAttr "L_toe_JNT.msg" "apose.m[6]";
connectAttr "L_lowerLegTwist01_JNT.msg" "apose.m[7]";
connectAttr "L_lowerLegTwist02_JNT.msg" "apose.m[8]";
connectAttr "L_lowerLegTwist03_JNT.msg" "apose.m[9]";
connectAttr "L_upperLegTwist01_JNT.msg" "apose.m[10]";
connectAttr "L_upperLegTwist02_JNT.msg" "apose.m[11]";
connectAttr "L_upperLegTwist03_JNT.msg" "apose.m[12]";
connectAttr "R_upperLeg_JNT.msg" "apose.m[13]";
connectAttr "R_lowerLeg_JNT.msg" "apose.m[14]";
connectAttr "R_foot_JNT.msg" "apose.m[15]";
connectAttr "R_ball_JNT.msg" "apose.m[16]";
connectAttr "R_toe_JNT.msg" "apose.m[17]";
connectAttr "R_lowerLegTwist01_JNT.msg" "apose.m[18]";
connectAttr "R_lowerLegTwist02_JNT.msg" "apose.m[19]";
connectAttr "R_lowerLegTwist03_JNT.msg" "apose.m[20]";
connectAttr "R_upperLegTwist01_JNT.msg" "apose.m[21]";
connectAttr "R_upperLegTwist02_JNT.msg" "apose.m[22]";
connectAttr "R_upperLegTwist03_JNT.msg" "apose.m[23]";
connectAttr "C_spine01_JNT.msg" "apose.m[24]";
connectAttr "C_spine02_JNT.msg" "apose.m[25]";
connectAttr "C_spine03_JNT.msg" "apose.m[26]";
connectAttr "L_clavicle_JNT.msg" "apose.m[27]";
connectAttr "L_upperArm_JNT.msg" "apose.m[28]";
connectAttr "L_lowerArm_JNT.msg" "apose.m[29]";
connectAttr "L_hand_JNT.msg" "apose.m[30]";
connectAttr "L_thumb01_JNT.msg" "apose.m[31]";
connectAttr "L_thumb02_JNT.msg" "apose.m[32]";
connectAttr "L_thumb03_JNT.msg" "apose.m[33]";
connectAttr "L_pinky_meta_JNT.msg" "apose.m[34]";
connectAttr "L_pinky01_JNT.msg" "apose.m[35]";
connectAttr "L_pinky02_JNT.msg" "apose.m[36]";
connectAttr "L_pinky03_JNT.msg" "apose.m[37]";
connectAttr "L_ring_meta_JNT.msg" "apose.m[38]";
connectAttr "L_ring01_JNT.msg" "apose.m[39]";
connectAttr "L_ring02_JNT.msg" "apose.m[40]";
connectAttr "L_ring03_JNT.msg" "apose.m[41]";
connectAttr "L_middle_meta_JNT.msg" "apose.m[42]";
connectAttr "L_middle01_JNT.msg" "apose.m[43]";
connectAttr "L_middle02_JNT.msg" "apose.m[44]";
connectAttr "L_middle03_JNT.msg" "apose.m[45]";
connectAttr "L_index_meta_JNT.msg" "apose.m[46]";
connectAttr "L_index01_JNT.msg" "apose.m[47]";
connectAttr "L_index02_JNT.msg" "apose.m[48]";
connectAttr "L_index03_JNT.msg" "apose.m[49]";
connectAttr "L_weapon_parent_JNT.msg" "apose.m[50]";
connectAttr "L_weapon_child_JNT.msg" "apose.m[51]";
connectAttr "L_lowerArmTwist03_JNT.msg" "apose.m[52]";
connectAttr "L_lowerArmTwist02_JNT.msg" "apose.m[53]";
connectAttr "L_lowerArmTwist01_JNT.msg" "apose.m[54]";
connectAttr "L_upperArmTwist01_JNT.msg" "apose.m[55]";
connectAttr "L_upperArmTwist02_JNT.msg" "apose.m[56]";
connectAttr "L_upperArmTwist03_JNT.msg" "apose.m[57]";
connectAttr "R_clavicle_JNT.msg" "apose.m[58]";
connectAttr "R_upperArm_JNT.msg" "apose.m[59]";
connectAttr "R_lowerArm_JNT.msg" "apose.m[60]";
connectAttr "R_hand_JNT.msg" "apose.m[61]";
connectAttr "R_thumb01_JNT.msg" "apose.m[62]";
connectAttr "R_thumb02_JNT.msg" "apose.m[63]";
connectAttr "R_thumb03_JNT.msg" "apose.m[64]";
connectAttr "R_pinky_meta_JNT.msg" "apose.m[65]";
connectAttr "R_pinky01_JNT.msg" "apose.m[66]";
connectAttr "R_pinky02_JNT.msg" "apose.m[67]";
connectAttr "R_pinky03_JNT.msg" "apose.m[68]";
connectAttr "R_ring_meta_JNT.msg" "apose.m[69]";
connectAttr "R_ring01_JNT.msg" "apose.m[70]";
connectAttr "R_ring02_JNT.msg" "apose.m[71]";
connectAttr "R_ring03_JNT.msg" "apose.m[72]";
connectAttr "R_middle_meta_JNT.msg" "apose.m[73]";
connectAttr "R_middle01_JNT.msg" "apose.m[74]";
connectAttr "R_middle02_JNT.msg" "apose.m[75]";
connectAttr "R_middle03_JNT.msg" "apose.m[76]";
connectAttr "R_index_meta_JNT.msg" "apose.m[77]";
connectAttr "R_index01_JNT.msg" "apose.m[78]";
connectAttr "R_index02_JNT.msg" "apose.m[79]";
connectAttr "R_index03_JNT.msg" "apose.m[80]";
connectAttr "R_weapon_parent_JNT.msg" "apose.m[81]";
connectAttr "R_weapon_child_JNT.msg" "apose.m[82]";
connectAttr "R_lowerArmTwist01_JNT.msg" "apose.m[83]";
connectAttr "R_lowerArmTwist02_JNT.msg" "apose.m[84]";
connectAttr "R_lowerArmTwist03_JNT.msg" "apose.m[85]";
connectAttr "R_upperArmTwist01_JNT.msg" "apose.m[86]";
connectAttr "R_upperArmTwist02_JNT.msg" "apose.m[87]";
connectAttr "R_upperArmTwist03_JNT.msg" "apose.m[88]";
connectAttr "C_neck01_JNT.msg" "apose.m[89]";
connectAttr "C_neck02_JNT.msg" "apose.m[90]";
connectAttr "C_head_JNT.msg" "apose.m[91]";
connectAttr "L_eye_JNT.msg" "apose.m[92]";
connectAttr "R_eye_JNT.msg" "apose.m[93]";
connectAttr "C_jaw_JNT.msg" "apose.m[94]";
connectAttr "C_placement_JNT.msg" "apose.m[95]";
connectAttr "apose.w" "apose.p[0]";
connectAttr "apose.m[0]" "apose.p[1]";
connectAttr "apose.m[1]" "apose.p[2]";
connectAttr "apose.m[2]" "apose.p[3]";
connectAttr "apose.m[3]" "apose.p[4]";
connectAttr "apose.m[4]" "apose.p[5]";
connectAttr "apose.m[5]" "apose.p[6]";
connectAttr "apose.m[3]" "apose.p[7]";
connectAttr "apose.m[3]" "apose.p[8]";
connectAttr "apose.m[3]" "apose.p[9]";
connectAttr "apose.m[2]" "apose.p[10]";
connectAttr "apose.m[2]" "apose.p[11]";
connectAttr "apose.m[2]" "apose.p[12]";
connectAttr "apose.m[1]" "apose.p[13]";
connectAttr "apose.m[13]" "apose.p[14]";
connectAttr "apose.m[14]" "apose.p[15]";
connectAttr "apose.m[15]" "apose.p[16]";
connectAttr "apose.m[16]" "apose.p[17]";
connectAttr "apose.m[14]" "apose.p[18]";
connectAttr "apose.m[14]" "apose.p[19]";
connectAttr "apose.m[14]" "apose.p[20]";
connectAttr "apose.m[13]" "apose.p[21]";
connectAttr "apose.m[13]" "apose.p[22]";
connectAttr "apose.m[13]" "apose.p[23]";
connectAttr "apose.m[1]" "apose.p[24]";
connectAttr "apose.m[24]" "apose.p[25]";
connectAttr "apose.m[25]" "apose.p[26]";
connectAttr "apose.m[26]" "apose.p[27]";
connectAttr "apose.m[27]" "apose.p[28]";
connectAttr "apose.m[28]" "apose.p[29]";
connectAttr "apose.m[29]" "apose.p[30]";
connectAttr "apose.m[30]" "apose.p[31]";
connectAttr "apose.m[31]" "apose.p[32]";
connectAttr "apose.m[32]" "apose.p[33]";
connectAttr "apose.m[30]" "apose.p[34]";
connectAttr "apose.m[34]" "apose.p[35]";
connectAttr "apose.m[35]" "apose.p[36]";
connectAttr "apose.m[36]" "apose.p[37]";
connectAttr "apose.m[30]" "apose.p[38]";
connectAttr "apose.m[38]" "apose.p[39]";
connectAttr "apose.m[39]" "apose.p[40]";
connectAttr "apose.m[40]" "apose.p[41]";
connectAttr "apose.m[30]" "apose.p[42]";
connectAttr "apose.m[42]" "apose.p[43]";
connectAttr "apose.m[43]" "apose.p[44]";
connectAttr "apose.m[44]" "apose.p[45]";
connectAttr "apose.m[30]" "apose.p[46]";
connectAttr "apose.m[46]" "apose.p[47]";
connectAttr "apose.m[47]" "apose.p[48]";
connectAttr "apose.m[48]" "apose.p[49]";
connectAttr "apose.m[30]" "apose.p[50]";
connectAttr "apose.m[50]" "apose.p[51]";
connectAttr "apose.m[29]" "apose.p[52]";
connectAttr "apose.m[29]" "apose.p[53]";
connectAttr "apose.m[29]" "apose.p[54]";
connectAttr "apose.m[28]" "apose.p[55]";
connectAttr "apose.m[28]" "apose.p[56]";
connectAttr "apose.m[28]" "apose.p[57]";
connectAttr "apose.m[26]" "apose.p[58]";
connectAttr "apose.m[58]" "apose.p[59]";
connectAttr "apose.m[59]" "apose.p[60]";
connectAttr "apose.m[60]" "apose.p[61]";
connectAttr "apose.m[61]" "apose.p[62]";
connectAttr "apose.m[62]" "apose.p[63]";
connectAttr "apose.m[63]" "apose.p[64]";
connectAttr "apose.m[61]" "apose.p[65]";
connectAttr "apose.m[65]" "apose.p[66]";
connectAttr "apose.m[66]" "apose.p[67]";
connectAttr "apose.m[67]" "apose.p[68]";
connectAttr "apose.m[61]" "apose.p[69]";
connectAttr "apose.m[69]" "apose.p[70]";
connectAttr "apose.m[70]" "apose.p[71]";
connectAttr "apose.m[71]" "apose.p[72]";
connectAttr "apose.m[61]" "apose.p[73]";
connectAttr "apose.m[73]" "apose.p[74]";
connectAttr "apose.m[74]" "apose.p[75]";
connectAttr "apose.m[75]" "apose.p[76]";
connectAttr "apose.m[61]" "apose.p[77]";
connectAttr "apose.m[77]" "apose.p[78]";
connectAttr "apose.m[78]" "apose.p[79]";
connectAttr "apose.m[79]" "apose.p[80]";
connectAttr "apose.m[61]" "apose.p[81]";
connectAttr "apose.m[81]" "apose.p[82]";
connectAttr "apose.m[60]" "apose.p[83]";
connectAttr "apose.m[60]" "apose.p[84]";
connectAttr "apose.m[60]" "apose.p[85]";
connectAttr "apose.m[59]" "apose.p[86]";
connectAttr "apose.m[59]" "apose.p[87]";
connectAttr "apose.m[59]" "apose.p[88]";
connectAttr "apose.m[26]" "apose.p[89]";
connectAttr "apose.m[89]" "apose.p[90]";
connectAttr "apose.m[90]" "apose.p[91]";
connectAttr "apose.m[91]" "apose.p[92]";
connectAttr "apose.m[91]" "apose.p[93]";
connectAttr "apose.m[91]" "apose.p[94]";
connectAttr "apose.m[0]" "apose.p[95]";
connectAttr "C_root_JNT.msg" "tpose.m[0]";
connectAttr "C_hips_JNT.msg" "tpose.m[1]";
connectAttr "L_upperLeg_JNT.msg" "tpose.m[2]";
connectAttr "L_lowerLeg_JNT.msg" "tpose.m[3]";
connectAttr "L_foot_JNT.msg" "tpose.m[4]";
connectAttr "L_ball_JNT.msg" "tpose.m[5]";
connectAttr "L_toe_JNT.msg" "tpose.m[6]";
connectAttr "L_lowerLegTwist01_JNT.msg" "tpose.m[7]";
connectAttr "L_lowerLegTwist02_JNT.msg" "tpose.m[8]";
connectAttr "L_lowerLegTwist03_JNT.msg" "tpose.m[9]";
connectAttr "L_upperLegTwist01_JNT.msg" "tpose.m[10]";
connectAttr "L_upperLegTwist02_JNT.msg" "tpose.m[11]";
connectAttr "L_upperLegTwist03_JNT.msg" "tpose.m[12]";
connectAttr "R_upperLeg_JNT.msg" "tpose.m[13]";
connectAttr "R_lowerLeg_JNT.msg" "tpose.m[14]";
connectAttr "R_foot_JNT.msg" "tpose.m[15]";
connectAttr "R_ball_JNT.msg" "tpose.m[16]";
connectAttr "R_toe_JNT.msg" "tpose.m[17]";
connectAttr "R_lowerLegTwist01_JNT.msg" "tpose.m[18]";
connectAttr "R_lowerLegTwist02_JNT.msg" "tpose.m[19]";
connectAttr "R_lowerLegTwist03_JNT.msg" "tpose.m[20]";
connectAttr "R_upperLegTwist01_JNT.msg" "tpose.m[21]";
connectAttr "R_upperLegTwist02_JNT.msg" "tpose.m[22]";
connectAttr "R_upperLegTwist03_JNT.msg" "tpose.m[23]";
connectAttr "C_spine01_JNT.msg" "tpose.m[24]";
connectAttr "C_spine02_JNT.msg" "tpose.m[25]";
connectAttr "C_spine03_JNT.msg" "tpose.m[26]";
connectAttr "L_clavicle_JNT.msg" "tpose.m[27]";
connectAttr "L_upperArm_JNT.msg" "tpose.m[28]";
connectAttr "L_lowerArm_JNT.msg" "tpose.m[29]";
connectAttr "L_hand_JNT.msg" "tpose.m[30]";
connectAttr "L_thumb01_JNT.msg" "tpose.m[31]";
connectAttr "L_thumb02_JNT.msg" "tpose.m[32]";
connectAttr "L_thumb03_JNT.msg" "tpose.m[33]";
connectAttr "L_pinky_meta_JNT.msg" "tpose.m[34]";
connectAttr "L_pinky01_JNT.msg" "tpose.m[35]";
connectAttr "L_pinky02_JNT.msg" "tpose.m[36]";
connectAttr "L_pinky03_JNT.msg" "tpose.m[37]";
connectAttr "L_ring_meta_JNT.msg" "tpose.m[38]";
connectAttr "L_ring01_JNT.msg" "tpose.m[39]";
connectAttr "L_ring02_JNT.msg" "tpose.m[40]";
connectAttr "L_ring03_JNT.msg" "tpose.m[41]";
connectAttr "L_middle_meta_JNT.msg" "tpose.m[42]";
connectAttr "L_middle01_JNT.msg" "tpose.m[43]";
connectAttr "L_middle02_JNT.msg" "tpose.m[44]";
connectAttr "L_middle03_JNT.msg" "tpose.m[45]";
connectAttr "L_index_meta_JNT.msg" "tpose.m[46]";
connectAttr "L_index01_JNT.msg" "tpose.m[47]";
connectAttr "L_index02_JNT.msg" "tpose.m[48]";
connectAttr "L_index03_JNT.msg" "tpose.m[49]";
connectAttr "L_weapon_parent_JNT.msg" "tpose.m[50]";
connectAttr "L_weapon_child_JNT.msg" "tpose.m[51]";
connectAttr "L_lowerArmTwist03_JNT.msg" "tpose.m[52]";
connectAttr "L_lowerArmTwist02_JNT.msg" "tpose.m[53]";
connectAttr "L_lowerArmTwist01_JNT.msg" "tpose.m[54]";
connectAttr "L_upperArmTwist01_JNT.msg" "tpose.m[55]";
connectAttr "L_upperArmTwist02_JNT.msg" "tpose.m[56]";
connectAttr "L_upperArmTwist03_JNT.msg" "tpose.m[57]";
connectAttr "R_clavicle_JNT.msg" "tpose.m[58]";
connectAttr "R_upperArm_JNT.msg" "tpose.m[59]";
connectAttr "R_lowerArm_JNT.msg" "tpose.m[60]";
connectAttr "R_hand_JNT.msg" "tpose.m[61]";
connectAttr "R_thumb01_JNT.msg" "tpose.m[62]";
connectAttr "R_thumb02_JNT.msg" "tpose.m[63]";
connectAttr "R_thumb03_JNT.msg" "tpose.m[64]";
connectAttr "R_pinky_meta_JNT.msg" "tpose.m[65]";
connectAttr "R_pinky01_JNT.msg" "tpose.m[66]";
connectAttr "R_pinky02_JNT.msg" "tpose.m[67]";
connectAttr "R_pinky03_JNT.msg" "tpose.m[68]";
connectAttr "R_ring_meta_JNT.msg" "tpose.m[69]";
connectAttr "R_ring01_JNT.msg" "tpose.m[70]";
connectAttr "R_ring02_JNT.msg" "tpose.m[71]";
connectAttr "R_ring03_JNT.msg" "tpose.m[72]";
connectAttr "R_middle_meta_JNT.msg" "tpose.m[73]";
connectAttr "R_middle01_JNT.msg" "tpose.m[74]";
connectAttr "R_middle02_JNT.msg" "tpose.m[75]";
connectAttr "R_middle03_JNT.msg" "tpose.m[76]";
connectAttr "R_index_meta_JNT.msg" "tpose.m[77]";
connectAttr "R_index01_JNT.msg" "tpose.m[78]";
connectAttr "R_index02_JNT.msg" "tpose.m[79]";
connectAttr "R_index03_JNT.msg" "tpose.m[80]";
connectAttr "R_weapon_parent_JNT.msg" "tpose.m[81]";
connectAttr "R_weapon_child_JNT.msg" "tpose.m[82]";
connectAttr "R_lowerArmTwist01_JNT.msg" "tpose.m[83]";
connectAttr "R_lowerArmTwist02_JNT.msg" "tpose.m[84]";
connectAttr "R_lowerArmTwist03_JNT.msg" "tpose.m[85]";
connectAttr "R_upperArmTwist01_JNT.msg" "tpose.m[86]";
connectAttr "R_upperArmTwist02_JNT.msg" "tpose.m[87]";
connectAttr "R_upperArmTwist03_JNT.msg" "tpose.m[88]";
connectAttr "C_neck01_JNT.msg" "tpose.m[89]";
connectAttr "C_neck02_JNT.msg" "tpose.m[90]";
connectAttr "C_head_JNT.msg" "tpose.m[91]";
connectAttr "L_eye_JNT.msg" "tpose.m[92]";
connectAttr "R_eye_JNT.msg" "tpose.m[93]";
connectAttr "C_jaw_JNT.msg" "tpose.m[94]";
connectAttr "C_placement_JNT.msg" "tpose.m[95]";
connectAttr "tpose.w" "tpose.p[0]";
connectAttr "tpose.m[0]" "tpose.p[1]";
connectAttr "tpose.m[1]" "tpose.p[2]";
connectAttr "tpose.m[2]" "tpose.p[3]";
connectAttr "tpose.m[3]" "tpose.p[4]";
connectAttr "tpose.m[4]" "tpose.p[5]";
connectAttr "tpose.m[5]" "tpose.p[6]";
connectAttr "tpose.m[3]" "tpose.p[7]";
connectAttr "tpose.m[3]" "tpose.p[8]";
connectAttr "tpose.m[3]" "tpose.p[9]";
connectAttr "tpose.m[2]" "tpose.p[10]";
connectAttr "tpose.m[2]" "tpose.p[11]";
connectAttr "tpose.m[2]" "tpose.p[12]";
connectAttr "tpose.m[1]" "tpose.p[13]";
connectAttr "tpose.m[13]" "tpose.p[14]";
connectAttr "tpose.m[14]" "tpose.p[15]";
connectAttr "tpose.m[15]" "tpose.p[16]";
connectAttr "tpose.m[16]" "tpose.p[17]";
connectAttr "tpose.m[14]" "tpose.p[18]";
connectAttr "tpose.m[14]" "tpose.p[19]";
connectAttr "tpose.m[14]" "tpose.p[20]";
connectAttr "tpose.m[13]" "tpose.p[21]";
connectAttr "tpose.m[13]" "tpose.p[22]";
connectAttr "tpose.m[13]" "tpose.p[23]";
connectAttr "tpose.m[1]" "tpose.p[24]";
connectAttr "tpose.m[24]" "tpose.p[25]";
connectAttr "tpose.m[25]" "tpose.p[26]";
connectAttr "tpose.m[26]" "tpose.p[27]";
connectAttr "tpose.m[27]" "tpose.p[28]";
connectAttr "tpose.m[28]" "tpose.p[29]";
connectAttr "tpose.m[29]" "tpose.p[30]";
connectAttr "tpose.m[30]" "tpose.p[31]";
connectAttr "tpose.m[31]" "tpose.p[32]";
connectAttr "tpose.m[32]" "tpose.p[33]";
connectAttr "tpose.m[30]" "tpose.p[34]";
connectAttr "tpose.m[34]" "tpose.p[35]";
connectAttr "tpose.m[35]" "tpose.p[36]";
connectAttr "tpose.m[36]" "tpose.p[37]";
connectAttr "tpose.m[30]" "tpose.p[38]";
connectAttr "tpose.m[38]" "tpose.p[39]";
connectAttr "tpose.m[39]" "tpose.p[40]";
connectAttr "tpose.m[40]" "tpose.p[41]";
connectAttr "tpose.m[30]" "tpose.p[42]";
connectAttr "tpose.m[42]" "tpose.p[43]";
connectAttr "tpose.m[43]" "tpose.p[44]";
connectAttr "tpose.m[44]" "tpose.p[45]";
connectAttr "tpose.m[30]" "tpose.p[46]";
connectAttr "tpose.m[46]" "tpose.p[47]";
connectAttr "tpose.m[47]" "tpose.p[48]";
connectAttr "tpose.m[48]" "tpose.p[49]";
connectAttr "tpose.m[30]" "tpose.p[50]";
connectAttr "tpose.m[50]" "tpose.p[51]";
connectAttr "tpose.m[29]" "tpose.p[52]";
connectAttr "tpose.m[29]" "tpose.p[53]";
connectAttr "tpose.m[29]" "tpose.p[54]";
connectAttr "tpose.m[28]" "tpose.p[55]";
connectAttr "tpose.m[28]" "tpose.p[56]";
connectAttr "tpose.m[28]" "tpose.p[57]";
connectAttr "tpose.m[26]" "tpose.p[58]";
connectAttr "tpose.m[58]" "tpose.p[59]";
connectAttr "tpose.m[59]" "tpose.p[60]";
connectAttr "tpose.m[60]" "tpose.p[61]";
connectAttr "tpose.m[61]" "tpose.p[62]";
connectAttr "tpose.m[62]" "tpose.p[63]";
connectAttr "tpose.m[63]" "tpose.p[64]";
connectAttr "tpose.m[61]" "tpose.p[65]";
connectAttr "tpose.m[65]" "tpose.p[66]";
connectAttr "tpose.m[66]" "tpose.p[67]";
connectAttr "tpose.m[67]" "tpose.p[68]";
connectAttr "tpose.m[61]" "tpose.p[69]";
connectAttr "tpose.m[69]" "tpose.p[70]";
connectAttr "tpose.m[70]" "tpose.p[71]";
connectAttr "tpose.m[71]" "tpose.p[72]";
connectAttr "tpose.m[61]" "tpose.p[73]";
connectAttr "tpose.m[73]" "tpose.p[74]";
connectAttr "tpose.m[74]" "tpose.p[75]";
connectAttr "tpose.m[75]" "tpose.p[76]";
connectAttr "tpose.m[61]" "tpose.p[77]";
connectAttr "tpose.m[77]" "tpose.p[78]";
connectAttr "tpose.m[78]" "tpose.p[79]";
connectAttr "tpose.m[79]" "tpose.p[80]";
connectAttr "tpose.m[61]" "tpose.p[81]";
connectAttr "tpose.m[81]" "tpose.p[82]";
connectAttr "tpose.m[60]" "tpose.p[83]";
connectAttr "tpose.m[60]" "tpose.p[84]";
connectAttr "tpose.m[60]" "tpose.p[85]";
connectAttr "tpose.m[59]" "tpose.p[86]";
connectAttr "tpose.m[59]" "tpose.p[87]";
connectAttr "tpose.m[59]" "tpose.p[88]";
connectAttr "tpose.m[26]" "tpose.p[89]";
connectAttr "tpose.m[89]" "tpose.p[90]";
connectAttr "tpose.m[90]" "tpose.p[91]";
connectAttr "tpose.m[91]" "tpose.p[92]";
connectAttr "tpose.m[91]" "tpose.p[93]";
connectAttr "tpose.m[91]" "tpose.p[94]";
connectAttr "tpose.m[0]" "tpose.p[95]";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of skel_biped_poses.ma
