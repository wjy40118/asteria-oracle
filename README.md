# Asteria · 星象手册

一个面向年轻人的反思型占卜交互原型。用户可以抽塔罗牌、输入出生信息生成个人星盘，也可以在双方知情同意的前提下生成双人合盘。界面把塔罗牌、行星节点和关系过程放在可探索的星图中：靠近指针的元素会放大，点击后右侧展开解读。

**Live prototype:** [asteria-oracle.streamlit.app](https://asteria-oracle.streamlit.app)  
**Repository:** [github.com/wjy40118/asteria-oracle](https://github.com/wjy40118/asteria-oracle)  
**做法:** Streamlit + 原生 HTML / CSS / JavaScript  
**费用:** 0 元，Demo 模式不需要 API Key

![Asteria home screen](docs/screenshots/home.png)

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=wjy40118/asteria-oracle&branch=main&mainModule=app.py)

## 它解决什么问题

当人面对关系、职业或自我方向的不确定时，常见的占卜产品会直接给出“吉凶”和确定答案。Asteria 保留抽牌与星盘的仪式感，但把输出改成可观察、可反思、可拒绝的描述。它不是决策系统，也不是心理治疗工具。

## 主要交互

- **鱼眼探索:** 指针靠近牌、行星或首页关键词时，局部内容放大并变亮。
- **塔罗抽牌:** 支持单牌与三牌牌阵，先洗牌再点击选牌。
- **星盘生成:** 输入姓名、出生日期、时间和城市，生成 12 宫轮盘、日月升和主要相位。
- **双人合盘:** 输入双方出生信息与关系问题，查看共鸣指数、情绪回应、生活节奏、信任表达、修复空间和三条感情建议。
- **AI 解读:** 右侧面板按“观察 / 自然节奏 / 主要相位 / 下一步”组织内容。
- **错误与边界状态:** 日期为空时阻止生成；时间为空时提示上升星座仅为区间估计；所有页面保留非医疗、非投资、非法律建议声明。

## 本地运行

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 评分要求对应文档

完整的九项 Design Spec 见 [DESIGN_SPEC.md](DESIGN_SPEC.md)。严格两页的演示文件见 `presentation/Asteria_Design_Spec.pdf`。

## 数据、模型和许可

- 22 张大阿卡纳的名称和自写关键词保存在 `data/tarot_major_arcana.json`。
- 星空水彩背景由项目作者提供，横向网页版本保存在 `assets/starfield-wide.webp`。
- 环境粒子与星座连线交互参考并移植自 React Bits Particles，第三方许可见 `THIRD_PARTY_NOTICES.md`。
- 本项目不使用 Rider-Waite-Smith 或其他受版权保护的牌面图像，界面中的牌背由 CSS 生成。
- 出生星位在浏览器内根据日期、时间与城市生成，是 **确定性演示数据**，没有调用天文服务，也不是专业星历。
- AI 解读使用离线模板完成，目的是保证 Streamlit 免费环境也能完整演示。
- 若未来接入开源模型，首选 `Qwen2.5-3B-Instruct`，提示词见 `prompts/system_prompt.txt`。模型权重遵循其官方模型卡许可。
- 塔罗过程语言与双人牌阵结构参考 [息观塔罗 · 分形结构语法](https://github.com/yihao-sun/fractal-tarot-prompt)，原作者为孙翊豪/太翊豪，适配部分遵循 CC BY-NC-SA 4.0。
- 用户输入不写入数据库。刷新页面即丢弃当前会话中的生日和问题。

## 部署

Streamlit Community Cloud:

1. 连接本 GitHub 仓库。
2. Main file path 填 `app.py`。
3. Python 依赖由 `requirements.txt` 安装。
4. 无需 Secrets，因为默认使用离线 Demo。

## 边界

Asteria 不预测死亡、疾病、怀孕、投资回报或他人的隐私；不替代医疗、心理、法律或财务建议。界面明确标注演示性质，星位与解读均保留“你可以不同意”的退出空间。
