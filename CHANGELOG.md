# Changelog

All notable changes to Market Scout are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-09-05

### Added — V3 决策层（Decision Layer）：Evidence → Score → Decision → MVP → Action

- **Market Evidence 市场证据（`references/v3-evidence.md`）**
  - 证据三态 Evidence / Inference / Unknown：每个关键结论标注依据类型
  - 证据充分度三级 Sufficient / Partial / Insufficient；Insufficient 熔断，不评分、不编造
  - Unknown 子信号按 0 计并显式标注；Inference 最高 7/10
  - `templates/v3-evidence-board.md` 证据看板
- **Opportunity Score 机会评分（`references/v3-scoring.md`）**
  - 统一 7 维加权 0-100（需求 15 / 痛点 15 / 竞争切入空间 15 / 变现 20 / 开发 15 / 获客 10 / AI 优势 10）
  - 每维拆 3-4 个 1-10 子信号，计算式可手工复算，20 格百分条可视化
  - 竞争维度 = 切入空间大小（禁止"竞争低=高分"），切入空间四问必答，无切入空间证据封顶 40
  - 7 条致命红旗一票否决（复用 project-evaluation §6）
  - `templates/v3-score-card.md` 机会评分卡
- **Decision 机会决策（`references/v3-decision.md`）**
  - 三档 RECOMMENDED / POTENTIAL / NOT_RECOMMENDED，由"总分+门槛+红旗+证据充分度"共同决定
  - 强制编号 Why 列表（每条绑定证据三态）
  - 与 V2 Verdict 一一对应：GO→RECOMMENDED / VALIDATE_FIRST→POTENTIAL / NO_GO→NOT_RECOMMENDED
  - `templates/v3-decision-card.md` 机会决策卡
- **MVP Blueprint（`references/v3-mvp.md`）**
  - 9 字段统一输出（Product / Target User / Core Problem / Core Value / Must Have≤3 / Nice to Have / Do Not Build / Build Difficulty / Recommended Stack）
  - 触发条件：RECOMMENDED 或（POTENTIAL 且 score≥65）
  - 单人最快验证铁律；方法完全复用 V2 BLUEPRINT
  - `templates/v3-mvp-card.md` MVP 方案卡
- **Action Plan 行动计划（`references/v3-action-plan.md`）**
  - 5 种机会类型动态模板（企业工具 / 个人工具 / AI Agent / 本地服务 / 数字产品），每步 5 要素（目标/做什么/成功标准/失败转向）
  - 与 Decision 联动：执行路径 / 验证优先路径 / 停止路径
  - `templates/v3-action-plan-card.md` 行动计划卡
- **V3 编排（`references/v3-overview.md`）**
  - 9 步主流程（INPUT→DISCOVERY→VALIDATION→EVIDENCE→COMPETITION→SCORING→DECISION→MVP→ACTION）
  - V2→V3 映射表、V3Input/V3Output 数据契约、四套代码正交、熔断降级、验收清单
- **最终报告（`templates/v3-report.md`）**：结论先行一屏报告（Score/Decision/Evidence/Pain/Competition/MVP/Action）

### Changed

- `SKILL.md`：版本升为 v3.0.0；新增 V3 决策层章节、V3 触发词路由、参考/模板/示例清单扩展；V2 全部内容保留
- `USER_GUIDE.md`：更新为 v3.0.0，新增 V3 决策层使用说明与版本验证词
- `tools/validate_skill.py`：扩展 v3 文件清单与检查项；修复 Windows GBK 控制台输出编码问题；发布整理阶段同步 README/安装包版本锚点（README 顶部版本对齐 v3.0.0、安装包纳入文件清单）
- `README.md`：重写为 V3 图文主页（V1→V2→V3 演进图、V3 完整闭环图、五大新模块卡片、真实 examples、Download 与安装入口、版本统一为 v3.0.0）
- 新增 `releases/market-scout-v3.0.0.zip`：V3.0.0 正式安装包（zip 内顶层为 `market-scout/`，与手动安装路径一致）

### Notes

- **v2.0.0 全部能力保留**：五阶段流水线、三种模式、铁律、停止机制、第一笔钱清单、模板与示例均未删除或破坏
- **决策口径统一**：V3 的 RECOMMENDED/POTENTIAL/NOT_RECOMMENDED 与 V2 的 GO/VALIDATE_FIRST/NO_GO 一一对应，最终报告统一用 V3 代码
- 仍是纯 Markdown 文档型 Agent Skill，无前端代码/构建链/数据库；`website/index.html` 为 v2 时期落地页，本次发布保留原样、未改写，后续版本再单独更新
- `examples/v3-decision-run.md` 与 `examples/v3-crowded-market.md` 为演示数据示例
## [2.0.0] - 2026-09-03

### Added — Four new pipeline stages (Find → Validate → Evaluate → Monetize)

- **Demand Validation（需求验证）**
  - `references/demand-validation.md`：需求强度 6 信号合成 1-10 分、三层目标用户、替代成本与定价锚、付费理由链 JTBD 5 环、需求证据可信度矩阵
  - `templates/demand-validation-card.md`：需求验证卡
