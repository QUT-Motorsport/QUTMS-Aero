## File Path
File_Path = 



## Inflation Inputs
#
#
#
#
#

import ansys.fluent.core as pyfluent
print("Meow - Import Success")

try:
    flglobals = pyfluent.setup_for_fluent(product_version="24.1.0", mode="meshing", version="3d", precision="double", processor_count=3)
    globals().update(flglobals)
except Exception:
    pass
print("Meow - Open in Meshing Success")

## Start Watertight Workflow
workflow.InitializeWorkflow(WorkflowType=r'Watertight Geometry')
print("Meow - Workflow Selection Success")

## Import Geometry
workflow.TaskObject['Import Geometry'].Arguments.set_state({r'FileName': r'C:/pythonscripting/wingtest/wingtest.scdoc',r'ImportCadPreferences': {r'MaxFacetLength': 0,},r'LengthUnit': r'mm',})
workflow.TaskObject['Import Geometry'].Execute()
print("Meow Meow - Geometry input success")

## Adding Local Sizing

## Named Selections
Named_Selections = ['frontwing', 'rearwing', 'flap', 'sidewing', 'body', 'rearwheel', 'frontwheel', 'diffuser', 'frontsuspension', 'frontupright', 'rearsuspension', 'rearupright', 'tyresquash', 'rollhoop', 'inlet', 'outlet', 'walls', 'ground', 'symmetry', 'enclosure-enclosure', 'boi-rw', 'boi-fw', 'boi-far']

## Curvature Sizings
Norm_Angle = 9

Front_Wing_Max = 
Front_Wing_Min = 

Rear_Wing_Max = 
Rear_Wing_Min = 

Flap_Max = 
Flap_Min = 

Sidewing_Max =
Sidewing_Min = 

Body_Max = 
Body_Min = 

Wheel_Max = 
Wheel_Min = 

Diffuser_Max = 
Diffuser_Min = 

Suspension_Max = 
Suspension_Min = 

Rear_Upright_Max = 
Rear_Upright_Min = 

Tyre_Squash_Max = 
Tyre_Squash_Min = 

Rollhoop_Max = 
Rollhoop_Min = 

## Proximity Sizing
Proximity_Max = 
Proximity_Min =

Global_Max = 
Global_Min = 

## Body of Influence 
Boi_Front_Wing = 
Boi_Rear_Wing =
Boi_Wheel = 
Boi_Far = 

# Front Wing
if 'frontwing' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-frontwing',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'frontwing'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Front_Wing_Max,r'BOIMinSize': Front_Wing_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Front Wing Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Rear Wing
if 'rearwing' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-rearwing',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'rearwing'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Rear_Wing_Max,r'BOIMinSize': Rear_Wing_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Rear Wing Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Flap
if 'flap' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-flap',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'flap'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Flap_Max,r'BOIMinSize': Flap_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Flap Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Sidewing
if 'sidewing' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-sidewing',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'sidewing'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Sidewing_Max,r'BOIMinSize': Sidewing_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Sidewing Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Body
if 'body' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-body',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'body'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Body_Max,r'BOIMinSize': Body_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Body Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Wheel 
if 'frontwheel' and 'rearwheel' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-wheel',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'rearwheel', r'frontwheel'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Wheel_Max,r'BOIMinSize': Wheel_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Wheel Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Diffuser 
if 'diffuser' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-diffuser',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'diffuser'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Diffuser_Max,r'BOIMinSize': Diffuser_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Diffuser Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Suspension
if 'frontsuspension' and 'rearsuspension' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-suspension',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'frontsuspension', r'rearsuspension'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Suspension_Max,r'BOIMinSize': Suspension_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Suspension Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Upright
if 'rearupright' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-upright',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'rearupright'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Rear_Upright_Max,r'BOIMinSize': Rear_Upright_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Upright Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Tyresquash 
if 'tyresquash' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-tyresquash',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'tyresquash'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Tyre_Squash_Max,r'BOIMinSize': Tyre_Squash_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Tyresquash Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

# Rollhoop 
if 'rollhoop' in Named_Selections:
    workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'curvature-rollhoop',r'BOICurvatureNormalAngle': Norm_Angle,r'BOIExecution': r'Curvature',r'BOIFaceLabelList': [r'rollhoop'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Rollhoop_Max,r'BOIMinSize': Rollhoop_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
    workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
    print("Meow - Diffuser Name Selection Success")
else:
    print("Part Not Found, Please Check Named Selections or Ignore If Desired, I mean Meow Meow")

## Body of Influences

# Front Wing
workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'boi-front-wing',r'BOICurvatureNormalAngle': 18,r'BOIExecution': r'Body Of Influence',r'BOIFaceLabelList': [r'boi-fw'],r'BOIGrowthRate': 1.2,r'BOISize': Boi_Front_Wing,r'BOIZoneorLabel': r'label',})
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
print("Meow - Front Wing Body of Influence Success")

# Rear Wing
workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'boi-rear-wing',r'BOICurvatureNormalAngle': 18,r'BOIExecution': r'Body Of Influence',r'BOIFaceLabelList': [r'boi-rw'],r'BOIGrowthRate': 1.2,r'BOISize': Boi_Rear_Wing,r'BOIZoneorLabel': r'label',})
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
print("Meow - Rear Wing Body of Influence Success")

# Wheel
workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'boi-wheel',r'BOICurvatureNormalAngle': 18,r'BOIExecution': r'Body Of Influence',r'BOIFaceLabelList': [r'boi-wheel-f', r'boi-wheel-r'],r'BOIGrowthRate': 1.2,r'BOISize': Boi_Wheel,r'BOIZoneorLabel': r'label',})
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
print("Meow - Wheel Body of Influence Success")

