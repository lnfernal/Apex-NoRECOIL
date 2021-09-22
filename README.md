# Apex-NoRECOIL
python 3.9 required

## USAGE
1. Disable real time protection in your Antivirus or it wont work
1. Install all packages in the requirements.txt file with this command "pip install -r requirements.txt"
2. Install the Tesseract program in the default directory
3. Execute "driver override.exe" to install the custom mouse drivers
3. You should now be able to run the program in your venv using command - "py main.py"

## PATTERN-TRACKER TOOL

1. In the Apex Firing Range, choose your weapon of choice and find a flat wall.
2. Stand as far away from the wall as possible while still being able to see the bullet impacts.
3. ADS and empty the clip into the wall.
4. Come out of ADS and screenshot the wall.
5. Open the screenshot in MS Paint.
6. Run the tool - `py pattern_tracker.py`
7. Enable the tool and click on the bullet impacts starting from the bottom working upwards.
8. Once completed, save your recoil-pattern and the `*.txt` file should be in the dir where the tool was run.
9. The pattern in the `*.txt` file can then be imported in the *recoil_patterns.py* file.

## CONFIG FILE

The following values are now more easily editable by the user from within the **config.yaml** file:

* Weapon slot scan position and dimensions
* Recoil-Pattern sensitivity modifier

The weapon slot scan position sets where the program scans for the names of the weapons you are using. The recoil-pattern sensitivity modifier adjusts the "strength" of the anti-recoil behavior, meaning a higher value applies less anti-recoil.

**IMPORTANT**
* When creating a recoil-pattern the fire-rate delay must be a float | Ex. - 0.0200 

## SUPPORTED WEAPONS

| Weapon | Status |
| ------------- | ------------- |
| Sentinel | ❌ |
| P2020 | ✅ |
| Charge Rifle | ❌ |
| Longbow | ❌ |
| G7 SCOUT | ❌ |
| RE-45 | ✅ |
| Flatline | ✅ |
| Hemlok | ✅ |
| Prowler | ✅ |
| Wingman | ❌ |
| 30-30 Repeater | ❌ |
| Rampage | ❌ |
| L-Star | ✅ |
| Havoc | ✅ |
| Devotion | ✅ |
| Volt | ✅ |
| Bocek | ❌ |
| Kraber | ❌ |
| Triple Take | ❌ |
| Alternator | ✅ |
| Spitfire | ✅ |
| Mastif | ❌ |
| EVA-8 Auto | ❌ |
| Peacekeeper | ❌ |
| Mozambique | ❌ |