- **Project Evaluation（项目评估）**
  - `references/project-evaluation.md`：7 维加权评分（需求20%/市场20%/竞争差异15%/AI可实现15%/开发难度10%/个人适配15%/风险5%）、综合机会评分 0-100（计算式可复算）、7 条致命红旗一票否决、三档结论 GO / VALIDATE_FIRST / NO_GO
  - `templates/project-evaluation-card.md`：项目评估卡（评分表/计算式/红旗检查）
- **Opportunity → Project（机会转项目）**
  - `references/project-blueprint.md`：产品形态（对齐 Level 1-5）、MoSCoW 核心功能、MVP 五项、技术方向、最小验证实验、差异化切入点
  - `templates/project-blueprint-card.md`：机会转项目卡
- **Monetization & GTM（商业化与获客）**
  - `references/monetization-gtm.md`：Target Customer（区分使用者/付费方）、Offer 三档、Business Model 模式库、可解释 Pricing、首批 10 客户获取、渠道矩阵、GTM 三阶段、7 种不开发产品的验证方式
  - `templates/monetization-gtm-card.md`：商业化获客卡
  - **模块化数据契约**：定义 `MonetizationInput` / `MonetizationPlan`，未来可独立成产品、独立收费，无需大规模重构

### Added — Pipeline & Runtime

- `references/pipeline-and-runtime.md`：五阶段流水线编排、三套代码（证据等级 A/B/C / 交付状态机 / Pipeline 阶段）正交区分、阶段熔断与回退、断点续跑
- **运行时健壮性规范**：外部搜索/API/子 Agent 调用统一超时、瞬时错误有限重试（指数退避）、分级失败降级（换来源→用用户材料→标【证据不足】）、确定性错误不重试

### Added — UI / UX

- `references/ui-rendering-spec.md`：统一输出渲染规范（Design System）
  - 结论带 Banner、阶段进度条、10 格分数条、行动按钮
  - Loading / Empty / Error / Success 四种状态模板
  - 移动端优先（表格≤6列、窄屏键值列表）、桌面端信息密度
  - 长报告目录与每阶段小结、双语规范、代码区格式、输出自检清单
- 所有 v2 阶段卡与报告模板统一顶部结论带、阶段进度条、底部行动按钮

### Added — Final Report

- `templates/opportunity-report.md`：五阶段汇总的最终机会报告，结论先行，10 秒看懂"在分析什么→得到了什么→下一步做什么"

### Added — Full Example

- `examples/full-pipeline-v2.md`：完整五阶段示例（本地教培工作室获客内容代做），含可复算评分（74/100）、演示"高分也可能是 VALIDATE_FIRST"、定价与首批客户获取

### Added — Open Source Release Assets

- `README.md`：重写为开源产品主页（Hero、四阶段流程图、Features、工作流、安装、使用、技术栈、项目结构、Roadmap、License）
- `CHANGELOG.md`：本文件
- `LICENSE`：MIT
- `CONTRIBUTING.md`：贡献指南
- `.gitignore`：Git 忽略规则
- `website/index.html`：产品落地页（可挂 GitHub Pages）

### Changed

- `SKILL.md`：版本升为 v2.0.0；新增 V2 主链路章节、四阶段能力要点、商业化模块独立化边界、三套代码区分、输出与 UI 规范、模式路由新增 v2 触发词、标准工作流新增第 10 步 V2 衔接
- `templates/opportunity-card.md`：增量升级到 v2，兼容全部 v1.1 字段，新增 Pipeline Stage、综合机会评分、三档结论、五阶段导航
- `USER_GUIDE.md`：更新为 v2.0.0，新增五阶段说明、版本验证词、触发词、FAQ

### Security / Quality

- `tools/validate_skill.py`：扩展自检（文件清单、交叉引用、frontmatter、必备字段、权重合计、版本一致性、UI 规范锚点），116+ 项检查全通过

### Notes

- **v1.x 全部能力保留**：三类搜索、证据链、三模式、8 维评分、Level 1-5、交付状态机、停止机制、第一笔钱清单、原有模板与示例均未删除或破坏
- **当前不实现**支付、订阅、会员、计费系统（只产出商业化方案与验证动作）
- 这是纯 Markdown 文档型 Agent Skill，无前端代码/构建链/数据库

---

## [1.1.0] - 2026 (previous)

### Added
- Evidence Chain 证据链机制（原始证据→观察→推断→假设→验证）
- Problem / Solution / Payment 三类搜索
- Quick / Research / Execution 三种工作模式
- Opportunity 交付状态机（HYPOTHESIS→…→PRODUCTIZED）
- 评分绑定证据（含 Payment 分档）
- 停止研究机制与重启条件
- `templates/evidence-card.md`、`templates/quick-scan.md`
- `references/evidence-chain.md`、`references/opportunity-state-machine.md`
- `examples/real-world-problem.md` 完整运行示例

## [1.0.0] - 2026 (initial)

### Added
- Market Scan 市场侦察
- Problem Card、8 维评分
- Level 1-5 解决方案分级
- 7 天/30 天验证模式
- 三池维护（Result/Demand/Payment）
- 视频/评论反向市场分析
