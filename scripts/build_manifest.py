# -*- coding: utf-8 -*-
"""
扫描 assest/videos/ 下的实际文件，生成 assest/manifest.js 供网页自适应渲染。
每次新增/删除 case 后重新运行: python scripts/build_manifest.py
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = os.path.join(ROOT, "assest", "videos")
OUT = os.path.join(ROOT, "assest", "manifest.js")

def scan_mask():
    cases = []
    mdir = os.path.join(VIDEOS, "mask")
    if not os.path.isdir(mdir): return cases
    for d in sorted(os.listdir(mdir)):
        pdir = os.path.join(mdir, d)
        if not os.path.isdir(pdir): continue
        gen = os.path.join(pdir, "generated_video.mp4")
        if not os.path.isfile(gen): continue
        overlay = next((f for f in os.listdir(pdir)
                        if f.startswith("overlay_video_pred_condition_masks") and f.endswith(".mp4")), None)
        if overlay:
            cases.append({"id": d,
                          "gen": f"assest/videos/mask/{d}/generated_video.mp4",
                          "overlay": f"assest/videos/mask/{d}/{overlay}"})
    return cases

def scan_traj():
    cases = []
    tdir = os.path.join(VIDEOS, "traj")
    if not os.path.isdir(tdir): return cases
    for d in sorted(os.listdir(tdir)):
        sdir = os.path.join(tdir, d)
        if not os.path.isdir(sdir): continue
        gen = next((f for f in os.listdir(sdir)
                    if f == f"{d}_generated_video.mp4"), None)
        overlay = next((f for f in os.listdir(sdir)
                        if f == f"{d}_overlay_predicted_vs_target.mp4"), None)
        if gen and overlay:
            cases.append({"id": d,
                          "gen": f"assest/videos/traj/{d}/{gen}",
                          "overlay": f"assest/videos/traj/{d}/{overlay}"})
    return cases

def scan_ef():
    samples = []
    edir = os.path.join(VIDEOS, "ef")
    if not os.path.isdir(edir): return samples
    for d in os.listdir(edir):
        cdir = os.path.join(edir, d)
        if not os.path.isdir(cdir): continue
        m = re.match(r"condition_(\d+)_ef([\dp]+)$", d)
        if not m: continue
        cid, ef = m.group(1), m.group(2)
        # 在子目录中找 generated_video_ef*.mp4（叶子目录名可能变化）
        src = None
        for sub in os.listdir(cdir):
            leaf = os.path.join(cdir, sub)
            if not os.path.isdir(leaf): continue
            f = f"generated_video_ef{ef}.mp4"
            if os.path.isfile(os.path.join(leaf, f)):
                src = f"assest/videos/ef/{d}/{sub}/{f}"
                break
        if src:
            val = float(ef.replace("p", "."))
            samples.append({"id": cid, "ef": ef, "val": val, "src": src})
    samples.sort(key=lambda s: -s["val"])
    return samples

manifest = {"mask": scan_mask(), "traj": scan_traj(), "ef": scan_ef()}
with open(OUT, "w", encoding="utf-8") as f:
    f.write("// 自动生成：python scripts/build_manifest.py\n")
    f.write("window.MANIFEST = ")
    f.write(json.dumps(manifest, ensure_ascii=False, indent=1))
    f.write(";\n")
print(f"manifest.js 已生成: mask {len(manifest['mask'])} | traj {len(manifest['traj'])} | ef {len(manifest['ef'])}")
