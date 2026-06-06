---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/systematic-debugging.txt
raw_sha256: 0437808740660ed5172ab2e4db3b2ec885c090d5763b77201682d4bd6177b67c
compiled_at: 2026-04-15T00:37:23.940Z
---
# 系统化调试案例：Parser嵌套对象处理测试失败
## 摘要
本素材记录了一个JavaScript/TypeScript项目单元测试失败案例，测试 Parser 模块处理嵌套对象的用例抛出类型错误，需要定位并修复故障。
## 关键要点
1.  出错测试模块为`src/utils/parser.test.ts`，出错用例为`Parser › should handle nested objects`
2.  错误类型为`TypeError: Cannot read property 'value' of undefined`
3.  错误抛出位置为`src/utils/parser.ts`的第42行第18个字符
4.  错误调用栈为：parse方法被测试用例在`parser.test.ts`第28行调用触发
## 证据片段
```
FAIL src/utils/parser.test.ts
  ● Parser › should handle nested objects
    TypeError: Cannot read property 'value' of undefined
      at parse (src/utils/parser.ts:42:18)
      at Object.<anonymous> (src/utils/parser.test.ts:28:20)
```
## 待解决问题
定位错误原因并修复 Parser 处理嵌套对象时的故障，使测试通过。
