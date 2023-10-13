https://github.com/Project-MONAI/tutorials/tree/main/bundle

# 01 - Instantiating a new bundle
python -m monai.bundle init_bundle TestBundle

# Make TestBundle...

# Test Run

## convenient to define the bundle's root in a variable
BUNDLE="./TestBundle"

## loads the test_config.yaml file and runs the test_config program it defines
python -m monai.bundle run test_config \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/test_config.yaml"

# Object Instantiation
BUNDLE="./TestBundle"

## prints normal values
python -W ignore -m monai.bundle run test \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/test_object.yaml"

# Command Line Definitions

## prints normal values
python -W ignore -m monai.bundle run test \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/test_cmdline.yaml"

## half the height
python -W ignore -m monai.bundle run test \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/test_cmdline.yaml" \
    '--shape#0' 4

## area definition replaces existing expression with a lie
python -W ignore -m monai.bundle run test \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/test_cmdline.yaml" \
    --area 32

# Multiple Files

BUNDLE="./TestBundle"

## area definition replaces existing expression with a lie
python -W ignore -m monai.bundle run test \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "['$BUNDLE/configs/multifile1.yaml','$BUNDLE/configs/multifile2.yaml']"

# 02 - Mednist Classification
