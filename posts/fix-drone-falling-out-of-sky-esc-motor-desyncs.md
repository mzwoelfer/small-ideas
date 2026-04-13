---
📅 created: 11.04.2026 15:39
aliases:
tags:
  - April 2026
  - fpv
  - drone
  - esc
author: Martin
---


# [[Fix Drone falling out of sky - ESC Motor Desyncs]]

Motor desyncs cause the "death roll" where a motor stalls under high load or rapid throttle changes. These adjustments help the ESC maintain sync with the motor's position.

### 1. Fast Fix: Startup Power

Lowering startup power to `0.125`. [1] 
Prevents the ESC from "over-pushing" the motor during rapid transitions.


1. Visit the ESC Configuratior [2] 
2. Connect to ESC Configurator (for BLHeli_S/Bluejay) or BLHeliSuite32.
3. Locate the `Startup Power` setting.
4. Change the value to `0.125`. [1]
5. `Write Setup` to save changes to all ESCs.

---

### Test Hardware 

Swap the desyncing motor 1 woth motor 2:
- Result A: The problem stays on Arm 1 -> Likely ESC.
- Result B: The problem moves to Arm 2 -> The Motor. Internal damage or a loose magnet.

---

📚 Sources

[1] How to FIX Desyncs in 5 Minutes. Chris Rosser. 2023. YouTube. https://www.youtube.com/watch?v=jWdkl0EHkyU 

[2] ESC Configurator (Web-based Tool). https://esc-configurator.com/

[3] How to Fix ESC Desync in FPV Drones: Tips & Fixes. Oscar Liang. 23.02.2024. Blog. https://oscarliang.com/fix-esc-desync/  



 🔮 Origin:: [[11.04.2026]]
