
# This script will initialize a new project with one initial design
    # 0 : output path of the script
    # 1 : file name
    # 2 : script_path
    # 3 : script_name
    # 4 : project_path
# New Project here
# User Name: qmle ,Script built on: 2018-06-14 14:30:10.372000
import sys
sys.path.append("C:/Program Files/AnsysEM/AnsysEM18.2/Win64")
sys.path.append("C:/Program Files/AnsysEM/AnsysEM18.2/Win64/PythonFiles/DesktopPlugin")
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.SaveAs("C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS/3.aedt", True)
oProject.Rename("C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS/3.aedt", True)
oProject = oDesktop.SetActiveProject("3")
oProject.InsertDesign("Q3D Extractor", "Q3DDesign1", "", "")
# Active design
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oDefinitionManager = oProject.GetDefinitionManager()

#0: x pos  #1: y pos  #2: z pos
#3: x size #4: y size #5: z size
#6: obj_name (ID of an object in q3d) #7: material
#8: color
# New Box 
oEditor.CreateBox(
    [
        "NAME:BoxParameters",
        "XPosition:="        , "0mm",
        "YPosition:="        , "0mm",
        "ZPosition:="        , "0mm",
        "XSize:="        , "60.0mm",
        "YSize:="        , "60.0mm",
        "ZSize:="        , "6.0mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="        , "Baseplate",
        "Flags:="        , "",
        "Color:="        , "(205 133 63)",
        "Transparency:="    , 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="        , "",
        "MaterialValue:="    , "\"copper\"",
        "SolveInside:="        , False
    ])       

#0: x pos  #1: y pos  #2: z pos
#3: x size #4: y size #5: z size
#6: obj_name (ID of an object in q3d) #7: material
#8: color
# New Box 
oEditor.CreateBox(
    [
        "NAME:BoxParameters",
        "XPosition:="        , "11.0mm",
        "YPosition:="        , "6.0mm",
        "ZPosition:="        , "6.0mm",
        "XSize:="        , "38.0mm",
        "YSize:="        , "48.0mm",
        "ZSize:="        , "0.2mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="        , "Metal1",
        "Flags:="        , "",
        "Color:="        , "(205 133 63)",
        "Transparency:="    , 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="        , "",
        "MaterialValue:="    , "\"copper\"",
        "SolveInside:="        , False
    ])       

#0: x pos  #1: y pos  #2: z pos
#3: x size #4: y size #5: z size
#6: obj_name (ID of an object in q3d) #7: material
#8: color
# New Box 
oEditor.CreateBox(
    [
        "NAME:BoxParameters",
        "XPosition:="        , "10.0mm",
        "YPosition:="        , "5.0mm",
        "ZPosition:="        , "6.2mm",
        "XSize:="        , "40.0mm",
        "YSize:="        , "50.0mm",
        "ZSize:="        , "0.64mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="        , "Substrate",
        "Flags:="        , "",
        "Color:="        , "(205 133 63)",
        "Transparency:="    , 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="        , "",
        "MaterialValue:="    , "\"Al_N\"",
        "SolveInside:="        , False
    ])       

