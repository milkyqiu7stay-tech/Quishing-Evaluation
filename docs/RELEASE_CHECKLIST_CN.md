# 上传 GitHub 前的核对清单

这是一份从用户提供的 8 个 Jupyter Notebook 整理出来的目录包。**没有改变 Notebook 的代码单元内容**，只是重命名、分类，清除了保存的执行输出（避免原始 URL/主机名在输出区直接公开）。原 ZIP 必须另外保存。

## 现在还需要你从 FYP 文件夹补充

- [ ] Exp6: `matched_holdout_summary.csv`、`paired_hostname_bootstrap_ci.csv`、`run_metadata.json`
- [ ] Exp7: `matched_robustness_summary.csv`、`paired_hostname_bootstrap_e2e.csv`、`exp7_metadata.json`
- [ ] Exp8 **full**（不要 pilot）: `original_and_mask_summary.csv`、`mask_specific_summary.csv`、`encoder_alignment_audit.csv`、`experiment_protocol.json`
- [ ] Exp9: `summary_mean_sd_by_regime_model.csv`、`split_integrity_audit.csv`、`paired_auc_cluster_bootstrap_ci.csv`、`experiment9_protocol.json`
- [ ] 如有需要，补充基础实验的精选 summary CSV；逐 URL 数据先不要公开。

## 发布前检查

- [ ] 检查源代码是否包含本机绝对路径。当前部分 Notebook 仍写有 `C:\Users\LENOVO\...`，公开不一定有风险，但可移植性有限。不要为了替换路径而无意改变已验证的结果。
- [ ] 检查是否含 token、API key、邮箱、未公开原始数据和模型权重。整理时没有做过完整的保密审计，不能保证 100% 安全。
- [ ] 校对 README、最终论文和所上传 CSV 是**同一次最终运行**，尤其是 Exp8 的 `full` 模式与 Exp9 的 split audit。
- [ ] 补充实际运行环境的版本清单（目前 `requirements.txt` 为从 import 推断的依赖名）。
- [ ] 与导师/合作者确认是否公开源码、采用何种 License、哪些第三方数据不得重新分发。
- [ ] GitHub 仓库公开后使用无登录浏览器测试链接可用性。
- [ ] 论文 Discussion 引用真实仓库 URL；不能写成已有全套可复现结果，除非实际文件和运行流程已核对。

## 论文中建议的句子

`The experiment-specific code and implementation details are available at \url{https://github.com/USERNAME/REPOSITORY}.`

填入真实仓库地址，并确保 LaTeX 支持 `\url`（例如已加载 `url` 或 `hyperref`）。Github 代码只作为可追溯性补充，不替代正文关键实验说明。


## 新补充的实验汇总结果

- 已从 `Experiments Output.zip` 整理八份 Exp6–Exp9 汇总/审计表，原始 `.xls` 实为 CSV 文本，已按字节原样拷贝并改为 `.csv`。
- 执行 `python scripts/verify_reported_results.py`，可核对绝大部分论文核心汇总数字。
- **仍需补充** Exp8 最终全量运行的 `per_url_mask_sensitivity.csv` 和 `hostname_bootstrap_ci.csv`，以及 Exp9 的 `paired_auc_cluster_bootstrap_ci.csv`（如有）。注意不要误用 40 样本 pilot 或单 seed 测试输出。
- 未上传原始 QR 图像、恶意 URL、训练模型；公开前仍须确认 Notebook 中没有私人路径、密钥、不可再分发的数据。


## 2026-11-12：三份补充验证文件已加入

- [x] Exp8 `per_url_mask_sensitivity.csv`：1777 行，复算 1132/1777=0.6370 和 mean probability range=0.6038。**出于公开隐私考虑已经以匿名分组编号替代 hostname，并去掉 original_index；原始文件请保存在本地。**
- [x] Exp8 `hostname_bootstrap_ci.csv`：保存的 F_mask CI [0.6035,0.6644]、mask 6 AUC delta -0.4011及CI [-0.4405,-0.3595] 与论文一致；**未独立重新抽样**。
- [x] Exp9 `paired_auc_cluster_bootstrap_ci.csv`：9 条比较（3 regimes ×3 seeds）所有 95% CI 均不跨 0，每条记录为 300 次有效 bootstrap。
- [ ] 上传前再次检查 Notebook 的代码、Markdown（**清除输出不代表删除代码中的绝对路径或潜在 secrets**），和导师确认公开权限及数据来源许可。
- [ ] 正式公开后用无痕窗口确认 README、结果表和 GitHub 链接可以打开。
