import unreal

print("=== STARTING H05 ASSET GENERATION ===")

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# ----------------------------------------------------
# 1. CREATE MATERIAL INSTANCES
# ----------------------------------------------------
base_mat_path = "/Engine/BasicShapes/BasicShapeMaterial"
base_mat = unreal.EditorAssetLibrary.load_asset(base_mat_path)
if not base_mat:
    base_mat = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/BasicShapeMaterial.BasicShapeMaterial")

print(f"Base Material: {base_mat}")

materials_data = [
    ("MI_Gold", (0.85, 0.55, 0.02, 1.0)),
    ("MI_Copper", (0.70, 0.22, 0.06, 1.0)),
    ("MI_Nickel", (0.35, 0.37, 0.42, 1.0)),
    ("MI_Highlight", (0.00, 0.55, 0.95, 1.0))
]

mat_factory = unreal.MaterialInstanceConstantFactoryNew()

for name, color in materials_data:
    package_path = "/Game/H05/Materials"
    asset_path = f"{package_path}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        instance = unreal.EditorAssetLibrary.load_asset(asset_path)
        print(f"Asset already exists, loading {name}")
    else:
        instance = asset_tools.create_asset(name, package_path, None, mat_factory)
        print(f"Created new asset {name}")

    if instance:
        if base_mat:
            unreal.MaterialEditingLibrary.set_material_instance_parent(instance, base_mat)
        linear_color = unreal.LinearColor(color[0], color[1], color[2], color[3])
        unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(instance, "Color", linear_color)
        unreal.EditorAssetLibrary.save_loaded_asset(instance)
        print(f"Saved Material Instance: {name}")

# ----------------------------------------------------
# 2. CREATE BLUEPRINTS
# ----------------------------------------------------
bp_configs = [
    ("BP_PuzzleGameMode", unreal.GameModeBase),
    ("BP_PuzzlePlayerController", unreal.PlayerController),
    ("BP_PuzzleBlock", unreal.Actor),
    ("BP_PuzzleGrid", unreal.Actor),
]

bp_factory = unreal.BlueprintFactory()

for bp_name, parent_cls in bp_configs:
    package_path = "/Game/H05/Blueprints"
    asset_path = f"{package_path}/{bp_name}"
    
    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        bp_factory.set_editor_property("parent_class", parent_cls)
        bp_asset = asset_tools.create_asset(bp_name, package_path, None, bp_factory)
        if bp_asset:
            unreal.EditorAssetLibrary.save_loaded_asset(bp_asset)
            print(f"Created Blueprint: {bp_name}")
    else:
        print(f"Blueprint already exists: {bp_name}")

# ----------------------------------------------------
# 3. CREATE WIDGET BLUEPRINT
# ----------------------------------------------------
widget_name = "W_PuzzleHUD"
widget_pkg = "/Game/H05/UI"
widget_path = f"{widget_pkg}/{widget_name}"

if not unreal.EditorAssetLibrary.does_asset_exist(widget_path):
    try:
        wbp_factory = unreal.WidgetBlueprintFactory()
        wbp_asset = asset_tools.create_asset(widget_name, widget_pkg, None, wbp_factory)
        if wbp_asset:
            unreal.EditorAssetLibrary.save_loaded_asset(wbp_asset)
            print(f"Created Widget Blueprint: {widget_name}")
    except Exception as e:
        print(f"Widget Blueprint creation notice: {e}")
else:
    print(f"Widget already exists: {widget_name}")

print("=== H05 ASSET GENERATION FINISHED SUCCESSFULLY ===")