#0: x pos  #1: y pos  #2: z pos
#3: x size #4: y size #5: z size
#6: obj_name (ID of an object in q3d) #7: material
#8: color
# New Box 
oEditor.CreateBox(
    [
        "NAME:BoxParameters",
        "XPosition:="        , "24.0mm",
        "YPosition:="        , "24.0mm",
        "ZPosition:="        , "6.84mm",
        "XSize:="        , "12.0mm",
        "YSize:="        , "12.0mm",
        "ZSize:="        , "0.2mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="        , "Metal2",
        "Flags:="        , "",
        "Color:="        , "(205 133 63)",
        "Transparency:="    , 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="        , "",
        "MaterialValue:="    , "\"copper\"",
        "SolveInside:="        , False
    ])       
        
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:Width",
                    "PropType:="        , "VariableProp",
                    "UserDef:="        , True,
                    "Value:="        , "9mm"
                ]
            ]
        ]
    ])

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "Metal2:CreateBox:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:XSize",
                    "Value:="        , "Width"
                ]
            ]
        ]
    ])
        
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:Length",
                    "PropType:="        , "VariableProp",
                    "UserDef:="        , True,
                    "Value:="        , "9mm"
                ]
            ]
        ]
    ])

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "Metal2:CreateBox:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:YSize",
                    "Value:="        , "Length"
                ]
            ]
        ]
    ])
        
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:XTrace",
                    "PropType:="        , "VariableProp",
                    "UserDef:="        , True,
                    "Value:="        , "9mm"
                ]
            ]
        ]
    ])
 
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "Metal2:CreateBox:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Position",
                    "X:="            , "XTrace",
                    "Y:="            , "0",
                    "Z:="            , "6.84"
                ]
            ]
        ]
    ])
        
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:YTrace",
                    "PropType:="        , "VariableProp",
                    "UserDef:="        , True,
                    "Value:="        , "9mm"
                ]
            ]
        ]
    ])
 
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "Metal2:CreateBox:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Position",
                    "X:="            , "XTrace",
                    "Y:="            , "YTrace",
                    "Z:="            , "6.84"
                ]
            ]
        ]
    ])
        
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:ZTrace",
                    "PropType:="        , "VariableProp",
                    "UserDef:="        , True,
                    "Value:="        , "6.84mm"
                ]
            ]
        ]
    ])
 
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "Metal2:CreateBox:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Position",
                    "X:="            , "XTrace",
                    "Y:="            , "YTrace",
                    "Z:="            , "ZTrace"
                ]
            ]
        ]
    ])

# Assign an object as signal net
    # 0: Net ID   # 1: Object ID
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignSignalNet(
    [
        "NAME:SignalNet1",     # Net ID
        "Objects:="        , ["Metal2"] # Object ID
    ])

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignSource(
    [
        "NAME:Source1",
        "Faces:="        , [93]
,
        "ParentBndID:="        , "SignalNet1",
        "Net:="            , "SignalNet1"

    ])
oModule.AssignSink(
    [
        "NAME:Sink1",
        "Faces:="        , [95]
,
        "ParentBndID:="        , "SignalNet1",
        "Net:="            , "SignalNet1"

    ])

# Set up an analysis in Q3d, where:
    # 0: frequency   -- String e.g: '100k'  # 1: save fields --True/False
    # 2: Maximum number of passes           # 3: Minimum number of passes required
    # 4: Least number of passes to converse # 5: Percentage error between 2 consecutive passes
    # 6: Mesh refine percentage for each pass
    # 7: Cap: true or false
    # 8: Add DC: True or False
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("Matrix", 
    [
        "NAME:Setup1",
        "AdaptiveFreq:="    , "100kHz",   # default 100 kHz
        "SaveFields:="        , False,      # default to be False 
        "Enabled:="        , True,
        
        [
            "NAME:AC",
            "MaxPass:="        , 10,
            "MinPass:="        , 10,
            "MinConvPass:="        , 1, # default 1
            "PerError:="        , 0.5,    # default 1
            "PerRefine:="        , 30    # default 30
        ]

    ])
    
 
# Linear sweep on frequency range
    # 0: Start Frequency     # 1: Stop Frequency # 2: Frequency Step Size
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSweep("Setup1", 
    [
        "NAME:Sweep1",
        "IsEnabled:="        , True,
        "RangeType:="        , "LinearStep",
        "RangeStart:="        , "10kHz",
        "RangeEnd:="        , "1000kHz",
        "RangeStep:="        , "10kHz",
        "Type:="        , "Discrete",
        "SaveFields:="        , False,
        "SaveRadFields:="    , False,
        "ExtrapToDC:="        , False
    ])

