### but GitHub does not provide shell access

```
执行： ssh -T git@github.com   
出现： 
Hi xiashuijun! You've successfully authenticated, but GitHub does not provide shell access.

解决办法：
注意之后在clone仓库的时候要使用ssh的url，而不是https！
git remote -v 查看远程仓库地址，如果不是git开头，就替换
替换remote url，执行 git remote set-url origin git@github.com:xiashuijun/xiaotun-project.git
```



### github配置SSH KEY

1. ssh-keygen -t rsa -b 4096 -C "uestchan@sina.com"



2. 按照以下步骤添加ssh keys

![img](https://ask.qcloudimg.com/http-save/1560260/436fe855c6ce63688723984b86ad12ec.png?imageView2/2/w/1620)





# git push 错误error: src refspec master does not match any. error: failed to push some refs to

```
由于特殊原因远程不是master，而是main了。所以是 git push -u origin main
```



### **使用github提交的时候，出现报错Support for password authentication was removed on August 13, 2021. Please use a personal access token instead**

```
你原先的密码凭证从2021年8月13日开始就不能用了，必须使用个人访问令牌（personal access token），就是把你的密码替换成token



```



生成自己的token步骤

1、在个人设置页面，找到Setting

![使用github提交的时候，出现报错Support for password authentication was removed on August 13, 2021. Please use a personal access token instead._开发者](https://s2.51cto.com/images/blog/202109/23/efbca963767c5b0469b7835279a1a82a.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_30,g_se,x_10,y_10,shadow_20,type_ZmFuZ3poZW5naGVpdGk=/format,webp/resize,m_fixed,w_750)

2、选择开发者设置Developer setting

![使用github提交的时候，出现报错Support for password authentication was removed on August 13, 2021. Please use a personal access token instead._命令行_02](https://s2.51cto.com/images/blog/202109/23/59c7aa987d12cb45fd929b5afc6be9bf.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_30,g_se,x_10,y_10,shadow_20,type_ZmFuZ3poZW5naGVpdGk=/format,webp/resize,m_fixed,w_750)

3. 设置token的有效期，访问权限等
4. 生成令牌Generate token
5. 复制token，添加到config. git config --global github.token  tokenxxxxxx(你的具体token)



### github拉取速度慢

```
https://tool.chinaz.com/dns?type=1&host=github.com&ip=

windows: c:\Windows\System32\Drivers\etc\hosts
mac/linux: sudo vim /etc/hosts

```





### git pull 出现 Pulling without specifying how to reconcile divergent branches is

```
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint:
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.

解决办法：
git config pull.rebase false
```

