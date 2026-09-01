# -*- coding: utf-8 -*-
"""Build the narrated revision video: Chromium-rendered slides + mbrola TTS + ffmpeg."""
import os, subprocess, wave, shutil, sys
from slides import SCENES

W, H = 1920, 1080
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT = "out"
GAP = 0.55          # seconds of silence after each scene
LEAD = 0.30         # seconds of silence before each scene
WPM = 150

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{background:#080d18}
html,body{width:%dpx;height:%dpx;overflow:hidden}
body{background:radial-gradient(120%% 120%% at 15%% 0%%,#1b2a4a 0%%,#0d1526 60%%,#080d18 100%%);
 font-family:"Liberation Sans","DejaVu Sans",sans-serif;color:#eaf1ff}
.wrap{padding:46px 74px 40px;height:1080px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #2c3f66;padding-bottom:16px}
.sec{background:#ffb454;color:#10182a;font-weight:bold;font-size:24px;padding:7px 18px;border-radius:8px;letter-spacing:.4px}
.brand{color:#7f96c4;font-size:23px;letter-spacing:1.6px;text-transform:uppercase}
h1{font-size:63px;line-height:1.1;margin:30px 0 10px;letter-spacing:-1px;font-weight:bold}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px}
.hero{font-size:35px;color:#9fbaea;margin:2px 0}
.eq{font-family:"DejaVu Serif",serif;font-style:italic;font-size:52px;line-height:1.34;margin:8px 0;color:#fff}
.eq.big{font-size:64px;text-align:center;margin:16px 0}
.eq.bad{color:#ff8f7a;text-align:center;font-size:64px}
.eq.good{color:#7ee0a8;text-align:center;font-size:64px}
.lbl{text-align:center;font-size:29px;margin-top:-2px}
.lbl.bad{color:#ff8f7a}.lbl.good{color:#7ee0a8}
.good{color:#7ee0a8}
sup{font-size:.62em}
.m{font-family:"DejaVu Serif",serif;font-style:italic;white-space:nowrap}
.hl{background:#ffb454;color:#10182a;padding:3px 16px;border-radius:9px;font-style:italic;display:inline-block}
.steps{display:flex;flex-direction:column;gap:14px}
.st{font-size:35px;line-height:1.35;background:rgba(255,255,255,.05);
 border-left:6px solid #4a7ad6;padding:14px 22px;border-radius:0 10px 10px 0}
.cards{display:flex;gap:20px;margin:10px 0}
.card{flex:1;background:rgba(255,255,255,.06);border:2px solid #35507f;border-radius:16px;padding:22px 24px}
.card .n{display:block;font-size:40px;font-weight:bold;color:#ffb454;line-height:1}
.card .t{display:block;font-size:31px;font-weight:bold;margin:9px 0 6px}
.card .b{display:block;font-size:26px;color:#a9c0e6;line-height:1.32}
.note{font-size:30px;line-height:1.35;padding:18px 24px;border-radius:12px;margin-top:6px}
.note.tip{background:rgba(126,224,168,.11);border-left:7px solid #4fc98a;color:#d3f5e3}
.note.warn{background:rgba(255,180,84,.12);border-left:7px solid #ffb454;color:#ffe6c2}
table.sg{width:100%%;border-collapse:collapse;font-size:31px;margin:8px 0}
table.sg th{background:#22355c;padding:14px 18px;text-align:left;font-size:27px;color:#bfd4f5}
table.sg td{padding:13px 18px;border-bottom:1px solid #2c3f66;font-family:"DejaVu Serif",serif}
table.sg td:first-child{font-weight:bold;color:#ffb454;font-family:"Liberation Sans",sans-serif}
.split{display:flex;gap:44px}.split>div{flex:1}
.frac{display:inline-block;text-align:center;vertical-align:-.55em;margin:0 .16em}
.frac>span{display:block;padding:0 .3em}
.frac .num{border-bottom:3px solid #eaf1ff}
.dg{display:block;width:520px;height:auto;margin:6px auto}
.prog{height:8px;background:#1d2b47;border-radius:4px;margin-top:22px}
.prog i{display:block;height:100%%;background:linear-gradient(90deg,#4a7ad6,#ffb454);border-radius:4px}
""" % (W, H)


def slide_html(section, title, body, idx, total):
    pct = 100.0 * (idx + 1) / total
    return ("<!doctype html><html><head><meta charset='utf-8'><style>%s</style></head><body>"
            "<div class='wrap'><div class='top'><span class='sec'>%s</span>"
            "<span class='brand'>Grade 9 Maths &middot; Test Revision</span></div>"
            "<h1>%s</h1><div class='body'>%s</div>"
            "<div class='prog'><i style='width:%.1f%%'></i></div></div></body></html>"
            % (CSS, section, title, body, pct))


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, **kw)
    if r.returncode != 0:
        sys.stderr.write(" ".join(cmd)[:300] + "\n" + r.stderr.decode()[-1500:] + "\n")
        raise SystemExit(1)
    return r


def main():
    for d in (OUT, "tmp"):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)

    total = len(SCENES)
    durations = []
    seg_paths = []

    for i, (section, title, body, narration) in enumerate(SCENES):
        tag = "%02d" % i
        # ---- slide image ----
        hp = os.path.abspath("tmp/s%s.html" % tag)
        with open(hp, "w") as f:
            f.write(slide_html(section, title, body, i, total))
        png = os.path.abspath("tmp/s%s.png" % tag)
        run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=%d,%d" % (W, H),
             "--screenshot=" + png, "file://" + hp])
        # ---- narration ----
        wav = "tmp/a%s.wav" % tag
        run(["espeak-ng", "-v", "mb-us1", "-s", str(WPM), "-w", wav, narration])
        with wave.open(wav) as w:
            secs = w.getnframes() / float(w.getframerate())
        durations.append(LEAD + secs + GAP)
        seg_paths.append(wav)
        print("scene %s  %5.1fs  %s" % (tag, durations[-1], title[:52]), flush=True)

    # ---- stitch narration with padding ----
    with wave.open(seg_paths[0]) as w:
        params = w.getparams()
    rate, sw, ch = params.framerate, params.sampwidth, params.nchannels
    lead = b"\x00" * int(rate * LEAD) * sw * ch
    gap = b"\x00" * int(rate * GAP) * sw * ch
    narr = "tmp/narration.wav"
    with wave.open(narr, "wb") as o:
        o.setnchannels(ch); o.setsampwidth(sw); o.setframerate(rate)
        for p in seg_paths:
            with wave.open(p) as w:
                o.writeframes(lead + w.readframes(w.getnframes()) + gap)

    # ---- frame list ----
    with open("tmp/frames.txt", "w") as f:
        for i, d in enumerate(durations):
            f.write("file '%s'\nduration %.3f\n" % (os.path.abspath("tmp/s%02d.png" % i), d))
        f.write("file '%s'\n" % os.path.abspath("tmp/s%02d.png" % (total - 1)))

    mp4 = os.path.join(OUT, "Maths_Revision_Factorising_and_Pythagoras.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error",
         "-f", "concat", "-safe", "0", "-i", "tmp/frames.txt",
         "-i", narr,
         "-filter_complex", "[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100[a]",
         "-map", "0:v", "-map", "[a]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p",
         "-vf", "fps=25,format=yuv420p", "-c:a", "aac", "-b:a", "160k",
         "-movflags", "+faststart", "-shortest", mp4])

    print("\nTOTAL RUNTIME: %d min %02d sec" % (sum(durations) // 60, sum(durations) % 60))
    print("OUTPUT:", mp4, os.path.getsize(mp4) // 1024, "KB")


if __name__ == "__main__":
    main()
