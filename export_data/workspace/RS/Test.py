
# This script will initialize a new project with one initial design
    # 0 : output path of the script
    # 1 : file name
    # 2 : script_path
    # 3 : script_name
    # 4 : project_path
# New Project here
# User Name: qmle ,Script built on: 2017-05-26 09:47:45.993000
import sys
sys.path.append("C:/Program Files/AnsysEM/AnsysEM16.2/Win64")
sys.path.append("C:/Program Files/AnsysEM/AnsysEM16.2/Win64/PythonFiles/DesktopPlugin")
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.SaveAs("C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS/Test.aedt", True)
oProject.Rename("C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS/Test.aedt", True)
oProject = oDesktop.SetActiveProject("Test")
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
        "XSize:="        , "80.0mm",
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
        "XPosition:="        , "6.0mm",
        "YPosition:="        , "6.0mm",
        "ZPosition:="        , "6.0mm",
        "XSize:="        , "68.0mm",
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
        "XPosition:="        , "5.0mm",
        "YPosition:="        , "5.0mm",
        "ZPosition:="        , "6.2mm",
        "XSize:="        , "70.0mm",
        "YSize:="        , "50.0mm",
        "ZSize:="        , "0.32mm"
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
        "XPosition:="        , "32.0mm",
        "YPosition:="        , "24.0mm",
        "ZPosition:="        , "6.52mm",
        "XSize:="        , "16.0mm",
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
                    "Z:="            , "6.52"
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
                    "Z:="            , "6.52"
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
                    "Value:="        , "6.52mm"
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
        "RangeStart:="        , "10.0kHz",
        "RangeEnd:="        , "300.0kHz",
        "RangeStep:="        , "10.0kHz",
        "Type:="        , "Discrete",
        "SaveFields:="        , False,
        "SaveRadFields:="    , False,
        "ExtrapToDC:="        , False
    ])

# Set up a report from analysis
    # 0: X_Params Default to 'Freq'   # 1: Type of data: ACR,ACL,C...
    # 2:Signal Net ID 3: Signal Net's Source ID 
    # 4 is for "LastAdaptive" or "Sweep1"
    # 5 Data Table id: e.g 1 2 3 4 5...
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Data Table 1", "Matrix", "Data Table", "Setup1 : Sweep1",   
    [
        "Context:="        , "Original"
    ], 
    [
        "Freq:="        , ["All"]
    ], 
    [
        "X Component:="        , "Freq", 
        "Y Component:="        , ["ACR(SignalNet1:Source1,SignalNet1:Source1)"] 
    ], [])

    # 0: X_Params Default to 'Freq'   # 1: Type of data: ACR,ACL,C...
    # 2:Signal Net ID 
    # 3: Signal Net's Source ID
    # 4 is for "LastAdaptive" or "Sweep1"
    # 5 Data Table id: e.g 1 2 3 4 5... 
oModule.AddTraces("Data Table 1", "Setup1 : Sweep1", 
    [
        "Context:="        , "Original"
    ], 
    [
        "Freq:="        , ["All"]
    ], 
    [
        "X Component:="        , "Freq",
        "Y Component:="        , ["ACL(SignalNet1:Source1,SignalNet1:Source1)"]
    ], [])    

    # 0: X_Params Default to 'Freq'   # 1: Type of data: ACR,ACL,C...
    # 2: Signal Net ID 
    # 3: is for "LastAdaptive" or "Sweep1"
    # 4: Data Table id: e.g 1 2 3 4 5...  
