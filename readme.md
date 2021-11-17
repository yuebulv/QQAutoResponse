# 目标：建一个QQ自动问答bot

## 阶段一：借助QQ群回复

> 流程图：

```flow
st=>start: 开始框
op=>operation: A私聊问题到bot
op1=>operation: bot提问题到群
op2=>operation: bot捕捉群反馈消息并回复给A
cond=>condition: A是否发出结束指令到bot(是或否?)
sub1=>subroutine: 循环
e=>end: 结束框
st->op->op1->op2->cond
cond(yes)->e
cond(no)->sub1(right)->op2
```

## 阶段二：常规问题借助答题数据库回复



