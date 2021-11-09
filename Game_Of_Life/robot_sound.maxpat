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
		"rect" : [ 51.0, 104.0, 1197.0, 685.0 ],
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
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 560.0, 1009.0, 35.0, 22.0 ],
					"text" : "dac~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 0,
					"patching_rect" : [ 999.0, 476.0, 49.0, 22.0 ],
					"text" : "noteout"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-111",
					"maxclass" : "number~",
					"mode" : 2,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "float" ],
					"patching_rect" : [ 21.0, 677.0, 56.0, 22.0 ],
					"sig" : 0.0
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-110",
					"maxclass" : "number~",
					"mode" : 2,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "float" ],
					"patching_rect" : [ 156.0, 687.0, 56.0, 22.0 ],
					"sig" : 0.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-106",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 756.0, 965.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-105",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 584.0, 965.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-104",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 399.600001513957977, 965.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-103",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 231.0, 970.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-102",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 85.0, 970.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-101",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 756.0, 669.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-100",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 584.0, 669.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-99",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 416.0, 673.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-98",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 246.0, 673.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-97",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 90.0, 673.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-96",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 832.0, 187.0, 50.0, 22.0 ],
					"text" : "0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-94",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 807.0, 187.0, 50.0, 22.0 ],
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-92",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 872.0, 217.0, 50.0, 22.0 ],
					"text" : "0.5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-90",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 845.0, 217.0, 50.0, 22.0 ],
					"text" : "2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-88",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 778.80000364780426, 217.0, 50.0, 22.0 ],
					"text" : "0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-86",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 756.0, 217.0, 50.0, 22.0 ],
					"text" : "3"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-84",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 911.0, 254.0, 50.0, 22.0 ],
					"text" : "0.5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-82",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 887.0, 254.0, 50.0, 22.0 ],
					"text" : "2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-80",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 816.0, 254.0, 50.0, 22.0 ],
					"text" : "0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-78",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 794.600001513957977, 254.0, 50.0, 22.0 ],
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-76",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 723.0, 254.0, 50.0, 22.0 ],
					"text" : "0.25"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-74",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 703.0, 254.0, 50.0, 22.0 ],
					"text" : "4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-72",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 947.0, 287.0, 50.0, 22.0 ],
					"text" : "0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-68",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 925.0, 287.0, 50.0, 22.0 ],
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-66",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 863.0, 287.0, 50.0, 22.0 ],
					"text" : "0.5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-64",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 841.0, 287.0, 50.0, 22.0 ],
					"text" : "2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-62",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 778.80000364780426, 287.0, 50.0, 22.0 ],
					"text" : "0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 756.0, 287.0, 50.0, 22.0 ],
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 692.0, 287.0, 50.0, 22.0 ],
					"text" : "0.25"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-56",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 673.80000364780426, 287.0, 50.0, 22.0 ],
					"text" : "4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-44",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 20,
					"outlettype" : [ "int", "float", "int", "float", "int", "float", "int", "float", "int", "float", "int", "float", "int", "float", "int", "float", "int", "float", "int", "float" ],
					"patching_rect" : [ 314.0, 155.0, 281.0, 22.0 ],
					"text" : "unpack 0 0. 0 0. 0 0. 0 0. 0 0. 0 0. 0 0. 0 0. 0 0. 0 0."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 309.80000364780426, 110.0, 332.0, 35.0 ],
					"text" : "arms 4. 0.25 1. 0.75 2. 0.5 1. 0.75 4. 0.25 1. 0.75 2. 0.5 3. 0.75 2. 0.5 1. 0.75"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 10,
					"outlettype" : [ "int", "int", "int", "int", "int", "int", "int", "int", "int", "int" ],
					"patching_rect" : [ 68.0, 155.0, 147.0, 22.0 ],
					"text" : "unpack 0 0 0 0 0 0 0 0 0 0"
				}

			}
, 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u548001118",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u121001427",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u811001125",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u948001440",
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
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u036001104",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u016001401",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u046001111",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u693001414",
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
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u087001090",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u883001375",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u245001097",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u102001388",
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
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u231001076",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u898001349",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u138001083",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u402001362",
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
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u833001060",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u329001323",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u861001068",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u497001336",
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
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u807001046",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u022001297",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u843001053",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u982001310",
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
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u737001032",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u880001271",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u599001039",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u320001284",
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
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u494001010",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u487001245",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u209001025",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u016001258",
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
								"absolutepath" : "Joy_2_short.mp3",
								"filename" : "Joy_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u078000970",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_2_short.mp3",
								"filename" : "Sadness_2_short.mp3",
								"filekind" : "audiofile",
								"id" : "u305001150",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u501000999",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u539001232",
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
								"absolutepath" : "Joy_short.mp3",
								"filename" : "Joy_short.mp3",
								"filekind" : "audiofile",
								"id" : "u121000956",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_short.mp3",
								"filename" : "Sadness_short.mp3",
								"filekind" : "audiofile",
								"id" : "u544001132",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Joy_1_short.mp3",
								"filename" : "Joy_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u826000989",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Sadness_1_short.mp3",
								"filename" : "Sadness_1_short.mp3",
								"filekind" : "audiofile",
								"id" : "u447001141",
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
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-100", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-101", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"source" : [ "obj-102", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"source" : [ "obj-103", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"source" : [ "obj-104", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"source" : [ "obj-105", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"source" : [ "obj-106", 0 ]
				}

			}
, 			{
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
					"destination" : [ "obj-44", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-111", 0 ],
					"order" : 2,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"order" : 1,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-97", 0 ],
					"order" : 0,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-98", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-99", 0 ],
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-100", 0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-101", 0 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 0 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-103", 0 ],
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-104", 0 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-105", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-106", 0 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-56", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-62", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-62", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-66", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-66", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-68", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-72", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-72", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-74", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-76", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-76", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-78", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-80", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-80", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-82", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-84", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-84", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-86", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-88", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-88", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-90", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-92", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-92", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-94", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-96", 1 ],
					"order" : 0,
					"source" : [ "obj-44", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-96", 0 ],
					"order" : 1,
					"source" : [ "obj-44", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-97", 1 ],
					"source" : [ "obj-58", 0 ]
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
, 			{
				"patchline" : 				{
					"destination" : [ "obj-98", 1 ],
					"source" : [ "obj-62", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-99", 1 ],
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-100", 1 ],
					"source" : [ "obj-72", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-101", 1 ],
					"source" : [ "obj-76", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 1 ],
					"source" : [ "obj-80", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-103", 1 ],
					"source" : [ "obj-84", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-104", 1 ],
					"source" : [ "obj-88", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-105", 1 ],
					"source" : [ "obj-92", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-106", 1 ],
					"source" : [ "obj-96", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"order" : 0,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-110", 0 ],
					"order" : 1,
					"source" : [ "obj-97", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-98", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-99", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "Joy_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
, 			{
				"name" : "Sadness_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
, 			{
				"name" : "Joy_1_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
, 			{
				"name" : "Sadness_1_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
, 			{
				"name" : "Joy_2_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
, 			{
				"name" : "Sadness_2_short.mp3",
				"bootpath" : "~/Documents/GitHub/Forest",
				"patcherrelativepath" : ".",
				"type" : "Mp3",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
