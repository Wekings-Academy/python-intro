# 🐍 Python 学生入门练习（支持自动评测）

欢迎来到本项目！这是一个为学生设计的 Python 基础教学项目，**结合 GitHub 实践（Fork + PR）与自动评测（GitHub Actions）**，帮助你在实战中掌握 Python 编程。

本项目将分阶段发布任务，例如：

- ✅ 作业一：函数定义与加法
- 🔜 作业二：条件判断（if-else）
- 🔜 作业三：循环（for/while）
- 🔜 作业四：列表与字符串处理
- ...

每个作业都包含测试用例，提交后会自动检查你的代码是否正确 ✅

---

## ✅ 作业一：实现加法函数

请在 `main.py` 中实现如下函数：

```python
def add(a: int, b: int) -> int:
    return a + b
```

> 初始代码会返回 `0`，请修改为正确的加法逻辑，使其通过测试。

---

## 📌 学习流程说明（重要！）

### 第一步：Fork 项目

1. 打开本仓库 GitHub 页面
2. 点击右上角的 **Fork** 按钮
3. 将仓库复制到你自己的账号下

---

### 第二步：在本地运行项目（建议用 Miniconda）

1. 打开 Terminal / Anaconda Prompt

2. 克隆你的仓库：

   ```bash
   git clone https://github.com/你的用户名/python-assignment-template.git
   cd python-assignment-template
   ```

3. 安装依赖（只包含 `pytest`）：

   ```bash
   pip install -r requirements.txt
   ```

4. 运行测试（你会看到测试失败）：

   ```bash
   pytest
   ```

---

### 第三步：完成代码

修改 `main.py`，完成 `add(a, b)` 函数，让测试通过。

完成后再次运行：

```bash
pytest
```

确认输出显示 ✅ 全部通过。

---

### 第四步：提交 Pull Request（PR）

1. 将你的修改推送到 GitHub：

   ```bash
   git add .
   git commit -m "完成作业1"
   git push origin main
   ```

2. 在你的 GitHub 页面点击 “Compare & Pull Request”
3. 填写标题，例如 “完成作业 1 - 张三”
4. 提交 PR（Pull Request）

---

### 第五步：查看评测结果

- 系统会自动运行测试（GitHub Actions）
- 所有测试通过 ✅：表示你完成了作业
- 如果失败 ❌：请根据提示修改，再次提交 PR

---

## 💡 学习建议 & 注意事项

- 不要修改 `test/` 文件夹内容
- 你可以多次提交代码，系统会自动重新评测
- 请耐心 debug，如果不通过可以查看报错内容提示
- 推荐使用 [Visual Studio Code](https://code.visualstudio.com) 开发，体验更佳

---

## 📬 联系作者

本项目由 **\[ChenYujunjks / Wekings Academy]** 维护，如果你有问题，可以提 Issue 或联系我。
