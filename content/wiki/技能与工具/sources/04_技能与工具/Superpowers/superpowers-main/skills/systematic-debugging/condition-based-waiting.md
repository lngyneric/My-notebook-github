---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/condition-based-waiting.md
raw_sha256: e89fec8400d6cd50f43407cec9fab50976ba4d55d0ec2eb51c0bd68036b54c26
compiled_at: 2026-04-14T16:54:37.498Z
---
# 基于条件的等待（Condition-Based Waiting）
## 摘要
基于条件的等待是系统化调试中解决不稳定测试（Flaky Tests）的技术方案，核心思路是等待需要验证的实际条件满足，而非猜测操作所需的固定时长，可消除测试中的竞态条件，提升测试通过率与执行效率。

## 核心原则
Wait for the actual condition you care about, not a guess about how long it takes.（等待你真正关心的实际条件满足，而非猜测任务需要多长时间）

## 使用场景
### 适用场景
- 测试中存在任意固定延迟（如`setTimeout`、`sleep`、`time.sleep()`）
- 测试不稳定（有时通过，负载下失败）
- 并行运行时测试超时
- 需要等待异步操作完成

### 不适用场景
- 需要测试实际的时间行为（如防抖、节流间隔）
- 若必须使用任意固定延迟，一定要文档记录使用原因

## 核心模式
替换代码中预先固定时长的等待，改为轮询检查目标条件直到满足：
❌ 错误示例（猜测时长）：
```typescript
await new Promise(r => setTimeout(r, 50));
const result = getResult();
expect(result).toBeDefined();
```
✅ 正确示例（条件等待）：
```typescript
await waitFor(() => getResult() !== undefined);
const result = getResult();
expect(result).toBeDefined();
```

## 常见场景快速模板
| 场景 | 模板 |
|----------|---------|
| 等待事件 | `waitFor(() => events.find(e => e.type === 'DONE'))` |
| 等待状态 | `waitFor(() => machine.state === 'ready')` |
| 等待计数满足 | `waitFor(() => items.length >= 5)` |
| 等待文件生成 | `waitFor(() => fs.existsSync(path))` |
| 复杂组合条件 | `waitFor(() => obj.ready && obj.value > 10)` |

## 通用实现
通用轮询实现示例：
```typescript
async function waitFor<T>(
  condition: () => T | undefined | null | false,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const startTime = Date.now();

  while (true) {
    const result = condition();
    if (result) return result;

    if (Date.now() - startTime > timeoutMs) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }

    await new Promise(r => setTimeout(r, 10)); // 每10ms轮询一次
  }
}
```

## 常见错误
1. ❌ 轮询过快（如每1ms检查一次），会浪费CPU资源；✅ 修复：每10ms轮询一次
2. ❌ 未设置超时，条件不满足时会无限循环；✅ 修复： always 添加上限超时，并抛出清晰的错误信息
3. ❌ 在循环外缓存状态，使用过期数据判断；✅ 修复：在循环内部调用获取状态的方法，保证数据最新

## 允许使用任意固定延迟的情况
当需要验证已知固定规律的时间行为时，可以使用任意延迟，但需要满足三个要求：
1. 先等待触发条件满足
2. 延迟时长基于已知的固定规律，而非猜测
3. 添加注释说明使用延迟的原因

示例：
```typescript
// Tool ticks every 100ms - need 2 ticks to verify partial output
await waitForEvent(manager, 'TOOL_STARTED'); // First: wait for condition
await new Promise(r => setTimeout(r, 200));   // Then: wait for timed behavior
// 200ms = 2 ticks at 100ms intervals - documented and justified
```

## 实际效果
根据2025年10月3日的调试实践：
- 修复了3个文件共15个不稳定测试
- 测试通过率从60%提升至100%
- 测试执行速度提升40%
- 彻底消除了竞态条件
