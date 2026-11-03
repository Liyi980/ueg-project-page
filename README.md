# UEG: Unified Sampling-time Guidance for Controllable Echocardiography Video Generation with Heterogeneous Medical Condition

> 🌐 **Project Page**: [链接待填](#) · 💻 **Github**: [链接待填](#)

Unified Echo Guidance (UEG) reuses a single frozen unconditional video diffusion prior to control myocardial masks, trajectories, and ejection fraction (EF) — without paired condition–video training or task-specific generator fine-tuning.

## 🎬 Demo

**Structure-conditioned generation** (red: target mask, green: prediction, yellow: overlap):

| Target Masks | UEG (Ours) | Target Masks | UEG (Ours) |
|:---:|:---:|:---:|:---:|
| ![Mask cond](assest/gifs/mask_1_cond.gif) | ![Mask ours](assest/gifs/mask_1_ours.gif) | ![Mask cond](assest/gifs/mask_2_cond.gif) | ![Mask ours](assest/gifs/mask_2_ours.gif) |

**Function-conditioned generation** at different target EF levels:

| Target EF 65.2% | Target EF 55.0% | Target EF 49.5% | Target EF 35.2% |
|:---:|:---:|:---:|:---:|
| ![EF 65](assest/gifs/ef_65.gif) | ![EF 55](assest/gifs/ef_55.gif) | ![EF 50](assest/gifs/ef_50.gif) | ![EF 35](assest/gifs/ef_35.gif) |

更多结果（三个任务的完整视频展示、点击放大）请查看 **[Project Page](#)**。

## 📖 Citation

```bibtex
@inproceedings{ueg2027,
  title     = {UEG: Unified Sampling-time Guidance for Controllable Echocardiography Video Generation with Heterogeneous Medical Condition},
  author    = {Anonymous},
  booktitle = {CVPR},
  year      = {2027}
}
```
