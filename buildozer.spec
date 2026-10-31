
[app]

title = JARVIS AI
package.name = jarvis
package.domain = org.jobayer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO
android.api = 35
android.minapi = 23
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
