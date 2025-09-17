---
title: "WhisperLiveKit——开源AI语音识别工具，实时语音转写与说话人识别的利器！"
source: "https://mp.weixin.qq.com/s/JmV_ETsR9OOkUzQWDhzetw"
author:
  - "[[有趣的开源集市]]"
published:
created: 2025-09-17
description:
tags:
  - "clippings"
---
![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kgXibFxsv0e3PvXrU76ADBK4BOzRQZiaV36Qlic0FNKZicVJPONX3kicfrwOvWurHl7APrOrwicpOHctTcb9sKwiatJ0g/0?wx_fmt=jpeg)

原创 有趣的开源集市 [有趣的开源集市](https://mp.weixin.qq.com/s/) *2025年09月17日 08:08*

\*\*点击上方蓝字 关注我\*\*

  

语音识别技术已经成为许多应用场景中不可或缺的一部分。无论是会议记录、实时字幕生成，还是无障碍辅助服务，语音识别技术都在发挥着重要作用。然而，传统的语音识别工具往往依赖于云端服务，存在延迟高、隐私风险大等问题。今天，我们要介绍的是一款完全本地化、实时性强的开源AI语音识别工具—WhisperLiveKit。

  

**01**

**—**

WhisperLiveKit 介绍

## 一款基于 OpenAI Whisper 模型的开源实时语音识别工具，能够将语音实时转录为文字，并支持说话人识别功能。该项目采用了客户端-服务端分离架构，通过本地化处理语音数据，确保用户隐私安全。WhisperLiveKit 融合了 SimulStreaming 与 WhisperStreaming 等前沿技术，实现了超低延迟的文字输出，适用于多种场景，如会议记录、远程教学、直播字幕等。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/kgXibFxsv0e3PvXrU76ADBK4BOzRQZiaV3dPEqTcFH8yp915j3hdxpHszWnd9S20JWnPwDmRWWDibAWkFa56CRSkg/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

****🏠 项目信息****

```bash
#Github地址https://github.com/QuentinFuxa/WhisperLiveKit
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/kgXibFxsv0e3PvXrU76ADBK4BOzRQZiaV3IkIwQNkRMVv0g4JYicrHiaOwEFj94SLgGNVFQcTePibI13OsVFiaiaqkfYw/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

🚀 ****功能特性****

1\. 实时语音转写WhisperLiveKit 支持多种语言输入，能够将语音内容即时转录为文本。无论是会议、讲座还是直播，它都能提供实时的文字输出，帮助用户快速获取信息。

  

2\. 说话人分离（Diarization）在多人对话环境中，WhisperLiveKit 能够自动识别并区分不同讲话者，提升记录的准确性。这一功能特别适用于会议记录和客服通话等场景。

  

3\. 本地化运行所有语音处理均在本地完成，无需上传至云端，确保敏感信息不外泄。这一特性使得 WhisperLiveKit 在处理隐私敏感数据时具有显著优势。

  

4\. 低延迟流式识别WhisperLiveKit 采用先进的流式处理算法，实现语音输入与文字输出几乎同步，响应迅速。无论是实时字幕推送还是无障碍信息服务，它都能提供极佳的用户体验。

  

5\. 多平台接入方式WhisperLiveKit 提供可视化 Web 界面和可编程 Python 接口，支持 Docker 容器化部署，便于集成与扩展。开发者可以根据需求灵活选择接入方式。

**🛠 系统架构**  

![图片](https://mmbiz.qpic.cn/mmbiz_png/kgXibFxsv0e3PvXrU76ADBK4BOzRQZiaV3uicZxTAdrOWzQLvMVQFdWU048pUCcicYBEk7KCzy693SicudQO1Fic7rhw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

  

技术原理：

- SimulStreaming

基于 AlignAtt 策略的实时转录技术，通过智能缓冲机制和增量解码，在语音输入过程中持续输出文本，有效避免短片段处理带来的上下文断裂问题，显著降低延迟。

- WhisperStreaming

采用 LocalAgreement 策略的流式识别算法，优化了实时响应性能，适合对延迟敏感的应用如实时字幕推送。

- 说话人识别技术

集成 Streaming Sortformer 和 Diart 等先进模型，结合语音活动检测（VAD）与说话人嵌入（Speaker Embedding），实现实时精准的说话人分离。

- 语音活动检测（VAD）

使用 Silero VAD 等工业级检测工具，准确识别语音段落，在静音或无语音时段自动暂停处理，节省系统资源。

**02**

**—**

安装

可以通过 Docker 容器化部署，简单易用。以下是安装步骤：

```apache
docker pull quentinfuxa/whisperlivekitdocker run -p 8000:8000 --name whisperlivekit quentinfuxa/whisperlivekit
```

打开浏览器并导航 `http://hostip:8000` ，即可开始使用 WhisperLiveKit 进行实时语音转写。

**03**

**—**

集成

WhisperLiveKit 提供了丰富的 Python API，可以根据需求进行二次开发。以下是一个简单的示例：

```python
from whisperlivekit import TranscriptionEngine, AudioProcessortranscription_engine = TranscriptionEngine(model="medium", diarization=True, language="en")audio_processor = AudioProcessor(transcription_engine=transcription_engine)# 处理音频数据audio_processor.process_audio(audio_data)
```

**04**

**—**

最后

如果你经常需要处理会议记录、采访内容或者任何需要将语音快速转换为文本的场景，WhisperLiveKit 绝对值得一试。它能实时将语音转录成文字，帮你节省大量手动整理的时间，还能区分不同说话人的语音，让记录更加清晰有条理。无论是线上会议、线下活动，还是录制播客、视频内容，它都能轻松应对。

**喜欢，记得 “点赞、在看”** ![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

---

  

继续滑动看下一个

有趣的开源集市

向上滑动看下一个

有趣的开源集市

剪存为飞书云文档