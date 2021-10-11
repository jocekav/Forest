{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 1,
			"revision" : 11,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 0.0, 0.0, 640.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 309.80000364780426, 110.0, 332.0, 22.0 ],
					"text" : "arms 1. 3. 1. 0. 3. 1. 0. 1. 0. 0."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 10,
					"outlettype" : [ "int", "int", "int", "int", "int", "int", "int", "int", "int", "int" ],
					"patching_rect" : [ 330.0, 145.0, 147.0, 22.0 ],
					"text" : "unpack 0 0 0 0 0 0 0 0 0 0"
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u065004982",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u263005242",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u320005472",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u285005624",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_4.wav",
								"filename" : "Joy_4.wav",
								"filekind" : "audiofile",
								"id" : "u761001664",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-39",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 741.600001513957977, 720.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u827004969",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u912005235",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u460005465",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u465005611",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-38",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 568.600001513957977, 720.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u104004955",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u963005228",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u131005458",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u826005598",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-36",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 392.600001513957977, 720.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u443004941",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u862005221",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u300005451",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u144005585",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-35",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 216.600001513957977, 720.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u252004927",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u208005214",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u329005444",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u074005572",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-34",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 36.600001513957977, 720.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u134004913",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u658005207",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u560005437",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u775005559",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-33",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 738.600001513957977, 407.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u997004900",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u112005200",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u271005430",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u936005546",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-32",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 565.600001513957977, 407.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u582004887",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u619005193",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u334005423",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u088005486",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-31",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 389.600001513957977, 407.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u212004838",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u242005186",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u508005416",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u985005533",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_4.wav",
								"filename" : "Joy_4.wav",
								"filekind" : "audiofile",
								"id" : "u761001664",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-30",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 213.600001513957977, 407.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy.wav",
								"filename" : "Joy.wav",
								"filekind" : "audiofile",
								"id" : "u017004825",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness.wav",
								"filename" : "Sadness.wav",
								"filekind" : "audiofile",
								"id" : "u580005179",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Joy_1.wav",
								"filename" : "Joy_1.wav",
								"filekind" : "audiofile",
								"id" : "u608005409",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/jocekav/Documents/GitHub/Forest/Sadness_2.wav",
								"filename" : "Sadness_2.wav",
								"filekind" : "audiofile",
								"id" : "u282005479",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_4.wav",
								"filename" : "Joy_4.wav",
								"filekind" : "audiofile",
								"id" : "u761001664",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Joy_5.wav",
								"filename" : "Joy_5.wav",
								"filekind" : "audiofile",
								"id" : "u237001679",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Guilt_2.wav",
								"filename" : "Guilt_2.wav",
								"filekind" : "audiofile",
								"id" : "u637001655",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_3.wav",
								"filename" : "Sadness_3.wav",
								"filekind" : "audiofile",
								"id" : "u131000930",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_4.wav",
								"filename" : "Sadness_4.wav",
								"filekind" : "audiofile",
								"id" : "u296000912",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Sadness_5.wav",
								"filename" : "Sadness_5.wav",
								"filekind" : "audiofile",
								"id" : "u197000862",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Disgust_4.wav",
								"filename" : "Disgust_4.wav",
								"filekind" : "audiofile",
								"id" : "u267001697",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "/Users/gil/Downloads/Robot Timbre/Relief_2.wav",
								"filename" : "Relief_2.wav",
								"filekind" : "audiofile",
								"id" : "u858001708",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-29",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 36.600001513957977, 407.300002813339233, 162.0, 231.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 657.600000572204635, 132.599995136260986, 66.0, 22.0 ],
					"text" : "route arms"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-17",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 546.80000364780426, 28.39999532699585, 63.0, 23.0 ],
					"text" : "port 7980"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 678.80000364780426, 74.000000178813934, 150.0, 47.0 ],
					"text" : "udp message:\narm number to route\nand audio file number"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 11,
					"numoutlets" : 11,
					"outlettype" : [ "", "", "", "", "", "", "", "", "", "", "" ],
					"patching_rect" : [ 399.600001513957977, 343.600001394748688, 143.0, 22.0 ],
					"text" : "route 1 2 3 4 5 6 7 8 9 10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 554.200003683567047, 58.800000131130219, 97.0, 22.0 ],
					"text" : "udpreceive 7980"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 10,
					"numoutlets" : 0,
					"patching_rect" : [ 358.600001513957977, 1008.000002980232239, 142.0, 22.0 ],
					"text" : "dac~ 1 2 3 4 5 9 7 8 6 10"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"order" : 0,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 1 ],
					"order" : 1,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 81.850001513957977, 822.650002896785736, 368.100001513957977, 822.650002896785736 ],
					"source" : [ "obj-29", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 46.100001513957977, 822.650002896785736, 368.100001513957977, 822.650002896785736 ],
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 1 ],
					"midpoints" : [ 258.850001513957977, 822.650002896785736, 381.766668180624663, 822.650002896785736 ],
					"source" : [ "obj-30", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 1 ],
					"midpoints" : [ 223.100001513957977, 822.650002896785736, 381.766668180624663, 822.650002896785736 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 2 ],
					"midpoints" : [ 434.850001513957977, 822.650002896785736, 395.433334847291292, 822.650002896785736 ],
					"source" : [ "obj-31", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 2 ],
					"midpoints" : [ 399.100001513957977, 822.650002896785736, 395.433334847291292, 822.650002896785736 ],
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 3 ],
					"midpoints" : [ 610.850001513957977, 822.650002896785736, 409.100001513957977, 822.650002896785736 ],
					"source" : [ "obj-32", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 3 ],
					"midpoints" : [ 575.100001513957977, 822.650002896785736, 409.100001513957977, 822.650002896785736 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 4 ],
					"midpoints" : [ 783.850001513957977, 822.650002896785736, 422.766668180624606, 822.650002896785736 ],
					"source" : [ "obj-33", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 4 ],
					"midpoints" : [ 748.100001513957977, 822.650002896785736, 422.766668180624606, 822.650002896785736 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 5 ],
					"midpoints" : [ 81.850001513957977, 979.150002896785736, 436.433334847291292, 979.150002896785736 ],
					"source" : [ "obj-34", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 5 ],
					"midpoints" : [ 46.100001513957977, 979.150002896785736, 436.433334847291292, 979.150002896785736 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 6 ],
					"midpoints" : [ 261.850001513957977, 979.150002896785736, 450.100001513957977, 979.150002896785736 ],
					"source" : [ "obj-35", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 6 ],
					"midpoints" : [ 226.100001513957977, 979.150002896785736, 450.100001513957977, 979.150002896785736 ],
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 7 ],
					"midpoints" : [ 437.850001513957977, 979.150002896785736, 463.766668180624663, 979.150002896785736 ],
					"source" : [ "obj-36", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 7 ],
					"midpoints" : [ 402.100001513957977, 979.150002896785736, 463.766668180624663, 979.150002896785736 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 8 ],
					"midpoints" : [ 613.850001513957977, 979.150002896785736, 477.433334847291292, 979.150002896785736 ],
					"source" : [ "obj-38", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 8 ],
					"midpoints" : [ 578.100001513957977, 979.150002896785736, 477.433334847291292, 979.150002896785736 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 9 ],
					"midpoints" : [ 786.850001513957977, 979.150002896785736, 491.100001513957977, 979.150002896785736 ],
					"source" : [ "obj-39", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 9 ],
					"midpoints" : [ 751.100001513957977, 979.150002896785736, 491.100001513957977, 979.150002896785736 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-5", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"source" : [ "obj-5", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"source" : [ "obj-5", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-5", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-5", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-5", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"source" : [ "obj-5", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-5", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-5", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-6", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"source" : [ "obj-6", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"source" : [ "obj-6", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-6", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-6", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-6", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"source" : [ "obj-6", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-6", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-6", 9 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "Joy.wav",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Sadness.wav",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Joy_1.wav",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Sadness_2.wav",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "WAVE",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
