# Mycroft Skill: Command

A skill for [MycroftAI](https://mycroft.ai/) which allows running shell script files (.sh)

To install this skill on Mycroft, run:
```bash
mycroft-msm install https://github.com/WTRV-0/mycroft-skill-script
```

To uninstall, run:
```bash
mycroft-msm remove https://github.com/WTRV-0/mycroft-skill-script
```

## About
NOTE: This skill has only been tested on Linux Mint 20.3

To change the default script directory, change the "localpath" variable in __init__.py . Scripts are run from localpath = '/opt/mycroft/skills/mycroft-skill-script.wtrv-0/scripts' by default.

## Example Scripts
There are three included example script files in the /scripts subfolder. They will create a file on ~/Desktop success_testfile.txt and add a line "File run with success!". These scripts are designed to show the functionality of converting user input to filenames.

## Examples
* "Run script test" (runs /scripts/test.sh)
* "Run script test 2" (runs /scripts/test2.sh)
* "Run script test underscore 3" (runs /scripts/test_3.sh)

## Credits
WTRV-0

## Tags
#script
#sh
#mycroft