oModule.AddTraces("Data Table 1", "Setup1 : Sweep1", 
    [
        "Context:="        , "Original"
    ], 
    [
        "Freq:="        , ["All"]
    ], 
    [
        "X Component:="        , "Freq",
        "Y Component:="        , ["C(SignalNet1,SignalNet1)"]
    ], [])    

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
                    "NAME:Width",
                    "Value:="        , "1.2 mm"
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
                    "NAME:Length",
                    "Value:="        , "10.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "39.4 mm"
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
                    "Value:="        , "25.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_1.2_L_10.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "1.2 mm"
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
                    "NAME:Length",
                    "Value:="        , "17.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "39.4 mm"
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
                    "Value:="        , "21.25 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_1.2_L_17.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "1.2 mm"
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
                    "NAME:Length",
                    "Value:="        , "25.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "39.4 mm"
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
                    "Value:="        , "17.5 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_1.2_L_25.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "1.2 mm"
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
                    "NAME:Length",
                    "Value:="        , "32.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "39.4 mm"
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
                    "Value:="        , "13.75 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_1.2_L_32.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "1.2 mm"
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
                    "NAME:Length",
                    "Value:="        , "40.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "39.4 mm"
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
                    "Value:="        , "10.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_1.2_L_40.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "3.4 mm"
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
                    "NAME:Length",
                    "Value:="        , "10.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "38.3 mm"
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
                    "Value:="        , "25.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_3.4_L_10.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "3.4 mm"
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
                    "NAME:Length",
                    "Value:="        , "17.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "38.3 mm"
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
                    "Value:="        , "21.25 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_3.4_L_17.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "3.4 mm"
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
                    "NAME:Length",
                    "Value:="        , "25.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "38.3 mm"
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
                    "Value:="        , "17.5 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_3.4_L_25.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "3.4 mm"
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
                    "NAME:Length",
                    "Value:="        , "32.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "38.3 mm"
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
                    "Value:="        , "13.75 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_3.4_L_32.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "3.4 mm"
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
                    "NAME:Length",
                    "Value:="        , "40.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "38.3 mm"
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
                    "Value:="        , "10.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_3.4_L_40.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "5.6 mm"
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
                    "NAME:Length",
                    "Value:="        , "10.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "37.2 mm"
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
                    "Value:="        , "25.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_5.6_L_10.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "5.6 mm"
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
                    "NAME:Length",
                    "Value:="        , "17.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "37.2 mm"
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
                    "Value:="        , "21.25 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_5.6_L_17.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "5.6 mm"
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
                    "NAME:Length",
                    "Value:="        , "25.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "37.2 mm"
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
                    "Value:="        , "17.5 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_5.6_L_25.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "5.6 mm"
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
                    "NAME:Length",
                    "Value:="        , "32.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "37.2 mm"
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
                    "Value:="        , "13.75 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_5.6_L_32.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "5.6 mm"
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
                    "NAME:Length",
                    "Value:="        , "40.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "37.2 mm"
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
                    "Value:="        , "10.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_5.6_L_40.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "7.8 mm"
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
                    "NAME:Length",
                    "Value:="        , "10.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "36.1 mm"
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
                    "Value:="        , "25.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_7.8_L_10.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "7.8 mm"
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
                    "NAME:Length",
                    "Value:="        , "17.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "36.1 mm"
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
                    "Value:="        , "21.25 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_7.8_L_17.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "7.8 mm"
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
                    "NAME:Length",
                    "Value:="        , "25.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "36.1 mm"
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
                    "Value:="        , "17.5 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_7.8_L_25.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "7.8 mm"
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
                    "NAME:Length",
                    "Value:="        , "32.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "36.1 mm"
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
                    "Value:="        , "13.75 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_7.8_L_32.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "7.8 mm"
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
                    "NAME:Length",
                    "Value:="        , "40.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "36.1 mm"
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
                    "Value:="        , "10.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_7.8_L_40.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "10.0 mm"
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
                    "NAME:Length",
                    "Value:="        , "10.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "35.0 mm"
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
                    "Value:="        , "25.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_10.0_L_10.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "10.0 mm"
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
                    "NAME:Length",
                    "Value:="        , "17.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "35.0 mm"
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
                    "Value:="        , "21.25 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_10.0_L_17.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "10.0 mm"
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
                    "NAME:Length",
                    "Value:="        , "25.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "35.0 mm"
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
                    "Value:="        , "17.5 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_10.0_L_25.0.csv")

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
                    "NAME:Width",
                    "Value:="        , "10.0 mm"
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
                    "NAME:Length",
                    "Value:="        , "32.5 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "35.0 mm"
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
                    "Value:="        , "13.75 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_10.0_L_32.5.csv")

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
                    "NAME:Width",
                    "Value:="        , "10.0 mm"
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
                    "NAME:Length",
                    "Value:="        , "40.0 mm"
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
                    "NAME:XTrace",
                    "Value:="        , "35.0 mm"
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
                    "Value:="        , "10.0 mm"
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
                    "Value:="        , "6.52 mm"
                ]
            ]
        ]
    ])


# Run Analysis
oDesign.AnalyzeAll()

# 0: data_name in Q3d, 1: data output path
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Data Table 1", "C:\PowerSynth_git\Response_Surface\PowerCAD-full\export_data\workspace\RS//Test_W_10.0_L_40.0.csv")