# Change value of existed parameters
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:XTrace",
                    "Value:="        , "(60.0mm -Width)/2 "
                ]
            ]
        ]
    ])


# Change value of existed parameters
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:YTrace",
                    "Value:="        , "(60.0mm -Length)/2 "
                ]
            ]
        ]
    ])


# Change value of existed parameters
oDesign = oProject.SetActiveDesign("Q3DDesign1")
oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:ZTrace",
                    "Value:="        , "6.84 mm"
                ]
            ]
        ]
    ])


oDesign = oProject.SetActiveDesign("Q3DDesign1")
oModule = oDesign.GetModule("Optimetrics")
oModule.InsertSetup("OptiParametric",
	[
		"NAME:ParametricSetup1", # parametric setup name -- default: ParametricSetup1
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupDataV2",
			"SaveFields:="		, False,
			"CopyMesh:="		, False,
			"SolveWithCopiedMeshOnly:=", True
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"], # Setup id, default: Setup1
		[
			"NAME:Sweeps",
			# Optimetric variable from add_optimetric_variable function
			

            [
				"NAME:SweepDefinition",
				"Variable:="		, "Width",
				"Data:="		, "LINC 1.2mm 10.0mm 5",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			] ,

            [
				"NAME:SweepDefinition",
				"Variable:="		, "Length",
				"Data:="		, "LINC 1.2mm 40.0mm 5",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			] 

		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oProject.Save()



oModule = oDesign.GetModule("Optimetrics")
oModule.SolveSetup("ParametricSetup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 1", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 1", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 1", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_1.2_L_1.2.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 2", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 2", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 2", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 2", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_1.2_L_10.9.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 3", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 3", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 3", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 3", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_1.2_L_20.6.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 4", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 4", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 4", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 4", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_1.2_L_30.3.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 5", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 5", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 5", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 5", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_1.2_L_40.0.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 6", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 6", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 6", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 6", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_3.4_L_1.2.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 7", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 7", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 7", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 7", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_3.4_L_10.9.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 8", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 8", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 8", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 8", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_3.4_L_20.6.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 9", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 9", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 9", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 9", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_3.4_L_30.3.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 10", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 10", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 10", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["3.4 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 10", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_3.4_L_40.0.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 11", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 11", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 11", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 11", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_5.6_L_1.2.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 12", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 12", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 12", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 12", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_5.6_L_10.9.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 13", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 13", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 13", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 13", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_5.6_L_20.6.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 14", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 14", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 14", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 14", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_5.6_L_30.3.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 15", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 15", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 15", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["5.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 15", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_5.6_L_40.0.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 16", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 16", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 16", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 16", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_7.8_L_1.2.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 17", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 17", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 17", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 17", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_7.8_L_10.9.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 18", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 18", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 18", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 18", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_7.8_L_20.6.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 19", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 19", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 19", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 19", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_7.8_L_30.3.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 20", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 20", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 20", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["7.8 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 20", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_7.8_L_40.0.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 21", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 21", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 21", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["1.2 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 21", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_10.0_L_1.2.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 22", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 22", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 22", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["10.9 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 22", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_10.0_L_10.9.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 23", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 23", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 23", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["20.6 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 23", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_10.0_L_20.6.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 24", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 24", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 24", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["30.3 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 24", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_10.0_L_30.3.csv")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 25", "Matrix", "Data Table", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACR(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 25", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
	], [])


oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Data Table 25", "Setup1 : Sweep1",
	[
		"Context:="		, "Original"
	],
	[
		"Freq:="		, ["All"],
        # Optimetric Family Values here
        
        "Width:="		, ["10.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
        "Length:="		, ["40.0 mm"], # 0: Name,  1: Value: 'All', 'Nominal' or 'Value+Unit' 
	],
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Sweep1(SignalNet1,SignalNet1)"]
	], [])

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 25", "C:\PowerSynth_git\Master_for_danfoss\PowerCAD-full\export_data\workspace\RS//3_W_10.0_L_40.0.csv")
