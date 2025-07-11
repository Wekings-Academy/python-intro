# 作业一：实现加法函数

请 fork 本仓库，在 `main.py` 中实现 `add(a, b)` 函数，使其通过测试。
完成后，请向本仓库提交 Pull Request（PR）并等待自动评测结果。

---

## 👩‍🎓 作业说明（Assignment Instructions）

### 📌 任务目标

请你 fork 本项目，完成其中的 Python 函数，并提交 Pull Request（PR）进行自动评测。

---

### ✅ 步骤一：Fork 项目

1. 打开本仓库（GitHub 页面）
2. 点击右上角的 **Fork** 按钮
3. 创建到你自己的 GitHub 账户下

---

### ✅ 步骤二：在本地运行（Miniconda 环境）

1. 打开你的终端（Terminal）或 Anaconda Prompt

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 运行测试（先不改代码，感受下失败的样子）：

   ```bash
   pytest
   ```

---

### ✅ 步骤三：完成代码

在 `main.py` 中实现指定函数。例如：

```python
def add(a: int, b: int) -> int:
    return a + b
```

然后再次运行测试确保通过：

```bash
pytest
```

---

### ✅ 步骤四：提交 PR（Pull Request）

1. 将你修改后的代码 **push 到 GitHub**
2. 打开你的仓库页面，点击 **“Compare & Pull Request”**
3. 填写标题，例如 `完成作业1 - 张三`
4. 点击提交（Create Pull Request）

---

### ✅ 步骤五：查看评测结果

- GitHub Actions 会自动运行测试
- 如果测试通过，会显示 ✅ green check
- 如果失败，请根据提示修改代码再提交

---

## ✅ 小贴士

- 不要修改 `tests/` 目录下的测试文件
- 你可以多次提交 PR，系统会自动重新评测
