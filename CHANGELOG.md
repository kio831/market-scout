# Changelog

All notable changes to Market Scout are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