# Far
# Rear Wing
workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 1,r'BOIControlName': r'boi-far',r'BOICurvatureNormalAngle': 18,r'BOIExecution': r'Body Of Influence',r'BOIFaceLabelList': [r'boi-far'],r'BOIGrowthRate': 1.2,r'BOISize': Boi_Far,r'BOIZoneorLabel': r'label',})
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
print("Meow - Far Body of Influence Success")

# Proximity
workflow.TaskObject['Add Local Sizing'].Arguments.set_state({r'AddChild': r'yes',r'BOICellsPerGap': 2,r'BOIControlName': r'proximity',r'BOICurvatureNormalAngle': 18,r'BOIExecution': r'Proximity',r'BOIFaceLabelList': [r'frontwing', r'rearwing', r'flap', r'sidewing', r'body', r'rearwheel', r'frontwheel', r'diffuser', r'frontsuspension', r'frontupright', r'rearsuspension', r'rearupright', r'tyresquash', r'rollhoop'],r'BOIGrowthRate': 1.2,r'BOIMaxSize': Proximity_Max,r'BOIMinSize': Proximity_Min,r'BOIScopeTo': r'faces and edges',r'BOIZoneorLabel': r'label',})
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate(DeferUpdate=False)
print("Meow - Proximity  of Influence Success")


## Generate Surface Mesh
workflow.TaskObject['Generate the Surface Mesh'].Arguments.set_state({r'CFDSurfaceMeshControls': {r'MaxSize': Global_Max,r'MinSize': Global_Min,r'ScopeProximityTo': r'faces-and-edges',},})
workflow.TaskObject['Generate the Surface Mesh'].Execute()
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=False)
print("Meow Meow, Meow Meow - Generated Surface Mesh Successfully")

## Improve Surface Mesh
workflow.TaskObject['Generate the Surface Mesh'].InsertNextTask(CommandName=r'ImproveSurfaceMesh')
workflow.TaskObject['Improve Surface Mesh'].Arguments.set_state({r'FaceQualityLimit': 0.1,r'MeshObject': r'',r'SMImprovePreferences': {r'AdvancedImprove': r'no',r'AllowDefeaturing': r'no',r'SIQualityCollapseLimit': 0.85,r'SIQualityIterations': 20,r'SIQualityMaxAngle': 80,r'SIRemoveStep': r'no',r'SIStepQualityLimit': 0,r'SIStepWidth': 0,r'ShowSMImprovePreferences': True,},r'SQMinSize': 0.2,})
workflow.TaskObject['Improve Surface Mesh'].Execute()
print("Meow Meow - Improve Surface Mesh Complete")

## Describe Geometry
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=False)
workflow.TaskObject['Describe Geometry'].Arguments.set_state({r'NonConformal': r'No',r'SetupType': r'The geometry consists of only fluid regions with no voids',})
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=True)
workflow.TaskObject['Describe Geometry'].Execute()
print("Meow - Describe Geometry Success")

## Update Boundaries (please note, if named properly these shouldn't have to change, hence why no change)
workflow.TaskObject['Update Boundaries'].Execute()
print("Meow Meow - Update Boundaries Complete")

## Update Regions (please note, if named properly these shouldn't have to change, hence why no change)
workflow.TaskObject['Update Regions'].Execute()
print("Meow Meow - Update Regions Complete")

## Boundary Layer Creation
workflow.TaskObject['Add Boundary Layers'].Arguments.set_state({r'FaceScope': {r'GrowOn': r'selected-zones',},r'LocalPrismPreferences': {r'Continuous': r'Continuous',},r'NumberOfLayers': 8,r'ZoneSelectionList': [r'frontwing', r'rearwing', r'flap', r'sidewing', r'body', r'rearwheel', r'frontwheel', r'diffuser', r'frontsuspension', r'frontupright', r'rearsuspension', r'rearupright', r'tyresquash', r'rollhoop', r'ground'],})
workflow.TaskObject['Add Boundary Layers'].AddChildAndUpdate(DeferUpdate=False)
workflow.TaskObject['Add Boundary Layers'].Execute()
print("Meow Meow, Meow, Meow! - Boundary Layer Creation Complete")

## Generate Volume Mesh

Hex_Max = 
Hex_Min = 

workflow.TaskObject['Generate the Volume Mesh'].Arguments.set_state({r'VolumeFill': r'poly-hexcore',r'VolumeFillControls': {r'HexMaxCellLength': Hex_Max,r'HexMinCellLength': Hex_Min,},r'VolumeMeshPreferences': {r'ShowVolumeMeshPreferences': True,},})
workflow.TaskObject['Generate the Volume Mesh'].Execute()
print("Meow - Volume Mesh Created")

## Improve Volume Mesh
meshing.tui.mesh.modify.auto_node_move('enclosure-enclosure', '()', 'enclosure-enclosure', '()', '0.2', '50', '120', 'yes', '10')
meshing.tui.mesh.modify.auto_improve_warp('enclosure-enclosure', 'enclosure-enclosure', '0.48', '50', '10')

## Write and Save Mesh as Case File
...

## Change to Solver
meshing.switch_to_solver()

## Setup Model
solver.setup.models.viscous.model = "k-omega"
solver.setup.models.viscous.k_omega_model = "sst"
solver.setup.models.viscous.options.curvature_correction = True











